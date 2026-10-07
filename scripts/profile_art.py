#!/usr/bin/env python3
"""Hacking-Notes profile art — editorial / minimal direction.

Near-monochrome (ink on white), a single restrained indigo accent used only as
hairlines and markers, precise line icons, hairline rules, typographic index
lists, and quiet slow motion. Standalone animated SVGs (inline CSS only — all
GitHub's image sandbox allows). Run:  python3 scripts/profile_art.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

A = Path(__file__).resolve().parent.parent / "assets"

MONO="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
INK="#15171a"; MUTE="#6b7280"; FAINT="#9aa1ab"; HAIR="#e6e8eb"; BG="#ffffff"; ACCENT="#3e63dd"
RM="@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def w(name, svg):
    p = A / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote assets/" + name)


def line_icon(kind, c=INK, sw=1.6):
    s=f'fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'
    if kind=="cursor": return f'<path d="M-9 -11 L9 -2 L1 1 L6 12 L2 14 L-3 3 L-9 8 Z" {s}/>'
    if kind=="split":  return f'<path d="M-12 -10 H12 M-12 0 H3 M-12 10 H12" {s}/><path d="M7 -3 L13 1 L7 5" {s}/>'
    if kind=="tree":   return f'<path d="M0 -12 V-4 M0 -4 H-11 V2 M0 -4 H11 V2 M0 -4 V2" {s}/><circle cx="0" cy="-12" r="2.4" {s}/><circle cx="-11" cy="6" r="2.4" {s}/><circle cx="0" cy="6" r="2.4" {s}/><circle cx="11" cy="6" r="2.4" {s}/>'
    if kind=="graph":  return f'<circle cx="0" cy="0" r="3" {s}/><circle cx="-11" cy="-8" r="2.2" {s}/><circle cx="12" cy="-6" r="2.2" {s}/><circle cx="8" cy="10" r="2.2" {s}/><path d="M0 0 L-11 -8 M0 0 L12 -6 M0 0 L8 10" {s}/>'
    if kind=="book":   return f'<path d="M-11 -11 H9 A2 2 0 0 1 11 -9 V12 H-9 A2 2 0 0 1 -11 10 Z" {s}/><path d="M-11 8 H9 M-4 -11 V8" {s}/>'
    if kind=="map":    return f'<path d="M-12 -8 L-4 -11 L4 -8 L12 -11 V9 L4 12 L-4 9 L-12 12 Z" {s}/><path d="M-4 -11 V9 M4 -8 V12" {s}/>'
    return ""


def hero():
    W, H = 1200, 300
    eyebrow = "SECURITY RESEARCH — OFFENSE · DEFENSE · RESEARCH"
    sub = "building tools · breaking apps · documenting the craft"
    subw = len(sub) * 15 * 0.6
    meta = [("19", "REPOSITORIES"), ("15", "CVES DISCLOSED"), ("2022", "ACTIVE SINCE")]
    mrows = ""
    for i, (num, lab) in enumerate(meta):
        y = 96 + i * 46
        mrows += (f'<text x="1140" y="{y}" text-anchor="end" font-family="{SANS}" font-size="22" font-weight="700" fill="{INK}">{num}</text>'
                  f'<text x="1140" y="{y+16}" text-anchor="end" font-family="{MONO}" font-size="10.5" letter-spacing="1.5" fill="{FAINT}">{lab}</text>')
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Hacking Notes — security research">
<title>Hacking Notes</title>
<style>
  .rule{{transform-box:fill-box;transform-origin:left;animation:rule 6s ease-in-out infinite}}
  @keyframes rule{{0%{{transform:scaleX(.1)}}50%{{transform:scaleX(1)}}100%{{transform:scaleX(.1)}}}}
  .cur{{animation:bl 1.1s step-end infinite}} @keyframes bl{{50%{{opacity:0}}}}
  {RM}
</style>
<rect width="{W}" height="{H}" fill="{BG}"/>
<text x="62" y="86" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">{eyebrow}</text>
<rect class="rule" x="62" y="98" width="150" height="2" fill="{ACCENT}"/>
<text x="58" y="186" font-family="{SANS}" font-size="74" letter-spacing="-1" fill="{INK}"><tspan font-weight="800">Hacking</tspan> <tspan font-weight="300" fill="{MUTE}">Notes</tspan></text>
<text x="62" y="228" font-family="{MONO}" font-size="15" fill="{MUTE}">{escape(sub)}</text>
<rect class="cur" x="{62+subw+6:.0f}" y="216" width="8" height="16" fill="{ACCENT}"/>
<line x1="980" y1="70" x2="980" y2="210" stroke="{HAIR}"/>
{mrows}
<line x1="62" y1="268" x2="1140" y2="268" stroke="{HAIR}"/>
</svg>"""


