# 11 July 2026 bibliography deduplication and citation-key audit

The survey previously passed chronological `egbib*.bib` supplements directly to BibTeX. Several correction files repeat keys, and the legacy Zotero export lower-cased many identifiers that remain mixed-case in the LaTeX sources. Both conditions can prevent a reproducible clean build.

This update generates `egbib_merged_20260711.bib` from 30 source files and keeps one highest-priority record for each of 357 case-insensitively unique keys. Priority is deterministic: `egbib.bib`, then `egbib_2026_updates.bib`, followed by dated supplements in chronological filename order, so later corrections override older records. The selected records are then renamed to the exact citation spelling used by the survey whenever the mapping is unambiguous. `bare_jrnl.tex` uses only the consolidated bibliography.

- Parsed source records: 376
- Case-insensitive duplicate replacements: 19
- Citation-key case normalizations: 83
- Ambiguous citation spellings: 0
- Truly missing citation keys: 0

## Duplicate records resolved

- `liTransiT2025` / `liTransiT2025`: `egbib.bib` → `egbib_2026_updates.bib`
- `somasundaramRoleTransients2023` / `somasundaramRoleTransients2023`: `egbib.bib` → `egbib_2026_updates.bib`
- `sunGeneralizable2025` / `sunGeneralizable2025`: `egbib.bib` → `egbib_20260701_updates.bib`
- `caohighresolutionnlos2022` / `caohighresolutionnlos2022`: `egbib.bib` → `egbib_20260702_updates.bib`
- `zhufastnonlineofsightimaging2021a` / `zhuFastNonlineofsightImaging2021a`: `egbib.bib` → `egbib_20260703_updates.bib`
- `fujimuraNLOSNeuS2023` / `fujimuraNLOSNeuS2023`: `egbib.bib` → `egbib_20260703_updates.bib`
- `suDGNLOS2025` / `suDGNLOS2025`: `egbib.bib` → `egbib_20260703_updates.bib`
- `musarranonlineofsight3dimaging2019` / `musarraNonlineofsight3DImaging2019`: `egbib.bib` → `egbib_20260705_updates.bib`
- `leidirectobjectrecognition2019` / `leiDirectObjectRecognition2019`: `egbib.bib` → `egbib_20260707_updates.bib`
- `liuFewShotSSCR2022` / `liuFewShotSSCR2022`: `egbib_2026_updates.bib` → `egbib_20260711_sscr_updates.bib`
- `nam_real-time_2020` / `nam_real-time_2020`: `egbib.bib` → `egbib_20260712_realtime_updates.bib`
- `royoVirtualMirrors2023` / `royoVirtualMirrors2023`: `egbib.bib` → `egbib_20260712_virtual_mirrors_updates.bib`
- `thrampoulidisexploitingocclusionnonlineofsight2018` / `thrampoulidisExploitingOcclusionNonLineofSight2018`: `egbib.bib` → `egbib_20260713_occlusion_updates.bib`
- `tanakapolarizednonlineofsightimaging2020` / `tanakaPolarizedNonLineofSightImaging2020`: `egbib.bib` → `egbib_20260713_polarization_updates.bib`
- `isogawaTransientSinograms2020` / `isogawaTransientSinograms2020`: `egbib_20260705_updates.bib` → `egbib_20260714_c2nlos_updates.bib`
- `grauOcclusionFields2022` / `grauOcclusionFields2022`: `egbib_20260703_updates.bib` → `egbib_20260714_occlusion_fields_updates.bib`
- `wangSignalSuperresolution2023` / `wangSignalSuperresolution2023`: `egbib.bib` → `egbib_20260715_sparse_sampling_updates.bib`
- `liuFewShotSSCR2022` / `liuFewShotSSCR2022`: `egbib_20260711_sscr_updates.bib` → `egbib_20260715_sparse_sampling_updates.bib`
- `liDeepUnderscanning2023` / `liDeepUnderscanning2023`: `egbib.bib` → `egbib_20260715_sparse_sampling_updates.bib`

## Citation-key spellings normalized

