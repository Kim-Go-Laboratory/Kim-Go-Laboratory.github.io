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
          align-items:center;
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
          text-align: justify;
          text-justify: inter-word;
          hyphens: auto;
          overflow-wrap:anywhere;
          word-break:break-word;
        }
        </style>
        {{< /rawhtml >}}

        {{< banner_title "Examples" >}}

        {{< rawhtml >}}

        <!-- Shape Memory Effect -->
        <div class="examples-col">
          <h3>Shape Memory Effect</h3>
          <hr>
          <div class="examples-list">

            <div class="examples-item">
              <img src="/images/sma1.png">
              <div class="examples-caption">(1) A spring-shaped shape memory alloy after shape-setting (training) treatment</div>
            </div>

            <div class="examples-item">
              <img src="/images/sma2.png">
              <div class="examples-caption">(2) At room temperature (below the martensitic transformation temperature), applying a load changes the shape.</div>
            </div>

            <div class="examples-item">
              <img src="/images/sma3.png">
              <div class="examples-caption">(3) Shape after sufficient deformation, with the load removed</div>
            </div>

            <div class="examples-item">
              <img src="/images/sma4.png">
              <div class="examples-caption">(4) When heated above the reverse transformation temperature, it begins to return to the memorized shape. (1/3 recovery)</div>
            </div>

            <div class="examples-item">
              <img src="/images/sma5.png">
              <div class="examples-caption">(5) Continue heating. (2/3 recovery)</div>
            </div>

            <div class="examples-item">
              <img src="/images/sma6.png">
              <div class="examples-caption">(6) Continue heating. (Full recovery to the original shape)</div>
            </div>

          </div>
        </div>

        <!-- Superelasticity -->
        <div class="examples-col">
          <h3>Superelasticity</h3>
          <hr>
          <div class="examples-list">

            <div class="examples-item">
              <img src="/images/sp1.png">
              <div class="examples-caption">(1) Even immediately after heating (above the reverse transformation temperature), applying a load causes deformation due to stress-induced martensitic transformation.</div>
            </div>

            <div class="examples-item">
              <img src="/images/sp2.png">
              <div class="examples-caption">(2) Because the temperature is above the reverse transformation temperature, simply unloading triggers reverse transformation back to the parent phase, and the shape returns to the original.</div>
            </div>

          </div>
        </div>

        {{< /rawhtml >}}
---