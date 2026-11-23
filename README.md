# akhostov.github.io: redesigned site

A fast, dependency-free personal academic website: plain HTML, one stylesheet, one small script.
There's no Jekyll, Ruby, or Node, and no build step is required to view or deploy it.

## Preview locally

```bash
cd ~/website/akhostov.github.io
python3 -m http.server 8000
# open http://localhost:8000
```

Use the local server rather than double-clicking the files. Links are root-relative (`/research/`),
which keeps the URLs clean on GitHub Pages.

## What's where

```
index.html                 Home
research/index.html        Research (four themes, cosmic timeline, glossary)
surveys/index.html         Surveys & data links
publications/index.html    Publications (list is generated from data/publications.json)
teaching/index.html        Teaching & mentoring
outreach/index.html        Outreach & service
music/index.html           Music
about/index.html           About, short bio, career, contact
404.html                   "Lost in space" page
about_me/, teaching_mentorship/, cv/, list_of_publications/   Redirects from old URLs

assets/css/style.css       All styling (colors, fonts, dark mode) in one file
assets/js/main.js          Starfield, theme toggle, mobile menu, glossary tooltips, publication filter
assets/img/                Photos, figures, icons (icons.svg), favicon, social-share card
assets/docs/               Khostovan_CV.pdf (web copy, references page removed) and Khostovan_Publications.pdf
content/*.md               The text of each page, in Markdown (edit here, then run the build script)
data/publications.json     Every paper: the single source of truth for the publications page
partials/                  Shared <head>, header, and footer copied into every page
scripts/build.py           Syncs partials, renders publications, updates counts, writes sitemap.xml
scripts/figures/           Scripts that re-plot paper figures in a common style (see each file's header)
```

## Common edits

**Edit the words on a page.** The text of every page lives in Markdown, one file per page:

```
content/home.md  research.md  surveys.md  publications.md  teaching.md  outreach.md  music.md  about.md
```

Each file is a list of sections that start with a line like `## @archives-why`. Edit the text under a
section, save, and run `python3 scripts/build.py`. The script converts it and puts it back in exactly the
same spot on the page, so the layout doesn't change. Don't rename the `## @…` lines; each one is tied to a
marker in the page's HTML. The build script warns if a section and a marker don't match up.

Markdown you can use: `**bold**`, `*italic*` (use `*z*` for redshift), `[link text](https://…)`,
`[term](#g-redshift)` for a glossary hover on the research page, and a blank line for a new paragraph.
Simple HTML like `<sup>12</sup>` also works, and `\*` gives a literal asterisk (as in L\*).

What stays in HTML: page layout, headings, and short structured items such as the mentee cards,
course names, honors list, and the service list. These are easy to find in the page files.

**Add a new paper.** Open `data/publications.json` and add an entry to `"papers"` (copy an existing one), then run:

```bash
python3 scripts/build.py
```

The script sorts papers by year, renders the list, and updates the counts shown on the home,
publications, teaching, and about pages. Fields:

| field | notes |
|---|---|
| `year`, `authors`, `title`, `journal`, `volume`, `page` | `title` may use `<i>`, `<sub>`, `<sup>` (for example `<i>z</i> ∼ 2`) |
| `status` | `published`, `accepted`, or `submitted` |
| `first_author`, `student_led` | `true` / `false`. Student-led papers get a badge and a filter |
| `summary` | One sentence, shown for first-author papers. May use `<i>`, `<sub>`, `<sup>` |
| `arxiv`, `doi`, `bibcode` | Any subset. Links to ADS, arXiv, and DOI are built automatically |
| `links` | Extra buttons, e.g. `[{"label": "Data", "url": "https://…"}]` |

**Update citation metrics.** Edit `"metrics"` at the top of `data/publications.json` (`citations`, `h_index`,
`first_author_citations`, and `as_of`; take them from NASA ADS), then run the build script.

**Change the menu or footer.** Edit `partials/header.html` or `partials/footer.html`, then run the build script.
Every page is updated between its `<!-- BEGIN … -->` / `<!-- END … -->` markers.

**Update the CV.** Replace `assets/docs/Khostovan_CV.pdf`. The current web copy (from the November 2026
JMU CV) has the references removed: they share page 9 with your last posters, so that page was turned
into an image with the references blanked out, which means the referee details are truly gone. The
easiest way to make future web copies is to compile your LaTeX CV once without the references section
and upload that PDF as-is. `assets/docs/Khostovan_Publications.pdf` is the publication list (pages
10–14 of the same CV).

**Edit text.** Everything else is ordinary HTML in the page files. Research terms marked
`<a class="term" href="#g-…">` show a glossary definition on hover; add new terms to the glossary at the
bottom of `research/index.html`.

## Deploying to GitHub Pages

The folder is ready to publish as-is (`.nojekyll` tells GitHub to serve the files directly). When you're
happy with it:

1. In the `akhostov.github.io` repository, move the old site out of the way (for example onto an
   `old-site` branch) and copy the contents of this folder into the repository root.
2. Delete `.github/workflows/jekyll.yml` (the old Jekyll build is no longer needed).
3. In the repository's **Settings → Pages**, set **Source** to *Deploy from a branch*, branch `main`, folder `/ (root)`.

Old links such as `/about_me/`, `/teaching_mentorship/`, and `/cv/` redirect to their new pages.

## Design notes

- Fonts: Newsreader (headings) and Inter (text), from Google Fonts. Everything falls back to system fonts.
- Colors are defined once at the top of `style.css`. The two accents come from emission lines:
  [O III] 5007 Å (teal) and Hα 6563 Å (red).
- Dark mode follows the visitor's system setting, and the moon/sun button overrides it.
- The night-sky backgrounds are drawn in the browser (no image files). Bright stars get JWST-style
  diffraction spikes and are kept out of the text column.
- YouTube videos load only when clicked, using YouTube's privacy-enhanced domain.
