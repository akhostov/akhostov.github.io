"""Re-plot Khostovan et al. (2016) Figure 4 (stellar mass functions of Hb+[OIII]-
and [OII]-selected galaxies) in the style of Khostovan et al. (2026b).

Data (all Chabrier IMF):
  * Binned SMFs: Tables A1 and A2 of Khostovan et al. 2016 ("final" column).
  * Schechter fits: Table 2 of Khostovan et al. 2016 (alpha fixed to -1.3).
    1-sigma bands use the covariance of a refit to the binned points, which
    reproduces the tabulated (phi*, M*) to within 0.01 dex.
  * Perez-Gonzalez et al. 2008 star-forming SMF at 1.3 < z <= 1.6 (their
    Table 2), Salpeter -> Chabrier (-0.215 dex in mass).
  * Muzzin et al. 2013 star-forming SMF at 3 <= z < 4 with alpha = -1.3 (their
    Table 1). Both literature curves match the published Figure 4 to <0.02 dex.
Schechter form: Phi(M) dlogM = ln(10) phi* (M/M*)^(1+alpha) exp(-M/M*) dlogM.
"""
import sys
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import khostovan_style as ks

OUT = sys.argv[1]
ks.apply(10)
LN10 = np.log(10)

def schechter(lm, lphi, lM, a=-1.3):
    x = 10 ** (lm - lM)
    return np.log10(LN10 * 10 ** lphi * x ** (1 + a) * np.exp(-x))

# (z, colour, marker, logM, logPhi, err, (log phi*, log M*))
HBO3 = [
    (0.84, "tab:purple", "o", [9.0, 9.5, 10.0, 10.5, 11.0, 11.5], [-2.82, -2.76, -3.01, -3.31, -3.42, -3.80], [.09, .09, .10, .13, .17, .29], (-3.87, 11.60)),
    (1.42, "tab:red", "s", [9.5, 10, 10.5, 11, 11.5, 12], [-2.86, -3.19, -3.35, -3.34, -4.02, -4.90], [.10, .11, .12, .12, .22, .55], (-3.90, 11.55)),
    (2.23, "tab:orange", "D", [9.5, 10, 10.5, 11, 11.5], [-3.05, -3.60, -3.74, -4.07, -4.58], [.11, .11, .12, .15, .26], (-4.16, 11.22)),
    (3.24, "tab:blue", "p", [9.75, 10.15, 10.55, 10.95, 11.35], [-3.56, -3.56, -3.79, -4.28, -5.10], [.11, .11, .14, .21, .66], (-4.16, 10.96)),
]
O2 = [
    (1.47, "tab:red", "s", [9.5, 9.9, 10.3, 10.7, 11.1, 11.5, 11.9], [-2.97, -2.97, -3.22, -3.35, -3.46, -3.97, -4.32], [.09, .09, .10, .11, .11, .16, .35], (-3.92, 11.62)),
    (2.25, "tab:orange", "D", [9.6, 10.2, 10.8, 11.4, 12.0], [-3.38, -3.79, -4.05, -4.45, -5.14], [.14, .13, .17, .26, .63], (-4.48, 11.58)),
    (3.34, "tab:blue", "p", [9.75, 10.25, 10.75, 11.25, 11.75], [-4.18, -4.43, -4.83, -5.01, -5.39], [.16, .17, .23, .29, .44], (-5.18, 11.58)),
]
PG08 = (-3.96, 11.62 - 0.215, -1.29)            # star-forming, 1.3 < z <= 1.6
MZ13 = (np.log10(0.08e-4), 11.47, -1.3)         # star-forming, 3 <= z < 4, alpha fixed

lm = np.linspace(7.6, 12.5, 300)
rng = np.random.default_rng(42)

fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.9), dpi=300, sharey=True)
fig.subplots_adjust(wspace=0)

for ax, data, title in [(axes[0], HBO3, r"\textbf{H$\bm{\beta}$+[O\,\textsc{iii}]-selected}"),
                        (axes[1], O2, r"\textbf{[O\,\textsc{ii}]-selected}")]:
    handles, labels = [], []
    for z, col, mk, m, y, e, best in data:
        m, y, e = map(np.array, (m, y, e))
        _, cov = curve_fit(lambda x, a, b: schechter(x, a, b), m, y, p0=best, sigma=e, absolute_sigma=True)
        draws = rng.multivariate_normal(best, cov, 3000)
        curves = np.array([schechter(lm, *d) for d in draws])
        lo, hi = np.nanpercentile(curves, [16, 84], axis=0)
        ax.fill_between(lm, lo, hi, color=col, alpha=0.18, lw=0, zorder=1)
        ax.plot(lm, schechter(lm, *best), color=col, lw=1.4, zorder=2)
        h = ax.errorbar(m, y, yerr=e, fmt=mk, ms=6.5 if mk != "p" else 7.5, mfc=ks.PAIRS[col], mec=col, mew=1.3,
                        ecolor=col, elinewidth=1.1, capsize=2.5, capthick=1.1, zorder=5)
        handles.append(h); labels.append(r"\textbf{$\bm{z = %.2f}$ (This Work)}" % z)
    l1, = ax.plot(lm, schechter(lm, *PG08), color="tab:green", ls="-.", lw=1.3, zorder=3)
    handles.append(l1); labels.append(r"P\'erez-Gonz\'alez+08 (SF; $z \approx 1.45$)")
    if data is O2:
        l2, = ax.plot(lm, schechter(lm, *MZ13), color="tab:pink", ls="--", lw=1.3, zorder=3)
        handles.append(l2); labels.append(r"Muzzin+13 (SF; $z \approx 3.5$)")
    ax.legend(handles, labels, loc="lower left", fontsize=7.6, handletextpad=0.4, borderaxespad=0.5, labelspacing=0.35)
    ax.text(0.96, 0.95, title, transform=ax.transAxes, ha="right", va="top", fontsize=9)
    ax.set_xlim(7.6, 12.45)
    ax.set_xlabel(r"$\log_{10}$ Stellar Mass (M$_\odot$)")

axes[0].set_ylim(-6.0, -2.3)
axes[0].set_ylabel(r"$\log_{10}\,\Phi$ (Mpc$^{-3}$ dex$^{-1}$)")
axes[1].set_xticks([8, 9, 10, 11, 12])
fig.tight_layout(pad=0.3)
fig.subplots_adjust(wspace=0)
fig.savefig(OUT, dpi=300)
print("saved", OUT)
