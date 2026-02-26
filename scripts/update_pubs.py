from scholarly import scholarly, ProxyGenerator
import json
import os
import time
import random
import hashlib

# 👉 Google Scholar ID
SCHOLAR_ID = "MAB85ZYAAAAJ"

DATA_DIR = "data"
OUT_PATH = os.path.join(DATA_DIR, "publications.json")
CKPT_PATH = os.path.join(DATA_DIR, "publications_checkpoint.json")

# 속도/차단 완화 파라미터
SLEEP_MIN = 6
SLEEP_MAX = 14

MAX_RETRIES_PER_PUB = 3          # 논문 1개당 재시도 횟수
BACKOFF_BASE_SECONDS = 15        # 실패 시 기본 대기
SAVE_EVERY = 10                  # N개마다 중간 저장

# 너무 오래 걸리면 최신만 우선 확보하고 끊고 싶을 때 사용(원하면 숫자 줄이기)
# None이면 제한 없이 끝까지 시도
MAX_ITEMS = None   # 예: 80 으로 하면 최신 80개만

def stable_key(title: str, year: str) -> str:
    """중복/이어받기용 키"""
    raw = f"{(title or '').strip().lower()}|{(year or '').strip()}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()

def load_checkpoint():
    if os.path.exists(CKPT_PATH):
        try:
            with open(CKPT_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"done_keys": [], "pubs": []}
    return {"done_keys": [], "pubs": []}

def save_checkpoint(done_keys, pubs):
    tmp = {"done_keys": list(done_keys), "pubs": pubs}
    with open(CKPT_PATH, "w", encoding="utf-8") as f:
        json.dump(tmp, f, ensure_ascii=False, indent=2)

def final_save(pubs):
    # 최신순 정렬(연도 desc, 연도 없는 건 뒤로)
    def year_sort_key(x):
        y = x.get("year", "")
        try:
            return int(str(y))
        except Exception:
            return -1

    pubs_sorted = sorted(pubs, key=year_sort_key, reverse=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(pubs_sorted, f, ensure_ascii=False, indent=2)

def try_enable_free_proxies():
    """프록시는 오히려 불안정할 때도 있어서 '시도'만 하고 실패해도 진행."""
    try:
        pg = ProxyGenerator()
        ok = pg.FreeProxies()
        scholarly.use_proxy(pg)
        return bool(ok)
    except Exception:
        return False

def safe_get(bib: dict, *keys, default=""):
    for k in keys:
        v = bib.get(k)
        if v:
            return v
    return default

def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    print("START fetching publications...")

    proxy_ok = try_enable_free_proxies()
    print(f"Proxy enabled: {proxy_ok}")

    ckpt = load_checkpoint()
    done_keys = set(ckpt.get("done_keys", []))
    pubs = ckpt.get("pubs", [])

    try:
        # 1) 저자 찾기
        author = scholarly.search_author_id(SCHOLAR_ID)
        print("Author found")

        # 2) 논문 목록 가져오기
        author = scholarly.fill(author, sections=["publications"])
        publications = author.get("publications", []) or []
        print("Total publications found:", len(publications))

        # 최신부터 처리
        publications = list(reversed(publications))

        processed_this_run = 0

        for i, pub in enumerate(publications):
            if MAX_ITEMS is not None and processed_this_run >= MAX_ITEMS:
                print(f"Reached MAX_ITEMS={MAX_ITEMS}. Stop early.")
                break

            # pub 자체에 bib 일부가 있을 수 있음
            base_bib = (pub.get("bib") or {}) if isinstance(pub, dict) else {}
            base_title = safe_get(base_bib, "title", default="")
            base_year = safe_get(base_bib, "pub_year", "year", default="")

            k = stable_key(base_title, str(base_year))
            if k in done_keys:
                continue

            print(f"Fetching {i+1}/{len(publications)}")

            success = False
            last_err = None

            for attempt in range(1, MAX_RETRIES_PER_PUB + 1):
                try:
                    filled = scholarly.fill(pub)
                    bib = filled.get("bib", {}) or {}

                    title = safe_get(bib, "title", default=base_title)
                    authors = safe_get(bib, "author", default="")
                    journal = safe_get(bib, "journal", "venue", default="")
                    volume = safe_get(bib, "volume", default="")
                    pages = safe_get(bib, "pages", default="")
                    year = safe_get(bib, "pub_year", "year", default=base_year)

                    pubs.append({
                        "title": title or "",
                        "authors": authors or "",
                        "journal": journal or "",
                        "year": year or "",
                        "volume": volume or "",
                        "pages": pages or ""
                    })

                    # 완료 표시
                    done_keys.add(stable_key(title, str(year)))
                    success = True
                    processed_this_run += 1

                    # 성공 시 랜덤 슬립
                    time.sleep(random.uniform(SLEEP_MIN, SLEEP_MAX))
                    break

                except Exception as e:
                    last_err = e
                    # 실패 시 백오프(점점 길게)
                    backoff = BACKOFF_BASE_SECONDS * attempt + random.uniform(0, 10)
                    print(f"  Attempt {attempt}/{MAX_RETRIES_PER_PUB} failed: {e}")
                    print(f"  Backing off for {backoff:.1f}s")
                    time.sleep(backoff)

            if not success:
                print("Skip one publication:", last_err)
                # 스킵해도 너무 빠르게 다음으로 가지 않게 약간 쉼
                time.sleep(random.uniform(5, 10))

            # 중간 저장
            if (len(pubs) % SAVE_EVERY) == 0:
                save_checkpoint(done_keys, pubs)
                print(f"Checkpoint saved ({len(pubs)} pubs).")

        # 최종 저장
        # 중복 제거(키 기반)
        unique = {}
        for p in pubs:
            kk = stable_key(p.get("title", ""), str(p.get("year", "")))
            if kk not in unique:
                unique[kk] = p
        pubs_unique = list(unique.values())

        final_save(pubs_unique)
        save_checkpoint(done_keys, pubs_unique)

        print(f"DONE — {OUT_PATH} created! Total saved: {len(pubs_unique)}")

    except Exception as e:
        print("ERROR:", e)
        # 에러 나도 지금까지는 저장
        save_checkpoint(done_keys, pubs)
        print("Checkpoint saved due to error.")

if __name__ == "__main__":
    main()