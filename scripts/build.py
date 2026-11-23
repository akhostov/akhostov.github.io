#!/usr/bin/env python3
"""Maintenance script for the website (Python 3.8+, standard library only).

Usage, from the website folder:

    python3 scripts/build.py

What it does:
  0. Converts the page text in content/*.md (Markdown) into HTML and places each section at its
     <!-- BEGIN md:name --> / <!-- BEGIN mdi:name --> marker. Edit the text there, not in the HTML.
  1. Copies the shared snippets in partials/ (head.html, header.html, footer.html) into
     every page, between the marker comments <!-- BEGIN header --> ... <!-- END header -->.
     Edit the menu or footer once in partials/, run this, and every page is updated.
  2. Renders data/publications.json into publications/index.html (lists, filters, counts).
  3. Updates any element marked data-stat="papers|first|coauthored|first-citations|citations|hindex|student" on any page.
  4. Rewrites sitemap.xml.

The pages are plain HTML and work without running this script; run it after you edit a
partial or the publication data. It only rewrites text between marker comments.
"""
import datetime
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://akhostov.github.io"
ME = "A. A. Khostovan"
PARTIALS = ("head", "header", "footer")


# --------------------------------------------------------------------------- helpers
def html_pages():
    skip = {"partials", "scripts", "data", "assets", ".git"}
    return sorted(p for p in ROOT.rglob("*.html") if not (set(p.relative_to(ROOT).parts) & skip))


def replace_block(text, name, content):
    pattern = re.compile(r"(<!-- BEGIN %s -->)(.*?)(<!-- END %s -->)" % (re.escape(name), re.escape(name)), re.S)
    if not pattern.search(text):
        return text, False
    return pattern.sub(lambda m: m.group(1) + "\n" + content.strip("\n") + "\n" + m.group(3), text, count=1), True


def safe_html(s):
    """Allow the simple inline HTML used in titles (<i>, <sub>, <sup>) but escape stray ampersands."""
    s = re.sub(r"&(?![a-zA-Z]+;|#\d+;|#x[0-9a-fA-F]+;)", "&amp;", s)
    return s.replace("[O III]", "[O&nbsp;III]").replace("[O II]", "[O&nbsp;II]").replace("[N II]", "[N&nbsp;II]")


def esc(s):
    return html.escape(str(s), quote=True)


def fmt_int(n):
    return "{:,}".format(n) if isinstance(n, int) else str(n)


# --------------------------------------------------------------------------- publications
def ads_url(p):
    if p.get("bibcode"):
        return "https://ui.adsabs.harvard.edu/abs/%s/abstract" % quote(p["bibcode"], safe="")
    if p.get("arxiv"):
        return "https://ui.adsabs.harvard.edu/abs/arXiv:%s/abstract" % p["arxiv"]
    return ""


def pub_links(p):
    links = []
    if ads_url(p):
        links.append(("ADS", ads_url(p)))
    if p.get("arxiv"):
        links.append(("arXiv", "https://arxiv.org/abs/%s" % p["arxiv"]))
    if p.get("doi"):
        links.append(("DOI", "https://doi.org/%s" % p["doi"]))
    seen = {label for label, _ in links}
    for extra in p.get("links", []):
        if extra["label"] not in seen:
            links.append((extra["label"], extra["url"]))
            seen.add(extra["label"])
    return links


def venue(p):
    j = "<i>%s</i>" % esc(p["journal"])
    if p["status"] == "submitted":
        return "Submitted to %s" % j
    if p["status"] == "accepted":
        return "%s, accepted (%s)" % (j, p["year"])
    parts = [j] + [esc(x) for x in (p.get("volume"), p.get("page")) if x]
    return "%s (%s)" % (", ".join(parts), p["year"])


def render_pub(p):
    links = pub_links(p)
    href = links[0][1] if links else ""
    title = safe_html(p["title"])
    title_html = '<a href="%s">%s</a>' % (esc(href), title) if href else title
    authors = esc(p["authors"]).replace(esc(ME), "<strong>%s</strong>" % esc(ME))
    badges = []
    if p.get("student_led"):
        badges.append('<span class="badge badge-violet">Student-led</span>')
    if p["status"] == "submitted":
        badges.append('<span class="badge badge-gold">Under review</span>')
    elif p["status"] == "accepted":
        badges.append('<span class="badge badge-teal">In press</span>')
    link_html = "".join(
        '<a href="%s">%s<svg class="icon" aria-hidden="true"><use href="/assets/img/icons.svg#i-external"/></svg></a>'
        % (esc(url), esc(label)) for label, url in links)
    out = ['<li class="pub" data-first="%d" data-student="%d">' % (p.get("first_author", False), p.get("student_led", False)),
           '  <h3 class="pub-title">%s</h3>' % title_html,
           '  <p class="pub-authors">%s</p>' % authors,
           '  <p class="pub-venue">%s</p>' % venue(p)]
    if p.get("summary"):
        out.append('  <p class="pub-summary"><b>In brief</b>%s</p>' % safe_html(p["summary"]))
    if badges or link_html:
        out.append('  <p class="pub-links">%s%s</p>' % ("".join(badges), link_html))
    out.append("</li>")
    return "\n".join(out)


