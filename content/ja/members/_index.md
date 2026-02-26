---

---

{{< banner_title "Members" >}}

{{< rawhtml >}}
<style>
/* ✅ 테마의 section-bar(파란계통) 색을 건드리지 않기 위해
   margin/padding만 최소로 조정 (background 지정 X) */
.section-bar{
  margin: 18px 0 10px;
  padding: 8px 12px;
}

/* 모바일에서 잘리지 않게: 숨기지 말고 스크롤 허용 */
.table-wrap{
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 18px;
}

/* 공통 테이블 */
.members-table,
.researcher-table,
.student-table{
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}

/* 셀 스타일 */
.members-table td,
.researcher-table td,
.student-table td{
  border: 1px solid #e5e5e5;
  padding: 10px 12px;
  vertical-align: middle;
  line-height: 1.5;
}

/* Staff 테이블: 1열(직급) 강조 */
.members-table td:nth-child(1){
  font-weight: 600;
  white-space: nowrap;
}

/* 링크 */
.members-table a,
.researcher-table a,
.student-table a{
  text-decoration: none;
}

/* 연구원/학생 표: 이름/기관은 줄바꿈 허용 */
.researcher-table td:nth-child(2),
.researcher-table td:nth-child(3),
.student-table td:nth-child(2),
.student-table td:nth-child(3){
  white-space: normal;
}

/* 모바일 패딩만 살짝 */
@media (max-width: 640px){
  .members-table td,
  .researcher-table td,
  .student-table td{
    padding: 10px 10px;
  }
}
</style>

<div class="section-bar">教官</div>

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
    <li>Visiting Student (M1)||French||XX University</li>
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
      tr.innerHTML = `<td>${col1}</td><td>${col2}</td><td>${col3}</td>`;
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