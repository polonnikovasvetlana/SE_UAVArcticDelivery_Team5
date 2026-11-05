"""Add evidence rings to a COPY of the existing vector relay map; originals stay intact."""
import csv, collections, html, re, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sites = list(csv.DictReader((ROOT / 'relay-locations.csv').open(encoding='utf-8-sig')))
SOURCES = {
 'MUR': ('documented', 'Apteka Pervaya: municipal pharmacy network', 'Pharmacy personnel implied by dispensing service; clinician shift unverified', 'https://www.xn----7sbabjpc1b5bemr2p.xn--p1ai/', 'Operator website with 2026 notices and pharmacy network description'),
 'NAR': ('documented', 'Nenetskaya Farmatsiya and other local pharmacies', 'Pharmacy service; local clinical organisation also listed in regional report', 'https://adm-nao.ru/media/uploads/userfiles/2025/04/02/ДОКЛАД_О_НАРКОСИТУАЦИИ_в_НАО_в_2024_г..pdf', 'Regional government 2024 activity report, published 2025; search-index evidence'),
 'DUD': ('documented', 'Gubernskie Apteki outlets', 'Pharmacy personnel implied by dispensing service; clinician shift unverified', 'https://krasnoyarsk.uteka.ru/pharmacies/krasnoarsk-ao-gubernskie-apteki-g-dudinka-ul-sorsa-zd30-35520/', 'Current pharmacy-marketplace listing; older operator licence corroborates local network'),
 'NOR': ('documented', 'Gubernskie Apteki municipal listing and pharmacy network', 'Pharmacy personnel implied by dispensing service; clinician shift unverified', 'https://xn--h1aecgfmj1g.xn--p1ai/areas-of-work/organizations/gpkk/gpkk_gapteki.php', 'City administration lists local pharmacy organisation; historical outlet counts not reused'),
 'PEV': ('documented', 'Chukotfarmatsiya district pharmacy No.2; Chaun medical service', 'Pharmacy service plus clinical facility directory', 'https://apt87.ru/catalog/ | https://chaunskaya.ru/contactinfo.php?copylenco=contactinfo', 'Operator pharmacy address Sovietskaya 30; medical reception described as round-the-clock'),
 'EGV': ('documented', 'Chukotfarmatsiya district pharmacy No.3; Iultin medical service', 'Pharmacy service plus regional clinical directory', 'https://apt87.ru/catalog/ | https://chukotmed.ru/контакты/', 'Operator pharmacy address Ryntyrgina 1; no specific stock confirmed'),
 'BBI': ('documented', 'Chukotfarmatsiya district pharmacy No.4; Bilibino medical service', 'Pharmacy service plus regional clinical directory', 'https://apt87.ru/catalog/ | https://chukotmed.ru/контакты/', 'Operator pharmacy address Kurchatova 4; inland supply candidate'),
 'ANA': ('documented', 'Chukotfarmatsiya district pharmacy No.1; regional medical service', 'Pharmacy service plus clinical operator website', 'https://apt87.ru/catalog/ | https://chukotmed.ru/', 'Operator pharmacy address Otke 22; no specific stock confirmed'),
 'DIK': ('lead', 'Gubernskie Apteki licensed dispensing rooms at local medical facility', 'Historical medical-facility and pharmacy evidence', 'https://24farmacia.ru/data/Лицензия_ЛО2402002234_от_11112020.pdf', '2020 licence, Tayana 38 rooms 114/115; indexed text only, full PDF fetch timed out; current operation unresolved'),
 'KHT': ('lead', 'Pharmacy No.97; local medical service', 'Historical article explicitly names pharmacist', 'https://xn--80aaal3c2at.xn--p1ai/novosti/338-apteka-97.html', '2021 local article describes medicines and pharmacist; 2020 operator licence also indexes Khatanga; current operation unresolved'),
 'TIK': ('lead', 'Central ulus pharmacy No.60; Bulun medical service', 'Clinical service and dispensing documented historically; current pharmacy register lead', 'https://www.rgo.ru/sites/default/files/18_sentyabrya_no37_10587_1_0.pdf | https://companies.rbc.ru/id/1021400578781-munitsipalnoe-unitarnoe-torgovo-proizvodstvennoe-predpriyatie-tsentralnaya-ulusnaya-apteka--60/', '2020 local publication describes staff and medicine provision; current stock/staffing not established'),
 'CHR': ('lead', 'Municipal pharmacy No.51; Nizhnekolymsk medicine provision', 'Pharmacy and clinical organisation named in procurement/company lead', 'https://reputation.ru/ogrn/1081448000215', 'Secondary register/procurement evidence for 2023-2024 medicine provision; verify with operator'),
 'SAB': ('lead', 'Industrial health post serving Yamal LNG workers', 'Medical staffing lead; medicine supply and third-party access unverified', 'https://vacancies.club/ads/sogaz-medservis/', 'Historical staffing advert describes Sabetta medical work; restricted industrial facility, not a public pharmacy'),
}
for sid in ('NOV', 'SYN', 'KHE'):
 SOURCES[sid] = ('lead', 'Medical-service address in Taymyr RB No.1 licence/register lead', 'Address evidence only; current staffing and medicine dispensing unresolved', 'https://inndex.ru/ul/hatanga/ogrn-1028400002157-51c-kgbuz-taymyrskaya-rb-1', 'Secondary register lists Novorybnaya, Syndassko and Kheta medical addresses; not proof of stocked dispatch point')
