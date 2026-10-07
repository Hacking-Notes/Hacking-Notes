#!/usr/bin/env python3
"""Animated SVG art for the Hacking-Notes GitHub profile README.

Every file is a standalone SVG using only inline CSS / SMIL animation, which is
all GitHub's image sandbox allows (no <script>, no external fonts/images).
Run:  python3 scripts/profile_art.py   (writes into assets/)
"""
import random
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "assets"

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
BG="#ffffff"; PANEL="#ffffff"; LINE="#d0d7de"; TEXT="#1f2328"; MUTED="#59636e"; BAR="#f6f8fa"
GREEN="#059669"; CYAN="#0891b2"; BLUE="#0284c7"; PURPLE="#7c3aed"; MAGENTA="#db2777"; AMBER="#d97706"; RED="#e5484d"
RM = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def w(name, svg):
    p = A / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", p.relative_to(ROOT))


def window_chrome(W, fname, c):
    return (f'<rect width="{W}" height="40" fill="{BAR}"/>'
            f'<circle cx="26" cy="20" r="5.5" fill="#ff5f57"/><circle cx="46" cy="20" r="5.5" fill="#febc2e"/><circle cx="66" cy="20" r="5.5" fill="#28c840"/>'
            f'<text x="{W/2}" y="25" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{MUTED}">{escape(fname)}</text>'
            f'<circle cx="{W-26}" cy="20" r="4" fill="{c}"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>')


def icon(kind, c, sw=2.4):
    s = f'fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'
    if kind=="user":   return f'<circle cx="0" cy="-6" r="7" {s}/><path d="M-12 14 C-12 2 12 2 12 14" {s}/>'
    if kind=="repo":   return f'<path d="M-11 -14 H9 A3 3 0 0 1 12 -11 V14 H-8 A3 3 0 0 1 -11 11 Z" {s}/><path d="M-11 9 H9" {s}/><path d="M-6 -14 V6" {s}/>'
    if kind=="shield": return f'<path d="M0 -15 L13 -10 V2 C13 11 0 16 0 16 C0 16 -13 11 -13 2 V-10 Z" {s}/><path d="M-5 0 L-1 5 L6 -5" {s}/>'
    if kind=="wrench": return f'<path d="M6 -10 A7 7 0 1 0 12 -2 L2 8 L-9 13 L-12 10 L-7 -1 Z" {s}/>'
    if kind=="bug":    return f'<ellipse cx="0" cy="3" rx="8" ry="11" {s}/><circle cx="0" cy="-11" r="4.5" {s}/><path d="M-8 -3 H-15 M8 -3 H15 M-8 4 H-15 M8 4 H15 M-7 11 L-13 15 M7 11 L13 15" {s}/>'
    return ""


# ------------------------------------------------------------------ hero
def hero():
    W, H = 1200, 460
    rnd = random.Random(7)
    rain = []
    for i in range(36):
        x = 16 + i * 33 + rnd.randint(-5, 5)
        chars = "".join(rnd.choice("01") for _ in range(24))
        dur = rnd.uniform(7, 15); dl = -rnd.uniform(0, dur)
        tsp = "".join(f'<tspan x="{x}" dy="19">{ch}</tspan>' for ch in chars)
        rain.append(f'<text class="rain" style="animation-duration:{dur:.1f}s;animation-delay:{dl:.1f}s" opacity="{rnd.uniform(0.05,0.16):.2f}">{tsp}</text>')
    title = "HACKING NOTES"
    sub = "> red team · blue team · bug bounty · research"
    n = len(sub); subw = n*22*0.6; subx=(W-subw)/2
    chips = ["OFFENSE","DEFENSE","TOOLS","CVEs"]
    cols = [RED, BLUE, PURPLE, AMBER]
    gap=210; start=W/2-gap*(len(chips)-1)/2; dots=""
    for i,(ch,col) in enumerate(zip(chips,cols)):
        cx=start+i*gap; lw=len(ch)*7.4
        dots+=(f'<g class="dot" style="animation-delay:{i*.3:.2f}s">'
               f'<circle cx="{cx-lw/2-12:.0f}" cy="388" r="5" fill="{col}"/>'
               f'<text x="{cx-lw/2:.0f}" y="393" font-family="{MONO}" font-size="13" letter-spacing="1" fill="{MUTED}">{ch}</text></g>')
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Hacking Notes">
<title>Hacking Notes</title>
<defs>
  <linearGradient id="ti" x1="0" x2="1"><stop offset="0" stop-color="{GREEN}"/><stop offset=".33" stop-color="{CYAN}"/><stop offset=".66" stop-color="{BLUE}"/><stop offset="1" stop-color="{PURPLE}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-0.3 0;0.3 0;-0.3 0" dur="8s" repeatCount="indefinite"/></linearGradient>
  <radialGradient id="gl" cx=".5" cy=".42" r=".6"><stop offset="0" stop-color="{GREEN}" stop-opacity=".10"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
  <linearGradient id="sc" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}" stop-opacity=".10"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient>
  <pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0 H0 V40" fill="none" stroke="{GREEN}" stroke-opacity=".10" stroke-width="1"/><animateTransform attributeName="patternTransform" type="translate" from="0 0" to="0 40" dur="4s" repeatCount="indefinite"/></pattern>
  <linearGradient id="fd" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".32" stop-color="#fff"/><stop offset=".82" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <mask id="fm"><rect width="{W}" height="{H}" fill="url(#fd)"/></mask>
  <clipPath id="fr"><rect width="{W}" height="{H}" rx="20"/></clipPath>
  <clipPath id="ty"><rect class="typer" x="{subx:.1f}" y="250" width="{subw:.1f}" height="40"/></clipPath>
