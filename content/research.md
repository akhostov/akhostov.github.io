<!--
  Text for the Research page (research/index.html).

  Edit the text under each "## @name" line, save, then run:  python3 scripts/build.py
  Do not rename the "## @name" lines: each one is tied to a spot on the page.

  Formatting:  **bold**   *italic* (also *z* for redshift)   [link text](https://...)
               [term](#g-redshift) adds a glossary hover (research page terms)
               a blank line starts a new paragraph;  \* gives a literal asterisk
  Simple HTML such as <sup>12</sup> or <sub>e</sub> also works.
-->

## @hero-lead
Every galaxy, including our Milky Way, assembled its stars and forged the heavy elements that make up planets and life over 13.8 billion years. Most of that growth happened about 9.5–11.5 billion years ago, during an era called cosmic noon, when the Universe formed stars about ten times faster than it does today. Why galaxies grew so quickly, and what later slowed them down, are among the central open questions in astrophysics.

## @toolkit-intro
JWST, Euclid, the Rubin Observatory, and the Roman Space Telescope (launched in August 2026) are producing galaxy data sets of unprecedented depth and size. Turning those data, together with decades of underused archival observations, into physical constraints requires data-intensive, statistical, and machine-learning methods, which are central to my work. The three concepts below underlie the results on this page; dotted terms show a short definition on hover or tap.

## @toolkit-time
Light from distant galaxies takes billions of years to reach us, so we observe them as they were when that light was emitted. Distance is expressed as [redshift](#g-redshift) (*z*), the factor by which cosmic expansion has stretched the light: a galaxy at *z* = 2 is seen as it was about 10.5 billion years ago, when the Universe was about 3.3 billion years old.

## @toolkit-lines
Ionized gas around young, massive stars emits light at specific wavelengths set by atomic physics, such as Hα (6563 Å) from hydrogen and [O III] (5007 Å) from doubly ionized oxygen. These [emission lines](#g-emission-line) measure the star-formation rate, the temperature, density, and ionization state of the gas, and its oxygen abundance.

## @toolkit-surveys
[Narrowband](#g-narrowband) imaging uses filters only about 1% wide in wavelength, selecting every galaxy above a flux limit whose emission line falls within a thin redshift slice. [Spectroscopy](#g-spectroscopy) disperses a galaxy's light by wavelength, giving precise redshifts and emission-line measurements.

## @archives-question
Which galaxies have we actually measured, which have we missed, and what remains unpublished in observatory archives?

## @archives-why-p
Nearly every measurement of galaxy evolution, from how fast galaxies form stars to how they cluster, depends on knowing their distances, measured as [redshifts](#g-redshift). The most precise redshifts come from [spectroscopy](#g-spectroscopy), but it is expensive, so surveys observe only some galaxies, usually the brightest and easiest. The resulting census is incomplete in ways that are rarely measured, and those gaps spread into the science: the redshifts that Rubin, Euclid, and Roman will estimate from colors for billions of galaxies are trained and checked against these same spectroscopic samples. Meanwhile, decades of spectra sit scattered across observatory archives, survey websites, and individual papers.

## @archives-compilation-title
The COSMOS Spectroscopic Redshift Compilation

## @archives-compilation
Precise galaxy distances require spectroscopy. In the 2 deg² COSMOS field, one of the most extensively observed regions of the extragalactic sky, two decades of spectroscopic redshifts were spread across 138 independent programs, each with its own quality flags and astrometric calibration. With Olivier Ilbert (LAM), I co-designed the compilation pipeline: Olivier built the original framework, and I extensively modified and expanded it to collect measurements from data archives, survey releases, publications, and principal investigators, correct the astrometry program by program, and map every quality flag onto a single uniform system. The first data release contains **487,666 redshifts for 266,284 unique objects** over 10 deg², from the local Universe to *z* ≈ 8, about 650 million years after the Big Bang.

The compilation is 50% complete to *i* ≈ 23.4 and *K*<sub>s</sub> ≈ 21.6 mag, with the highest completeness in the central CANDELS region. At *z* < 1.25 it is dominated by low- to intermediate-mass star-forming galaxies and massive quiescent galaxies; at *z* > 2 it shifts toward low-mass galaxies with high specific star-formation rates, indicative of bursty star formation. It is now standard infrastructure for the field: COSMOS2025, the photometric catalog of the JWST COSMOS-Web survey, uses about 12,000 of its highest-confidence redshifts to calibrate and validate photometric redshifts. The pipeline is designed for incremental updates, so new measurements are added in periodic data releases.

## @archives-compilation-ref
[Khostovan et al. 2026, ApJS, 282, 6](https://ui.adsabs.harvard.edu/abs/arXiv:2503.00120/abstract) · [Download the data](https://cosmos.astro.caltech.edu/page/specz)

## @archives-caption-massz
**Stellar mass versus redshift for the compilation.** Galaxies with high-confidence spectroscopic redshifts, colored by specific star-formation rate over the past 10 Myr. The black line and shaded band show the median stellar mass and its 1σ scatter: quiescent galaxies are concentrated at *z* < 1.25 and above 10<sup>10</sup> M<sub>⊙</sub>, while galaxies with high specific star-formation rates dominate at *z* > 2. From [Khostovan et al. 2026](https://ui.adsabs.harvard.edu/abs/arXiv:2503.00120/abstract).

## @archives-gaps-title
Identifying galaxy populations missing from spectroscopic samples

## @archives-gaps
Spectroscopic programs preferentially target bright galaxies, so the compilation samples the galaxy population unevenly. To quantify this, I trained [self-organizing maps](#g-som) (SOMs), an unsupervised machine-learning method that arranges galaxies with similar multi-band colors in neighboring cells of a two-dimensional grid, on the full COSMOS2020 photometric catalog, and then projected the spectroscopic sample onto the same grid. Cells without spectroscopic redshifts identify populations that have not been targeted.

Even at *z* < 1, intermediate-mass quiescent galaxies and low- to intermediate-mass galaxies with high specific star-formation rates remain undersampled. At higher redshift, the gaps include massive quiescent galaxies at *z* ≈ 2 and massive star-forming galaxies at *z* > 3. These gaps propagate into the photometric redshifts that Rubin, Euclid, and Roman will derive for billions of galaxies, because those estimates are trained and validated on spectroscopic samples. The maps therefore show where new spectroscopy would most improve the census.

## @archives-gaps-ref
[Khostovan et al. 2026, ApJS, 282, 6](https://ui.adsabs.harvard.edu/abs/arXiv:2503.00120/abstract)

## @archives-caption-som
**Spectroscopic coverage in color space.** A self-organizing map trained on COSMOS2020 photometry arranges galaxies at *z* < 1 on a grid by their colors. Top row: median redshift, stellar mass, and specific star-formation rate in each cell. Bottom row: the spectroscopic compilation projected onto the same map; white cells contain no spectroscopic redshifts. From [Khostovan et al. 2026](https://ui.adsabs.harvard.edu/abs/arXiv:2503.00120/abstract).

## @archives-archive-title
The COSMOS Spectroscopic Archive

## @archives-archive
A substantial fraction of the spectroscopy obtained in COSMOS was never published, including filler targets, lower-priority targets, and programs that were not completed. The **COSMOS Spectroscopic Archive** is a collaborative effort to recover these data, initiated through NASA Astrophysics Data Analysis Program (ADAP) and NSF grants led by Jeyhan Kartaltepe (RIT), which brought me on as a postdoctoral researcher. Over the past four years I have led the archive's development, in particular the data gathering and reduction: identifying these observations in the Keck, Subaru, and Gemini archives (2,660 multi-object slit masks, about 12,200 hours of telescope time) and reducing them uniformly, primarily with a customized version of the PypeIt pipeline, into calibrated spectra, redshifts, and emission-line measurements. When complete, the archive will contain about 250,000 galaxies out to *z* ≈ 9.

To validate redshifts at this scale, our team developed **Redshift Wrangler**, a Zooniverse citizen-science project led by RIT PhD student Sadie Coffin, in which volunteers identify spectral features and check automated emission-line fits. The archive has already produced new results: EELG1002 (below) was identified in seven-year-old Gemini spectra reduced for the archive.

## @archives-archive-ref
First result from the archive: [Khostovan et al. 2025, ApJ, 994, 34](https://ui.adsabs.harvard.edu/abs/2025ApJ...994...34K/abstract) · [Redshift Wrangler on Zooniverse](https://www.zooniverse.org/projects/jeyhansk/redshift-wrangler)

## @archives-caption-wrangler
**Citizen science.** Volunteers on [Redshift Wrangler](https://www.zooniverse.org/projects/jeyhansk/redshift-wrangler) classify features in spectra from the archive; no prior experience is required.

## @starformation-question
Did galaxies grow steadily, or in short, intense bursts of star formation?

## @starformation-why-p
Most stars in present-day galaxies formed around [cosmic noon](#g-cosmic-noon), yet how that star formation proceeded remains uncertain. Whether galaxies grew steadily or through short, intense bursts determines how quickly they consume their gas, how feedback regulates them, and how many ionizing photons they produce. JWST observations showing that bursty star formation is common in the first billion years have made the question more pressing. Answering it requires large samples with well-understood selection, which [narrowband surveys](#g-narrowband) provide: each filter selects all line-emitting galaxies above a flux limit within a thin redshift slice.

## @starformation-lfsmf-title
Luminosity and stellar mass functions of Hβ+[O III] and [O II] emitters to *z* ≈ 5

## @starformation-lfsmf
Using the High-*z* Emission Line Survey (HiZELS), I assembled what were then the largest samples of Hβ+[O III] (3,298) and [O II] (3,475) emitters, selected in four narrowband redshift slices per line between *z* ≈ 0.8 and 5. The samples cover roughly 10<sup>6</sup> Mpc³ in two independent fields (COSMOS and UDS), which limits cosmic variance, and provided the first self-consistent measurement of both [luminosity functions](#g-luminosity-function) over this redshift range. For both lines, the characteristic luminosity *L*\* increases strongly with redshift while the characteristic number density φ\* decreases; for Hβ+[O III], *L*\* rises by about a factor of ten from *z* ≈ 0.84 to 3.24.

I then measured stellar masses for about 7,000 of these emitters, spanning 10<sup>7.5</sup>–10<sup>12</sup> M<sub>⊙</sub>, and derived their stellar mass functions. Based on rest-frame *UVJ* colors, about 98% are star-forming or AGN-dominated galaxies rather than quiescent ones. The [O II]-selected mass functions have a nearly constant characteristic mass of about 10<sup>11.6</sup> M<sub>⊙</sub> from *z* = 3.34 to 1.47, while their normalization increases by a factor of about 18 with cosmic time, tracing the rapid build-up of stellar mass in star-forming galaxies. For Hβ+[O III] emitters, the characteristic mass increases from 10<sup>10.96</sup> to 10<sup>11.60</sup> M<sub>⊙</sub> toward lower redshift.

## @starformation-lfsmf-ref
[Khostovan et al. 2015, MNRAS, 452, 3948](https://ui.adsabs.harvard.edu/abs/2015MNRAS.452.3948K/abstract) · [Khostovan et al. 2016, MNRAS, 463, 2363](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2363K/abstract)

## @starformation-caption-lf
**Hβ+[O III] luminosity functions.** HiZELS luminosity functions at *z* ≈ 0.84, 1.42, 2.23, and 3.24. The characteristic luminosity *L*\* increases by about an order of magnitude over this range (right-hand panels). From [Khostovan et al. 2015](https://ui.adsabs.harvard.edu/abs/2015MNRAS.452.3948K/abstract).

## @starformation-caption-smf
**Stellar mass functions of emission-line galaxies.** Hβ+[O III]-selected (left) and [O II]-selected (right) stellar mass functions from *z* ≈ 0.84 to 3.34 (symbols), with Schechter fits (α = −1.3) and their 1σ uncertainties (lines and bands), compared with the star-forming mass functions of Pérez-González et al. (2008) and Muzzin et al. (2013). Adapted from Figure 4 of [Khostovan et al. 2016](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2363K/abstract).

## @starformation-sfrd-title
The cosmic star-formation history and stellar mass assembly

## @starformation-sfrd
Integrating the [O II] luminosity functions gives the cosmic star-formation history out to *z* ≈ 5 from a single tracer, the first such [O II]-based measurement over this range. After correcting for dust and AGN, the star-formation rate density rises from *z* ≈ 5 to a peak near *z* ≈ 3 and then declines by about an order of magnitude toward the present, in agreement with a large compilation of ultraviolet, infrared, radio, and emission-line measurements. The Hβ+[O III] star-formation rate densities agree with the [O II] and Hα values, indicating that high-redshift Hβ+[O III] samples are dominated by star-forming galaxies rather than [AGN](#g-agn).

Integrating this star-formation history over time, accounting for the mass that stars return to the interstellar medium, reproduces the observed growth of the cosmic stellar mass density out to *z* ≈ 5, an independent consistency check based on a single tracer. In the 2016 study, I also measured the stellar mass densities of the emitters directly from their mass functions: they follow the total (star-forming plus quiescent) population at high redshift but fall below it by *z* ≈ 0.84, marking the transition of star-forming galaxies into quiescent ones as cosmic star formation declines.

## @starformation-sfrd-ref
[Khostovan et al. 2015, MNRAS, 452, 3948](https://ui.adsabs.harvard.edu/abs/2015MNRAS.452.3948K/abstract) · [Khostovan et al. 2016, MNRAS, 463, 2363](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2363K/abstract)

## @starformation-caption-sfrd
**The [O II] cosmic star-formation history.** Dust- and AGN-corrected [O II] star-formation rate densities (gray circles) and the best-fitting parameterization with its 1σ uncertainty (dashed line and band; dash-dotted beyond *z* = 5), together with the Hβ+[O III] measurements (blue squares), other [O II], Hα, and radio measurements, the Madau & Dickinson (2014) compilation (open gray circles), and the fits of Madau & Dickinson (2014) and Hopkins & Beacom (2006). Adapted from Figure 9 of [Khostovan et al. 2015](https://ui.adsabs.harvard.edu/abs/2015MNRAS.452.3948K/abstract).

## @starformation-caption-smd
**Stellar mass assembly in star-forming galaxies.** Stellar mass densities of HiZELS Hβ+[O III] (blue squares) and [O II] (orange diamonds) emitters, with Hα emitters from Sobral et al. (2014), compared with measurements of the full galaxy population (open circles; Madau & Dickinson 2014 compilation, with Pérez-González et al. 2008, Muzzin et al. 2013, and Ilbert et al. 2013 highlighted). The emission-line samples follow the full population at *z* ≳ 1.5 but fall below it by *z* ≈ 0.84. Adapted from Figure 5 of [Khostovan et al. 2016](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2363K/abstract).

## @starformation-lager-title
Deep emission-line luminosity functions from LAGER

## @starformation-lager
The Lyman Alpha Galaxies in the Epoch of Reionization (LAGER) survey used the Dark Energy Camera (DECam) on the 4-m Blanco telescope to obtain one of the deepest narrowband images to date, reaching a 5σ line-flux limit of 8.2 × 10<sup>−18</sup> erg s<sup>−1</sup> cm<sup>−2</sup> over 3 deg² of COSMOS. From these data I selected 1,577 Hα emitters at *z* = 0.47, 3,933 [O III] emitters at *z* = 0.93, and 5,367 [O II] emitters at *z* = 1.59, using spectroscopic redshifts, photometric redshifts, and color–color criteria, and measured their luminosity functions. I also derived a new empirical dust-attenuation calibration based on rest-frame *g* − *r* color, calibrated with SDSS DR12 and tested against zCOSMOS spectra.

After correcting for dust and AGN, the [O III] and [O II] samples account for the full cosmic star-formation rate density at their redshifts, as measured from multiwavelength tracers, while the Hα sample accounts for about 70% at *z* = 0.47. The bright end of the [O III] luminosity function (above 10<sup>42</sup> erg s<sup>−1</sup>) shows an excess consistent with AGN contamination.

## @starformation-lager-ref
[Khostovan et al. 2020, MNRAS, 493, 3966](https://ui.adsabs.harvard.edu/abs/2020MNRAS.493.3966K/abstract)

## @starformation-caption-lager
**LAGER luminosity functions.** Observed luminosity functions of Hα emitters at *z* = 0.47 (top left), [O III] emitters at *z* = 0.93 (top right), and [O II] emitters at *z* = 1.59 (bottom), with the best-fitting Schechter functions (red bands) and literature measurements; insets show the constraints on φ\* and *L*\*. Select a panel to enlarge it. From Figures 9–11 of [Khostovan et al. 2020](https://ui.adsabs.harvard.edu/abs/2020MNRAS.493.3966K/abstract).

## @starformation-bursty-title
Bursty star formation and its contribution to cosmic star formation

## @starformation-bursty
The [equivalent width](#g-ew) (EW) of an emission line, its flux relative to the stellar continuum, is an observational proxy for the specific star-formation rate and a tracer of bursty star formation. Using the HiZELS samples, I made the first direct measurement of EW evolution for Hβ+[O III] and [O II] emitters to *z* ≈ 2 and 3, respectively: at fixed stellar mass (10<sup>9.5</sup>–10<sup>10</sup> M<sub>⊙</sub>), the rest-frame EW increases as (1+*z*)<sup>3.81</sup> for Hβ+[O III] emitters and as (1+*z*)<sup>2.72</sup> for [O II] emitters, and the Hβ+[O III] EW rises by a factor of about 100 between *z* = 0 and *z* ≈ 2. At higher redshift the Hβ+[O III] EW evolution flattens and the [O II] EW declines, implying a rising [O III]/[O II] ratio and a higher ionization parameter in high-redshift galaxies, consistent with the high ratios later measured by JWST at *z* > 5. These results were the subject of an international press release.

Emission-line surveys preferentially detect galaxies with strong lines, so observed EW trends can be partly produced by selection. I therefore developed a forward-modeling framework that assumes an intrinsic EW distribution, generates mock samples, applies the survey's selection and filter profile, and compares the result with observations. Applied to 1,572 Hα emitters at *z* = 0.47 from LAGER, it shows that the intrinsic EW scales with stellar mass as *M*<sub>⋆</sub><sup>−0.16 ± 0.03</sup>, shallower than the uncorrected *M*<sub>⋆</sub><sup>−0.25</sup>, and that this intrinsic relation, combined with an observed stellar mass function, reproduces the observed Hα luminosity function. Even after correction, low-mass galaxies are about 320 times more likely than high-mass galaxies to have EWs above 200 Å: bursty star formation is intrinsically more common at low mass.

Extending the framework to Hα emitters at *z* ≈ 0.4–2.2 from HiZELS and the Deep And Wide Narrowband (DAWN) survey, I found that the intrinsic EW–stellar mass anticorrelation steepens with redshift (slope −0.18 at *z* ≈ 0.4 to −0.24 at *z* ≈ 2.2), and that the typical EW of a 10<sup>10</sup> M<sub>⊙</sub> galaxy rises as (1+*z*)<sup>1.78</sup>, from about 9 Å at *z* = 0 to about 73 Å at *z* ≈ 2.2. The resulting model, *W*<sub>0</sub>(*M*, *z*), reproduces the observed Hα luminosity and star-formation rate functions, so the cosmic star-formation rate density can be divided by EW (figure below). At *z* ≈ 1.5–2, galaxies with EWs above 200 Å contribute about 40% of all star formation, and at *z* > 1.5, galaxies with EWs above 100 Å and specific star-formation rates above 10<sup>−8.5</sup> yr<sup>−1</sup> contribute 50–60%; below *z* ≈ 0.5, star formation is dominated by galaxies with EWs below 25 Å. Bursty, low-mass galaxies were therefore major contributors to cosmic star formation at cosmic noon. The model also shows that the reported tension between observed and simulated specific star-formation rates can arise from observational selection, and it predicts about 24,000 (Roman) and 30,000 (Euclid) Hα emitters per deg² at 0.5 < *z* < 1.9, including galaxies of 10<sup>7.2</sup>–10<sup>8</sup> M<sub>⊙</sub> at *z* > 1 with EWs above 1,000 Å.

## @starformation-bursty-ref
[Khostovan et al. 2016, MNRAS, 463, 2363](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2363K/abstract) · [Khostovan et al. 2021, MNRAS, 503, 5115](https://ui.adsabs.harvard.edu/abs/2021MNRAS.503.5115K/abstract) · [Khostovan et al. 2024, MNRAS, 535, 2903](https://ui.adsabs.harvard.edu/abs/2024MNRAS.535.2903K/abstract) · [Press release](https://astronomynow.com/2016/10/07/using-oxygen-as-a-tracer-of-galactic-evolution/)

## @starformation-caption-ewsfrd
**Cosmic star-formation rate density by Hα equivalent width.** Contributions from galaxies with rest-frame EWs of 0–25 Å (red), 25–100 Å (green), 100–200 Å (blue), and above 200 Å (purple), predicted by the *W*<sub>0</sub>(*M*, *z*) model (dashed lines and bands) and measured from narrowband samples (circles), compared with total Hα and radio measurements (gray) and the [O II]-based history of Khostovan et al. (2015; dotted line). High-EW galaxies account for a rapidly growing share toward cosmic noon. From Figure 8 of [Khostovan et al. 2024](https://ui.adsabs.harvard.edu/abs/2024MNRAS.535.2903K/abstract).

## @starformation-eelg1002-title
EELG1002: a low-redshift analog of reionization-era galaxies

## @starformation-eelg1002
Extreme emission-line galaxies at lower redshift are valuable analogs of early galaxies because they can be studied in much greater detail. In archival Gemini/GMOS spectra reduced for the COSMOS Spectroscopic Archive, I identified **EELG1002**, a galaxy at *z* = 0.8275 (seen about 7 billion years ago) with a rest-frame [O III]+Hβ equivalent width of 3,100–3,700 Å, a record for a star-forming galaxy at its redshift and stellar mass. This is 32–36 times the typical value for *z* ≈ 0.8 galaxies of similar mass, and higher than typical galaxies at *z* > 5.

EELG1002 has a stellar mass of about 10<sup>8</sup> M<sub>⊙</sub>, an effective radius of about 530 pc, and a star-formation rate of 7.7 M<sub>⊙</sub> yr<sup>−1</sup>, implying a stellar mass-doubling time of only 15–35 Myr. Star-formation-history modeling indicates a recent burst with no significant earlier star formation, and there is no clear evidence for an AGN. Its direct-method oxygen abundance, 12 + log(O/H) = 7.52 (about 7% of the solar value), matches that of *z* > 5 galaxies of the same stellar mass.

A high [O III]/[O II] ratio (about 9) and elevated [Ne III]/[O II] indicate a highly ionized interstellar medium and a hard radiation field. EELG1002 produces ionizing photons efficiently (ξ<sub>ion</sub> ≈ 10<sup>25.74</sup> erg<sup>−1</sup> Hz, comparable to extreme galaxies at *z* > 7), and empirical calibrations suggest that 10–20% of its Lyman-continuum radiation may escape. Its dynamical mass of about 10<sup>9</sup> M<sub>⊙</sub>, ten times its stellar mass, implies a large gas reservoir, consistent with analogs identified in the IllustrisTNG simulation. EELG1002 may be in its first major episode of star formation, which makes it a nearby laboratory for the conditions in reionization-era galaxies.

## @starformation-eelg1002-ref
[Khostovan et al. 2025, ApJ, 994, 34](https://ui.adsabs.harvard.edu/abs/2025ApJ...994...34K/abstract) · [Data reduction files](https://doi.org/10.5281/zenodo.16990022)

## @starformation-caption-eelg-spec
**Spectrum and spectral energy distribution of EELG1002.** Top: Gemini/GMOS spectrum (blue) with the fitted emission-line model (black dashed), showing strong [O III] λ5007 relative to [O II] λ3727, comparable [Ne III] λ3869 and [O II] emission, and the auroral [O III] λ4363 line used for the direct-method abundance; the two-dimensional spectrum is shown below. Bottom: multiwavelength photometry with the best-fitting Cigale (green) and Bagpipes (red) models; the strong [O III]+Hβ emission produces clear excesses in the Subaru and HST bands. From [Khostovan et al. 2025](https://ui.adsabs.harvard.edu/abs/2025ApJ...994...34K/abstract).

## @starformation-caption-eelg
**[O III]+Hβ equivalent width versus stellar mass.** EELG1002 (stars) lies 32–36× above the typical relation for *z* ≈ 0.8 [O III] emitters (blue line). Inset: Hubble image. From [Khostovan et al. 2025](https://ui.adsabs.harvard.edu/abs/2025ApJ...994...34K/abstract).

## @starformation-caption-ionizing
**Ionizing-photon production efficiency.** EELG1002 (stars) has a ξ<sub>ion</sub> comparable to galaxies at *z* ≳ 5. From [Khostovan et al. 2025](https://ui.adsabs.harvard.edu/abs/2025ApJ...994...34K/abstract).

## @chemistry-question
How quickly did galaxies fill their gas with heavy elements, and do our best simulations get it right?

## @chemistry-why-p
Nearly every element heavier than helium, including the oxygen we breathe, was produced in stars and dispersed by supernovae and stellar winds. The [metallicity](#g-metallicity) of a galaxy's gas therefore records the balance between gas inflow, star formation, and metal-enriched outflows, a balance summarized by the [mass–metallicity relation](#g-mzr) (MZR) and its extension to star-formation rate, the fundamental metallicity relation (FMR). At high redshift, most metallicities are derived from strong-line calibrations established for nearby galaxies, which may not apply to young, intensely star-forming systems. The [direct method](#g-direct-te) avoids these calibrations by measuring the electron temperature of the gas from faint auroral lines, but it requires very deep spectra that only JWST can provide at cosmic noon.

## @chemistry-direct-mzr-title
A direct-method mass–metallicity relation at cosmic noon

## @chemistry-direct-mzr
Using ultra-deep JWST/NIRSpec spectroscopy from the AURORA survey, I measured direct-method oxygen abundances for **34 galaxies at 1.4 ≤ *z* ≤ 3.5** (median *z* = 2.28, about 10.8 billion years ago) from the auroral [O III] λ4363 and [O II] λλ7320,7331 lines. In 18 galaxies both lines are detected, so temperatures can be measured separately for the high- and low-ionization zones. The sample spans 12 + log(O/H) = 7.68–8.65, stellar masses of 10<sup>8</sup>–10<sup>10.4</sup> M<sub>⊙</sub>, and star-formation rates of 1–100 M<sub>⊙</sub> yr<sup>−1</sup>, a wider range than previous direct-method studies at high redshift.

The resulting MZR has a slope of 0.27 ± 0.04, a normalization of 12 + log(O/H) = 8.44 ± 0.04 at 10<sup>10</sup> M<sub>⊙</sub>, and an intrinsic scatter of 0.10 dex. These values agree with strong-line measurements at *z* ≈ 2–3, supporting the use of those calibrations for galaxy populations at this epoch. The galaxies also lie on the local (*z* ≈ 0) FMR to within 0.1 dex, with no significant evidence for evolution. The processes that regulate chemical enrichment, star formation, and metal-enriched outflows in present-day galaxies were therefore already in place at cosmic noon.

## @chemistry-direct-mzr-ref
[Khostovan et al. 2026, ApJL, 1003, L41](https://ui.adsabs.harvard.edu/abs/arXiv:2512.16989/abstract)

## @chemistry-caption-mzr
**Direct-method mass–metallicity relation at *z* ≈ 2.3.** Left: direct-*T*<sub>e</sub> metallicities from AURORA (blue squares and band) compared with strong-line relations at similar redshift (colored lines) and with *z* ≈ 0 galaxies (black squares). Right: predictions from six cosmological simulations, none of which reproduce the observed evolution in normalization between *z* ≈ 0 and *z* ≈ 2. From [Khostovan et al. 2026](https://ui.adsabs.harvard.edu/abs/arXiv:2512.16989/abstract).

## @chemistry-simulations-title
Comparison with cosmological simulations

## @chemistry-simulations
I compared these measurements with predictions from six cosmological simulations: EAGLE, FIRE, Illustris, IllustrisTNG, NewHorizon, and SIMBA. None reproduces the observed evolution of the MZR normalization between *z* ≈ 0 and *z* ≈ 2. EAGLE, FIRE, and IllustrisTNG predict slopes consistent with the data, while Illustris, SIMBA, and NewHorizon predict steeper relations, indicating that current prescriptions for chemical enrichment and feedback remain incomplete.

Sample selection also matters. All 34 galaxies lie on or above the star-forming main sequence, so if the FMR holds at *z* ≈ 2, the sample is biased toward lower metallicity. Correcting for this raises O/H by about 0.1 dex at the median stellar mass of the sample (10<sup>9.3</sup> M<sub>⊙</sub>), bringing the measured relation into better agreement with IllustrisTNG.

## @chemistry-simulations-ref
[Khostovan et al. 2026, ApJL, 1003, L41](https://ui.adsabs.harvard.edu/abs/arXiv:2512.16989/abstract)

## @environment-question
Do the invisible dark-matter halos around galaxies, and their place in the cosmic web, decide whether galaxies keep forming stars?

## @environment-why-p
Galaxies reside in [dark matter halos](#g-halo) embedded in a cosmic web of filaments, sheets, and clusters, and their position within this structure may regulate their gas supply. Theory predicts that above a critical halo mass of roughly 10<sup>12</sup> M<sub>⊙</sub>, infalling gas is shock-heated and can no longer cool efficiently to form stars, whereas filaments may channel cold gas into galaxies. Testing these predictions requires precise three-dimensional positions for large, well-defined samples. Photometric redshifts are too imprecise, and spectroscopic surveys have complex selection functions that bias the measurements. Narrowband surveys address both problems by isolating thin redshift slices with a well-understood selection.

## @environment-oxygen-halos-title
Halo masses of Hβ+[O III] and [O II] emitters to *z* ≈ 5

## @environment-oxygen-halos
Galaxies in more massive dark matter halos are more strongly [clustered](#g-clustering), so the clustering of a galaxy population measures the mass of its host halos. I measured the [angular correlation functions](#g-acf) of about 7,000 HiZELS Hβ+[O III] (*z* ≈ 0.8–3.2) and [O II] (*z* ≈ 1.5–4.7) emitters. The clustering length increases with both line luminosity and redshift, corresponding to minimum halo masses of 10<sup>10.7</sup>–10<sup>12.1</sup> M<sub>⊙</sub> for Hβ+[O III] emitters and 10<sup>11.5</sup>–10<sup>12.6</sup> M<sub>⊙</sub> for [O II] emitters.

When line luminosity is normalized by the characteristic luminosity of each epoch, *L*/*L*\*(*z*), the relation between luminosity and halo mass becomes independent of redshift: the faintest Hβ+[O III] emitters reside in halos of about 10<sup>9.5</sup> M<sub>⊙</sub> and the brightest in halos of about 10<sup>13</sup> M<sub>⊙</sub>. Halo mass also increases with stellar mass, from 10<sup>11</sup> to 10<sup>12.5</sup> M<sub>⊙</sub> over stellar masses of 10<sup>8.5</sup>–10<sup>11.5</sup> M<sub>⊙</sub>, but the dependence on line luminosity is the stronger of the two. Above *L*\*, halo masses flatten at 10<sup>12.5</sup>–10<sup>13</sup> M<sub>⊙</sub> at all epochs, consistent with the transitional halo mass above which models predict that star formation is quenched.

## @environment-oxygen-halos-ref
[Khostovan et al. 2018, MNRAS, 478, 2999](https://ui.adsabs.harvard.edu/abs/2018MNRAS.478.2999K/abstract)

## @environment-caption-lstar
**Halo mass versus normalized line luminosity.** Minimum dark matter halo mass versus *L*/*L*\*(*z*) for (a) Hβ+[O III] and (b) [O II] emitters at *z* ≈ 0.8–4.7, and (c) Hα emitters from the literature. Each relation is independent of redshift and flattens above *L*\* at 10<sup>12.5</sup>–10<sup>13</sup> M<sub>⊙</sub>. From [Khostovan et al. 2018](https://ui.adsabs.harvard.edu/abs/2018MNRAS.478.2999K/abstract).

## @environment-lya-halos-title
Halo masses of Lyα emitters at *z* ≈ 2.5–6

## @environment-lya-halos
I applied the same approach to about 5,000 Lyα-emitting galaxies at *z* ≈ 2.5–6 (11–12.8 billion years ago) from the Slicing COSMOS 4K (SC4K) survey and archival NB497 imaging of the SA22 field, divided into 15 redshift slices. For each slice, I measured the angular correlation function, *w*(θ), and converted its amplitude into a clustering length and host halo mass. Narrowband-selected Lyα emitters, with luminosities of 10<sup>42</sup>–10<sup>43</sup> erg s<sup>−1</sup>, have clustering lengths of about 3–6 *h*<sup>−1</sup> Mpc and typical halo masses of about 10<sup>11</sup> M<sub>⊙</sub>, while the more luminous intermediate-band-selected emitters reside in halos of 10<sup>11</sup>–10<sup>12</sup> M<sub>⊙</sub>.

Halo mass again follows a redshift-independent relation with *L*/*L*\*(*z*), from about 10<sup>10</sup> M<sub>⊙</sub> at 0.1 *L*\* to about 5 × 10<sup>12</sup> M<sub>⊙</sub> at 7 *L*\*. Halo mass scales as (*L*/*L*\*)<sup>2.08</sup> below *L*\* but only as (*L*/*L*\*)<sup>0.63</sup> above it, where the most luminous emitters are predominantly powered by AGN rather than star formation. Halo mass also increases with ultraviolet luminosity and dust-corrected star-formation rate. Using halo mass accretion histories, these relations connect high-redshift Lyα emitters to a wide range of present-day descendants, from dwarf galaxies to Milky Way–mass galaxies and galaxies in clusters.

## @environment-lya-halos-ref
[Khostovan et al. 2019, MNRAS, 489, 555](https://ui.adsabs.harvard.edu/abs/2019MNRAS.489..555K/abstract)

## @environment-caption-halo
**Clustering and halo masses of Lyα emitters.** Left: angular correlation function of NB497-selected Lyα emitters at *z* ≈ 3.1 (red circles), with the best-fitting model and its 1σ uncertainty (black line and gray band) and previous measurements; the top axis gives the corresponding comoving separation. Right: minimum halo mass versus *L*/*L*\*(*z*) for Lyα emitters at *z* ≈ 2.8–5.7, following a single relation that flattens above *L*\* (dashed line). From [Khostovan et al. 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.489..555K/abstract).

## @environment-lss-title
Three-dimensional structure of overdense regions in COSMOS

## @environment-lss
The density of spectroscopic redshifts in the COSMOS compilation makes it possible to map large-scale structure directly in three dimensions. Using a 10th-nearest-neighbor density estimator, I showed how the compilation resolves the internal structure of extended overdense regions. The "Hyperion" proto-supercluster at *z* ≈ 2.42–2.53, first identified as a multicomponent system by Cucciati et al. (2018), separates into three overdensities at *z* ≈ 2.44, 2.47, and 2.51, and a thin slice at *z* ≈ 1.24–1.27 contains two overdense regions separated by about 40 comoving Mpc. Maps like these provide the environmental context needed to test how a galaxy's position in the cosmic web affects its growth.

## @environment-lss-ref
[Khostovan et al. 2026, ApJS, 282, 6](https://ui.adsabs.harvard.edu/abs/arXiv:2503.00120/abstract)

## @environment-caption-lss
**Large-scale structure from the spectroscopic redshift compilation.** Rotating three-dimensional views of the "Hyperion" proto-supercluster at *z* ≈ 2.42–2.53 (left; 102 × 102 × 129 comoving Mpc) and a structure at *z* ≈ 1.24–1.27 (right; 68 × 68 × 63 comoving Mpc). Each point is a galaxy with a spectroscopic redshift, colored by its local number density Σ<sub>10</sub> (kpc<sup>−3</sup>) from the distance to its 10th-nearest neighbor (red is densest), with redshift increasing upward. Animations from [Khostovan et al. 2026](https://ui.adsabs.harvard.edu/abs/arXiv:2503.00120/abstract).

## @glossary-redshift
How much the expansion of the Universe has stretched a galaxy's light toward redder colors on its way to us. Higher redshift means farther away and further back in time: light from *z* = 1 left its galaxy about 8 billion years ago, and from *z* = 6 about 12.9 billion years ago.

## @glossary-emission-line
Light given off at one precise wavelength when electrons in atoms drop between energy levels. Hot gas around young stars glows in lines of hydrogen (such as Hα and Lyman-α) and oxygen (such as [O III] and [O II]).

## @glossary-ew
The strength of an emission line relative to the starlight at the same wavelength. A high equivalent width indicates a high star-formation rate relative to the stellar mass already in place (a high specific star-formation rate).

## @glossary-narrowband
Imaging through a filter that lets in only a narrow range of colors. Galaxies whose emission line falls in that window appear brighter, which picks out galaxies at one specific redshift: a thin slice of cosmic time.

## @glossary-spectroscopy
Splitting light into its component colors (a spectrum) to measure emission lines and redshifts precisely.

## @glossary-luminosity-function
A census of galaxies: how many exist per unit volume at each brightness. How it changes over time reveals how galaxy populations evolve.

## @glossary-cosmic-noon
The era about 9.5 to 11.6 billion years ago (redshift ~1.5–3) when the Universe formed stars at its fastest rate.

## @glossary-reionization
The era within the first billion years when light from the first stars and galaxies split apart the neutral hydrogen atoms filling space, making the Universe transparent to ultraviolet light.

## @glossary-metallicity
The amount of elements heavier than hydrogen and helium (which astronomers call “metals”) in a galaxy's gas or stars, usually measured through the abundance of oxygen.

## @glossary-mzr
The observed trend that more massive galaxies have more metal-rich gas. How it changes over time records how galaxies produce, lose, and recycle metals.

## @glossary-halo
A vast, roughly spherical cloud of invisible dark matter surrounding every galaxy, typically far more massive than the galaxy's stars and gas combined. Its gravity draws in the gas that forms stars.

## @glossary-clustering
How much more likely galaxies are to be found near one another than if they were scattered at random. Stronger clustering means more massive host halos.

## @glossary-acf
A measure of how much more likely pairs of galaxies are to be found at a given angular separation on the sky than in a random distribution. Its amplitude gives the clustering strength and, through models, the mass of the galaxies' dark matter halos.

## @glossary-som
A machine-learning technique that arranges galaxies on a two-dimensional grid so that those with similar colors sit together, revealing which kinds of galaxies a survey has covered well and which it has missed.

## @glossary-agn
Active galactic nucleus: a supermassive black hole at the center of a galaxy that is accreting gas and radiating strongly. Its emission lines can contaminate or mimic those produced by star formation.

## @glossary-direct-te
A measurement of a gas's oxygen abundance based on its electron temperature, which is derived from the ratio of faint “auroral” emission lines to brighter lines of the same ion. It does not rely on calibrations from nearby galaxies.

## @explore
Most of these results come from large collaborations, and many of their data sets are public. See what each survey does and where to download its data.
