"""Re-plot Khostovan et al. (2015) Figure 9 (dust- and AGN-corrected [OII] cosmic
star-formation history) in the style of Khostovan et al. (2026b).

Data (Salpeter IMF, Kennicutt 1998 calibrations, as in the paper):
  * This work: Table 3 of Khostovan et al. 2015 (rho_SFR, AGN-corr column).
  * [OII] fit: eq. 9 of Khostovan et al. 2015, rho = a(1+z)^b / (1 + [(1+z)/c]^d)
    with a = 0.015 +/- 0.002, b = 2.26 +/- 0.20, c = 4.07 +/- 0.51, d = 8.39 +/- 2.60.
    The 1-sigma band is from Monte Carlo draws treating the parameters as
    independent (their covariance is not published).
  * Ciardullo+13 and Bayliss+11: Table C1 of Khostovan et al. 2015 (A[OII] = 0)
    plus the paper's A[OII] = 0.62 mag (+0.248 dex), which reproduces the points
    in the published figure to <0.01 dex.
  * Sobral+12, Sobral+13 (H-alpha), Sobral+15, Karim+11 (radio stacking): read
    from the published Figure 9 (no error bars shown here). Sobral+13 at z = 1.47
    is hidden behind the [OII] point in the original and is approximate.
  * Grey compilation: Madau & Dickinson (2014) Table 1 (data/md14_sfrd.csv), a
    subset of the larger compilation shown in the original figure.
  * Fits: Madau & Dickinson (2014) and Hopkins & Beacom (2006; Cole et al. form,
    h = 0.7; shifted by -0.114 dex, which reproduces the curve in the
    published figure. Note: SalA -> Salpeter would normally be +0.114 dex). The original's three alternative fits
    ([OII]+Ha+Radio, [OII]+UV, [OII]+Ha+Radio+UV) are not reproduced because
    their parameters are not published.
"""
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullFormatter
from matplotlib.lines import Line2D
import khostovan_style as ks

OUT = sys.argv[1]
ks.apply(10)
HERE = os.path.dirname(os.path.abspath(__file__))
X = lambda z: np.log10(1.0 + np.asarray(z, float))

O2 = [(1.47, -0.973, .04, .04), (2.25, -0.723, .06, .07), (3.34, -0.964, .43, .20), (4.69, -1.348, .11, .11)]
HB = [(0.84, -1.062, .03, .03), (1.42, -0.882, .06, .05), (2.23, -0.766, .11, .12), (3.24, -0.873, .11, .10)]
DUST = 0.62 / 2.5
CIAR = [(0.0, 0.2, -2.05, .11), (0.2, 0.325, -1.82, .06), (0.325, 0.45, -1.71, .05), (0.45, 0.56, -1.66, .06)]
BAYL = [(1.85, -0.92, .08)]
SOB12 = [(1.47, -0.91)]
SOB13 = [(0.40, -1.54), (0.84, -1.00), (1.47, -0.90), (2.23, -0.69)]
SOB15 = [(2.25, -0.58)]
KAR11 = [(0.3, -1.48), (0.5, -1.35), (0.7, -1.15), (0.9, -1.01), (1.1, -0.97), (1.4, -0.95), (1.8, -0.78), (2.25, -0.79), (2.75, -0.67)]

def md_form(z, a, b, c, d):
    return a * (1 + z) ** b / (1 + ((1 + z) / c) ** d)

z = np.linspace(0, 10.5, 600)
p = np.array([0.015, 2.26, 4.07, 8.39]); pe = np.array([0.002, 0.20, 0.51, 2.60])
rng = np.random.default_rng(7)
draws = rng.normal(p, pe, size=(4000, 4))
draws = draws[(draws[:, 0] > 0) & (draws[:, 2] > 0) & (draws[:, 3] > 0)]
curves = np.log10(np.array([md_form(z, *d) for d in draws]))
lo, hi = np.percentile(curves, [16, 84], axis=0)
best = np.log10(md_form(z, *p))
md14 = np.log10(md_form(z, 0.015, 2.7, 2.9, 5.6))
hb06 = np.log10((0.017 + 0.13 * z) * 0.7 / (1 + (z / 3.3) ** 5.3)) - 0.114   # as plotted in the published figure

fig, ax = plt.subplots(figsize=(4.6, 3.6), dpi=300)

# grey compilation (MD14 Table 1)
rows = [l.strip().split(";") for l in open(os.path.join(HERE, "data", "md14_sfrd.csv")) if not l.startswith("#")]
zl, zh, v, ep, em = (np.array([float(r[i]) for r in rows]) for i in range(1, 6))
zc = 0.5 * (zl + zh)
ax.errorbar(X(zc), v, xerr=[X(zc) - X(zl), X(zh) - X(zc)], yerr=[em, ep], color="0.6", alpha=0.5, zorder=1, **ks.LIT)

ins = z <= 5
ax.fill_between(X(z), lo, hi, color="tab:orange", alpha=0.18, lw=0, zorder=0)
ax.plot(X(z[ins]), best[ins], color="tab:blue", lw=1.8, ls="--", zorder=4)
ax.plot(X(z[~ins]), best[~ins], color="tab:cyan", lw=1.5, ls="-.", zorder=4)
ax.plot(X(z), md14, color="k", lw=1.0, ls=":", zorder=3)
ax.plot(X(z), hb06, color="tab:brown", lw=1.0, ls=(0, (5, 2, 1, 2)), zorder=3)

