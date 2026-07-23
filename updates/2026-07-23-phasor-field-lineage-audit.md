# 23 July 2026 phasor-field theory lineage and venue audit

## Scope

This citation-tracing pass followed the phasor-field branch seeded by the field-defining virtual-wave papers and compared the resulting records against `README.md`, `index.html`, `article/2active.tex`, `article/5newscenes.tex`, `bare_jrnl.tex`, and the consolidated bibliography.

No direct NLOS paper with a verified publication date later than 22 July 2026 was identified. The newest date-verified direct result remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

## Missing survey integration

The repository already listed the preprint of the following theory paper in `README.md`, but the final publication was absent from the website explorer, survey prose, and bibliography:

- Justin Dove and Jeffrey H. Shapiro, “Paraxial theory of phasor-field imaging,” *Optics Express* 27(13), 18016–18037, 2019. DOI: `10.1364/OE.27.018016`.

The paper gives the formal paraxial wave-optics foundation for phasor-field imaging and introduces two-frequency spatial-Wigner-distribution propagation primitives for occlusion and specular transport that the P-field alone cannot represent.

## Final-venue corrections

Four README records were still labeled by their arXiv versions despite verified Optica publications:

1. Syed Azer Reza, Marco La Manna, Sebastian Bauer, and Andreas Velten, “Phasor field waves: experimental demonstrations of wave-like properties,” *Optics Express* 27(22), 32587–32608, 2019. DOI: `10.1364/OE.27.032587`.
2. Justin Dove and Jeffrey H. Shapiro, “Paraxial phasor-field physical optics,” *Optics Express* 28(14), 21095–21109, 2020. DOI: `10.1364/OE.396577`.
3. Justin Dove and Jeffrey H. Shapiro, “Nonparaxial phasor-field propagation,” *Optics Express* 28(20), 29212–29229, 2020. DOI: `10.1364/OE.401203`.
4. Pablo Luesia, Miguel Crespo, Adrian Jarabo, and Albert Redo-Sanchez, “Non-line-of-sight imaging in the presence of scattering media using phasor fields,” *Optics Letters* 47(15), 3796–3799, 2022. DOI: `10.1364/OL.463296`.

## Intended synchronized changes

The guarded synchronizer performs the following operations only when every expected anchor is unique:

- replaces the five preprint records in `README.md` with final publisher links, venues, and contribution summaries;
- adds the five completed records to the website explorer and updates the 2019, 2020, and 2022 timeline narratives;
- inserts a semantically placed literature-review paragraph in the wave-based section of `article/2active.tex`, connecting paraxial theory, experimental validation, physical P-field optics, and nonparaxial Rayleigh–Sommerfeld propagation;
- retains the established `luesiaScatteringPhasor2023` citation key while overriding its metadata with the final 2022 Optics Letters record;
- marks the integration in `bare_jrnl.tex` without altering the survey structure or coverage date;
- regenerates the consolidated bibliography, builds `bare_jrnl.pdf`, and validates DOI/key uniqueness, resolved citations, PDF structure, and extracted survey text.

## Completion criterion

The update is complete only after the workflow commits synchronized `README.md`, `index.html`, survey source files, merged bibliography, and a newly generated `bare_jrnl.pdf`. Source-only commits must not be interpreted as evidence that the public PDF was rebuilt.