</defs>
<style>
  .rain{{font-family:{MONO};font-size:15px;fill:{GREEN};animation:fall linear infinite}}
  @keyframes fall{{from{{transform:translateY(-460px)}}to{{transform:translateY(460px)}}}}
  .scan{{animation:scn 6s linear infinite}} @keyframes scn{{from{{transform:translateY(-160px)}}to{{transform:translateY({H}px)}}}}
  .typer{{transform-box:fill-box;transform-origin:left;animation:ty 9s steps({n},end) infinite}}
  @keyframes ty{{0%{{transform:scaleX(0)}}45%,90%{{transform:scaleX(1)}}100%{{transform:scaleX(0)}}}}
  .cur{{animation:cu 9s steps({n},end) infinite,bl 1s step-end infinite}}
  @keyframes cu{{0%{{transform:translateX(0)}}45%,90%{{transform:translateX({subw:.1f}px)}}100%{{transform:translateX(0)}}}}
  @keyframes bl{{50%{{opacity:0}}}}
  .g1{{animation:g1 5s infinite}} .g2{{animation:g2 5s infinite}}
  @keyframes g1{{0%,88%,100%{{transform:translate(0,0);opacity:0}}90%{{transform:translate(-5px,2px);opacity:.75}}93%{{transform:translate(4px,-2px);opacity:.75}}96%{{transform:translate(-2px,0);opacity:.5}}}}
  @keyframes g2{{0%,88%,100%{{transform:translate(0,0);opacity:0}}90%{{transform:translate(5px,-2px);opacity:.75}}93%{{transform:translate(-4px,2px);opacity:.75}}96%{{transform:translate(2px,0);opacity:.5}}}}
  .dot{{animation:pu 2.4s ease-in-out infinite}} @keyframes pu{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
  .badge{{animation:pu 3s ease-in-out infinite}}
  {RM}
</style>
<g clip-path="url(#fr)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect width="{W}" height="{H}" fill="url(#gr)" mask="url(#fm)"/>
  <g mask="url(#fm)">{''.join(rain)}</g>
  <rect width="{W}" height="{H}" fill="url(#gl)"/>
  <rect class="scan" width="{W}" height="160" fill="url(#sc)"/>
  <g class="badge"><rect x="{W/2-140}" y="66" width="280" height="30" rx="15" fill="{GREEN}" fill-opacity=".08" stroke="{GREEN}" stroke-opacity=".45"/>
    <text x="{W/2}" y="86" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{GREEN}">[ SECURITY RESEARCHER ]</text></g>
  <g font-family="{SANS}" font-size="88" font-weight="800" text-anchor="middle" letter-spacing="5">
    <text class="g1" x="{W/2}" y="215" fill="{MAGENTA}">{title}</text>
    <text class="g2" x="{W/2}" y="215" fill="{CYAN}">{title}</text>
    <text x="{W/2}" y="215" fill="url(#ti)">{title}</text>
  </g>
  <g clip-path="url(#ty)"><text x="{subx:.1f}" y="279" font-family="{MONO}" font-size="22" fill="{TEXT}" xml:space="preserve">{escape(sub)}</text></g>
  <rect class="cur" x="{subx+2:.1f}" y="259" width="12" height="26" fill="{GREEN}"/>
  <path d="M{W/2-430} 346 H{W/2+430}" stroke="{LINE}"/>
  {dots}
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="none" stroke="{GREEN}" stroke-opacity=".25"/>
</g>
</svg>"""


# ------------------------------------------------------------------ stats strip
def stats():
    W, H = 1200, 160
    tiles = [("490+","FOLLOWERS","user",GREEN),("19","PUBLIC REPOS","repo",BLUE),
             ("12","CVEs DISCLOSED","shield",RED),("12+","TOOLS SHIPPED","wrench",PURPLE)]
    tw = W/4; parts=""
    for i,(num,lab,ic,c) in enumerate(tiles):
        cx = tw*i + tw/2
        parts += f"""
  <g class="tile" style="animation-delay:{i*.18:.2f}s">
    <g transform="translate({cx-120:.0f} {H/2-4}) scale(1.05)" stroke-width="2.4">{icon(ic,c)}</g>
    <text x="{cx-86:.0f}" y="{H/2-14:.0f}" font-family="{SANS}" font-size="44" font-weight="800" fill="{c}" class="num" style="animation-delay:{i*.18:.2f}s">{num}</text>
    <text x="{cx-86:.0f}" y="{H/2+20:.0f}" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{MUTED}">{lab}</text>
    <rect x="{cx-88:.0f}" y="{H/2+34:.0f}" width="150" height="3" rx="1.5" fill="{LINE}"/>
    <rect x="{cx-88:.0f}" y="{H/2+34:.0f}" width="150" height="3" rx="1.5" fill="{c}" class="bar" style="animation-delay:{i*.18:.2f}s"/>
  </g>"""
        if i < 3:
            parts += f'<line x1="{tw*(i+1):.0f}" y1="40" x2="{tw*(i+1):.0f}" y2="{H-40}" stroke="{LINE}"/>'
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Profile stats">
<title>Profile stats</title>
<style>
  .tile{{opacity:0;animation:up .7s ease-out forwards}}
  @keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
  .num{{transform-box:fill-box;transform-origin:left center;animation:pop .7s cubic-bezier(.2,1.3,.4,1) both}}
  @keyframes pop{{from{{transform:scale(.4);opacity:0}}to{{transform:scale(1);opacity:1}}}}
  .bar{{transform-box:fill-box;transform-origin:left;animation:fill 1s ease-out .3s both}}
  @keyframes fill{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
  {RM}
</style>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="{PANEL}" stroke="{LINE}"/>
{parts}
</svg>"""


# ------------------------------------------------------------------ project card
def card(fname, title, desc, tags, pill, c, motif):
    W, H = 580, 280
    def rp(x,y,w_,h_,r):
        return (f"M{x+r} {y} H{x+w_-r} A{r} {r} 0 0 1 {x+w_} {y+r} V{y+h_-r} A{r} {r} 0 0 1 {x+w_-r} {y+h_} "
                f"H{x+r} A{r} {r} 0 0 1 {x} {y+h_-r} V{y+r} A{r} {r} 0 0 1 {x+r} {y} Z")
    border = rp(1.5,1.5,W-3,H-3,18)
    d1,d2 = (desc+["",""])[:2]
    chips=""; x=260
    for t in tags:
        cw=len(t)*7.4+22
        chips+=(f'<rect x="{x:.0f}" y="212" width="{cw:.0f}" height="26" rx="6" fill="{c}" fill-opacity=".10" stroke="{c}" stroke-opacity=".4"/>'
                f'<text x="{x+cw/2:.0f}" y="229" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" letter-spacing=".5" fill="{c}">{escape(t)}</text>')
        x+=cw+10
    pw=len(pill)*7+24
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<defs>
  <radialGradient id="cg" cx=".12" cy=".2" r=".9"><stop offset="0" stop-color="{c}" stop-opacity=".16"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>
  <pattern id="cd" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="{c}" fill-opacity=".15"/></pattern>
  <clipPath id="cf"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<style>
  .sweep{{stroke-dasharray:26 110;animation:sw 5s linear infinite}} @keyframes sw{{to{{stroke-dashoffset:-136}}}}
  .blink{{animation:bk 1.2s step-end infinite}} @keyframes bk{{50%{{opacity:.2}}}}
  .flo{{animation:flo 4s ease-in-out infinite}} @keyframes flo{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
  {motif['css']}
  {RM}
</style>
<g clip-path="url(#cf)">
  <rect width="{W}" height="{H}" fill="{PANEL}"/>
  <rect width="{W}" height="{H}" fill="url(#cg)"/>
  <rect x="236" width="{W-236}" height="{H}" fill="url(#cd)"/>
  {window_chrome(W, fname, c)}
  <g transform="translate(130 162)">{motif['svg']}</g>
  <text x="258" y="104" font-family="{SANS}" font-size="30" font-weight="800" fill="{TEXT}">{escape(title)}</text>
  <text x="260" y="140" font-family="{SANS}" font-size="14.5" fill="{MUTED}">{escape(d1)}</text>
  <text x="260" y="162" font-family="{SANS}" font-size="14.5" fill="{MUTED}">{escape(d2)}</text>
  {chips}
  <rect x="260" y="{H-42}" width="{pw:.0f}" height="26" rx="13" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-opacity=".5"/>
  <text x="{260+pw/2:.0f}" y="{H-24}" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" letter-spacing=".5" fill="{c}">{escape(pill)}</text>
</g>
<path d="{border}" fill="none" stroke="{c}" stroke-opacity=".22" stroke-width="1.5"/>
<path class="sweep" d="{border}" pathLength="136" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>
</svg>"""


# -------- motifs (centred on 0,0, ~190 box) ----------
def m_notes():
    # red | blue split screen with typing lines
    css=(".l1{animation:t1 4s steps(10) infinite}.l2{animation:t2 4s steps(14) infinite}"
         "@keyframes t1{0%,100%{width:0}40%{width:48px}}@keyframes t2{0%,100%{width:0}60%{width:62px}}"
         ".sp{animation:sp 3s ease-in-out infinite}@keyframes sp{0%,100%{opacity:.5}50%{opacity:1}}")
    g=(f'<rect x="-92" y="-66" width="92" height="132" rx="10" fill="{RED}" fill-opacity=".08" stroke="{RED}" stroke-opacity=".5"/>'
       f'<rect x="0" y="-66" width="92" height="132" rx="10" fill="{BLUE}" fill-opacity=".08" stroke="{BLUE}" stroke-opacity=".5"/>'
       f'<line class="sp" x1="0" y1="-66" x2="0" y2="66" stroke="{PURPLE}" stroke-width="2"/>'
       f'<text x="-46" y="-44" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{RED}">RED</text>'
       f'<text x="46" y="-44" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{BLUE}">BLUE</text>')
    for i,y in enumerate((-18,2,22,42)):
        g+=f'<rect class="l1" x="-80" y="{y}" height="6" rx="3" fill="{RED}" fill-opacity=".55" style="animation-delay:{i*.2}s"/>'
        g+=f'<rect class="l2" x="12" y="{y}" height="6" rx="3" fill="{BLUE}" fill-opacity=".55" style="animation-delay:{i*.2}s"/>'
    return {"css":css,"svg":g}

def m_roadmap():
    pts=[(-78,36),(-36,-6),(8,30),(50,-14),(84,20)]
    c=CYAN; css=(".nd{animation:nd 4s ease-in-out infinite}@keyframes nd{0%,100%{opacity:.4}50%{opacity:1}}"
                 ".ln{stroke-dasharray:6 8;animation:ln 1s linear infinite}@keyframes ln{to{stroke-dashoffset:-14}}")
    path="M"+" L".join(f"{x} {y}" for x,y in pts)
    g=f'<path d="{path}" fill="none" stroke="{LINE}" stroke-width="3"/><path class="ln" d="{path}" fill="none" stroke="{c}" stroke-width="3"/>'
    for i,(x,y) in enumerate(pts):
        last = i==len(pts)-1
        g+=(f'<g class="nd" style="animation-delay:{i*.35}s"><circle cx="{x}" cy="{y}" r="{11 if last else 9}" fill="{PANEL}" stroke="{c}" stroke-width="2.5"/>'
            f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{c}">{i+1}</text></g>')
    g+=f'<text x="84" y="-28" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{c}">★</text>'
    return {"css":css,"svg":g}

def m_clickme():
    c=MAGENTA
    css=(".rip{transform-box:fill-box;transform-origin:center;animation:rip 2.4s ease-out infinite}"
         "@keyframes rip{0%{transform:scale(.3);opacity:.9}100%{transform:scale(1.8);opacity:0}}"
         ".cur{animation:cur 2.4s ease-in-out infinite}@keyframes cur{0%{transform:translate(28px,30px)}45%,100%{transform:translate(6px,8px)}}")
    g=(f'<rect x="-74" y="-54" width="118" height="92" rx="8" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>'
       f'<rect x="-74" y="-54" width="118" height="18" rx="8" fill="{BAR}"/>'
       f'<rect x="-52" y="-30" width="74" height="42" rx="6" fill="{MAGENTA}" fill-opacity=".10" stroke="{MAGENTA}" stroke-opacity=".6" stroke-dasharray="4 4"/>'
       f'<text x="-15" y="-4" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{MAGENTA}">CLICK</text>'
       f'<circle class="rip" cx="-6" cy="4" r="12" fill="none" stroke="{c}" stroke-width="2"/>'
       f'<g class="cur"><path d="M0 0 L0 20 L5 15 L9 23 L12 21 L8 14 L15 14 Z" fill="{TEXT}" stroke="#fff" stroke-width="1"/></g>')
    return {"css":css,"svg":g}

def m_smuggler():
    c=RED
    css=(".pkt{animation:pk 3s ease-in-out infinite}@keyframes pk{0%{transform:translateX(0);opacity:0}30%{opacity:1}70%{transform:translateX(60px);opacity:1}100%{transform:translateX(66px);opacity:0}}")
    g=(f'<rect x="-88" y="-50" width="96" height="100" rx="8" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>'
       f'<text x="-40" y="-30" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" fill="{TEXT}">POST /</text>'
       f'<text x="-40" y="-10" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{MUTED}">CL: 6</text>'
       f'<text x="-40" y="6" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{MUTED}">TE: chunk</text>'
       f'<rect x="-80" y="18" width="80" height="22" rx="4" fill="{c}" fill-opacity=".10" stroke="{c}" stroke-opacity=".5"/>'
       f'<text x="-40" y="33" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{c}">smuggled</text>'
       f'<g class="pkt"><rect x="6" y="18" width="80" height="22" rx="4" fill="{c}" fill-opacity=".14" stroke="{c}"/><text x="46" y="33" text-anchor="middle" font-family="{MONO}" font-size="9" font-weight="700" fill="{c}">GET /admin</text></g>'
       f'<path d="M8 -20 h70" stroke="{c}" stroke-opacity=".4" stroke-dasharray="3 4"/>')
    return {"css":css,"svg":g}

def m_obsidian():
    c=PURPLE
    nodes=[(0,0,13),(-66,-34,8),(60,-40,8),(-54,40,8),(58,36,8),(10,-66,7),(0,62,7)]
    edges=[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,3),(2,4)]
    css=(".no{animation:no 3s ease-in-out infinite}@keyframes no{0%,100%{opacity:.6}50%{opacity:1}}"
         ".ed{stroke-dasharray:4 6;animation:ed 1.4s linear infinite}@keyframes ed{to{stroke-dashoffset:-20}}")
    g=""
    for a,b in edges:
        g+=f'<line class="ed" x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" stroke="{c}" stroke-opacity=".5" stroke-width="1.6"/>'
    for i,(x,y,r) in enumerate(nodes):
        g+=f'<circle class="no" style="animation-delay:{i*.25}s" cx="{x}" cy="{y}" r="{r}" fill="{c}" fill-opacity="{.22 if i else .35}" stroke="{c}" stroke-width="2"/>'
    return {"css":css,"svg":g}

def m_subtakeover():
    c=GREEN
    css=(".dng{animation:dng 2.6s ease-in-out infinite}@keyframes dng{0%,100%{opacity:.5}50%{opacity:1}}"
         ".brk{stroke-dasharray:5 5;animation:brk 1s linear infinite}@keyframes brk{to{stroke-dashoffset:-20}}")
    g=(f'<rect x="-40" y="-64" width="80" height="26" rx="6" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-opacity=".6"/>'
       f'<text x="0" y="-47" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{c}">target.com</text>'
       f'<path d="M0 -38 V-20 M0 -20 H-60 V-6 M0 -20 H0 V-6 M0 -20 H64 V-6" fill="none" stroke="{LINE}" stroke-width="2"/>')
    subs=[(-60,"www",c,False),(0,"dev",c,False),(64,"api",RED,True)]
    for x,name,col,bad in subs:
        g+=f'<rect x="{x-32}" y="-6" width="64" height="24" rx="6" fill="{col}" fill-opacity=".10" stroke="{col}" stroke-opacity=".6"/>'
        g+=f'<text x="{x}" y="10" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{col}">{name}</text>'
        if bad:
            g+=(f'<path class="brk" d="M{x} 18 V40" stroke="{RED}" stroke-width="2"/>'
                f'<g class="dng"><circle cx="{x}" cy="54" r="12" fill="{RED}" fill-opacity=".12" stroke="{RED}" stroke-width="2"/>'
                f'<text x="{x}" y="58" text-anchor="middle" font-family="{SANS}" font-size="14" font-weight="800" fill="{RED}">!</text></g>'
                f'<text x="{x}" y="76" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{RED}">dangling</text>')
    return {"css":css,"svg":g}


# ------------------------------------------------------------------ skills marquee
def skills():
    W, H = 1200, 76
    items=["BURP SUITE","PYTHON","JAVASCRIPT","LINUX","HTTP/2","XSS","CSRF","SSRF","RECON","REQUEST SMUGGLING","CLICKJACKING","OSINT","OBSIDIAN","OSCP","WEB","CTF"]
    cols=[GREEN,CYAN,BLUE,PURPLE,MAGENTA,AMBER,RED]
    def run(dx):
        x=dx; out=""
        for i,t in enumerate(items):
            cw=len(t)*8.4+30; cc=cols[i%len(cols)]
            out+=(f'<g transform="translate({x:.0f} 22)"><rect width="{cw:.0f}" height="32" rx="8" fill="{cc}" fill-opacity=".08" stroke="{cc}" stroke-opacity=".4"/>'
                  f'<circle cx="16" cy="16" r="4" fill="{cc}"/>'
                  f'<text x="{cw/2+8:.0f}" y="21" text-anchor="middle" font-family="{MONO}" font-size="12.5" font-weight="700" letter-spacing=".5" fill="{TEXT}">{t}</text></g>')
            x+=cw+16
        return out, x-dx
    row, span = run(0)
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Skills and techniques">
<title>Skills</title>
<defs>
  <linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="#fff"/><stop offset=".06" stop-color="#fff" stop-opacity="0"/><stop offset=".94" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
</defs>
<style>
  .mq{{animation:mq {span/55:.0f}s linear infinite}} @keyframes mq{{from{{transform:translateX(0)}}to{{transform:translateX(-{span:.0f}px)}}}}
  {RM}
</style>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{PANEL}" stroke="{LINE}"/>
<svg x="2" y="2" width="{W-4}" height="{H-4}">
  <g class="mq"><g>{row}</g><g transform="translate({span:.0f} 0)">{row}</g></g>
</svg>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#edge)"/>
</svg>"""


def main():
    w("hero.svg", hero())
    w("stats.svg", stats())
    w("skills.svg", skills())
    w("cards/notes.svg",   card("~/hacking-notes — live","Hacking Notes",["Red & blue team notes — concise, expert-","curated. The whole methodology, online."],["RED TEAM","BLUE TEAM"],"★ hacking-notes.com",GREEN,m_notes()))
    w("cards/roadmap.svg", card("~/hacker-roadmap","Hacker Roadmap",["Structured paths from zero to pro — hobbyist,","bug bounty, certs & a cheap degree route."],["5 PATHS","GUIDE"],"★ start here",CYAN,m_roadmap()))
    w("cards/clickme.svg", card("~/clickme — poc","ClickMe",["Multi-step clickjacking framework. Build,","preview & export complex POCs."],["CLICKJACKING","POC"],"★ live demo",MAGENTA,m_clickme()))
    w("cards/smuggler.svg",card("~/hr-smuggler","HR-Smuggler",["Detects HTTP request smuggling —","HTTP/1.1 (TE.CL / CL.TE) and HTTP/2."],["HTTP/1.1","HTTP/2"],"★ python",RED,m_smuggler()))
    w("cards/obsidian.svg",card("~/burp-obsidian","Burp × Obsidian",["Turn Burp output into a linked Obsidian","vault. Structured bug-bounty note-taking."],["BURP","NOTES"],"★ methodology",PURPLE,m_obsidian()))
    w("cards/subtakeover.svg",card("~/subdomain-takeover","Subdomain Takeover",["Enumerate subdomains and flag the ones","pointing at dangling, claimable services."],["RECON","TAKEOVER"],"★ python",GREEN,m_subtakeover()))

if __name__ == "__main__":
    main()
