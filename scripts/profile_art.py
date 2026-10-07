#!/usr/bin/env python3
"""Hacking-Notes profile art — editorial / minimal, theme-aware.

Near-monochrome with a single restrained indigo accent, hairline rules, rounded
panels, tag pills and quiet motion. Emits a light set (*.svg) and a dark set
(*-dark.svg) in GitHub's dark palette; the README swaps them with <picture>.
Standalone animated SVGs (inline CSS only). Run: python3 scripts/profile_art.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

A = Path(__file__).resolve().parent.parent / "assets"
MONO="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
RM="@media (prefers-reduced-motion: reduce){*{animation:none!important}}"

THEME = {
  "light": dict(BG="#ffffff", INK="#15171a", MUTE="#6b7280", FAINT="#9aa1ab", HAIR="#e6e8eb", ACCENT="#3e63dd"),
  "dark":  dict(BG="#0d1117", INK="#e6edf3", MUTE="#9198a1", FAINT="#6e7681", HAIR="#30363d", ACCENT="#7c93ff"),
}
BG=INK=MUTE=FAINT=HAIR=ACCENT=""

def use(t):
    globals().update(THEME[t])

def wr(name, svg):
    p = A / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(svg.strip() + "\n", encoding="utf-8")


def panel(W, H, rx=14):
    return f'<rect x="0.75" y="0.75" width="{W-1.5}" height="{H-1.5}" rx="{rx}" fill="{BG}" stroke="{HAIR}"/>'


def pills(items, x0, y0, maxx, h=28, fs=12.5):
    x, y, out = x0, y0, ""
    for it in items:
        wd = len(it) * fs * 0.56 + 26
        if x + wd > maxx:
            x = x0; y += h + 10
        out += (f'<rect x="{x:.0f}" y="{y:.0f}" width="{wd:.0f}" height="{h}" rx="{h/2:.0f}" fill="none" stroke="{HAIR}"/>'
                f'<text x="{x+wd/2:.0f}" y="{y+h/2+4.5:.0f}" text-anchor="middle" font-family="{SANS}" font-size="{fs}" fill="{INK}">{escape(it)}</text>')
        x += wd + 10
    return out, y + h


def line_icon(kind, c=None, sw=1.6):
    c = c or INK
    s=f'fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'
    if kind=="cursor": return f'<path d="M-9 -11 L9 -2 L1 1 L6 12 L2 14 L-3 3 L-9 8 Z" {s}/>'
    if kind=="split":  return f'<path d="M-12 -10 H12 M-12 0 H3 M-12 10 H12" {s}/><path d="M7 -3 L13 1 L7 5" {s}/>'
    if kind=="tree":   return f'<path d="M0 -12 V-4 M0 -4 H-11 V2 M0 -4 H11 V2 M0 -4 V2" {s}/><circle cx="0" cy="-12" r="2.4" {s}/><circle cx="-11" cy="6" r="2.4" {s}/><circle cx="0" cy="6" r="2.4" {s}/><circle cx="11" cy="6" r="2.4" {s}/>'
    if kind=="graph":  return f'<circle cx="0" cy="0" r="3" {s}/><circle cx="-11" cy="-8" r="2.2" {s}/><circle cx="12" cy="-6" r="2.2" {s}/><circle cx="8" cy="10" r="2.2" {s}/><path d="M0 0 L-11 -8 M0 0 L12 -6 M0 0 L8 10" {s}/>'
    if kind=="book":   return f'<path d="M-11 -11 H9 A2 2 0 0 1 11 -9 V12 H-9 A2 2 0 0 1 -11 10 Z" {s}/><path d="M-11 8 H9 M-4 -11 V8" {s}/>'
    if kind=="map":    return f'<path d="M-12 -8 L-4 -11 L4 -8 L12 -11 V9 L4 12 L-4 9 L-12 12 Z" {s}/><path d="M-4 -11 V9 M4 -8 V12" {s}/>'
    if kind=="people": return f'<circle cx="-5" cy="-4" r="3.6" {s}/><circle cx="6" cy="-5" r="2.8" {s}/><path d="M-11 8 c0 -6.5 12 -6.5 12 0" {s}/><path d="M2 6 c1.2 -5 11 -4.5 11 1.5" {s}/>'
    if kind=="globe":  return f'<circle cx="0" cy="0" r="10" {s}/><path d="M-10 0 H10 M0 -10 V10 M-6.5 -7 C-2.5 -3 -2.5 3 -6.5 7 M6.5 -7 C2.5 -3 2.5 3 6.5 7" {s}/>'
    if kind=="pen":    return f'<path d="M-9 9 V4 L5 -10 L10 -5 L-4 9 Z" {s}/><path d="M2 -7 L7 -2" {s}/>'
    if kind=="chat":   return f'<path d="M-11 -7 H11 V4 H-3 L-8 9 V4 H-11 Z" {s}/><circle cx="-4" cy="-1.5" r="1.2" fill="{c}" stroke="none"/><circle cx="0" cy="-1.5" r="1.2" fill="{c}" stroke="none"/><circle cx="4" cy="-1.5" r="1.2" fill="{c}" stroke="none"/>'
    return ""


def chip_button(icon, text, accent_icon=True):
    """A rounded hairline pill-button: accent line icon + label. Own link."""
    H = 44; fs = 14.5
    tw = len(text) * fs * 0.56
    W = int(30 + 24 + tw + 22)
    ic = ACCENT if accent_icon else INK
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="{escape(text)}"><title>{escape(text)}</title>'
            f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="{(H-2)//2}" fill="{BG}" stroke="{HAIR}"/>'
            f'<g transform="translate(28 {H/2:.0f})">{line_icon(icon, ic, 1.8)}</g>'
            f'<text x="48" y="{H/2+5:.0f}" font-family="{SANS}" font-size="{fs}" font-weight="600" fill="{INK}">{escape(text)}</text>'
            f'</svg>')


HR_STYLE=('.hr{transform-box:fill-box;transform-origin:left;animation:hr 6s ease-in-out infinite}'
          '@keyframes hr{0%{transform:scaleX(0)}45%,90%{transform:scaleX(1)}100%{transform:scaleX(0)}}')

def hr_accent(x, y, w=70):
    return f'<rect class="hr" x="{x}" y="{y-1:.0f}" width="{w}" height="2" rx="1" fill="{ACCENT}"/>'


def svg(W, H, inner, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="{escape(label)}"><title>{escape(label)}</title>{inner}</svg>')


def hero():
    W, H = 1200, 300
    eyebrow = "SECURITY RESEARCH — OFFENSE · DEFENSE · RESEARCH"
    sub = "building tools · breaking apps · documenting the craft"
    subw = len(sub) * 15 * 0.6
    meta = [("19","REPOSITORIES"),("15","CVES DISCLOSED"),("2022","ACTIVE SINCE")]
    mrows = ""
    for i,(num,lab) in enumerate(meta):
        y = 100 + i*46
        mrows += (f'<text x="1130" y="{y}" text-anchor="end" font-family="{SANS}" font-size="22" font-weight="700" fill="{INK}">{num}</text>'
                  f'<text x="1130" y="{y+16}" text-anchor="end" font-family="{MONO}" font-size="10.5" letter-spacing="1.5" fill="{FAINT}">{lab}</text>')
    style=('<style>.rule{transform-box:fill-box;transform-origin:left;animation:rule 6s ease-in-out infinite}'
           '@keyframes rule{0%{transform:scaleX(.1)}50%{transform:scaleX(1)}100%{transform:scaleX(.1)}}'
           '.cur{animation:bl 1.1s step-end infinite}@keyframes bl{50%{opacity:0}}' + RM + '</style>')
    inner = (style + panel(W,H) +
        f'<text x="60" y="88" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">{eyebrow}</text>'
        f'<rect class="rule" x="60" y="100" width="150" height="2" rx="1" fill="{ACCENT}"/>'
        f'<text x="56" y="188" font-family="{SANS}" font-size="74" letter-spacing="-1" fill="{INK}"><tspan font-weight="800">Hacking</tspan> <tspan font-weight="300" fill="{MUTE}">Notes</tspan></text>'
        f'<text x="60" y="230" font-family="{MONO}" font-size="15" fill="{MUTE}">{escape(sub)}</text>'
        f'<rect class="cur" x="{60+subw+6:.0f}" y="218" width="8" height="16" rx="1" fill="{ACCENT}"/>'
        f'<line x1="968" y1="74" x2="968" y2="214" stroke="{HAIR}"/>{mrows}')
    return svg(W,H,inner,"Hacking Notes — security research")


def star_chip(W, stars, live):
    """Rounded chip pinned to the card's top-right, well above the separator."""
    yt, h = 24, 24
    if live:
        txt = "live"; w = len(txt) * 7.2 + 36; x = W - 26 - w
        return (f'<rect x="{x:.0f}" y="{yt}" width="{w:.0f}" height="{h}" rx="{h/2:.0f}" fill="none" stroke="{HAIR}"/>'
                f'<circle cx="{x+16:.0f}" cy="{yt+h/2:.0f}" r="3.5" fill="{ACCENT}"/>'
                f'<text x="{x+27:.0f}" y="{yt+h/2+4:.0f}" font-family="{MONO}" font-size="12" fill="{INK}">{txt}</text>')
    s = f"{stars/1000:.1f}k" if stars >= 1000 else str(stars)
    w = len(s) * 7.4 + 42; x = W - 26 - w
    star = (f'<path transform="translate({x+17:.0f} {yt+h/2:.0f}) scale(.52)" '
            f'd="M0 -11 L3.2 -3.4 L11 -2.6 L5.2 2.6 L6.8 10.4 L0 6.2 L-6.8 10.4 L-5.2 2.6 L-11 -2.6 L-3.2 -3.4 Z" fill="{ACCENT}"/>')
    return (f'<rect x="{x:.0f}" y="{yt}" width="{w:.0f}" height="{h}" rx="{h/2:.0f}" fill="none" stroke="{HAIR}"/>'
            f'{star}<text x="{x+29:.0f}" y="{yt+h/2+4:.0f}" font-family="{MONO}" font-size="12" fill="{INK}">{s}</text>')


