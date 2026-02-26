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
        .justify-text p{
          text-align: justify;
          text-justify: inter-word;
          hyphens: auto;
          line-height: 1.75;
          margin-bottom: 1.2em;
        }
        .justify-text h3{
          margin-top: 2.2em;
          margin-bottom: 0.8em;
        }
        </style>
        <div class="justify-text">
        {{< /rawhtml >}}

        ### Martensitic Transformation

        　The shape memory effect is closely related to martensitic transformation. A martensitic transformation is a type of solid-state crystallographic phase transformation that occurs without atomic diffusion. Because diffusion does not take place, the atoms move cooperatively in a coordinated manner. As a result, a pseudo-shear deformation accompanied by a slight volume change is produced. This deformation serves as the driving force behind the shape memory effect.

        　In general, the martensitic transformation observed in shape memory alloys is specifically referred to as a thermoelastic martensitic transformation. With the exception of certain ferrous alloys, the temperature hysteresis between forward and reverse transformations is small, typically ranging from several to several tens of degrees. Furthermore, the interface between the martensite phase and the parent phase has good coherency, and the martensite variants can easily reorient under low stress. Therefore, dislocations that would cause permanent deformation are not formed. These characteristics constitute one of the essential conditions for the shape memory effect.

        ### Shape Memory Mechanism

        <figure style="float:right; width:45%; margin: 0 0 1em 2em; text-align:center;">
          <img src="/images/sma.png" style="width:100%;" />
          <figcaption style="font-size:1.0em; margin-top:0.5em;color:inherit;">
            Figure 1. Mechanisms of the shape memory effect and superelasticity
          </figcaption>
        </figure>

        　For simplicity, let us examine the operation of the shape memory effect using a two-dimensional crystal model.

        　First, when the parent phase shown in Fig. 1(a) is cooled below the Mf temperature, it transforms into the martensite phase shown in Fig. 1(b). In an actual three-dimensional crystal, 24 crystallographic variants of martensite are formed. Variants are martensite crystals that share the same crystal structure but differ in crystallographic orientation. In Fig. 1(b), two variants, labeled A and B, are illustrated. Each individual variant exhibits shear strain relative to the original parent phase. However, the variants formed during cooling self-accommodate in such a way that their strains mutually compensate. As a result, there is no macroscopic change in the specimen shape.

        　In thermoelastic martensitic transformations observed in shape memory alloys, the boundary between variants A and B can move easily under low stress. Therefore, in the martensitic state, the specimen becomes soft and deformable, similar to rubber. When an external force is applied, the favorably oriented variant grows at the expense of the other variant, as shown in Fig. 1(c), leading to macroscopic shear deformation of the specimen. When this deformed specimen is heated, all martensite transforms back to the parent phase through reverse transformation, and the specimen completely recovers its original shape as shown in Fig. 1(a). This is the shape memory effect.

        　Martensite generally forms upon cooling below the transformation temperature. However, even above the transformation temperature, the application of external stress can induce martensitic transformation. As described above, because martensitic transformation is driven by shear deformation, applied stress assists the transformation. Therefore, when stress is applied at temperatures above the Af temperature, the transformation proceeds directly from Fig. 1(a) to Fig. 1(c), forming only the favorably oriented martensite variant and producing macroscopic shear strain. At temperatures above the reverse transformation temperature, the martensite phase is energetically unstable. Thus, simply removing the applied stress causes the material to return from Fig. 1(c) to Fig. 1(a), reverting to the parent phase. Repetition of this process makes the material appear to exhibit elastic strains of several tens of percent. This phenomenon is known as superelasticity.

        {{< rawhtml >}}
        </div>
        {{< /rawhtml >}}

        {{< banner_title "Mechanism" >}}

---