- `ahn_2019_iccv` → `Ahn_2019_ICCV`
- `aittalacomputationalmirrorsblind2019` → `aittalaComputationalMirrorsBlind2019`
- `andersonrolepartialocclusion1994` → `andersonRolePartialOcclusion1994`
- `arellanofastbackprojectionnonline2017` → `arellanoFastBackprojectionNonline2017`
- `baradadinferringlightfields2018a` → `baradadInferringLightFields2018a`
- `batarsehpassivesensingcorner2018a` → `batarsehPassiveSensingCorner2018a`
- `beckusmultimodalnonlineofsightpassive2019` → `beckusMultiModalNonLineofSightPassive2019`
- `bertolottinoninvasiveimagingopaque2012a` → `bertolottiNoninvasiveImagingOpaque2012a`
- `boger-lombardpassiveopticaltimeofflight2019` → `boger-lombardPassiveOpticalTimeofflight2019`
- `boumanturningcornerscameras2017` → `boumanTurningCornersCameras2017`
- `buttafavanonlineofsightimagingusing2015` → `buttafavaNonlineofsightImagingUsing2015`
- `caramazzaneuralnetworkidentification2017` → `caramazzaNeuralNetworkIdentification2017`
- `chandranadaptivelightingdatadriven2019` → `chandranAdaptiveLightingDataDriven2019`
- `channonlineofsighttrackingpeople2017a` → `chanNonlineofsightTrackingPeople2017a`
- `chantotalvariationblind1998` → `chanTotalVariationBlind1998`
- `chensteadystatenonlineofsightimaging2019` → `chenSteadystateNonLineofSightImaging2019`
- `chopitedeepnonlineofsightreconstruction2020` → `chopiteDeepNonLineofSightReconstruction2020`
- `dblp:conf/iccp/seidelmmsfyg19` → `DBLP:conf/iccp/SeidelMMSFYG19`
- `dblp:journals/corr/abs-1810-11710` → `DBLP:journals/corr/abs-1810-11710`
- `facciononlineofsightimaging2020` → `faccioNonlineofsightImaging2020`
- `fengcorrelationsfluctuationscoherent1988` → `fengCorrelationsFluctuationsCoherent1988`
- `fienupphaseretrievalalgorithms1982` → `fienupPhaseRetrievalAlgorithms1982`
- `freundmemoryeffectspropagation1988` → `freundMemoryEffectsPropagation1988`
- `galindodatasetbenchmarkingtimeresolved2019` → `galindoDatasetBenchmarkingTimeresolved2019`
- `gariepydetectiontrackingmoving2016` → `gariepyDetectionTrackingMoving2016`
- `guptareconstructionhidden3d2012` → `guptaReconstructionHidden3D2012`
- `hedeepresiduallearning2016a` → `heDeepResidualLearning2016a`
- `heidediffusemirrors3d2014` → `heideDiffuseMirrors3D2014`
- `heidenonlineofsightimagingpartial2017` → `heideNonlineofsightImagingPartial2017`
- `hochreiterlongshorttermmemory1997` → `hochreiterLongShortTermMemory1997`
- `isogawaefficientnonlineofsightimaging` → `isogawaEfficientNonLineofSightImaging`
- `isogawaopticalnonlineofsightphysicsbased2020` → `isogawaOpticalNonLineofSightPhysicsBased2020`
- `jinreconstructionmultiplenonlineofsight2018` → `jinReconstructionMultipleNonlineofsight2018`
- `jinscannerlessnonlineofsightthree2020` → `jinScannerlessNonlineofsightThree2020`
- `kadambioccludedimagingtimeofflight2016` → `kadambiOccludedImagingTimeofflight2016`
- `kirmanilookingcornerusing2011` → `kirmaniLookingCornerUsing2011`
- `kleintrackingobjectsoutside2016` → `kleinTrackingObjectsOutside2016`
- `kundurblindimagedeconvolution1996` → `kundurBlindImageDeconvolution1996`
- `kupyndeblurganblindmotion2018` → `kupynDeblurGANBlindMotion2018`
- `laurenzismultiplereturnsinglephotoncounting2015` → `laurenzisMultiplereturnSinglephotonCounting2015`
- `lecundeeplearning2015` → `lecunDeepLearning2015`
- `lecungradientbasedlearningapplied1998a` → `lecunGradientbasedLearningApplied1998a`
- `levinunderstandingevaluatingblind2009` → `levinUnderstandingEvaluatingBlind2009`
- `li:20` → `Li:20`
- `lindell:2019:acoustic` → `Lindell:2019:Acoustic`
- `lindell:2019:wave` → `Lindell:2019:Wave`
- `lindellsinglephoton3dimaging2018` → `lindellSinglephoton3DImaging2018`
- `lisinglephotonimaging2002021` → `liSinglephotonImaging2002021`
- `liuanalysisfeaturevisibility2019` → `liuAnalysisFeatureVisibility2019`
- `liuphasorfielddiffraction2020` → `liuPhasorFieldDiffraction2020`
- `liurolewignerdistribution2020` → `liuRoleWignerDistribution2020`
- `liuvirtualwaveoptics2018` → `liuVirtualWaveOptics2018`
- `maedarecentadvancesimaging2019` → `maedaRecentAdvancesImaging2019`
- `mannaerrorbackprojectionalgorithms2018` → `mannaErrorBackprojectionAlgorithms2018`
- `mannanonlineofsightimagingusingdynamic2020` → `mannaNonlineofsightimagingUsingDynamic2020`
- `metzlerdeepinversecorrelographyrealtime2020` → `metzlerDeepinverseCorrelographyRealtime2020`
- `musarradetectionidentificationtracking2019` → `musarraDetectionIdentificationTracking2019`
- `newhallhistoryphotography1982` → `newhallHistoryPhotography1982`
- `osnabruggegeneralizedopticalmemory2017` → `osnabruggeGeneralizedOpticalMemory2017`
- `otooleconfocalnonlineofsightimaging2018` → `otooleConfocalNonlineofsightImaging2018`
- `pediredlasnlosnonlineofsightscanning2019` → `pediredlaSNLOSNonlineofsightScanning2019`
- `phongilluminationcomputergenerated1975` → `phongIlluminationComputerGenerated1975`
- `raskar5dtimelighttransport2008` → `raskar5dTimelightTransport2008`
- `rezaphasorfieldwaves2019` → `rezaPhasorFieldWaves2019`
- `ronnebergerunetconvolutionalnetworks2015a` → `ronnebergerUnetConvolutionalNetworks2015a`
- `satatobjectclassificationscattering2017` → `satatObjectClassificationScattering2017`
- `saunderscomputationalperiscopyordinary2019` → `saundersComputationalPeriscopyOrdinary2019`
- `seideltwodimensionalnonlineofsightscene2020` → `seidelTwoDimensionalNonLineofSightScene2020`
- `smithtrackingmultipleobjects2018a` → `smithTrackingMultipleObjects2018a`
- `torralbaaccidentalpinholepinspeck2012` → `torralbaAccidentalPinholePinspeck2012`
- `tsaigeometryfirstreturningphotons2017` → `tsaiGeometryFirstreturningPhotons2017`
- `tsaivolumetricalbedosurface2019` → `tsaiVolumetricAlbedoSurface2019`
- `veeraraghavandappledphotographymask2007` → `veeraraghavanDappledPhotographyMask2007`
- `veltenrecoveringthreedimensionalshape2012` → `veltenRecoveringThreedimensionalShape2012`
- `willomitzer:18` → `Willomitzer:18`
- `wunonlineofsightimaging2021` → `wuNonLineofsightImaging2021`
- `xintheoryfermatpaths2019` → `xinTheoryFermatPaths2019`
- `yecompressedsensingactive2021` → `yeCompressedSensingActive2021`
- `yedidiausingunknownoccluders2019` → `yedidiaUsingUnknownOccluders2019`
- `young:2020:dlct` → `Young:2020:dlct`
- `yunonlineofsightimagingdeep2019` → `yuNonLineofSightImagingDeep2019`
- `zhounonlineofsightimagingphong2020` → `zhouNonlineofsightImagingPhong2020`
- `shennonlineofsightimagingneural2021` → `shenNonlineofsightImagingNeural2021`

## Ambiguous citation spellings

- None.

## Truly missing citation keys and source locations

- None.

The CI workflow performs a clean LaTeX/BibTeX build, rejects undefined citations or repeated entries, validates the PDF with `pdfinfo` and `pdftotext`, and verifies that the newly integrated X-band radar and Neural Illumination Fields records appear in the generated bibliography.