def card(idx, title, cat, desc, meta, icon, stars=None, live=False):
    W, H = 560, 196
    d1,d2 = (desc+["",""])[:2]
    style=('<style>.u{transform-box:fill-box;transform-origin:left;animation:u 5s ease-in-out infinite}'
           '@keyframes u{0%{transform:scaleX(0)}45%,90%{transform:scaleX(1)}100%{transform:scaleX(0)}}'
           '.ic{transform-box:fill-box;transform-origin:center;animation:ic 4s ease-in-out infinite}'
           '@keyframes ic{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}' + RM + '</style>')
    inner = (style + panel(W,H,12) +
        f'<circle cx="34" cy="37" r="3" fill="{ACCENT}"/>'
        f'<text x="46" y="42" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{FAINT}">{idx}</text>'
        f'<text x="72" y="42" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{FAINT}">· {escape(cat)}</text>'
        f'<g transform="translate({W-46} 88)"><g class="ic">{line_icon(icon)}</g></g>'
        f'<text x="30" y="94" font-family="{SANS}" font-size="26" font-weight="700" fill="{INK}">{escape(title)}</text>'
        f'<rect class="u" x="30" y="106" width="46" height="2" rx="1" fill="{ACCENT}"/>'
        f'<text x="30" y="134" font-family="{SANS}" font-size="14.5" fill="{MUTE}">{escape(d1)}</text>'
        f'<text x="30" y="155" font-family="{SANS}" font-size="14.5" fill="{MUTE}">{escape(d2)}</text>'
        f'<line x1="30" y1="169" x2="{W-26}" y2="169" stroke="{HAIR}"/>'
        f'<text x="30" y="185" font-family="{MONO}" font-size="11.5" fill="{FAINT}">{escape(meta)}</text>'
        + star_chip(W, stars, live))
    return svg(W,H,inner,title)


