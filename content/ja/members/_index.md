---

---

{{< banner_title "Members" >}}

<div class="section-bar">教官</div>

<div class="table-wrap">
  <table class="members-table">
    <tbody>
      <tr>
        <td>教授</td>
        <td>金 照榮（きむ へよん）</td>
        <td><a href="https://trios.tsukuba.ac.jp/en/researcher/0000000798">Profile</a></td>
        <td><a href="mailto:heeykim@ims.tsukuba.ac.jp">E-mail</a></td>
        <td><a href="https://scholar.google.com/citations?user=MAB85ZYAAAAJ&hl=ja" target="_blank" rel="noopener">Google Scholar</a></td>
      </tr>
      <tr>
        <td>助教</td>
        <td>高 鍾斌（ご じょんびん）</td>
        <td><a href="https://trios.tsukuba.ac.jp/ja/researcher/0000005178">Profile</a></td>
        <td><a href="mailto:go.jongbin.gn@u.tsukuba.ac.jp">E-mail</td>
        <td><a href="https://scholar.google.com/citations?user=DJz0gHQAAAAJ&hl=ja" target="_blank" rel="noopener">Google Scholar</td>
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

{{< rawhtml >}}
<script>
document.addEventListener("DOMContentLoaded", () => {

  function listToTable({ groupSelector, listSelector, tableClass }) {
    const groups = document.querySelectorAll(groupSelector);
    if (!groups.length) return;

    const allLis = document.querySelectorAll(`${groupSelector} ${listSelector} li`);
    if (!allLis.length) return;

    // ✅ table-wrap로 감싸서 모바일에서도 안전하게 스크롤되게
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

    // 첫 group 위치에 wrap+table 넣고, 기존 group 전부 삭제
    groups[0].parentNode.insertBefore(wrap, groups[0]);
    groups.forEach(g => g.remove());
  }

  // 연구원 표 만들기
  listToTable({
    groupSelector: ".researcher-group",
    listSelector: ".researcher-list",
    tableClass: "researcher-table"
  });

  // 학생 표 만들기
  listToTable({
    groupSelector: ".student-group",
    listSelector: ".student-list",
    tableClass: "student-table"
  });

});
</script>
{{< /rawhtml >}}