def render_publications(data):
    papers = data["papers"]
    first = sorted((p for p in papers if p.get("first_author")), key=lambda p: -p["year"])
    others = [p for p in papers if not p.get("first_author")]
    pending = [p for p in others if p["status"] != "published"]
    published = sorted((p for p in others if p["status"] == "published"), key=lambda p: -p["year"])
    n_all, n_first = len(papers), len(first)
    n_student = sum(1 for p in papers if p.get("student_led"))

    h = []
    h.append('<div class="pub-toolbar" data-pubs>')
    h.append('  <div class="seg" role="group" aria-label="Filter publications">')
    h.append('    <button type="button" data-filter="all" aria-pressed="true">All <span class="n">%d</span></button>' % n_all)
    h.append('    <button type="button" data-filter="first" aria-pressed="false">First-author <span class="n">%d</span></button>' % n_first)
    h.append('    <button type="button" data-filter="student" aria-pressed="false">Student-led <span class="n">%d</span></button>' % n_student)
    h.append('  </div>')
    h.append('  <label class="search"><span class="visually-hidden">Search publications</span>'
             '<svg class="icon" aria-hidden="true"><use href="/assets/img/icons.svg#i-search"/></svg>'
             '<input type="search" placeholder="Search titles, authors, journals…" autocomplete="off"></label>')
    h.append('  <span class="pub-count" data-count aria-live="polite">%d papers</span>' % n_all)
    h.append('</div>')
    h.append('<p class="pub-legend"><span class="badge badge-violet">Student-led</span> marks papers led by a student I mentored. '
             'Titles link to NASA ADS.</p>')

    h.append('<section class="pub-section" data-pub-group id="first-author">')
    h.append('  <h2>First-author papers</h2>')
    h.append('  <p class="muted">Papers I led, each with a one-line summary in plain language.</p>')
    h.append('  <ol class="pub-list first-list" reversed>')
    h.extend("    " + line for p in first for line in render_pub(p).split("\n"))
    h.append('  </ol>')
    h.append('</section>')

    h.append('<section class="pub-section" id="collaborations">')
    h.append('  <h2>Collaborative papers</h2>')
    h.append('  <p class="muted">Papers from the surveys and teams I am part of, newest first.</p>')
    groups = []
    if pending:
        groups.append(("In press &amp; under review", "pending", pending))
    years = []
    for p in published:
        if p["year"] not in years:
            years.append(p["year"])
    for y in years:
        groups.append((str(y), "y%d" % y, [p for p in published if p["year"] == y]))
    for label, gid, items in groups:
        h.append('  <div data-pub-group id="%s">' % gid)
        h.append('    <h3 class="pub-year">%s</h3>' % label)
        h.append('    <ul class="pub-list">')
        h.extend("      " + line for p in items for line in render_pub(p).split("\n"))
        h.append('    </ul>')
        h.append('  </div>')
    h.append('</section>')
    h.append('<p class="pub-empty" data-pub-empty hidden>No papers match your search. Try a different word or clear the filter.</p>')
    return "\n".join(h)


def stat_values(data):
    papers = data["papers"]
    m = data.get("metrics", {})
    return {
        "papers": fmt_int(len(papers)),
        "first": fmt_int(sum(1 for p in papers if p.get("first_author"))),
        "coauthored": fmt_int(sum(1 for p in papers if not p.get("first_author"))),
        "student": fmt_int(sum(1 for p in papers if p.get("student_led"))),
        "citations": fmt_int(m.get("citations", "")),
        "hindex": fmt_int(m.get("h_index", "")),
        "first-citations": fmt_int(m.get("first_author_citations", "")),
        "metrics-date": esc(m.get("as_of", "")),
    }


STAT_RE = re.compile(r'(<[a-z][a-z0-9]*\b[^>]*\bdata-stat="([a-z-]+)"[^>]*>)[^<]*(?=</)')


def apply_stats(text, values):
    """Replace the text inside any element carrying data-stat="key" with the current value."""
    return STAT_RE.sub(lambda m: m.group(1) + values[m.group(2)] if m.group(2) in values else m.group(0), text)


# --------------------------------------------------------------------------- page text (Markdown)
# Each page's prose lives in content/<page>.md as sections that start with "## @name".
# The matching spot in the HTML is marked <!-- BEGIN md:name --> ... <!-- END md:name -->
# (paragraphs) or <!-- BEGIN mdi:name --> ... (inline text inside one element).
CONTENT_FILES = {"index.html": "home", "research/index.html": "research", "surveys/index.html": "surveys",
                 "publications/index.html": "publications", "teaching/index.html": "teaching", "mentoring/index.html": "mentoring",
                 "outreach/index.html": "outreach", "music/index.html": "music", "about/index.html": "about"}
NBSP = " "


