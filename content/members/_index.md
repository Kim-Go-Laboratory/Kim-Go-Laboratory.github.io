---

---

{{< banner_title "Members" >}}

{{< rawhtml >}}
<style>
.section-bar{
  margin: 18px 0 10px;
  padding: 8px 12px;
  font-weight: 700;
}

/* ✅ 페이지 깨짐 방지 핵심: wrap이 스크롤을 담당 */
.table-wrap{
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 18px;
}

/* ✅ 테이블은 100% + 내용이 길면 자연스럽게 넓어지게 */
.members-table,
.researcher-table,
.student-table{
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
  white-space: nowrap;     /* 링크/짧은 컬럼 줄바꿈 방지 */
}

.members-table td,
.researcher-table td,
.student-table td{
  border: 1px solid #e5e5e5;
  padding: 10px 12px;
  vertical-align: middle;
  line-height: 1.5;
}

/* ✅ 2~3열(이름/기관 등)은 줄바꿈 허용해서 너무 길면 내려가게 */
.researcher-table td:nth-child(2),
.researcher-table td:nth-child(3),
.student-table td:nth-child(2),
.student-table td:nth-child(3){
  white-space: normal;
}

/* Staff 테이블: 1열 직급 강조 */
.members-table td:nth-child(1){
  font-weight: 600;
  background: #fafafa;
}

.members-table a,
.researcher-table a,
.student-table a{
  text-decoration: none;
}

@media (max-width: 640px){
  .members-table td,
  .researcher-table td,
  .student-table td{
    padding: 10px 10px;
  }
}
</style>

<div class="section-bar">Staff</div>

<div class="table-wrap">
  <table class="members-table">
    <tbody>
      <tr>
        <td>Professor</td>
        <td>Heeyoung Kim</td>
        <td><a href="https://trios.tsukuba.ac.jp/en/researcher/0000000798">Profile</a></td>
        <td><a href="mailto:heeykim@ims.tsukuba.ac.jp">E-mail</a></td>
        <td><a href="https://scholar.google.com/citations?user=MAB85ZYAAAAJ&hl=ja" target="_blank" rel="noopener">Google Scholar</a></td>
      </tr>
      <tr>
        <td>Assistant Professor</td>
        <td>Jongbin Go</td>
        <td><a href="https://trios.tsukuba.ac.jp/ja/researcher/0000005178">Profile</a></td>
        <td><a href="mailto:go.jongbin.gn@u.tsukuba.ac.jp">E-mail</a></td>
        <td><a href="https://scholar.google.com/citations?user=DJz0gHQAAAAJ&hl=ja" target="_blank" rel="noopener">Google Scholar</a></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="section-bar">Researcher</div>

<div class="researcher-group">
  <ul class="researcher-list">
    <li>Postdoctoral Researcher||Ricardo D. Parga Montemayor||</li>
    <li>Visiting Scholar||Karol Marek Golasiński||Cardinal Stefan Wyszynski University in Warsaw</li>
  </ul>
</div>

<div class="section-bar">Student</div>

<div class="student-group">
  <ul class="student-list">
    <li>M2||Hiroto Tanaka||</li>
    <li>M2||Ami Furuhashi||</li>
    <li>M2||Takanao Nambu||</li>
    <li>Visiting Student (M1)||French||XX University</li>
  </ul>
</div>

<div class="student-group">
  <ul class="student-list">
    <li>M1||Toru Kurisaki||</li>
    <li>M1||Yu Hayashi||</li>
    <li>M1||Taketo Yamaguchi||</li>
  </ul>
</div>

<div class="student-group">
  <ul class="student-list">
    <li>B4||Tsukasa Katayanagi||</li>
    <li>B4||Shotaro Fukumitsu||</li>
    <li>B4||Gaku Otsuka||</li>
    <li>B4||Kazuki Takahashi||</li>
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