<br><br><br><br>
## 試料作製関連
---
<table class="equip-table">
<tr><td>非消耗電極型アーク炉||金属をアーク溶解してボタン材を作ります。ここでの配合、不純物除去で出来上がる

合金の良し悪しが決まります。 </td></tr>
<tr><td>各種電気炉||合金の熱処理を行います。高温用や長時間時効用など各種の電気炉があります。</td></tr>
<tr><td>ワイヤー放電加工機||アーク放電を用いて複雑かつ精密な加工を行います。</td></tr>
<tr><td>冷間圧延機||ロール圧延により、バルク試料の冷間圧延を行います。</td></tr>
<tr><td>回転研磨機||金属組織観察のため表面研磨を行うのに用います。</td></tr>
</table>

## 特性評価関連
---
<table class="equip-table">
  <tr><td>引張試験機||形状記憶合金の引張り試験をします。形状記憶合金の変形挙動や金属としての一般的機械特性を調べます。</td></tr>
  <tr><td>疲労試験機||金属材料の繰返し荷重に対する強さを評価できます。</td></tr>
  <tr><td>光学顕微鏡||試料表面の組織観察に用います。最大1000倍までの観察ができます。付属のXYZリニアステージを用いることで対象物の精密な形状測定が可能です。</td></tr>
  <tr><td>走査型電子顕微鏡 (SEM-EBSD)||試料に電子線をあて、反射してきた電子から得られる像を観察する顕微鏡です。試料表面の形状や表面近傍の内部構造を観察するのに適しています。</td></tr>
  <tr><td>X線回折装置||相同定を行ったり、結晶の格子定数や方位分布を調べることができます。低温から高温まで測定が可能です。</td></tr>
  <tr><td>熱機械分析装置||温度や荷重を変えて機械的特性を調べることができます。温度-歪み曲線などから形状記憶特性の評価を行います。</td></tr>
  <tr><td>示差走査熱量計 (DSC)||金属の相変態温度及びその熱量を測ります。マルテンサイト変態温度などが調べられる中低温用と、融点や規則-不規則変態などが調べられる高温用があります。</td></tr>
  <tr><td>硬度測定試験機||ビッカース硬度、ヌープ硬度などの圧痕式硬度試験を行います。</td></tr>

</table>

## 共通設備
---
<table class="equip-table">
  <tr><td>電子線マイクロアナライザ (EPMA)||作製した合金、リボン、薄膜などの組成を測定します。</td></tr>
    <tr><td>X線光電子分光装置 (XPS)||超高真空中におかれた固体試料表面に電磁波を照射し、光電効果により真空中に放出される光電子の運動エネルギーを測定することによって、試料表面の元素分析や元素の結合状態、存在状態を判定するための装置です。</td></tr>
  <tr><td>集束イオンビーム (FIB)||イオンビームを試料面に照射してスパッタリングすることによって試料表面の加工を行います。この加工によってTEM観察用の試料を作製することができます。</td></tr>
  <tr><td>透過型電子顕微鏡 (TEM)||試料に電子線をあて、試料を透過した電子による像を拡大して観察する顕微鏡です。格子像で0.1nmの高分解能を持つ電子顕微鏡であり、原子配列の観察が可能です。加熱冷却フォルダを用いることにより、相変態をその場で観察することもできます。</td></tr>
</table>



<script>
document.addEventListener("DOMContentLoaded", function(){

  document.querySelectorAll(".equip-table").forEach(table => {
    let rows = table.querySelectorAll("tr");

    rows.forEach((tr, index) => {
      let cell = tr.querySelector("td");
      if(!cell) return;

      let text = cell.textContent;

      // 이름과 비고 분리
      let parts = text.split("||");
      let name = parts[0].trim();
      let note = parts[1] ? parts[1].trim() : "";

      tr.innerHTML = "";

      let tdNo = document.createElement("td");
      tdNo.className = "equip-no";
      tdNo.textContent = index + 1;

      let tdName = document.createElement("td");
      tdName.className = "equip-name";
      tdName.textContent = name;

      let tdNote = document.createElement("td");
      tdNote.className = "equip-note";
      tdNote.textContent = note || "—";

      tr.appendChild(tdNo);
      tr.appendChild(tdName);
      tr.appendChild(tdNote);
    });
  });

});
</script>