def parse_content(path):
    blocks, name, lines = {}, None, []
    text = re.sub(r"(?s)<!--.*?-->", "", path.read_text(encoding="utf-8"))  # drop editor notes
    for line in text.splitlines():
        m = re.match(r"^##\s*@([\w-]+)\s*$", line)
        if m:
            if name:
                blocks[name] = "\n".join(lines).strip()
            name, lines = m.group(1), []
        elif name:
            lines.append(line)
    if name:
        blocks[name] = "\n".join(lines).strip()
    return blocks


def _links(s):
    """[text](url) -> <a>, allowing balanced parentheses inside the URL."""
    out, i = [], 0
    while True:
        j = s.find("[", i)
        if j < 0:
            out.append(s[i:]); break
        k = s.find("]", j)
        if k < 0 or s[k + 1:k + 2] != "(":       # plain brackets such as [O III], not a link
            out.append(s[i:j + 1]); i = j + 1; continue
        depth, e = 1, k + 2
        while e < len(s) and depth:
            depth += {"(": 1, ")": -1}.get(s[e], 0); e += 1
        if depth:
            out.append(s[i:j + 1]); i = j + 1; continue
        label, url = s[j + 1:k], s[k + 2:e - 1].strip()
        cls = ' class="term"' if url.startswith("#g-") else ""
        out.append(s[i:j] + '<a%s href="%s">%s</a>' % (cls, url.replace('"', "%22"), label))
        i = e
    return "".join(out)


def md_inline(s):
    s = s.replace("\\*", "\x00")                                   # literal asterisks
    s = re.sub(r"&(?![a-zA-Z]+;|#\d+;|#x[0-9a-fA-F]+;)", "&amp;", s)
    s = re.sub(r"<(?![a-zA-Z/!])", "&lt;", s)
    s = _links(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = s.replace("\x00", "*")
    # typographic non-breaking spaces (so "10.5 billion" or "z = 2" never split across lines)
    s = s.replace("[O III]", "[O" + NBSP + "III]").replace("[O II]", "[O" + NBSP + "II]")
    s = re.sub(r"(\d) (billion|million|Å|dex)\b", r"\1" + NBSP + r"\2", s)
    s = re.sub(r"(<i>z</i>) (=|≈|≳|&lt;|&gt;|<|>) ", r"\1" + NBSP + r"\2" + NBSP, s)
    return s


def md_to_html(text, inline):
    paras = [" ".join(p.split()) for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    if inline:
        return "<br><br>".join(md_inline(p) for p in paras)
    return "\n".join("<p>%s</p>" % md_inline(p) for p in paras)


def apply_content(rel, text, problems):
    key = CONTENT_FILES.get(rel)
    src = ROOT / "content" / ("%s.md" % key) if key else None
    if not src or not src.exists():
        return text
    blocks, used = parse_content(src), set()

    def sub(m):
        kind, name = m.group(1), m.group(2)
        if name not in blocks:
            problems.append("%s: no section '## @%s' in content/%s.md (kept existing text)" % (rel, name, key))
            return m.group(0)
        used.add(name)
        html_ = md_to_html(blocks[name], inline=(kind == "mdi"))
        sep = "" if kind == "mdi" else "\n"
        return "<!-- BEGIN %s:%s -->%s%s%s<!-- END %s:%s -->" % (kind, name, sep, html_, sep, kind, name)

    text = re.sub(r"<!-- BEGIN (mdi?):([\w-]+) -->.*?<!-- END \1:\2 -->", sub, text, flags=re.S)
    for name in sorted(set(blocks) - used):
        problems.append("content/%s.md: section '@%s' is not used on the page" % (key, name))
    return text


# --------------------------------------------------------------------------- sitemap
def write_sitemap(pages):
    urls = []
    for p in pages:
        text = p.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in text or 'name="robots" content="noindex' in text or p.name == "404.html":
            continue
        rel = p.relative_to(ROOT).as_posix()
        loc = SITE_URL + "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
        lastmod = datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()
        urls.append("  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (esc(loc), lastmod))
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % "\n".join(urls)
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    return len(urls)


# --------------------------------------------------------------------------- main
def main():
    partials = {name: (ROOT / "partials" / ("%s.html" % name)).read_text(encoding="utf-8") for name in PARTIALS}
    data = json.loads((ROOT / "data" / "publications.json").read_text(encoding="utf-8"))
    values = stat_values(data)
    pubs_html = render_publications(data)

    pages = html_pages()
    changed, problems = [], []
    for page in pages:
        original = page.read_text(encoding="utf-8")
        text = apply_content(page.relative_to(ROOT).as_posix(), original, problems)
        for name, content in partials.items():
            text, _ = replace_block(text, name, content)
        text, _ = replace_block(text, "publications", pubs_html)
        text = apply_stats(text, values)
        if text != original:
            page.write_text(text, encoding="utf-8")
            changed.append(page.relative_to(ROOT).as_posix())

    n_urls = write_sitemap(pages)
    print("Pages updated: %s" % (", ".join(changed) if changed else "none (already up to date)"))
    print("Publications: %s total, %s first-author, %s student-led" % (values["papers"], values["first"], values["student"]))
    print("Sitemap: %d URLs" % n_urls)
    for p in problems:
        print("WARNING: " + p)


if __name__ == "__main__":
    sys.exit(main())