def capabilities():
    W = 1160
    groups = [("OFFENSE", ["Burp Suite","Request Smuggling","Clickjacking","XSS","CSRF","SSRF"]),
              ("RECON",   ["Subdomain Enum","Wayback","JS Analysis","OSINT"]),
              ("CRAFT",   ["Python","JavaScript","Linux","HTTP/2","Obsidian"])]
    body=""; y=66
    for label, items in groups:
        body += f'<text x="30" y="{y+19}" font-family="{MONO}" font-size="11.5" letter-spacing="1.5" fill="{ACCENT}">{label}</text>'
        pl, bottom = pills(items, 132, y, W-30)
        body += pl; y = bottom + 16
    H = y + 6
    head = (f'<text x="30" y="36" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">CAPABILITIES</text>'
            f'<line x1="176" y1="31" x2="{W-30}" y2="31" stroke="{HAIR}"/>' + hr_accent(176, 31))
    style = f'<style>{HR_STYLE}{RM}</style>'
    return svg(W,H, style+panel(W,H)+head+body, "Capabilities")


def index(title, rows, right_note=None):
    W=1160; top=70; rh=46; H=top+rh*len(rows)+22
    body=(f'<text x="30" y="40" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">{escape(title)}</text>')
    if right_note:
        body+=f'<text x="{W-30}" y="40" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="{FAINT}">{escape(right_note)}</text>'
    body+=f'<line x1="30" y1="52" x2="{W-30}" y2="52" stroke="{INK}" stroke-opacity=".55"/>' + hr_accent(30, 52)
    n=len(rows); dur=max(8, n*1.1)
    keys="".join(f"{(i/(n-1))*100*0.9:.1f}%{{transform:translateY({i*rh}px)}}" for i in range(n))
    marker=(f'<rect class="mk" x="22" y="{top+6}" width="3" height="28" rx="1.5" fill="{ACCENT}"/>')
    style=(f'<style>{HR_STYLE}'
           f'.mk{{animation:mk {dur:.0f}s steps(1,end) infinite,mkf {dur:.0f}s ease-in-out infinite}}'
           f'@keyframes mk{{{keys}100%{{transform:translateY(0)}}}}'
           f'@keyframes mkf{{0%,100%{{opacity:.3}}50%{{opacity:.9}}}}{RM}</style>')
    for i,(name,tag) in enumerate(rows):
        y=top+i*rh+28
        body+=(f'<text x="30" y="{y}" font-family="{MONO}" font-size="12" fill="{FAINT}">{i+1:02d}</text>'
               f'<text x="74" y="{y}" font-family="{SANS}" font-size="18" font-weight="600" fill="{INK}">{escape(name)}</text>'
               f'<text x="{W-30}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{MUTE}">{escape(tag)}</text>')
        if i<len(rows)-1:
            body+=f'<line x1="30" y1="{top+i*rh+rh}" x2="{W-30}" y2="{top+i*rh+rh}" stroke="{HAIR}"/>'
    return svg(W,H, style+panel(W,H)+marker+body, title)


