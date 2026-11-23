"""Shared matplotlib style matching the figures in Khostovan et al. (2026b, AURORA MZR).

Computer Modern via LaTeX, inward ticks on all four sides with minor ticks,
matplotlib "tab" colours, faint open circles for literature data, and filled
markers with dark edges plus bold legend text for "This Work".

Run the figure scripts with MacTeX first on PATH (the MacPorts LaTeX format
file is broken on this machine):
    PATH=/Library/TeX/texbin:$PATH python3 scripts/figures/<script>.py out.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# light fill / dark edge pairs used for "This Work" markers
PAIRS = {
    "tab:blue": "#aec7e8", "tab:orange": "#ffbb78", "tab:green": "#98df8a",
    "tab:red": "#ff9896", "tab:purple": "#c5b0d5", "tab:brown": "#c49c94",
    "tab:pink": "#f7b6d2", "tab:olive": "#dbdb8d", "tab:cyan": "#9edae5",
}

def apply(fontsize=10):
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman"],
        "text.latex.preamble": r"\usepackage[T1]{fontenc}\usepackage{amsmath}\usepackage{bm}",
        "font.size": fontsize,
        "axes.linewidth": 0.9,
        "xtick.direction": "in", "ytick.direction": "in",
        "xtick.top": True, "ytick.right": True,
        "xtick.major.size": 4, "ytick.major.size": 4,
        "xtick.minor.size": 2, "ytick.minor.size": 2,
        "xtick.minor.visible": True, "ytick.minor.visible": True,
        "legend.frameon": False,
        "savefig.facecolor": "white",
    })

# literature "open circle" errorbar style
LIT = dict(fmt="o", ms=4.2, mfc="none", mew=0.8, elinewidth=0.7, capsize=1.6, capthick=0.7)

OIII = r"[O\,\textsc{iii}]"
OII = r"[O\,\textsc{ii}]"
