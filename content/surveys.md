<!--
  Text for the Surveys & Data page (surveys/index.html).

  Edit the text under each "## @name" line, save, then run:  python3 scripts/build.py
  Do not rename the "## @name" lines: each one is tied to a spot on the page.

  Formatting:  **bold**   *italic* (also *z* for redshift)   [link text](https://...)
               [term](#g-redshift) adds a glossary hover (research page terms)
               a blank line starts a new paragraph;  \* gives a literal asterisk
  Simple HTML such as <sup>12</sup> or <sub>e</sub> also works.
-->

## @hero-lead
Modern astronomy is a team sport. Survey collaborations pool telescope time, people, and expertise to build data sets no single scientist could. Here is what each one does, the role I play, and where you can find its data.

## @techniques-intro
A survey systematically maps a patch of sky to build large, uniform samples. Wide surveys find rare, bright objects; deep ones reach faint, distant galaxies. These are the three techniques behind the surveys on this page.

## @technique-narrowband
A filter only about 1% wide in wavelength, such as LAGER's NB964 (92 Å wide at 9640 Å), isolates a thin slice of color. A galaxy whose emission line lands in the window appears brighter in the narrowband image than in a broadband one, which selects every line-emitting galaxy above a flux limit in a thin redshift slice (here Hα at *z* = 0.47). Used by HiZELS, SC4K, LAGER, DAWN, and CIDER, and by JELS on JWST.

## @technique-slitless
A grism, a prism combined with a diffraction grating, disperses the light of every object in the field into a short spectrum, as in Hubble's 3D-HST survey. Each trace is then extracted into a 1D spectrum, giving emission-line redshifts for thousands of galaxies without choosing targets in advance; overlapping traces from neighbors must be modeled. Used by POPPIES on JWST and GRACE on Roman.

## @technique-slitmask
Slits are placed over chosen targets, using configurable bars (as on Keck/MOSFIRE), milled masks, or JWST's microshutters, and each slit yields a 2D spectrum. Emission lines fall at different wavelengths for galaxies at different redshifts, while sky lines appear in every slit and are subtracted. AURORA used JWST's microshutters; my COSMOS Spectroscopic Archive reprocesses 2,660 slit masks from Keck, Subaru, and Gemini.

## @group-lead
Public resources I built or lead, so that anyone can use two decades of COSMOS spectroscopy.

## @specz-about
One uniform catalog of 487,666 spectroscopic redshifts for 266,284 objects, gathered from 138 observing programs over about 20 years and standardized with common quality flags. Researchers use it to calibrate photometric redshifts, check contamination, and plan follow-up observations. Data Release 2.0, with about 15% more redshifts, goes public in December 2026.

## @specz-role
Lead. I co-developed the compilation pipeline with Olivier Ilbert, led the analysis and the release paper, and maintain the catalog with an automated literature-mining pipeline.

## @archive-about
Reduced spectra, redshifts, and emission-line measurements for about 250,000 galaxies out to *z* ≈ 9, drawn from 2,660 spectroscopic masks (12,200 observing hours) in the Keck, Subaru, and Gemini archives. Many of these data were never published, and the archive has already produced new results such as the extreme emission-line galaxy EELG1002.

## @archive-role
Development lead. The archive began with NASA ADAP and NSF grants led by Jeyhan Kartaltepe (RIT); I lead its development, in particular the data gathering and reduction.

## @redshift-wrangler-about
Volunteers inspect real galaxy spectra from the archive and mark emission and absorption features, which are turned into redshifts and quality-checked line fits. No experience is needed, and thousands of volunteers have already taken part.

## @redshift-wrangler-role
Core team member. I helped build the project, supplied the spectra I reduced, and answered volunteers' questions on the forum and during office hours.

## @group-space
Programs on JWST, Hubble, and NASA's Roman Space Telescope, which launched in August 2026. Their observations are archived at MAST, and each program page links to its data.

## @cosmos-web-about
The largest JWST program of its first year: 255 hours of imaging that mapped 0.54 square degrees of the COSMOS field (nearly three times the area of the full Moon) with NIRCam, plus a smaller area with MIRI. Its COSMOS2025 catalog describes more than 700,000 galaxies.

## @cosmos-web-role
Team member since 2021. My redshift compilation supplies about 12,000 high-confidence redshifts used to calibrate and validate COSMOS2025.

## @aurora-about
Ultra-deep NIRSpec spectroscopy, with roughly a full day of exposure, of 97 galaxies mostly seen 9–12 billion years ago in the COSMOS and GOODS-N fields. The depth reveals faint “auroral” emission lines that act as thermometers, giving direct measurements of chemical abundances.

## @aurora-role
Team member since 2024. I lead chemical-enrichment studies: direct, temperature-based metallicity relations and the α-element-to-iron ratios of stars.

## @poppies-about
A 400-hour survey that rides along with other JWST programs: while one instrument observes a primary target, NIRCam takes slitless spectra of a neighboring patch of sky. Across about 150 fields, it builds an unbiased census of emission-line galaxies over cosmic time.

## @poppies-role
Team member since 2024.

## @jels-about
The first blind narrowband survey for hydrogen-emitting galaxies seen less than a billion years after the Big Bang (*z* ≈ 6.1), using NIRCam's narrowband filters. It carries the technique behind HiZELS into the epoch of reionization.

## @jels-role
Team member since 2021.

## @clutch-about
A 214-orbit Hubble Treasury program adding ultraviolet, optical, and medium-band imaging across the COSMOS field. It complements JWST's infrared view with the colors that trace young, hot stars, and its medium-band filters will pick out emission-line galaxies at cosmic noon.

## @clutch-role
Co-investigator since 2024. I helped choose the medium-band filters using emission-line predictions.

## @grace-about
An ultra-deep slitless spectroscopy survey with NASA's Roman Space Telescope, which launched in August 2026: 421 hours of observing in the Chandra Deep Field-South. It will find Lyman-α galaxies from more than 13 billion years ago (*z* ≈ 7–10) to time the end of reionization, while mapping star formation and chemistry at cosmic noon.

## @grace-role
Co-investigator since 2026. I lead GRACE's archival redshift compilation, which will calibrate its redshifts, and will use its spectra to measure metallicity relations for large samples of galaxies.

## @hidden-web-about
A Roman analysis program that will map intergalactic gas in 3D and use those maps to calibrate where galaxies at cosmic noon live in the cosmic web.

## @hidden-web-role
Co-investigator since 2026, in a program led by my former mentee Nima Chartab (IPAC).

## @rex-about
A proposed narrowband space mission designed to find galaxies during reionization, the era when the first galaxies cleared the fog of neutral hydrogen.

## @rex-role
Science team member, extending my narrowband and extreme-galaxy work to the early Universe.

## @group-ground
Wide-field imaging surveys, mostly with narrowband filters, on telescopes in Hawaiʻi, Chile, and Arizona.

## @hizels-about
A narrowband survey on the UKIRT and Subaru telescopes that found thousands of hydrogen- and oxygen-emitting galaxies in thin slices of cosmic time, across well-studied fields including COSMOS and UDS.

## @hizels-role
PhD research (2012–2018). I built the oxygen-emitter samples and led studies of their luminosity functions, stellar masses, equivalent widths, and clustering.

## @sc4k-about
Imaging through 16 medium- and narrowband filters that sliced the COSMOS field into 16 windows of cosmic time, finding about 4,000 Lyman-α-emitting galaxies seen 10.5–12.9 billion years ago (*z* ≈ 2–6).

## @sc4k-role
I measured how SC4K galaxies cluster to infer the masses of their dark-matter halos.

## @lager-about
A narrowband survey with the Dark Energy Camera on the 4-meter Blanco telescope in Chile, using a custom filter designed to find Lyman-α galaxies about 13 billion years ago (*z* ≈ 6.9), during reionization. The same images reveal thousands of nearer hydrogen- and oxygen-emitting galaxies.

## @lager-role
Team member since 2018. I led the analyses of those nearer emission-line galaxies: their luminosity functions and equivalent widths.

## @dawn-about
A deep near-infrared narrowband survey with the NEWFIRM camera on the 4-meter Mayall telescope, searching for Lyman-α galaxies at *z* ≈ 7.7 and, in the same images, hydrogen-emitting galaxies at *z* ≈ 0.62.

## @dawn-role
Team member since 2018. I mentored Santosh Harish, then an Arizona State PhD student, on the hydrogen-emitter analysis.

## @cider-about
A 20-square-degree narrowband survey with the Dark Energy Camera at Cerro Tololo in Chile that maps emission-line galaxies in thin slices of cosmic time. Its samples will be several times larger than those of previous narrowband surveys, enough to study rare extreme galaxies as a population.

## @cider-role
Team member since 2018, in a collaboration spanning Chile and China.

## @group-legacy
The field where most of my work lives, and the surveys where I started research as an undergraduate.

## @cosmos-about
A 2-square-degree patch of sky, about ten times the area of the full Moon, observed by nearly every major telescope from X-rays to radio. Its depth and wealth of data make it one of the most important fields for studying how galaxies evolve.

## @cosmos-role
Collaboration member since 2018. I lead the COSMOS spectroscopic redshift compilation and the development of the spectroscopic archive.

## @candels-about
A 902-orbit Hubble Treasury program that imaged five famous deep fields in near-infrared light, charting galaxies from cosmic dawn to cosmic noon.

## @candels-role
Undergraduate research (2008–2012) with Asantha Cooray at UC Irvine.

## @h-atlas-about
The widest extragalactic survey with the Herschel Space Observatory, mapping about 600 square degrees in far-infrared and submillimeter light to find dusty, star-forming galaxies, including many magnified by gravitational lensing.

## @h-atlas-role
Undergraduate research (2008–2012), including Spitzer imaging of gravitationally lensed galaxies.

## @students
Many of these data sets are public and make a great starting point for student research. If you'd like to explore them, get in touch.
