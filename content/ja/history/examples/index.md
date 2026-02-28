---
type: landing
toc: false
reading_time: false
share: false

sections:
  - block: markdown
    content:
      title: ""
      text: |-

        {{< rawhtml >}}
        <style>
        .examples-col{
          margin-bottom:60px;
        }

        .examples-col h3{
          margin:0 0 8px 0;
        }

        .examples-col hr{
          margin:0 0 18px 0;
        }

        .examples-list{
          display:flex;
          flex-direction:column;
          gap:22px;
        }

        .examples-item{
          display:grid;
          grid-template-columns:220px 1fr;
          column-gap:18px;
          align-items:center; /* ← 세로 가운데 정렬 */
        }

        .examples-item img{
          width:220px;
          height:150px;
          object-fit:cover;
          border-radius:8px;
          display:block;
          margin:0;
        }

        .examples-caption{
          margin:0;
          line-height:1.55;
          text-align: justify;         /* ← 양쪽 정렬 */
          text-justify: inter-word;
          hyphens: auto;
          overflow-wrap:anywhere;
          word-break:break-word;
        }
        </style>
        {{< /rawhtml >}}

        {{< banner_title "動作例" >}}

        {{< rawhtml >}}

        <!-- 形状記憶効果 -->
        <div class="examples-col">
          <h3>形状記憶効果</h3>
          <hr>
          <div class="examples-list">

            <div class="examples-item">
              <img src="/~sma_lab/images/sma1.png">
              <div class="examples-caption">(1) 記憶処理された形状のバネ状形状記憶合金</div>
            </div>

            <div class="examples-item">
              <img src="/~sma_lab/images/sma2.png">
              <div class="examples-caption">(2) 室温(マルテンサイト変態温度以下)で負荷を加えると形状が変化する。</div>
            </div>

            <div class="examples-item">
              <img src="/~sma_lab/images/sma3.png">
              <div class="examples-caption">(3) 十分に変形した後、力を除いた状態の形状</div>
            </div>

            <div class="examples-item">
              <img src="/~sma_lab/images/sma4.png">
              <div class="examples-caption">(4) 逆変態温度以上に加熱すると、元の記憶した形状に戻っていく。(1/3の形状回復)</div>
            </div>

            <div class="examples-item">
              <img src="/~sma_lab/images/sma5.png">
              <div class="examples-caption">(5) 加熱を続ける。(2/3の形状回復)</div>
            </div>

            <div class="examples-item">
              <img src="/~sma_lab/images/sma6.png">
              <div class="examples-caption">(6) 加熱を続ける。(完全に元の形状に回復)</div>
            </div>

          </div>
        </div>

        <!-- 超弾性効果 -->
        <div class="examples-col">
          <h3>超弾性効果</h3>
          <hr>
          <div class="examples-list">

            <div class="examples-item">
              <img src="/~sma_lab/images/sp1.png">
              <div class="examples-caption">(1) 加熱直後(逆変態温度以上)でも荷重を加えるとマルテンサイト変態誘起により変形する。</div>
            </div>

            <div class="examples-item">
              <img src="/~sma_lab/images/sp2.png">
              <div class="examples-caption">(2) 逆変態温度以上なので、除荷するだけで元の構造に逆変態し、形状は元に戻る。</div>
            </div>

          </div>
        </div>

        {{< /rawhtml >}}
---