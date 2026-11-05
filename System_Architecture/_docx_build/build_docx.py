from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape
from PIL import Image
import json, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'UAV_candidates_short_comparison.docx'
URLS=json.loads((ROOT/'source_urls.json').read_text(encoding='utf-8'))
PHOTOS=json.loads((ROOT/'photo_urls.json').read_text(encoding='utf-8'))
NS='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
RELS=[]
def run(text,bold=False,size=21,color=None):
 props=f'<w:sz w:val="{size}"/>'+('<w:b/>' if bold else '')+(f'<w:color w:val="{color}"/>' if color else '')
 return f'<w:r><w:rPr>{props}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
def para(text='',size=21,bold=False,color=None,after=70,before=0,align=None):
 return '<w:p><w:pPr>'+f'<w:spacing w:before="{before}" w:after="{after}" w:line="250" w:lineRule="auto"/>'+ (f'<w:jc w:val="{align}"/>' if align else '')+'</w:pPr>'+run(text,bold,size,color)+'</w:p>'
def link(label,url):
 rid=f'rIdLink{len(RELS)+1}'; RELS.append((rid,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',url,'External'))
 return f'<w:hyperlink r:id="{rid}">'+run(label,False,17,'19658C')+'</w:hyperlink>'
def links(items):
 return '<w:p><w:pPr><w:spacing w:before="60" w:after="30"/></w:pPr>'+run('Sources: ',True,17)+run('  |  ',size=17).join(link(a,b) for a,b in items)+'</w:p>'
def table(rows):
 s='<w:tbl><w:tblPr><w:tblW w:w="9638" w:type="dxa"/><w:tblLayout w:type="fixed"/><w:tblCellMar><w:top w:w="90" w:type="dxa"/><w:bottom w:w="90" w:type="dxa"/><w:left w:w="115" w:type="dxa"/><w:right w:w="115" w:type="dxa"/></w:tblCellMar><w:tblBorders><w:bottom w:val="single" w:sz="4" w:color="CED9DF"/><w:insideH w:val="single" w:sz="4" w:color="CED9DF"/></w:tblBorders></w:tblPr><w:tblGrid><w:gridCol w:w="2050"/><w:gridCol w:w="7588"/></w:tblGrid>'
 for label,value in rows:
  s+='<w:tr><w:trPr><w:cantSplit/></w:trPr>'
  for i,text in enumerate([label,value]):
   width=2050 if i==0 else 7588
   s+=f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>'+('<w:shd w:fill="EDF3F6"/>' if i==0 else '')+'</w:tcPr>'+para(text,bold=i==0,after=0)+'</w:tc>'
  s+='</w:tr>'
 return s+'</w:tbl>'
def picture(key,idx,crop=False):
 im=Image.open(ROOT/(key+'.jpg')); w,h=im.size
 if crop:
  # Native Word framing only: original photograph remains embedded unchanged.
  h=h*.40
 width=min(6.3,2.25*w/h); height=width*h/w
 cx,cy=int(width*914400),int(height*914400)
 rid=f'rIdImage{idx}'; RELS.append((rid,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image',f'media/{key}.jpg',None))
 return f'''<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="40"/></w:pPr><w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{idx}" name="{key}" descr="Manufacturer photograph, verified on the named product page"/><wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr><a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="{key}.jpg"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="{rid}"/>{'<a:srcRect t="50000" b="10000"/>' if crop else ''}<a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'''

pages=[
 dict(name='Airbus U030 Flexrotor',key='flexrotor',subtitle='Compact shipboard VTOL • liquid fuel',caption='Photo: Airbus product page; Flexrotor in its vertical takeoff/landing position.',rows=[
 ('Takeoff / landing','Autonomous vertical takeoff and landing; transitions to wing-borne cruise. No catapult or runway. Published landing zone: 3.7 × 3.7 m.'),
 ('Weight / cargo','Maximum takeoff mass: 25 kg; empty: 15 kg. Useful load: 10 kg INCLUDING fuel. Payload up to 8 kg; fuel and cargo must share the mass allowance. Wingspan: 3 m.'),
 ('Energy','28 cc two-stroke engine; gasoline or heavy-fuel engine configurations. Requires refuelling, not just a battery swap.'),
 ('Speed','Minimum cruise: 78 km/h; maximum dash: 140 km/h. Use current brochure values; dash speed is not an endurance cruise.'),
 ('Maximum distance','Maximum flight distance with 3 kg cargo is not published. Typical endurance: 12–14 h. The 312–600 km mission needs a payload, wind and reserve calculation.'),
 ('Arctic features','Airbus reports 6 h in a −40 °C cold chamber and takeoff/landing winds up to 27 kt (≈13.9 m/s). Cold-chamber exposure does not establish flight at −40 °C or icing capability.'),
 ],note='Project fit: promising for compact ship recovery. Medical packaging, weather instruments and loaded mission reach require integration checks.',sources=[('2026 Airbus brochure',URLS['flexrotor_pdf']),('Product page / photo',URLS['flexrotor_page'])]),
 dict(name='TEKEVER AR3-EVO',key='ar3',subtitle='Modular fixed-wing / VTOL • several propulsion options',caption='Photo: TEKEVER AR3-EVO product gallery; aircraft with VTOL modules fitted.',rows=[
 ('Takeoff / landing','VTOL configuration: vertical ship-deck launch and recovery, advertised from 5 × 5 m. Fixed-wing option: catapult launch / parachute recovery; small-deck recovery is a separate check.'),
 ('Weight / cargo','Maximum takeoff mass: 25 kg, up to 30 kg with VTOL. Published payload capacity: 6 kg. Wingspan: 4.2 m; length: 1.96 m.'),
 ('Energy','Manufacturer offers electric, combustion and heavy-fuel options. Exact propulsion, fuel grade and payload/endurance combination must be specified in a quotation.'),
 ('Speed','Cruise: 46 kt (≈85 km/h). Maximum speed is not stated in the reviewed EVO specifications.'),
 ('Maximum distance','Loaded maximum flight distance is not published. Up to 14 h endurance with VTOL; 22 h fixed-wing. The 230 km figure is COMMUNICATIONS range, not flight distance; SATCOM options are offered.'),
 ('Arctic features','Ship-deck capability and modular SATCOM support are relevant. Reviewed EVO sources do not establish −40 °C operation, a landing wind limit or whole-aircraft icing capability.'),
 ],note='Project fit: promising for long legs and ship operations. Do not apply the 14-hour endurance figure to a battery version without confirmation.',sources=[('Specifications / photo',URLS['ar3_page']),('Manufacturer brochure',URLS['ar3_pdf'])]),
 dict(name='ElevonX Tango VTOL',key='tango',subtitle='Two sizes: Tango 3.0 / Tango 4.4 MAX',caption='Photo: ElevonX Tango product gallery; exact size/propulsion variant is not identified.',rows=[
 ('Takeoff / landing','Electric lift rotors provide vertical takeoff and landing; wing-borne cruise. Naval versions are offered. A verified minimum deck area and moving-deck limits were not found.'),
 ('Weight / cargo','Tango 3.0 / 4.4 MAX: maximum takeoff mass 21.5 / 29 kg; payload up to 5 / 10 kg; wingspan 3 / 4.4 m. Payload and endurance maxima are not simultaneous guarantees.'),
 ('Energy','Battery-electric, internal-combustion and hydrogen fuel-cell options are advertised. The brochure does not map each endurance figure to an exact propulsion and payload configuration.'),
 ('Speed','Published cruise up to 22 / 24 m/s (≈79 / 86 km/h), for 3.0 / 4.4 MAX respectively. Maximum dash speed is not given.'),
 ('Maximum distance','No loaded maximum distance published. Up to 3 / 5 h with lightweight payloads. Simple speed × time gives ≈238 / 432 km before reserves (illustration only). Radio link: 70 km, not flight distance.'),
 ('Arctic features','Naval versions and optional sealed payload bay. Wind limits: 8 m/s takeoff/landing; 17 m/s cruise. No whole-aircraft −40 °C or icing qualification found. Snow in the photo is not qualification evidence.'),
 ],note='Project fit: the larger variant is conditional near the lower reach target; 312 km with our payload and reserves remains unproven.',sources=[('Manufacturer brochure',URLS['tango_pdf']),('Product page / photo',URLS['tango_page'])]),
]
body=''
for i,p in enumerate(pages,1):
 if i>1: body+='<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
 body+=para('ARCTIC MEDICAL DELIVERY  |  UAV CANDIDATES  |  5 NOV 2026',size=17,bold=True,color='527484',after=100)
 body+=para(p['name'],size=36,bold=True,color='173F55',after=45)
 body+=para(p['subtitle'],size=21,color='527484',after=95)
 body+=picture(p['key'],i,crop=p['key']=='ar3')
 body+=para(p['caption'],size=16,color='667580',after=95)
 body+=table(p['rows'])
 body+=para(p['note'],size=19,bold=True,color='173F55',before=100,after=40)
 body+=links(p['sources'])
 body+=para('Manufacturer claims checked 5 Nov 2026. Maximum values may refer to different configurations. Cargo allowance must cover packaging and added equipment.',size=16,color='667580',after=30)
 body+=para(f'{i} / 3',size=16,color='667580',align='right',after=0)
body+='<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="850" w:right="1134" w:bottom="850" w:left="1134" w:header="400" w:footer="400"/></w:sectPr>'
document='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="'+NS+'" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><w:body>'+body+'</w:body></w:document>'
styles=f'''<?xml version="1.0" encoding="UTF-8"?><w:styles xmlns:w="{NS}"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="21"/><w:color w:val="263842"/><w:lang w:val="en-GB"/></w:rPr></w:rPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style></w:styles>'''
rels='<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
rels+='<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
for rid,typ,target,mode in RELS:
 rels+=f'<Relationship Id="{rid}" Type="{typ}" Target="{escape(target)}"'+(f' TargetMode="{mode}"' if mode else '')+'/>'
rels+='</Relationships>'
ct='''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="jpg" ContentType="image/jpeg"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>'''
package_rels='''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'''
for xml in [document,styles,rels,ct,package_rels]: ET.fromstring(xml)
with ZipFile(OUT,'w',ZIP_DEFLATED) as z:
 for name,data in {'[Content_Types].xml':ct,'_rels/.rels':package_rels,'word/document.xml':document,'word/styles.xml':styles,'word/_rels/document.xml.rels':rels}.items(): z.writestr(name,data.encode('utf-8'))
 for p in pages: z.write(ROOT/(p['key']+'.jpg'),'word/media/'+p['key']+'.jpg')
print(OUT,OUT.stat().st_size)
