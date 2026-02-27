---

---

{{< banner_title "Members" >}}

{{< rawhtml >}}
<style>
/* ✅ section-bar 색은 유지: margin/padding만 */
.section-bar{
  margin: 18px 0 10px;
  padding: 8px 12px;
}

/* ✅ Equipment 방식: 가로 스크롤 래퍼 */
.table-wrap{
  width:100%;
  overflow-x:auto;
  -webkit-overflow-scrolling:touch;
  margin-bottom:18px;
}

/* 공통 테이블 */
.members-table,
.researcher-table,
.student-table{
  width:100%;
  border-collapse:collapse;
  table-layout:auto;
  margin-bottom: 0; /* wrap이 margin-bottom을 가짐 */
}

/* 공통 셀 */
.members-table td,
.researcher-table td,
.student-table td{
  border:1px solid #e5e5e5;
  padding:10px 12px;
  vertical-align:middle;
  line-height:1.6;
}

/* Staff 테이블: 1열 강조 */
.members-table td:nth-child(1){
  font-weight:600;
  white-space:nowrap;
}

/* 링크 */
.members-table a,
.researcher-table a,
.student-table a{
  text-decoration:none;
}

/* 연구원/학생: 이름/기관 줄바꿈 허용 */
.researcher-table td:nth-child(2),
.researcher-table td:nth-child(3),
.student-table td:nth-child(2),
.student-table td:nth-child(3){
  white-space:normal;
}

/* ✅ Equipment 방식: 본문(긴 설명/소속) 문단 스타일 */
.researcher-table td,
.student-table td{
  text-align:justify;
  text-justify:inter-word;
  hyphens:auto;
}

/* ✅ Mobile Optimization (Equipment 방식) */
@media (max-width: 640px){
  .members-table td,
  .researcher-table td,
  .student-table td{
    padding:10px 10px;
  }

  /* 모바일에서는 justify 해제 + 가독성 */
  .researcher-table td,
  .student-table td{
    text-align:left;
    hyphens:none;
    word-break:keep-all;
  }
}

/* =========================
   ✅ FIX: Mobile table overlap / vertical letters
   ========================= */

/* 1) Staff(5열) 테이블: 모바일에서는 줄이지 말고 스크롤로 넘기기 */
.members-table{ table-layout: auto; } /* 일단 auto 유지 */

/* 모바일에서 가로 스크롤이 생기도록 최소 폭 확보 */
@media (max-width: 900px){
  .members-table{ min-width: 760px; }
  .researcher-table, .student-table{ min-width: 720px; }
}

/* 2) "글자 단위로 세로로 떨어지는" 현상 방지
   (전역 overflow-wrap:anywhere 같은 걸 이 영역에서 무력화) */
.members-table td,
.researcher-table td,
.student-table td{
  word-break: normal;        /* 글자 단위 분해 금지 */
  overflow-wrap: normal;     /* anywhere 무력화 */
}

/* 3) Researcher/Student 이름 칸은 단어 단위 줄바꿈만 허용 */
.researcher-table td:nth-child(2),
.student-table td:nth-child(2){
  white-space: normal;
  overflow-wrap: break-word; /* 너무 길면 단어 단위로만 끊기 */
  word-break: normal;
}

/* 4) Staff 테이블에서 링크 칼럼은 짧게 유지(겹침 방지) */
.members-table td:nth-child(3),
.members-table td:nth-child(4),
.members-table td:nth-child(5){
  white-space: nowrap;       /* Profile / E-mail / Scholar는 한 덩어리로 */
}
</style>

<div class="section-bar">教員</div>

<div class="table-wrap">
  <table class="members-table">
    <tbody>
      <tr>
        <td>教授</td>
        <td>金 熙榮（きむ へよん）</td>
        <td><a href="https://trios.tsukuba.ac.jp/en/researcher/0000000798">Profile</a></td>
        <td><a href="mailto:heeykim@ims.tsukuba.ac.jp">E-mail</a></td>
        <td><a href="https://scholar.google.com/citations?user=MAB85ZYAAAAJ&hl=ja" target="_blank" rel="noopener">Google Scholar</a></td>
      </tr>
      <tr>
        <td>助教</td>
        <td>高 鍾斌（ご じょんびん）</td>
        <td><a href="https://trios.tsukuba.ac.jp/ja/researcher/0000005178">Profile</a></td>
        <td><a href="mailto:go.jongbin.gn@u.tsukuba.ac.jp">E-mail</a></td>
        <td><a href="https://scholar.google.com/citations?user=DJz0gHQAAAAJ&hl=ja" target="_blank" rel="noopener">Google Scholar</a></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="section-bar">研究員</div>

<div class="researcher-group">
  <ul class="researcher-list">
    <li>Postdoctoral Researcher||Ricardo D. Parga Montemayor||</li>
    <li>Visiting Scholar||Karol Marek Golasiński||Cardinal Stefan Wyszynski University in Warsaw</li>
  </ul>
</div>

<div class="section-bar">学生</div>

<div class="student-group">
  <ul class="student-list">
    <li>M2||田中　大翔 (たなか ひろと)||</li>
    <li>M2||古橋　愛実 (ふるはし あみ)||</li>
    <li>M2||南部　孝尚 (なんぶ たかなお)||</li>
  </ul>
</div>

<div class="student-group">
  <ul class="student-list">
    <li>M1||栗崎　透 (くりさき とおる)||</li>
    <li>M1||林　悠 (はやし ゆう)||</li>
    <li>M1||山口　毅人 (やまぐち たけと)||</li>
  </ul>
</div>

<div class="student-group">
  <ul class="student-list">
    <li>B4||片柳　司 (かたやなぎ つかさ)||</li>
    <li>B4||福満　翔太郎 (ふくみつ しょうたろう)||</li>
    <li>B4||大塚　岳 (おおつか がく)||</li>
    <li>B4||高橋　和己 (たかはし かずき)||</li>
  </ul>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {

  function listToTable({ groupSelector, listSelector, tableClass }) {
    const groups = document.querySelectorAll(groupSelector);
    if (!groups.length) return;

    const allLis = document.querySelectorAll(`${groupSelector} ${listSelector} li`);
    if (!allLis.length) return;

    const wrap = document.createElement("div");
    wrap.className = "table-wrap";

    const table = document.createElement("table");
    table.className = tableClass;

    const tbody = document.createElement("tbody");

    allLis.forEach(li => {
      const parts = li.textContent.split("||");
      const col1 = (parts[0] || "").trim();
      const col2 = (parts[1] || "").trim();
      const col3 = (parts[2] || "").trim();

      const tr = document.createElement("tr");
      tr.innerHTML = `<td>${col1 || "—"}</td><td>${col2 || "—"}</td><td>${col3 || "—"}</td>`;
      tbody.appendChild(tr);
    });

    table.appendChild(tbody);
    wrap.appendChild(table);

    groups[0].parentNode.insertBefore(wrap, groups[0]);
    groups.forEach(g => g.remove());
  }

  listToTable({
    groupSelector: ".researcher-group",
    listSelector: ".researcher-list",
    tableClass: "researcher-table"
  });

  listToTable({
    groupSelector: ".student-group",
    listSelector: ".student-list",
    tableClass: "student-table"
  });

});
</script>
{{< /rawhtml >}}