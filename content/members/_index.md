<br><br><br><br>

## 2026 Members
---

<div class="section-bar">教官</div>
<table class="members-table">
  <tbody>
    <tr>
      <td>教授</td>
      <td>金 照榮（きん ひよん）</td>
      <td><a href="mailto:heeykim@ims.tsukuba.ac.jp">E-mail</a></td>
      <td><a href="https://scholar.google.com/citations?user=MAB85ZYAAAAJ&hl=ja" target="_blank">Google Scholar</a></td>
    </tr>
    <tr>
      <td>助教</td>
      <td>高 鍾斌（ご じょんびん）</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

<div class="section-bar">研究員</div>

<div class="researcher-group">
  <ul class="researcher-list">
    <li>Postdoctoral Researcher||Ricardo P Montemeyor||数理物質系</li>
    <li>Visiting Scholar||Polish||XX University</li>
    
  </ul>
</div>


<div class="section-bar">学生</div>

<div class="student-group">
  <ul class="student-list">
    <li>M2||田中　大翔 (たなか ひろと)||数理物質科学研究群 物性・分子工学サブプログラム</li>
    <li>M2||古橋　愛実 (ふるはし あみ)||数理物質科学研究群 物性・分子工学サブプログラム</li>
    <li>M2||南部　孝尚 (なんぶ たかなお)||数理物質科学研究群 物性・分子工学サブプログラム</li>
    <li>M2||菅谷　龍 (すがや りゅう)||数理物質科学研究群 物性・分子工学サブプログラム</li>
    <li>Visiting Student (M1)||French||XX University</li>

  </ul>
</div>

<div class="student-group">
  <ul class="student-list">
    <li>M1||栗崎　透 (くりさき とおる)||数理物質科学研究群 物性・分子工学サブプログラム</li>
    <li>M1||林　悠 (はやし ゆう)||数理物質科学研究群 物性・分子工学サブプログラム</li>
    <li>M1||山口　毅人 (やまぐち たけと)||数理物質科学研究群 物性・分子工学サブプログラム</li>
  </ul>
</div>

<div class="student-group">
  <ul class="student-list">
    <li>B4||片柳　司 (かたやなぎ つかさ)||応用理工学類 物性工学主専攻</li>
    <li>B4||福満　翔太郎 (ふくみつ しょうたろう)||応用理工学類 物性工学主専攻</li>
    <li>B4||大塚　岳 (おおつか がく)||応用理工学類 物性工学主専攻</li>
    <li>B4||高橋　和己 (たかはし かずき)||応用理工学類 物性工学主専攻</li>
  </ul>
</div>

<script>
(() => {
  function listToTable({ groupSelector, listSelector, tableClass }) {
    const groups = document.querySelectorAll(groupSelector);
    if (!groups.length) return;

    const allLis = document.querySelectorAll(`${groupSelector} ${listSelector} li`);
    if (!allLis.length) return;

    const table = document.createElement("table");
    table.className = `members-table ${tableClass}`;

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

    // 첫 group 위치에 table 넣고, 기존 group 전부 삭제
    groups[0].parentNode.insertBefore(table, groups[0]);
    groups.forEach(g => g.remove());
  }

  // 연구원 표 만들기
  listToTable({
    groupSelector: ".researcher-group",
    listSelector: ".researcher-list",
    tableClass: "researcher-table"
  });

  // 학생 표 만들기 (기존 동작)
  listToTable({
    groupSelector: ".student-group",
    listSelector: ".student-list",
    tableClass: "student-table"
  });
})();
</script>
