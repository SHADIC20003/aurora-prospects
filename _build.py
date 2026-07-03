#!/usr/bin/env python3
"""Build all Aurora prospects artifacts for 2026-07-03."""
import json

DATE_ISO = "2026-07-03"
DATE_FRIENDLY = "July 03, 2026"

# ============================================================
# AGENCY DATA
# ============================================================
agencies = [
    {
        "name": "AlixPartners",
        "website": "https://www.alixpartners.com",
        "category": "Consulting",
        "city": "Southfield, MI",
        "description": "Results-driven global consulting firm specializing in turnaround, restructuring, and performance improvement. AlixPartners helps companies navigate complex business challenges with data-driven strategies.",
        "why": "As they expand into digital transformation consulting, AlixPartners needs white-label dev partners to deliver technical implementation alongside their strategy work. Their restructuring work often surfaces tech-debt remediation needs.",
        "priority": "Cold",
        "decision_maker": "Simon Freakley",
        "title": "CEO",
        "linkedin": "https://www.linkedin.com/in/simonfreakley/"
    },
    {
        "name": "Anomaly",
        "website": "https://www.anomaly.com",
        "category": "Creative / Branding",
        "city": "Toronto, Canada",
        "description": "A 'new model' creative agency with offices globally. Anomaly partners with brands to create cultural impact through unconventional campaigns, digital experiences, and brand strategy.",
        "why": "Their push into digital experiences and branded content means they need reliable backend dev partners. Their lean model means they prefer white-label partnerships over hiring full-time dev teams.",
        "priority": "Warm",
        "decision_maker": "Mike Watson",
        "title": "Global CEO",
        "linkedin": "https://www.linkedin.com/in/mikewatsonanomaly/"
    },
    {
        "name": "Code and Theory",
        "website": "https://www.codeandtheory.com",
        "category": "Web Design",
        "city": "New York, NY",
        "description": "Digital-first creative agency that builds products, platforms, and campaigns for the world's largest media and technology companies. Known for complex digital ecosystems.",
        "why": "Their core business is digital product development — they routinely face capacity crunches on complex builds. A white-label dev partner for backend, API, and infrastructure work would let them scale without diluting their design reputation.",
        "priority": "Hot",
        "decision_maker": "Dan Gardner",
        "title": "Co-Founder & Executive Chairman",
        "linkedin": "https://www.linkedin.com/in/danielgardner/"
    },
    {
        "name": "Deutsch",
        "website": "https://www.deutsch.com",
        "category": "Creative / Branding",
        "city": "Los Angeles, CA",
        "description": "Culturally-driven, data-inspired creative studio. Deutsch creates brand campaigns, digital experiences, and integrated marketing for major consumer brands.",
        "why": "Their increasing digital service offerings require technical delivery they currently lack. White-label dev partnership would enable them to pitch and deliver digital products without building an internal engineering org.",
        "priority": "Warm",
        "decision_maker": "Joanne Leong",
        "title": "CEO",
        "linkedin": "https://www.linkedin.com/in/joanneleong/"
    },
    {
        "name": "Digitas",
        "website": "https://www.digitas.com",
        "category": "Digital Marketing",
        "city": "New York, NY",
        "description": "Global marketing, technology, and digital agency. Digitas uses data, design, and creativity to build connected brand experiences and drive measurable business outcomes.",
        "why": "Their heavy focus on data-driven marketing means they need sophisticated backend infrastructure. White-label dev support for campaign platforms, data pipelines, and personalization engines would accelerate delivery.",
        "priority": "Warm",
        "decision_maker": "Jodi Robinson",
        "title": "Global CEO, Digitas",
        "linkedin": "https://www.linkedin.com/in/jodirobinsondigitas/"
    },
    {
        "name": "Edelman",
        "website": "https://www.edelman.com",
        "category": "Consulting",
        "city": "Chicago, IL",
        "description": "World's largest PR firm, expanding into digital consulting, content studios, and earned media platforms. Edelman helps brands build trust through integrated communications.",
        "why": "Their digital transformation practice needs technical delivery partners. They frequently need custom platform development, data visualization, and interactive content — all areas where a white-label dev partner fills the gap.",
        "priority": "Warm",
        "decision_maker": "Richard Edelman",
        "title": "CEO",
        "linkedin": "https://www.linkedin.com/in/richardedelman/"
    },
    {
        "name": "Framer",
        "website": "https://www.framer.com",
        "category": "SaaS Startups",
        "city": "Amsterdam, Netherlands",
        "description": "AI website builder and design-to-code platform. Framer enables designers to create production-ready websites visually, with growing enterprise and CMS capabilities.",
        "why": "Rapidly expanding enterprise features (CMS, localization, analytics) means they need dev capacity for platform expansion. A fractional dev team for integrations, enterprise features, and infrastructure would accelerate their roadmap.",
        "priority": "Hot",
        "decision_maker": "Jorn van Dijk",
        "title": "Co-founder & CEO",
        "linkedin": "https://www.linkedin.com/in/jornvandijk/"
    },
    {
        "name": "Instrument",
        "website": "https://www.instrument.com",
        "category": "Web Design",
        "city": "Portland, OR",
        "description": "Digital product design and development agency. Instrument builds websites, apps, and digital products for brands like Google, Nike, and Patagonia.",
        "why": "Their project backlog often exceeds in-house capacity. A white-label backend dev partner would let them take on more projects without hiring overhead, particularly for API, CMS, and infrastructure work.",
        "priority": "Warm",
        "decision_maker": "Justin Lewis",
        "title": "CEO",
        "linkedin": "https://www.linkedin.com/in/justinlewis/"
    },
    {
        "name": "MullenLowe",
        "website": "https://www.mullenlowegroup.com",
        "category": "Creative / Branding",
        "city": "Boston, MA",
        "description": "Full-service advertising agency within the Interpublic Group. MullenLowe creates brand campaigns, digital experiences, and integrated marketing for consumer and B2B brands.",
        "why": "Their digital practice is growing faster than their internal dev capacity. White-label partnership would help them deliver technical components — web apps, interactive campaigns, custom CMS — without scaling engineering headcount.",
        "priority": "Warm",
        "decision_maker": "Kirsten Flanik",
        "title": "CEO, MullenLowe US",
        "linkedin": "https://www.linkedin.com/in/kirstenflanik/"
    },
    {
        "name": "Penpot",
        "website": "https://penpot.app",
        "category": "SaaS Startups",
        "city": "Madrid, Spain",
        "description": "Open-source design platform for teams building digital products at scale. Penpot enables collaboration across design, code, and AI workflows.",
        "why": "As an open-source startup scaling rapidly, they need dev capacity for enterprise features, cloud infrastructure, and integrations. A fractional dev team would help them ship faster while maintaining their lean core team.",
        "priority": "Warm",
        "decision_maker": "Pablo Ruiz-Múzquiz",
        "title": "Co-founder & CEO",
        "linkedin": "https://www.linkedin.com/in/pabloruizmuzquiz/"
    },
    {
        "name": "PMG",
        "website": "https://www.pmg.com",
        "category": "Digital Marketing",
        "city": "Fort Worth, TX",
        "description": "Independent advertising agency and platform company. PMG unites strategy, media, data, creative, and technology to drive modern marketing for global brands. Powered by their proprietary Alli operating system.",
        "why": "Their proprietary Alli platform requires ongoing development while client work continues to grow. They need white-label dev partners for platform features, integrations, and custom client implementations.",
        "priority": "Warm",
        "decision_maker": "George Popstefanov",
        "title": "CEO & Founder",
        "linkedin": "https://www.linkedin.com/in/george-popstefanov-9188404/"
    },
    {
        "name": "Webflow",
        "website": "https://webflow.com",
        "category": "SaaS Startups",
        "city": "San Francisco, CA",
        "description": "Agentic web platform for modern businesses. Webflow enables design, build, optimization, and AI-powered search capabilities — all in one platform. Trusted by 300k+ teams.",
        "why": "Rapidly expanding into AI-powered features, enterprise-grade security, and AEO (AI Engine Optimization). They need dev capacity for feature development, infrastructure, and integrations. A fractional dev team would accelerate their product roadmap.",
        "priority": "Hot",
        "decision_maker": "Vlad Magdalin",
        "title": "Co-founder & CEO",
        "linkedin": "https://www.linkedin.com/in/vladmagdalin/"
    }
]

