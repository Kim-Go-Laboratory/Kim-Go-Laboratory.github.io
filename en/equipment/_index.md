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

<h3>Sample Preparation Equipment</h3>
<hr>

<div class="table-scroll">
<table class="equip-table">
<tr><td>Arc Melting Furnace||Used to produce alloy buttons by arc melting metals. The alloy composition and impurity removal at this stage largely determine the quality of the final alloy.</td></tr>
<tr><td>Electric Furnaces||Used for heat treatment of alloys. Various furnaces are available, including high-temperature furnaces and long-term aging furnaces.</td></tr>
<tr><td>Wire Electrical Discharge Machine (Wire-EDM)||Performs complex and precise machining using arc discharge.</td></tr>
<tr><td>Cold Rolling Mill||Used for cold rolling of bulk samples through roll processing.</td></tr>
<tr><td>Rotary Polishing Machine||Used for surface polishing of samples for microstructural observation.</td></tr>
</table>
</div>

<h3>Characterization and Property Evaluation Equipment</h3>
<hr>

<div class="table-scroll">
<table class="equip-table">
<tr><td>Tensile Testing Machine||Used for tensile testing of metallic materials to investigate deformation behavior and mechanical properties.</td></tr>
<tr><td>Fatigue Testing Machine||Evaluates the fatigue properties of metallic materials under cyclic loading.</td></tr>
<tr><td>Optical Microscope||Used for observing surface microstructures of samples. Observation is possible up to 1000× magnification. With the attached XYZ linear stage, precise dimensional measurements can also be performed.</td></tr>
<tr><td>Scanning Electron Microscope (SEM-EBSD)||A microscope that observes images obtained from electrons reflected after irradiating the sample with an electron beam. Suitable for observing surface morphology and for crystal orientation analysis.</td></tr>
<tr><td>X-ray Diffractometer (XRD)||Used for phase identification and for examining lattice parameters and crystallographic orientation distributions. Measurements can be performed from low to high temperatures.</td></tr>
<tr><td>Thermomechanical Analyzer (TMA)||Evaluates mechanical properties under varying temperature and load conditions. Shape memory properties can be analyzed from temperature–strain curves.</td></tr>
<tr><td>Differential Scanning Calorimeter (DSC)||Measures phase transformation temperatures and associated heat in metals. Low- to mid-temperature DSC is used for martensitic transformation temperatures, while high-temperature DSC is used for melting points and order–disorder transformations.</td></tr>
<tr><td>Hardness Tester||Performs indentation hardness tests such as Vickers hardness and Knoop hardness measurements.</td></tr>
</table>
</div>

<h3>Shared Facilities</h3>
<hr>

<div class="table-scroll">
<table class="equip-table">
<tr><td>Electron Probe Microanalyzer (EPMA)||Measures the composition of fabricated alloys, ribbons, thin films, and other materials.</td></tr>
<tr><td>X-ray Photoelectron Spectroscopy (XPS)||Determines elemental composition, chemical bonding states, and electronic states of solid sample surfaces by measuring the kinetic energy of photoelectrons emitted under ultra-high vacuum conditions via the photoelectric effect.</td></tr>
<tr><td>Focused Ion Beam (FIB)||Processes sample surfaces by sputtering with an ion beam. This technique is used to prepare specimens for TEM observation.</td></tr>
<tr><td>Transmission Electron Microscope (TEM)||Observes magnified images formed by electrons transmitted through a sample. With lattice imaging resolution down to 0.1 nm, atomic arrangements can be observed. Using heating and cooling holders, in-situ observation of phase transformations is also possible.</td></tr>
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