def card(idx, title, cat, desc, meta, icon):
    W, H = 560, 196
    d1, d2 = (desc + ["", ""])[:2]
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<style>
  .u{{transform-box:fill-box;transform-origin:left;animation:u 5s ease-in-out infinite}}
  @keyframes u{{0%{{transform:scaleX(0)}}45%,90%{{transform:scaleX(1)}}100%{{transform:scaleX(0)}}}}
  {RM}
</style>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{BG}" stroke="{HAIR}"/>
<rect x="0.5" y="0.5" width="3" height="{H-1}" fill="{ACCENT}"/>
<text x="30" y="42" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{FAINT}">{idx}</text>
<text x="{W-26}" y="42" text-anchor="end" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{FAINT}">{escape(cat)}</text>
<g transform="translate({W-46} 86)">{line_icon(icon)}</g>
<text x="30" y="92" font-family="{SANS}" font-size="26" font-weight="700" fill="{INK}">{escape(title)}</text>
<rect class="u" x="30" y="104" width="46" height="2" fill="{ACCENT}"/>
<text x="30" y="132" font-family="{SANS}" font-size="14.5" fill="{MUTE}">{escape(d1)}</text>
<text x="30" y="153" font-family="{SANS}" font-size="14.5" fill="{MUTE}">{escape(d2)}</text>
<line x1="30" y1="168" x2="{W-26}" y2="168" stroke="{HAIR}"/>
<text x="30" y="185" font-family="{MONO}" font-size="11.5" fill="{FAINT}">{escape(meta)}</text>
</svg>"""


def index(title, rows, right_note=None):
    W = 1160; top = 74; rh = 46; H = top + rh * len(rows) + 18
    body = f'<text x="30" y="40" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">{escape(title)}</text>'
    if right_note:
        body += f'<text x="{W-30}" y="40" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="{FAINT}">{escape(right_note)}</text>'
    body += f'<line x1="30" y1="56" x2="{W-30}" y2="56" stroke="{INK}" stroke-opacity=".85"/>'
    for i, (name, tag) in enumerate(rows):
        y = top + i * rh + 28
        body += (f'<text x="30" y="{y}" font-family="{MONO}" font-size="12" fill="{FAINT}">{i+1:02d}</text>'
                 f'<text x="74" y="{y}" font-family="{SANS}" font-size="18" font-weight="600" fill="{INK}">{escape(name)}</text>'
                 f'<text x="{W-30}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{MUTE}">{escape(tag)}</text>')
        if i < len(rows) - 1:
            body += f'<line x1="30" y1="{top+i*rh+rh}" x2="{W-30}" y2="{top+i*rh+rh}" stroke="{HAIR}"/>'
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title><rect width="{W}" height="{H}" fill="{BG}"/>{body}</svg>"""


def skills():
    W, H = 1160, 104
    groups = [("OFFENSE", ["Burp Suite","Request Smuggling","Clickjacking","XSS","CSRF","SSRF"]),
              ("RECON",   ["Subdomain Enum","Wayback","JS Analysis","OSINT"]),
              ("CRAFT",   ["Python","JavaScript","Linux","HTTP/2","Obsidian"])]
    body = f'<text x="30" y="34" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">CAPABILITIES</text>'
    body += f'<line x1="172" y1="29" x2="{W-30}" y2="29" stroke="{HAIR}"/>'
    y = 64
    for label, items in groups:
        body += f'<text x="30" y="{y}" font-family="{MONO}" font-size="11.5" letter-spacing="1.5" fill="{ACCENT}">{label}</text>'
        x = 132
        for it in items:
            body += f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="14.5" fill="{INK}">{escape(it)}</text>'
            x += len(it) * 8.4 + 26
            if it != items[-1]:
                body += f'<text x="{x-16}" y="{y}" font-family="{SANS}" font-size="14.5" fill="{HAIR}">·</text>'
        y += 22
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Capabilities">
<title>Capabilities</title><rect width="{W}" height="{H}" fill="{BG}"/>{body}</svg>"""


def bugbounty():
    W, H = 1160, 132
    sectors = ["Search Engines", "Governments", "Domain Providers", "Hotel Chains", "& more"]
    body = f'<text x="30" y="34" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{MUTE}">BUG BOUNTY</text>'
    body += f'<text x="{W-30}" y="34" text-anchor="end" font-family="{MONO}" font-size="12" fill="{FAINT}">reported across sectors</text>'
    body += f'<line x1="146" y1="29" x2="{W-30}" y2="29" stroke="{HAIR}"/>'
    x = 30
    for i, sec in enumerate(sectors):
        body += f'<text x="{x}" y="92" font-family="{SANS}" font-size="27" font-weight="600" fill="{INK}">{escape(sec)}</text>'
        x += len(sec) * 15.0 + 34
        if i < len(sectors) - 1:
            body += f'<rect x="{x-24}" y="74" width="2" height="22" fill="{ACCENT}" opacity=".5"/>'
    body += f'<text x="30" y="118" font-family="{MONO}" font-size="12" fill="{FAINT}">more at hacking-notes.com · bug-bounty.blog</text>'
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Bug bounty — reported across sectors">
<title>Bug bounty</title><rect width="{W}" height="{H}" fill="{BG}"/>{body}</svg>"""