def bugbounty():
    W=1160
    sectors=["Search Engines","Governments","Domain Providers","Hotel Chains","Domain Registrars","& more"]
    head=(f'<text x="30" y="36" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">BUG BOUNTY</text>'
          f'<text x="{W-30}" y="36" text-anchor="end" font-family="{MONO}" font-size="12" fill="{FAINT}">reported across sectors</text>'
          f'<line x1="150" y1="31" x2="{W-30}" y2="31" stroke="{HAIR}"/>' + hr_accent(150, 31))
    pl, bottom = pills(sectors, 30, 58, W-30, h=32, fs=14)
    cap=f'<text x="30" y="{bottom+28:.0f}" font-family="{MONO}" font-size="11.5" fill="{FAINT}">details at hacking-notes.com · bug-bounty.blog</text>'
    H=bottom+44
    style=f'<style>{HR_STYLE}{RM}</style>'
    return svg(W,H, style+panel(W,H)+head+pl+cap, "Bug bounty — reported across sectors")


def footer():
    W,H=1160,86
    style='<style>.cur{animation:bl 1.1s step-end infinite}@keyframes bl{50%{opacity:0}}' + RM + '</style>'
    inner=(style+panel(W,H)+
        f'<text x="30" y="52" font-family="{MONO}" font-size="13" fill="{MUTE}">Hacking-Notes — security research</text>'
        f'<text x="{W-30}" y="52" text-anchor="end" font-family="{MONO}" font-size="13" fill="{MUTE}">hacking-notes.com <tspan class="cur" fill="{ACCENT}">_</tspan></text>')
    return svg(W,H,inner,"footer")