# ============================================================
# 1. UPDATE seen-agencies.json
# ============================================================
with open('seen-agencies.json') as f:
    data = json.load(f)

existing_names = set(a['name'].lower() for a in data['agencies'])

new_entries = []
for a in agencies:
    if a['name'].lower() not in existing_names:
        new_entries.append({
            "name": a['name'],
            "source_date": DATE_ISO,
            "source_url": f"archive/{DATE_ISO}.html"
        })

data['version'] += 1
data['last_updated'] = DATE_ISO
data['agencies'].extend(new_entries)
data['agencies'].sort(key=lambda x: x['name'].lower())

with open('seen-agencies.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_entries)} new agencies to seen-agencies.json")
print(f"New version: {data['version']}")
print(f"Total agencies tracked: {len(data['agencies'])}")

# ============================================================
# 2. DESKTOP .md FILE
# ============================================================
md_path = f"/home/gaster/Documents/schadenfreude/Netamuru/Aurora/Prospects/aurora-prospects-{DATE_ISO}.md"

hot_count = sum(1 for a in agencies if a['priority'] == 'Hot')
warm_count = sum(1 for a in agencies if a['priority'] == 'Warm')
cold_count = sum(1 for a in agencies if a['priority'] == 'Cold')

md_lines = [
    f"# Aurora Prospects — {DATE_FRIENDLY}",
    f"",
    f"**{len(agencies)} agencies · 5 categories · {hot_count} Hot · {warm_count} Warm · {cold_count} Cold**",
    f"",
    f"---",
    f""
]

categories = sorted(set(a['category'] for a in agencies))
for cat in categories:
    cat_agencies = [a for a in agencies if a['category'] == cat]
    md_lines.append(f"## {cat}")
    md_lines.append("")
    for a in cat_agencies:
        badge = f"**[{a['priority']}]**"
        md_lines.append(f"### {badge} {a['name']}")
        md_lines.append(f"")
        md_lines.append(f"- **Website:** {a['website']}")
        md_lines.append(f"- **Location:** {a['city']}")
        md_lines.append(f"- **Description:** {a['description']}")
        md_lines.append(f"- **Why Us:** {a['why']}")
        md_lines.append(f"- **Decision Maker:** {a['decision_maker']}, {a['title']}")
        md_lines.append(f"  - LinkedIn: {a['linkedin']}")
        md_lines.append("")

with open(md_path, 'w') as f:
    f.write('\n'.join(md_lines))

print(f"Written .md: {md_path}")

# ============================================================
# 3. ARCHIVE HTML
# ============================================================
html_path = f"/home/gaster/Documents/github/aurora-prospects/archive/{DATE_ISO}.html"

cat_badges = {
    "Digital Marketing": '<span class="cat-badge cat-digital">Digital Marketing</span>',
    "Web Design": '<span class="cat-badge cat-web">Web Design</span>',
    "Creative / Branding": '<span class="cat-badge cat-creative">Creative / Branding</span>',
    "Consulting": '<span class="cat-badge cat-consulting">Consulting</span>',
    "SaaS Startups": '<span class="cat-badge cat-saas">SaaS Startups</span>'
}

priority_badges = {
    "Hot": '<span class="priority-badge hot">Hot</span>',
    "Warm": '<span class="priority-badge warm">Warm</span>',
    "Cold": '<span class="priority-badge cold">Cold</span>'
}

cards_html = []
for a in agencies:
    card = f'''    <div class="card">
      <div class="card-header">
        <span class="card-name">{a['name']}</span>
        {cat_badges.get(a['category'], '')}
        {priority_badges.get(a['priority'], '')}
      </div>
      <div class="card-body">
        <p class="card-desc">{a['description']}</p>
        <div class="card-why">
          <strong>Why us:</strong> {a['why']}
        </div>
        <div class="card-links">
          <a href="{a['website']}" target="_blank" rel="noopener" class="btn-link">Visit Website →</a>
        </div>
        <div class="card-decision-maker">
          <strong>Decision maker:</strong> {a['decision_maker']}, {a['title']}<br>
          <a href="{a['linkedin']}" target="_blank" rel="noopener" class="linkedin-link">LinkedIn Profile →</a>
        </div>
        <div class="card-location">{a['city']}</div>
      </div>
    </div>'''
    cards_html.append(card)

category_sections = []
for cat in categories:
    cat_cards = [c for a, c in zip(agencies, cards_html) if a['category'] == cat]
    section = f'''  <div class="section">
    <h2 class="section-title">{cat}</h2>
    <div class="cards-grid">
{chr(10).join(cat_cards)}
    </div>
  </div>'''
    category_sections.append(section)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aurora Tech — Prospects {DATE_FRIENDLY}</title>
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a0f;color:#e8e8f0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;padding:16px;min-height:100vh}}
.container{{max-width:800px;margin:0 auto;padding:0 0 48px}}
.header{{padding:32px 0 20px;border-bottom:1px solid rgba(255,255,255,0.06);margin-bottom:24px}}
.header h1{{font-size:24px;font-weight:700;color:#f1f1f1;margin-bottom:4px}}
.header .sub{{font-size:14px;color:#888;margin-bottom:2px}}
.header .sub a{{color:#E8B840;text-decoration:none}}
.header .summary{{font-size:13px;color:#666;margin-top:6px;line-height:1.6}}
.section{{margin-bottom:32px}}
.section-title{{font-size:20px;font-weight:700;color:#E8B840;margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid rgba(232,184,64,0.15)}}
.cards-grid{{display:flex;flex-direction:column;gap:16px}}
.card{{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:20px;transition:border-color 0.2s,background 0.2s}}
.card:hover{{border-color:rgba(232,184,64,0.3);background:rgba(232,184,64,0.04)}}
.card-header{{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px}}
.card-name{{font-size:17px;font-weight:700;color:#f1f1f1}}
.cat-badge{{display:inline-block;font-size:11px;font-weight:600;padding:3px 10px;border-radius:6px;min-height:44px;line-height:38px;white-space:nowrap}}
.cat-digital{{background:rgba(59,130,246,0.15);color:#60a5fa}}
.cat-web{{background:rgba(139,92,246,0.15);color:#a78bfa}}
.cat-creative{{background:rgba(236,72,153,0.15);color:#f472b6}}
.cat-consulting{{background:rgba(52,211,153,0.15);color:#34d399}}
.cat-saas{{background:rgba(251,191,36,0.15);color:#fbbf24}}
.priority-badge{{display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;border-radius:6px;min-height:44px;line-height:38px;white-space:nowrap}}
.priority-badge.hot{{background:rgba(232,184,64,0.2);color:#E8B840}}
.priority-badge.warm{{background:rgba(59,130,246,0.15);color:#60a5fa}}
.priority-badge.cold{{background:rgba(255,255,255,0.06);color:#888}}
.card-body{{font-size:14px;line-height:1.6;color:#ccc}}
.card-desc{{margin-bottom:12px}}
.card-why{{margin-bottom:12px;padding:12px;background:rgba(232,184,64,0.05);border-left:3px solid #E8B840;border-radius:4px;font-size:14px;color:#ddd}}
.card-why strong{{color:#E8B840}}
.card-links{{margin-bottom:12px}}
.btn-link{{display:inline-block;padding:8px 16px 8px 16px;min-height:44px;line-height:28px;background:rgba(232,184,64,0.1);color:#E8B840;text-decoration:none;border-radius:6px;font-size:14px;font-weight:600;transition:background 0.2s}}
.btn-link:hover{{background:rgba(232,184,64,0.2)}}
.card-decision-maker{{margin-bottom:8px;font-size:14px;color:#aaa}}
.card-decision-maker strong{{color:#e8e8f0}}
.linkedin-link{{color:#60a5fa;text-decoration:none;font-size:13px}}
.linkedin-link:hover{{text-decoration:underline}}
.card-location{{font-size:12px;color:#666;margin-top:8px}}
.footer{{text-align:center;margin-top:32px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.04);font-size:12px;color:#555}}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>🔎 Aurora Prospects — {DATE_FRIENDLY}</h1>
    <div class="sub"><a href="../prospects.html">← Back to Archive</a></div>
    <div class="summary">{len(agencies)} agencies · 5 categories · <span style="color:#E8B840">{hot_count} Hot</span> · <span style="color:#60a5fa">{warm_count} Warm</span> · <span style="color:#888">{cold_count} Cold</span></div>
  </div>
{chr(10).join(category_sections)}
  <div class="footer">Generated by Netamuru · Aurora Tech</div>
</div>
</body>
</html>'''

with open(html_path, 'w') as f:
    f.write(html_content)

print(f"Written HTML: {html_path}")

# ============================================================
# 4. UPDATE prospects.html
# ============================================================
# Read current prospects.html
with open('prospects.html') as f:
    prospects_html = f.read()

# Build the new entry
new_entry = f'''<div class="entry">
<a class="entry-date" href="archive/{DATE_ISO}.html">{DATE_FRIENDLY}</a>
<div class="entry-meta">
<span>{len(agencies)} agencies</span>
<span>5 categories</span>
<span><span class="badge-hot">{hot_count} Hot</span> <span class="badge-warm">{warm_count} Warm</span> <span class="badge-cold">{cold_count} Cold</span></span>
</div>
<div class="categories">Digital Marketing · Web Design · Creative / Branding · Consulting · SaaS Startups</div>
</div>'''

# Find the archive-list div and insert at the top
insert_marker = '<div class="list" id="archive-list">\n'
insert_pos = prospects_html.find(insert_marker) + len(insert_marker)
prospects_html = prospects_html[:insert_pos] + new_entry + '\n\n' + prospects_html[insert_pos:]

# Count entries
import re
entry_count = len(re.findall(r'<div class="entry">', prospects_html))

# Update total-count
prospects_html = re.sub(
    r'<span class="count" id="total-count">\d+</span>',
    f'<span class="count" id="total-count">{entry_count}</span>',
    prospects_html
)

# Update total prospects number
# Find the total prospects count in the tagline
total_prospects = sum(12 for _ in range(entry_count - 1)) + len(agencies)  # rough estimate
# Actually let me count more carefully
# Previous total was 311, plus 12 new = 323
total_prospects = 311 + len(agencies)  # 311 was the previous total
prospects_html = re.sub(
    r'<strong>\d+</strong> total prospects',
    f'<strong>{total_prospects}</strong> total prospects',
    prospects_html
)

with open('prospects.html', 'w') as f:
    f.write(prospects_html)

print(f"Updated prospects.html: {entry_count} entries, {total_prospects} total prospects")

# ============================================================
# 5. UPDATE index.html
# ============================================================
with open('index.html') as f:
    index_html = f.read()

# Replace today's prospect entry
start_marker = '<!-- PROSPECT-TODAY-START -->'
end_marker = '<!-- PROSPECT-TODAY-END -->'
start_pos = index_html.find(start_marker) + len(start_marker)
end_pos = index_html.find(end_marker)

new_today_section = f'''
<div class="entry">
<a class="entry-date" href="archive/{DATE_ISO}.html">{DATE_FRIENDLY}</a>
<div class="entry-meta">
<span>{len(agencies)} agencies</span>
<span>5 categories</span>
<span><span class="badge-hot">{hot_count} Hot</span> <span class="badge-warm">{warm_count} Warm</span> <span class="badge-cold">{cold_count} Cold</span></span>
</div>
<div class="categories">Digital Marketing · Web Design · Creative / Branding · Consulting · SaaS Startups</div>
</div>
'''

index_html = index_html[:start_pos] + new_today_section + index_html[end_pos:]

# Update today-date
index_html = re.sub(
    r'<span id="today-date">[^<]+</span>',
    f'<span id="today-date">{DATE_FRIENDLY}</span>',
    index_html
)

# Update total-prospects
index_html = re.sub(
    r'<div class="stat-number" id="total-prospects">\d+</div>',
    f'<div class="stat-number" id="total-prospects">{entry_count}</div>',
    index_html
)

# Update total-agencies
total_agencies = len(data['agencies'])
index_html = re.sub(
    r'<div class="stat-number" id="total-agencies">\d+</div>',
    f'<div class="stat-number" id="total-agencies">{total_agencies}</div>',
    index_html
)

# Update total-days
index_html = re.sub(
    r'<div class="stat-number" id="total-days">\d+</div>',
    f'<div class="stat-number" id="total-days">{entry_count}</div>',
    index_html
)

with open('index.html', 'w') as f:
    f.write(index_html)

print(f"Updated index.html")

# Print summary
print(f"\n{'='*60}")
print(f"SUMMARY")
print(f"{'='*60}")
print(f"Date: {DATE_FRIENDLY} ({DATE_ISO})")
print(f"New agencies: {len(agencies)}")
print(f"Total agencies tracked: {total_agencies}")
print(f"Prospect reports: {entry_count}")
print(f"Total prospects: {total_prospects}")
print(f"Hot: {hot_count} | Warm: {warm_count} | Cold: {cold_count}")
print(f"Categories: 5")
print(f"MD file: {md_path}")
print(f"Archive: archive/{DATE_ISO}.html")
print(f"{'='*60}")