def footer():
    W, H = 1160, 92
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer">
<style>.cur{{animation:bl 1.1s step-end infinite}}@keyframes bl{{50%{{opacity:0}}}}{RM}</style>
<line x1="0" y1="22" x2="{W}" y2="22" stroke="{HAIR}"/>
<text x="0" y="60" font-family="{MONO}" font-size="13" fill="{MUTE}">Hacking-Notes — security research</text>
<text x="{W}" y="60" text-anchor="end" font-family="{MONO}" font-size="13" fill="{MUTE}">hacking-notes.com <tspan class="cur" fill="{ACCENT}">_</tspan></text>
</svg>"""


def main():
    w("hero.svg", hero())
    w("skills.svg", skills())
    w("bugbounty.svg", bugbounty())
    w("footer.svg", footer())
    w("cards/notes.svg",      card("01","Hacking Notes","RED · BLUE TEAM",["Red & blue team methodology, online —","concise notes curated for practitioners."],"hacking-notes.com","book"))
    w("cards/roadmap.svg",    card("02","Hacker Roadmap","GUIDE",["Structured paths from zero to pro:","hobbyist, bug bounty, certs & degree."],"github.com/Hacking-Notes/Hacker-Roadmap","map"))
    w("cards/clickme.svg",    card("03","ClickMe","CLICKJACKING",["Multi-step clickjacking framework —","build, preview and export POCs."],"python · hacking-poc.com","cursor"))
    w("cards/smuggler.svg",   card("04","HR-Smuggler","REQUEST SMUGGLING",["Detects HTTP request smuggling across","HTTP/1.1 (TE.CL / CL.TE) and HTTP/2."],"python · github.com/Hacking-Notes/HR-Smuggler","split"))
    w("cards/obsidian.svg",   card("05","Burp × Obsidian","NOTE-TAKING",["Turns Burp output into a linked Obsidian","vault for structured bug-bounty notes."],"burp extension · methodology","graph"))
    w("cards/subtakeover.svg",card("06","Subdomain Takeover","RECON",["Enumerates subdomains and flags those","pointing at dangling, claimable services."],"python · github.com/Hacking-Notes/Subdomain-Takeover","tree"))
    w("arsenal.svg", index("THE ARSENAL", [
        ("JWT","chrome · auth testing"), ("lazy-js","chrome · webpack recon"),
        ("Wayback-Crawler","python · archive recon"), ("Endpoint-JS Explorer","bookmarklet · js endpoints"),
        ("DCJ-Action","python · exploit server"), ("Extensions","curated chrome toolkit"),
        ("Bookmarks","curated resources"), ("VulnScan","python · ai scanner"),
        ("BSCP","burp · exam guide"), ("CVE","research · disclosures"),
    ]))
    w("cve.svg", index("CVE RESEARCH", [
        ("CVE-2024-51379","Stored XSS"), ("CVE-2024-51380","Stored XSS"),
        ("CVE-2024-51381","CSRF"), ("CVE-2024-51382","CSRF"),
        ("CVE-2024-51484","CSRF"), ("CVE-2024-51485","CSRF"),
        ("CVE-2024-51486","Stored XSS"), ("CVE-2024-51487","CSRF"),
        ("CVE-2024-51488","CSRF"), ("CVE-2024-51489","CSRF"),
        ("CVE-2024-51490","Stored XSS"), ("CVE-2024-55008","Advisory"),
    ], right_note="15 DISCLOSED · 3 PENDING"))


if __name__ == "__main__":
    main()
