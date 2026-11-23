"""Top-down astroTopics illustration (after the original image), in the site's palette."""
CX, CY, R, TR = 480, 270, 206, 186
people = [
    # angle, shirt, skin, hair, item
    (0,   "#f6b2a2", "#e2b48e", "#e9c46a", "paper"),
    (45,  "#5fd0dc", "#c99a74", "#1d1712", "laptop"),
    (90,  "#ff8f73", "#f0d4b8", "#7a4b2a", "laptop"),
    (135, "#7aa7ff", "#8d5f3f", "#120d0a", "tablet"),
    (180, "#2f8f9d", "#b07d57", "#241a12", "laptop"),
    (225, "#e9c46a", "#f3dcc4", "#3a2a1d", "paper"),
    (270, "#b9a7ff", "#d8a982", "#4a3324", "tablet"),
    (315, "#9be7a0", "#c99a74", "#2b2118", "laptop"),
]

def person(a, shirt, skin, hair, item):
    y = -R  # person's centre (shoulders); +y points toward the table centre
    g = [f'<g transform="translate({CX} {CY}) rotate({a})">']
    # chair back
    g.append(f'<rect x="-34" y="{y-40}" width="68" height="22" rx="10" fill="#4b5878"/>')
    # arms reaching onto the table
    for sx in (-1, 1):
        g.append(f'<path d="M{sx*30} {y-4} Q{sx*40} {y+26} {sx*22} {y+52}" fill="none" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(f'<circle cx="{sx*21}" cy="{y+56}" r="8" fill="{skin}"/>')
    # shoulders / torso seen from above
    g.append(f'<rect x="-42" y="{y-24}" width="84" height="34" rx="17" fill="{shirt}"/>')
    # head seen from above: mostly hair, a sliver of face toward the table
    g.append(f'<ellipse cx="0" cy="{y+6}" rx="15" ry="13" fill="{skin}"/>')
    g.append(f'<circle cx="0" cy="{y-4}" r="19" fill="{hair}"/>')
    # item on the table
    if item == "laptop":
        g.append(f'<rect x="-32" y="{y+62}" width="64" height="30" rx="3" fill="#c9d3ea"/>')
        g.append(f'<g fill="#9aa6c4">' + "".join(f'<rect x="{-27+i*9}" y="{y+67+j*7}" width="6" height="4" rx="1"/>' for i in range(6) for j in range(3)) + '</g>')
        g.append(f'<rect x="-32" y="{y+93}" width="64" height="26" rx="3" fill="#dfe6f5"/><rect x="-27" y="{y+97}" width="54" height="18" rx="2" fill="#1b2747"/>')
        g.append(f'<polyline points="-22,{y+110} -12,{y+108} -6,{y+109} -2,{y+100} 3,{y+109} 12,{y+107} 22,{y+108}" fill="none" stroke="#5fd0dc" stroke-width="1.6"/>')
    elif item == "tablet":
        g.append(f'<rect x="-24" y="{y+66}" width="48" height="34" rx="4" fill="#0b1124" stroke="#c9d3ea" stroke-width="2"/>')
        g.append(f'<path d="M0 {y+83} m-12 0 a12 5 -20 1 0 24 0 a12 5 -20 1 0 -24 0" fill="none" stroke="#b9a7ff" stroke-width="1.8"/><circle cx="0" cy="{y+83}" r="2.2" fill="#fff"/>')
        g.append(f'<circle cx="40" cy="{y+74}" r="9" fill="#e8edf8"/><circle cx="40" cy="{y+74}" r="5.5" fill="#6b4a32"/>')
    else:  # paper + notebook
        g.append(f'<g transform="translate(-8 {y+82}) rotate(-8)"><rect x="-22" y="-16" width="44" height="32" rx="2" fill="#f4f6fb"/><path d="M-14 -6h28M-14 2h20M-14 9h24" stroke="#9aa6c4" stroke-width="1.5"/></g>')
        g.append(f'<g transform="translate(34 {y+76}) rotate(14)"><rect x="-6" y="-14" width="12" height="28" rx="2" fill="#1b2747"/></g>')
        g.append(f'<circle cx="-46" cy="{y+70}" r="9" fill="#e8edf8"/><circle cx="-46" cy="{y+70}" r="5.5" fill="#6b4a32"/>')
    g.append("</g>")
    return "\n    ".join(g)

stars = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(70, 60, 1.6), (150, 440, 1.2), (880, 90, 1.5), (830, 470, 1.2), (220, 110, 1), (760, 36, 1), (905, 300, 1.3), (40, 300, 1.1), (120, 230, 0.9), (860, 220, 0.9)])
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img" aria-labelledby="t">
  <title id="t">Illustration of astroTopics seen from above: eight people seated around a round table with laptops, tablets, papers, and coffee</title>
  <defs>
    <radialGradient id="bg" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#1c2c4c"/><stop offset=".65" stop-color="#0f1730"/><stop offset="1" stop-color="#0a1022"/></radialGradient>
    <radialGradient id="table" cx="45%" cy="40%" r="70%"><stop offset="0" stop-color="#2d4472"/><stop offset="1" stop-color="#1f3058"/></radialGradient>
  </defs>
  <rect width="960" height="540" fill="url(#bg)"/>
  <g fill="#fff" opacity=".45">{stars}</g>
  <circle cx="{CX}" cy="{CY}" r="{TR}" fill="url(#table)" stroke="#4a62a0" stroke-width="2.5"/>
    {chr(10).join("    " + person(*p) for p in people)}
  <text x="{CX}" y="{CY+2}" text-anchor="middle" fill="#ffffff" font-family="Georgia, 'Times New Roman', serif" font-size="27">astroTopics</text>
  <text x="{CX}" y="{CY+24}" text-anchor="middle" fill="#8fe3ec" font-family="Inter, Helvetica, Arial, sans-serif" font-size="10.5" letter-spacing="1.4">VOTE · READ · DISCUSS</text>
</svg>
'''
open("/Users/aahsps/website/updated_website/assets/img/teaching/astrotopics.svg", "w").write(svg)
print("ok")