SOURCES['BYK'] = ('lead', 'Bulun medical-service registered local address', 'Address evidence only; staffing and medicines unresolved', 'https://star-pro.ru/proverka-kontragenta/organization/1021400578770', 'Secondary medical-licence/register lead includes Bykovsky')
for sid in ('AYO', 'BIL', 'RYT'):
 SOURCES[sid] = ('lead', 'Local medical point in regional health order', 'Historical medical contact; medicine supply unresolved', 'https://xn--80atapud1a.xn--p1ai/upload/iblock/5ad/Prikaz-122-ot-20.02.2020g.pdf', '2020 government health order lists local medical contacts; current staffing/stock not established')

rows = []
for s in sites:
 evidence = SOURCES.get(s['id'], ('not_verified', 'Not established in this rapid screen', 'Not verified', '', 'No conclusion about absence; not individually verified within the time limit'))
 rows.append(dict(id=s['id'], name=s['name'], name_ru=s['name_ru'], status=evidence[0], facility_or_service=evidence[1], personnel_evidence=evidence[2], sources=evidence[3], evidence_limits=evidence[4], specific_drug_stock='not_verified', uav_dispatch_agreement='not_verified', checked='2026-11-05'))
with (ROOT/'relay-medical-screening.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

ns={'s':'http://www.w3.org/2000/svg'}
original=(ROOT/'Arctic_relay_map_1.svg').read_text(encoding='utf-8')
tree=ET.fromstring(original)
overlays=[]
for ax in tree.findall('.//s:g',ns):
 if not ax.get('id','').startswith('axes_'): continue
 markers=[g for g in list(ax) if g.get('id','').startswith('PathCollection')]
 assert len(markers)==57, 'Unexpected source-map point ordering'
 for site, marker in zip(sites,markers):
  if site['id'] not in SOURCES: continue
  u=marker.find('.//s:use',ns)
  x,y=float(u.get('x')),float(u.get('y'))
  clipped=next((e for e in marker.iter() if e.get('clip-path')),None)
  clip=clipped.get('clip-path') if clipped is not None else ''
  status=SOURCES[site['id']][0]
  color='#00834b' if status=='documented' else '#b87400'
  dash='' if status=='documented' else ' stroke-dasharray="3 2"'
  title=html.escape(site['name']+': '+SOURCES[site['id']][1])
  overlays.append(f'<g clip-path="{clip}"><title>{title}</title><circle cx="{x}" cy="{y}" r="7.3" fill="none" stroke="white" stroke-width="4.4"/><circle cx="{x}" cy="{y}" r="7.3" fill="none" stroke="{color}" stroke-width="2.5"{dash}/></g>')

def txt(x,y,text,size=12,color='#173f5d',weight='normal'):
 return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{html.escape(text)}</text>'
counts=collections.Counter(r['status'] for r in rows)
footer=['<rect x="0" y="1152" width="1800" height="168" fill="#fbfcfd"/>', '<path d="M63 1160 H1737" stroke="#c5d4dc"/>']
footer += [txt(63,1185,'MEDICINE DISPATCH SCREEN  |  5 November 2026',18,weight='bold')]
footer += ['<circle cx="72" cy="1210" r="7.3" fill="none" stroke="#00834b" stroke-width="2.5"/>',txt(90,1215,f"Green ring: medicine service documented ({counts['documented']})",13)]
footer += ['<circle cx="650" cy="1210" r="7.3" fill="none" stroke="#b87400" stroke-width="2.5" stroke-dasharray="3 2"/>',txt(670,1215,f"Amber ring: medical / historical supply lead ({counts['lead']})",13)]
footer += [txt(1250,1215,f"No ring: not verified ({counts['not_verified']})",13)]
footer += [txt(63,1242,'Initial supply shortlist: Murmansk, Naryan-Mar, Dudinka, Norilsk, Pevek, Egvekinot, Bilibino, Anadyr.',14,weight='bold')]
footer += [txt(63,1266,'Tiksi, Khatanga and Dikson remain useful leads; older evidence needs current confirmation. Small medical posts may also hold drugs.',12)]
footer += [txt(63,1289,'Personnel means medical OR pharmacy service; current shifts, specific drug stocks and authority to release UAV consignments are unverified.',12)]
footer += [txt(63,1310,'Rapid screen of 57 candidates. Rings preserve original port/relay symbols. Sources, dates and limitations: relay-medical-screening.csv; medical-dispatch-screening.md.',11)]
svg=re.sub(r'width="1800pt" height="1152pt" viewBox="0 0 1800 1152"', 'width="1800pt" height="1320pt" viewBox="0 0 1800 1320"', original, count=1)
svg=svg.replace('</svg>', '<g id="medical-screening">'+''.join(overlays+footer)+'</g></svg>')
(ROOT/'Arctic_relay_map_1_medical.svg').write_text(svg,encoding='utf-8')
# A local, self-contained browser preview also provides a renderer for the vector map.
(ROOT/'Arctic_relay_map_1_medical.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>Medical relay screen</title><style>html,body{margin:0;background:#fbfcfd}svg{display:block;width:3600px;height:2640px}</style></head><body>'+svg[svg.index('<svg '):]+'</body></html>',encoding='utf-8')

lines=['# Medicine dispatch candidates: rapid screen', '', 'Checked: 5 November 2026. Scope: a brief evidence screen using the existing 57 candidates, not an exhaustive facility inventory.', '', 'Map copy: [Arctic_relay_map_1_medical.png](Arctic_relay_map_1_medical.png), [SVG](Arctic_relay_map_1_medical.svg). Source map `Arctic_relay_map_1` is preserved.', '', 'Green rings identify documented medicine dispensing services. Staff capability is inferred from the medical/pharmacy service, not a verified current roster. Amber rings identify medical leads or older/indirect medicine evidence. Unringed points are unverified, not evidence of no medical service. Exact drug availability, cold storage, opening hours, access and UAV dispatch agreements remain unverified at every location.', '', '**Result:** Main ports are useful starting points, but the shortlist also includes Naryan-Mar, Egvekinot, Bilibino and inland Norilsk. Port status alone does not establish medicine availability. Tiksi, Khatanga and Dikson should remain priority follow-up candidates, rather than being rejected because the quickly retrieved evidence is older.', '', f"Counts: {counts['documented']} documented medicine-service candidates; {counts['lead']} medical/historical leads; {counts['not_verified']} not verified. Only the first two groups received specific source leads; the remaining candidates were retained without individual verification within the time limit.", '', '| Candidate | Classification | Evidence and source |', '| --- | --- | --- |']
for r in rows:
 if r['status']=='not_verified':continue
 links='; '.join(f'[source {i+1}]({url})' for i,url in enumerate(r['sources'].split(' | ')))
 lines.append(f"| {r['name']} | {r['status']} | {r['facility_or_service']}. {r['evidence_limits']}. {links} |")
lines += ['', 'The pharmacy operator catalogue establishes locations and a drug catalogue, not stock at every branch: several displayed products are marked unavailable. No live-stock claim is made. Some evidence was available only as indexed text; the CSV records retrieval limitations.', '', 'The map retains the original distance chain and all original map notes. New rings only screen medical supply leads; they do not change aircraft coverage, relay eligibility or operational readiness.', '', '[All 57 candidate records with evidence and unresolved questions](relay-medical-screening.csv).']
(ROOT/'medical-dispatch-screening.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(dict(counts))
print('Created vector map, browser preview, source CSV and short analysis.')
