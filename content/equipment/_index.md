---

---

{{< banner_title "Equipment" >}}

{{< rawhtml >}}

<style>
/* Scroll wrapper (모바일에서 잘리지 않게) */
.table-scroll{
  width:100%;
  overflow-x:auto;
  -webkit-overflow-scrolling:touch;
}

/* Table overall */
.equip-table{
  width:100%;
  border-collapse:collapse;
  margin-bottom:28px;
}

.equip-table td{
  border:1px solid #e5e5e5;
  padding:10px 14px;
  vertical-align:middle; /* center → middle (정상값) */
}

/* Column styling */
.equip-no{
  width:40px;
  text-align:center;
  font-weight:600;
  background:#fafafa;
}

.equip-name{
  width:260px;
  font-weight:600;
}

.equip-note{
  text-align:justify;
  text-justify:inter-word;
  hyphens:auto;
  line-height:1.6;
}

/* Section spacing */
h2{
  margin-top:24px;
}

/* =========================
   Mobile Optimization
   ========================= */
@media (max-width: 640px){

  .equip-no{
    width:36px;
  }

  .equip-name{
    width:auto; /* 고정 260px 해제 */
  }

  .equip-note{
    text-align:left;  /* justify 해제 */
    hyphens:none;
    word-break:keep-all;
  }

}
</style>

<h3>試料作製関連</h3>
<hr>

<div class="table-scroll">
<table class="equip-table">
<tr><td>非消耗電極型アーク炉||金属をアーク溶解してボタン材を作製します。ここでの配合や不純物除去の良し悪しが、最終合金の品質を大きく左右します。</td></tr>
<tr><td>各種電気炉||合金の熱処理に用います。高温炉や長時間時効炉など、各種の電気炉があります。</td></tr>
<tr><td>ワイヤー放電加工機||アーク放電を用いて、複雑かつ高精度な加工を行います。</td></tr>
<tr><td>冷間圧延機||ロール圧延により、バルク試料の冷間圧延を行います。</td></tr>
<tr><td>回転研磨機||金属組織観察のための表面研磨に用います。</td></tr>
</table>
</div>

<h3>特性評価関連</h3>
<hr>

<div class="table-scroll">
<table class="equip-table">
<tr><td>引張試験機||形状記憶合金の引張試験を行い、変形挙動や一般的な機械特性を評価します。</td></tr>
<tr><td>疲労試験機||金属材料の繰返し荷重に対する強さ（疲労特性）を評価します。</td></tr>
<tr><td>光学顕微鏡||試料表面の組織観察に用います。最大1000倍まで観察可能です。付属のXYZリニアステージにより、精密な寸法測定も行えます。</td></tr>
<tr><td>走査型電子顕微鏡 (SEM-EBSD)||試料に電子線を照射し、反射電子などから得られる像を観察します。表面形状や表面近傍の内部構造観察に適しています。</td></tr>
<tr><td>X線回折装置||相同定、格子定数、結晶方位分布の評価に用います。低温から高温まで測定可能です。</td></tr>
<tr><td>熱機械分析装置 (TMA)||温度や荷重を変化させながら機械的特性を評価します。温度-ひずみ曲線などから形状記憶特性の解析が可能です。</td></tr>
<tr><td>示差走査熱量計 (DSC)||金属の相変態温度および変態熱を測定します。中低温DSCはマルテンサイト変態温度、高温DSCは融点や規則-不規則変態などの評価に用います。</td></tr>
<tr><td>硬度計||ビッカース硬度、ヌープ硬度などの圧痕硬度試験を行います。</td></tr>
</table>
</div>

<h3>共通設備</h3>
<hr>

<div class="table-scroll">
<table class="equip-table">
<tr><td>電子線マイクロアナライザ (EPMA)||作製した合金、リボン、薄膜などの組成を測定します。</td></tr>
<tr><td>X線光電子分光装置 (XPS)||超高真空中で固体試料表面にX線を照射し、光電効果で放出される光電子の運動エネルギーを測定します。表面の元素組成、化学結合状態、電子状態を解析できます。</td></tr>
<tr><td>集束イオンビーム (FIB)||イオンビームによるスパッタリングで試料表面を加工します。TEM観察用試料の作製などに用います。</td></tr>
<tr><td>透過型電子顕微鏡 (TEM)||試料を透過した電子による像を拡大して観察します。格子像で0.1 nmの分解能を持ち、原子配列の観察が可能です。加熱・冷却ホルダーにより、相変態のその場観察も行えます。</td></tr>
</table>
</div>

<script>
document.addEventListener("DOMContentLoaded", function(){

  document.querySelectorAll(".equip-table").forEach(table => {
    let rows = table.querySelectorAll("tr");

    rows.forEach((tr, index) => {
      let cell = tr.querySelector("td");
      if(!cell) return;

      let text = cell.textContent;

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

{{< /rawhtml >}}