# literature points (open symbols)
zc_ = np.array([0.5 * (a + b) for a, b, _, _ in CIAR])
ax.errorbar(X(zc_), [c + DUST for _, _, c, _ in CIAR], yerr=[e for *_, e in CIAR],
            xerr=[X(zc_) - X([a for a, *_ in CIAR]), X([b for _, b, *_ in CIAR]) - X(zc_)],
            color="tab:green", alpha=0.75, zorder=2, **ks.LIT)
ax.errorbar(X([1.85]), [BAYL[0][1] + DUST], yerr=[BAYL[0][2]], color="tab:purple", alpha=0.8, zorder=2, **ks.LIT)
for data, col, mk in [(SOB12, "tab:blue", "v"), (SOB13, "tab:red", "^"), (SOB15, "tab:pink", "o"), (KAR11, "tab:olive", "s")]:
    zz, vv = zip(*data)
    ax.plot(X(zz), vv, mk, ms=4.6, mfc="none", mec=col, mew=0.9, alpha=0.85, zorder=2)

# this work
for data, col, mk, ms in [(HB, "tab:blue", "s", 6.5), (O2, "k", "o", 7.0)]:
    zz, vv, ep_, em_ = map(np.array, zip(*data))
    fc = "#aec7e8" if col == "tab:blue" else "#7f7f7f"
    ax.errorbar(X(zz), vv, yerr=[em_, ep_], fmt=mk, ms=ms, mfc=fc, mec=col, mew=1.4, ecolor=col,
                elinewidth=1.3, capsize=2.5, capthick=1.3, zorder=6)

ticks = [0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10]
ax.xaxis.set_major_locator(FixedLocator(X(ticks)))
ax.set_xticklabels(["%g" % t for t in ticks])
minor = [t for t in np.r_[np.arange(0.1, 1, 0.1), np.arange(1.5, 10.5, 0.5)] if round(t, 1) not in ticks]
ax.xaxis.set_minor_locator(FixedLocator(X(minor)))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_xlim(X(0) - 0.008, X(10.5))
ax.set_ylim(-2.6, -0.3)
ax.set_xlabel(r"Redshift ($z$)")
ax.set_ylabel(r"$\log_{10}\,\dot{\rho}_\star$ (M$_\odot$ yr$^{-1}$ Mpc$^{-3}$)")

h1 = [Line2D([], [], ls="none", marker="o", ms=6.5, mfc="#7f7f7f", mec="k", mew=1.3),
      Line2D([], [], ls="none", marker="s", ms=6, mfc="#aec7e8", mec="tab:blue", mew=1.3),
      Line2D([], [], color="tab:blue", ls="--", lw=1.8),
      Line2D([], [], color="tab:cyan", ls="-.", lw=1.5),
      Line2D([], [], color="k", ls=":", lw=1.0),
      Line2D([], [], color="tab:brown", ls=(0, (5, 2, 1, 2)), lw=1.0)]
l1 = [r"\textbf{[O\,\textsc{ii}] (This Work)}", r"\textbf{H$\bm{\beta}$+[O\,\textsc{iii}] (This Work)}",
      r"\textbf{[O\,\textsc{ii}] fit (This Work)}", r"Extrapolation ($z > 5$)", r"Madau \& Dickinson (2014)", r"Hopkins \& Beacom (2006)"]
leg1 = ax.legend(h1, l1, loc="lower center", bbox_to_anchor=(0.62, 0.0), fontsize=6.6, handletextpad=0.4, labelspacing=0.3, borderaxespad=0.4)
ax.add_artist(leg1)
h2 = [Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="tab:green"),
      Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="tab:purple"),
      Line2D([], [], ls="none", marker="v", ms=4.6, mfc="none", mec="tab:blue"),
      Line2D([], [], ls="none", marker="^", ms=4.6, mfc="none", mec="tab:red"),
      Line2D([], [], ls="none", marker="o", ms=4.6, mfc="none", mec="tab:pink"),
      Line2D([], [], ls="none", marker="s", ms=4.6, mfc="none", mec="tab:olive"),
      Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="0.55")]
l2 = [r"Ciardullo+13 ([O\,\textsc{ii}])", r"Bayliss+11 ([O\,\textsc{ii}])", r"Sobral+12 ([O\,\textsc{ii}])",
      r"Sobral+13 (H$\alpha$)", r"Sobral+15 ([O\,\textsc{ii}])", r"Karim+11 (radio)", r"Compilation (MD14)"]
ax.legend(h2, l2, loc="lower left", fontsize=6.6, handletextpad=0.3, labelspacing=0.3, borderaxespad=0.4)
ax.text(0.03, 0.955, r"\textbf{HiZELS [O\,\textsc{ii}] star-formation history}", transform=ax.transAxes, ha="left", va="top", fontsize=8)
ax.text(0.03, 0.885, r"Dust and AGN corrected", transform=ax.transAxes, ha="left", va="top", fontsize=7.4, color="tab:blue")

fig.tight_layout(pad=0.3)
fig.savefig(OUT, dpi=300)
print("saved", OUT)