# (key, idx, title, cat, desc, meta, icon, stars, live)
CARDS=[("notes","01","Hacking Notes","RED · BLUE TEAM",["Red & blue team methodology, online —","concise notes curated for practitioners."],"hacking-notes.com","book", None, True),
       ("roadmap","02","Hacker Roadmap","GUIDE",["Structured paths from zero to pro:","hobbyist, bug bounty, certs & degree."],"github.com/Hacking-Notes/Hacker-Roadmap","map", 1336, False),
       ("clickme","03","ClickMe","CLICKJACKING",["Multi-step clickjacking framework —","build, preview and export POCs."],"python · hacking-poc.com","cursor", 41, False),
       ("obsidian","04","Burp × Obsidian","NOTE-TAKING",["Turns Burp output into a linked Obsidian","vault for structured bug-bounty notes."],"burp extension · methodology","graph", 51, False)]

ARSENAL=[("HR-Smuggler","python · request smuggling"),("Subdomain-Takeover","python · takeover recon"),
         ("JWT","chrome · auth testing"),("lazy-js","chrome · webpack recon"),("Wayback-Crawler","python · archive recon"),
         ("Endpoint-JS Explorer","bookmarklet · js endpoints"),("DCJ-Action","python · exploit server"),("Extensions","curated chrome toolkit"),
         ("Bookmarks","curated resources"),("VulnScan","python · ai scanner"),("BSCP","burp · exam guide"),("CVE","research · disclosures")]

CVES=[("CVE-2024-51379","Stored XSS"),("CVE-2024-51380","Stored XSS"),("CVE-2024-51381","CSRF"),("CVE-2024-51382","CSRF"),
      ("CVE-2024-51484","CSRF"),("CVE-2024-51485","CSRF"),("CVE-2024-51486","Stored XSS"),("CVE-2024-51487","CSRF"),
      ("CVE-2024-51488","CSRF"),("CVE-2024-51489","CSRF"),("CVE-2024-51490","Stored XSS"),("CVE-2024-55008","Advisory")]


def build(sfx):
    wr(f"hero{sfx}.svg", hero())
    wr(f"hdr-followers{sfx}.svg", chip_button("people", "489 followers"))
    wr(f"hdr-website{sfx}.svg", chip_button("globe", "hacking-notes.com"))
    wr(f"hdr-blog{sfx}.svg", chip_button("pen", "blog"))
    wr(f"hdr-discord{sfx}.svg", chip_button("chat", "discord"))
    wr(f"skills{sfx}.svg", capabilities())
    wr(f"bugbounty{sfx}.svg", bugbounty())
    wr(f"footer{sfx}.svg", footer())
    for key,idx,title,cat,desc,meta,icon,stars,live in CARDS:
        wr(f"cards/{key}{sfx}.svg", card(idx,title,cat,desc,meta,icon,stars,live))
    wr(f"arsenal{sfx}.svg", index("THE ARSENAL", ARSENAL))
    wr(f"cve{sfx}.svg", index("CVE RESEARCH", CVES, right_note="15 DISCLOSED · 3 PENDING"))


def main():
    use("light"); build("")
    use("dark");  build("-dark")
    print("done")

if __name__ == "__main__":
    main()
