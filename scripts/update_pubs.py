from scholarly import scholarly, ProxyGenerator
import json
import os
import time

# 👉 너가 준 Google Scholar ID
SCHOLAR_ID = "MAB85ZYAAAAJ"

print("START fetching publications...")

# --- Google Scholar 차단 방지 설정 (핵심) ---
pg = ProxyGenerator()
pg.FreeProxies()   # 무료 프록시 자동 사용
scholarly.use_proxy(pg)

os.makedirs("data", exist_ok=True)

try:
    # 1) 저자 찾기
    author = scholarly.search_author_id(SCHOLAR_ID)
    print("Author found")

    # 2) 논문 목록 가져오기
    author = scholarly.fill(author, sections=["publications"])
    publications = author.get("publications", [])
    print("Total publications found:", len(publications))

    pubs = []

    # 3) 논문 상세정보 하나씩 가져오기
    for i, pub in enumerate(publications):
        print(f"Fetching {i+1}/{len(publications)}")
        try:
            filled = scholarly.fill(pub)
            bib = filled.get("bib", {})

            journal = bib.get("journal", "") or bib.get("venue", "")
            volume = bib.get("volume", "")
            pages = bib.get("pages", "")
            year = bib.get("pub_year", "")

            pubs.append({
                "title": bib.get("title", ""),
                "authors": bib.get("author", ""),
                "journal": journal,
                "year": year,
                "volume": volume,
                "pages": pages
            })

            time.sleep(2)  # 과도한 요청 방지 (중요)

        except Exception as e:
            print("Skip one publication:", e)

    # 4) 최신순 정렬 후 저장
    pubs_sorted = sorted(pubs, key=lambda x: str(x.get("year", "")), reverse=True)

    with open("data/publications.json", "w", encoding="utf-8") as f:
        json.dump(pubs_sorted, f, ensure_ascii=False, indent=2)

    print("DONE — publications.json created!")

except Exception as e:
    print("ERROR:", e)
