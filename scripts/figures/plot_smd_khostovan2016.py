"""Re-plot Khostovan et al. (2016) Figure 5 (cosmic stellar mass density) in the
style of Khostovan et al. (2026b, AURORA MZR): Computer Modern via LaTeX, inward
ticks on all sides with minor ticks, matplotlib tab colours, faint open circles
for literature data, filled squares with dark edges + bold legend for this work.

Data:
  * This work: Table 2 of Khostovan et al. 2016 (alpha = -1.3 SMDs, Chabrier IMF).
  * Literature: Madau & Dickinson 2014, Table 2 (Salpeter) converted to Chabrier
    with -0.215 dex, the conversion stated in Khostovan et al. 2016.
  * H-alpha (Sobral et al. 2014): digitized from Khostovan et al. 2016 Fig. 5.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullFormatter
import sys

OUT = sys.argv[1]
SAL2CHAB = -0.215

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "text.latex.preamble": r"\usepackage[T1]{fontenc}\usepackage{amsmath}\usepackage{bm}",
    "font.size": 10,
    "axes.linewidth": 0.9,
    "xtick.direction": "in", "ytick.direction": "in",
    "xtick.top": True, "ytick.right": True,
    "xtick.major.size": 4, "ytick.major.size": 4,
    "xtick.minor.size": 2, "ytick.minor.size": 2,
    "xtick.minor.visible": True, "ytick.minor.visible": True,
    "legend.frameon": False,
})

# (z_lo, z_hi, logrho, +err, -err)   Salpeter, from MD14 Table 2
MD14 = {
    "Li & White (2009)": [(0.07, 0.07, 8.59, 0.01, 0.01)],
    "Gallazzi (2008)": [(0.005, 0.22, 8.78, 0.07, 0.08)],
    "Moustakas (2013)": [(0.0, 0.2, 8.59, .05, .05), (0.2, 0.3, 8.56, .09, .09), (0.3, 0.4, 8.59, .06, .06), (0.4, 0.5, 8.55, .08, .08)],
    "Bielby (2012)": [(0.2, 0.4, 8.46, .09, .12), (0.4, 0.6, 8.33, .03, .03), (0.6, 0.8, 8.45, .08, .10), (0.8, 1.0, 8.42, .05, .06),
                      (1.0, 1.2, 8.25, .04, .04), (1.2, 1.5, 8.14, .06, .06), (1.5, 2.0, 8.16, .32, .03)],
    "PG08": [(0.0, 0.2, 8.75, .12, .12), (0.2, 0.4, 8.61, .06, .06), (0.4, 0.6, 8.57, .04, .04), (0.6, 0.8, 8.52, .05, .05),
             (0.8, 1.0, 8.44, .05, .05), (1.0, 1.3, 8.35, .05, .05), (1.3, 1.6, 8.18, .07, .07), (1.6, 2.0, 8.02, .07, .07),
             (2.0, 2.5, 7.87, .09, .09), (2.5, 3.0, 7.76, .18, .18), (3.0, 3.5, 7.63, .14, .14), (3.5, 4.0, 7.49, .13, .13)],
    "I13": [(0.2, 0.5, 8.55, .08, .09), (0.5, 0.8, 8.47, .07, .08), (0.8, 1.1, 8.50, .08, .08), (1.1, 1.5, 8.34, .10, .07),
            (1.5, 2.0, 8.11, .05, .06), (2.0, 2.5, 7.87, .08, .08), (2.5, 3.0, 7.64, .15, .14), (3.0, 4.0, 7.24, .18, .20)],
    "M13": [(0.2, 0.5, 8.61, .06, .06), (0.5, 1.0, 8.46, .03, .03), (1.0, 1.5, 8.22, .03, .03), (1.5, 2.0, 7.99, .05, .03),
            (2.0, 2.5, 7.63, .11, .04), (2.5, 3.0, 7.52, .13, .09), (3.0, 4.0, 6.84, .43, .20)],
    "Arnouts (2007)": [(z, z, v, p, m) for z, v, p, m in [(0.3, 8.78, .12, .16), (0.5, 8.64, .09, .11), (0.7, 8.62, .08, .10),
                       (0.9, 8.70, .11, .15), (1.1, 8.51, .08, .11), (1.35, 8.39, .10, .13), (1.75, 8.13, .10, .13)]],
    "Pozzetti (2010)": [(0.1, 0.35, 8.58, 0, 0), (0.35, 0.55, 8.49, 0, 0), (0.55, 0.75, 8.50, 0, 0), (0.75, 1.0, 8.42, 0, 0)],
    "Kajisawa (2009)": [(0.5, 1.0, 8.63, 0, 0), (1.0, 1.5, 8.30, 0, 0), (1.5, 2.5, 8.04, 0, 0), (2.5, 3.5, 7.74, 0, 0)],
    "Marchesini (2009)": [(1.3, 2.0, 8.11, .02, .02), (2.0, 3.0, 7.75, .05, .04), (3.0, 4.0, 7.47, .37, .13)],
    "Reddy (2012)": [(1.9, 2.7, 8.10, .03, .03), (2.7, 3.4, 7.87, .03, .03)],
    "Caputi (2011)": [(3.0, 3.5, 7.32, .04, .02), (3.5, 4.25, 7.05, .11, .10), (4.25, 5.0, 6.37, .14, .54)],
    "Gonzalez (2011)": [(3.8, 3.8, 7.24, .06, .06), (5.0, 5.0, 6.87, .08, .09), (5.9, 5.9, 6.79, .09, .09)],
    "Lee (2012)": [(3.7, 3.7, 7.30, .07, .09), (5.0, 5.0, 6.75, .33, .16)],
    "Yabe (2009)": [(5.0, 5.0, 7.19, .19, .35)],
}

# Khostovan et al. 2016, Table 2 (alpha = -1.3), Chabrier. rho = phi* M* Gamma(alpha+2):
# for z=0.84 Hb+[OIII] and z=1.47 [OII] the tabulated rho (7.62, 7.74) disagree with the
# integral of the tabulated Schechter parameters (7.84, 7.81) and with the published Fig. 5;
# we use the integrated values, matching the published figure.
HBO3 = [(0.84, 7.84, 0.20, 0.08), (1.42, 7.76, 0.07, 0.06), (2.23, 7.18, 0.06, 0.05), (3.24, 6.90, 0.07, 0.06)]
O2 = [(1.47, 7.81, 0.06, 0.06), (2.25, 7.21, 0.10, 0.08), (3.34, 6.51, 0.16, 0.09)]
# Sobral et al. 2014 H-alpha, digitized from Khostovan et al. 2016 Fig. 5
HA = [(0.40, 7.71), (0.84, 7.78), (1.47, 7.55), (2.23, 7.61)]

X = lambda z: np.log10(1.0 + np.asarray(z, float))

def lit(rows):
    zl, zh, v, p, m = map(np.array, zip(*rows))
    zc = 0.5 * (zl + zh)
    x, xl, xh = X(zc), X(zc) - X(zl), X(zh) - X(zc)
    return x, [xl, xh], v + SAL2CHAB, [m, p]

fig, ax = plt.subplots(figsize=(3.6, 3.5), dpi=300)

ekw = dict(fmt="o", ms=4.2, mfc="none", mew=0.8, elinewidth=0.7, capsize=1.6, capthick=0.7)
comp = [r for k, rows in MD14.items() if k not in ("PG08", "I13", "M13") for r in rows]
x, xe, y, ye = lit(comp)
ax.errorbar(x, y, xerr=xe, yerr=ye, color="0.6", alpha=0.55, zorder=1, **ekw)
for key, col, lab in [("PG08", "tab:purple", r"P\'erez-Gonz\'alez+08 (IRAC)"),
                      ("M13", "tab:red", r"Muzzin+13 ($K_s$)"),
                      ("I13", "tab:green", r"Ilbert+13 ($K_s$)")]:
    x, xe, y, ye = lit(MD14[key])
    ax.errorbar(x, y, xerr=xe, yerr=ye, color=col, alpha=0.6, zorder=2, **ekw)

zh, vh = zip(*HA)
ax.plot(X(zh), vh, "h", ms=6.5, mfc="#c5e0b4", mec="tab:olive", mew=1.0, zorder=3)

for data, fc, ec, mk in [(HBO3, "#aec7e8", "tab:blue", "s"), (O2, "#ffbb78", "tab:orange", "D")]:
    z, v, p, m = map(np.array, zip(*data))
    ax.errorbar(X(z), v, yerr=[m, p], fmt=mk, ms=8 if mk == "s" else 7, mfc=fc, mec=ec, mew=1.6,
                ecolor=ec, elinewidth=1.6, capsize=3, capthick=1.6, zorder=5)

ticks = [0, 0.5, 1, 2, 3, 4, 5, 6]
ax.xaxis.set_major_locator(FixedLocator(X(ticks)))
ax.set_xticklabels([("%g" % t) for t in ticks])
minor = [z for z in np.arange(0.1, 6.2, 0.1) if round(z, 1) not in ticks]
ax.xaxis.set_minor_locator(FixedLocator(X(minor)))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_xlim(X(0) - 0.01, X(6.3))
ax.set_ylim(6.0, 9.0)
ax.set_xlabel(r"Redshift ($z$)")
ax.set_ylabel(r"$\log_{10}\,\rho_\star$ (M$_\odot$ Mpc$^{-3}$)")

# legend, styled like the AURORA figures (bold for this work)
from matplotlib.lines import Line2D
h = [Line2D([], [], ls="none", marker="s", ms=7, mfc="#aec7e8", mec="tab:blue", mew=1.5),
     Line2D([], [], ls="none", marker="D", ms=6, mfc="#ffbb78", mec="tab:orange", mew=1.5),
     Line2D([], [], ls="none", marker="h", ms=6, mfc="#c5e0b4", mec="tab:olive", mew=1.0),
     Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="tab:purple", alpha=0.7),
     Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="tab:red", alpha=0.7),
     Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="tab:green", alpha=0.7),
     Line2D([], [], ls="none", marker="o", ms=4.2, mfc="none", mec="0.55", alpha=0.7)]
l = [r"\textbf{H$\bm{\beta}$+[O\,\textsc{iii}] (This Work)}", r"\textbf{[O\,\textsc{ii}] (This Work)}",
     r"H$\alpha$ (Sobral+14)", r"P\'erez-Gonz\'alez+08 (IRAC)", r"Muzzin+13 ($K_s$)", r"Ilbert+13 ($K_s$)",
     r"Compilation (MD14)"]
ax.legend(h, l, loc="lower left", fontsize=7.6, handletextpad=0.4, borderaxespad=0.5, labelspacing=0.35)
ax.text(0.97, 0.95, r"\textbf{HiZELS star-forming galaxies}", transform=ax.transAxes, ha="right", va="top", fontsize=8.5)
ax.text(0.97, 0.885, r"Chabrier IMF", transform=ax.transAxes, ha="right", va="top", fontsize=8, color="tab:blue")

fig.tight_layout(pad=0.3)
fig.savefig(OUT, dpi=300, facecolor="white")
print("saved", OUT)
