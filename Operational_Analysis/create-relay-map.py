"""Render the existing relay catalogue; no source coordinates or distances are changed.

Bundled public-domain coastline: Natural Earth 1:110m land.
https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_land.geojson
"""
import csv, json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import patheffects as pe

ROOT = Path(__file__).resolve().parent
sites = list(csv.DictReader((ROOT/'relay-locations.csv').open(newline='')))
by_id = {s['id']: s for s in sites}
legs = list(csv.DictReader((ROOT/'relay-chain-distances.csv').open(newline='')))
land = json.loads((ROOT/'relay-map-land.geojson').read_text())
PORTS = {'MUR','DIK','DUD','TIK','PEV','ANA'}  # Port labels in Arc_map_full; visual grouping, not a size ranking.
NAVY, TEAL, RED, ORANGE = '#153b59', '#207e89', '#bd343d', '#c08021'
scale = math.cos(math.radians(70))
def lon(s):
    v = float(s['longitude'])
    return v+360 if v < 0 else v

def xy(s): return lon(s)*scale, float(s['latitude'])

def curve(a,b):
    # Great-circle interpolation for drawing only; distance labels use WGS84 CSV results.
    a,b=by_id[a],by_id[b]
    def unit(s):
        la,lo=map(math.radians,(float(s['latitude']),lon(s)))
        return np.array([math.cos(la)*math.cos(lo),math.cos(la)*math.sin(lo),math.sin(la)])
    u,v=unit(a),unit(b); angle=math.acos(np.clip(np.dot(u,v),-1,1))
    t=np.linspace(0,1,50)
    w=(np.sin((1-t)*angle)[:,None]*u+np.sin(t*angle)[:,None]*v)/math.sin(angle)
    ll=np.degrees(np.unwrap(np.arctan2(w[:,1],w[:,0])))
    ll+=360*round((lon(a)-ll[0])/360)
    return ll*scale,np.degrees(np.arctan2(w[:,2],np.hypot(w[:,0],w[:,1])))

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titleweight':'bold'})
fig=plt.figure(figsize=(25,16),facecolor='#fbfcfd')
fig.text(.035,.965,'MURMANSK–ANADYR  |  RELAY CANDIDATES & DISTANCE GAPS',fontsize=23,weight='bold',color=NAVY)
fig.text(.035,.94,'57 candidate sites • 36 illustrative-chain legs • 4 direct gaps over 300 km • 4 November 2026',fontsize=13,color='#536474')
main=fig.add_axes([.035,.555,.93,.355])
west=fig.add_axes([.035,.205,.30,.28])
central=fig.add_axes([.355,.205,.30,.28])
east=fig.add_axes([.675,.205,.29,.28])

def base(ax, bounds, title):
    lo,hi,bot,top=bounds
    ax.set_facecolor('#e8f2f7')
    for feature in land['features']:
        g=feature['geometry']; polygons=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
        for poly in polygons:
            ring=np.asarray(poly[0]); ls=np.degrees(np.unwrap(np.radians(ring[:,0])))
            for shift in (-360,0,360):
                xx=ls+shift
                if xx.max()<lo or xx.min()>hi or ring[:,1].max()<bot:continue
                ax.fill(xx*scale,ring[:,1],facecolor='#e7e8de',edgecolor='#b7c2bb',linewidth=.55,zorder=1)
    ax.set_xlim(lo*scale,hi*scale);ax.set_ylim(bot,top);ax.set_aspect('equal',adjustable='box')
    tickstep=20 if hi-lo>100 else 10
    ticks=np.arange(math.ceil(lo/tickstep)*tickstep,hi+1,tickstep)
    ax.set_xticks(ticks*scale,[f'{v}°E' if v<=180 else f'{360-v}°W' for v in ticks])
    ticks=np.arange(math.ceil(bot/2)*2,math.floor(top/2)*2+.01,2)
    ax.set_yticks(ticks,[f'{v}°N' for v in ticks])
    ax.tick_params(labelsize=8,length=0,pad=5)
    ax.grid(color='#bacbd3',alpha=.5,linewidth=.5,zorder=0)
    for sp in ax.spines.values():sp.set_color('#c4d1d8')
    ax.set_title(title,loc='left',fontsize=12,color=NAVY,pad=10)
    # All main-chain links and the recorded gap detours.
    for leg in legs:
        typ=leg['chain']
        if typ!='illustrative_main' and not typ.startswith('detour_') and typ!='alternative_CHR_PEV_via_Bilibino':continue
        x,y=curve(leg['from_id'],leg['to_id'])
        if typ=='illustrative_main':
            gap=float(leg['distance_km'])>300
            if gap:ax.plot(x,y,color=RED,lw=15,alpha=.14,zorder=2,solid_capstyle='round')
            ax.plot(x,y,color=RED if gap else TEAL,lw=2.2 if gap else 1.25,zorder=3)
        else:ax.plot(x,y,color=ORANGE,lw=1.3,ls=(0,(4,3)),alpha=.85,zorder=3)
    for s in sites:
        x,y=xy(s)
        if s['category']=='industrial_staff_candidate':marker,size,color='D',68,ORANGE
        elif s['id'] in PORTS:marker,size,color='s',100,NAVY
        else:marker,size,color='o',31,TEAL
        ax.scatter(x,y,s=size,marker=marker,c=color,edgecolors='white',linewidths=.9,zorder=6)

base(main,(27,190,63,78),'OVERVIEW — red corridors identify direct legs longer than 300 km')
base(west,(28,106,65.5,75.5),'WEST  |  Kola, Yamal and Taymyr')
base(central,(100,163,67.2,75.5),'CENTRAL  |  Laptev and East Siberian coast')
base(east,(158,189,63.5,74.2),'EAST  |  Kolyma and Chukotka')
fig.canvas.draw()

def labels(ax, selection, fontsize=8):
    renderer=fig.canvas.get_renderer(); occupied=[]
    bounds=ax.get_window_extent(renderer)
    # Place important labels first, then find a free nearby position for each other label.
    ordered=sorted(selection,key=lambda s: (s['id'] not in PORTS,s['name']))
    for s in ordered:
        x,y=xy(s)
        if not(ax.get_xlim()[0]<x<ax.get_xlim()[1] and ax.get_ylim()[0]<y<ax.get_ylim()[1]):continue
        choices=[(7,7),(7,-12),(-7,7),(-7,-12),(7,19),(7,-24),(-7,19),(-7,-24),(17,31),(-17,31),(17,-36),(-17,-36)]
        if ax is main:
            overrides={'NIZ':(-15,28),'CHO':(-8,-30),'RUS':(12,-12),'POK':(-10,-28),'CHR':(8,-25),'KHT':(12,-18)}
            if s['id'] in overrides: choices=[overrides[s['id']]]
        if ax is central:
            overrides={'KHT':(7,-20),'YUR':(7,13)}
            if s['id'] in overrides: choices=[overrides[s['id']]]
        best=None
        for dx,dy in choices:
            ann=ax.annotate(s['name'],(x,y),xytext=(dx,dy),textcoords='offset points',fontsize=fontsize,
                color=NAVY,weight='bold' if s['id'] in PORTS else 'normal',ha='left' if dx>0 else 'right',
                va='bottom',zorder=8,arrowprops=dict(arrowstyle='-',lw=.4,color='#81929b'),
                path_effects=[pe.withStroke(linewidth=2.5,foreground='#fbfcfd')])
            box=ann.get_window_extent(renderer).expanded(1.025,1.1)
            overlap=sum(max(0,min(box.x1,b.x1)-max(box.x0,b.x0))*max(0,min(box.y1,b.y1)-max(box.y0,b.y0)) for b in occupied)
            outside=max(0,bounds.x0-box.x0)+max(0,box.x1-bounds.x1)+max(0,bounds.y0-box.y0)+max(0,box.y1-bounds.y1)
            score=overlap+outside*100
            ann.remove()
            if best is None or score<best[0]:best=(score,dx,dy)
            if score==0:break
        _,dx,dy=best
        ann=ax.annotate(s['name'],(x,y),xytext=(dx,dy),textcoords='offset points',fontsize=fontsize,
            color=NAVY,weight='bold' if s['id'] in PORTS else 'normal',ha='left' if dx>0 else 'right',va='bottom',zorder=8,
            arrowprops=dict(arrowstyle='-',lw=.4,color='#81929b'),path_effects=[pe.withStroke(linewidth=2.5,foreground='#fbfcfd')])
        occupied.append(ann.get_window_extent(renderer).expanded(1.025,1.1))

labels(main,[s for s in sites if s['id'] in PORTS or s['id'] in {'SAB','KHT','NIZ','CHO','RUS','POK','CHR'}],10)
for ax in (west,central,east):labels(ax,sites,8)
gaps=[r for r in legs if r['chain']=='illustrative_main' and float(r['distance_km'])>300]
for i,r in enumerate(gaps,1):
    xx,yy=curve(r['from_id'],r['to_id']);k=len(xx)//2
    main.annotate(f"{i}  |  {float(r['distance_km']):.0f} km",(xx[k],yy[k]),xytext=(0,55 if i in (2,3) else 26),textcoords='offset points',ha='center',
        color=RED,weight='bold',fontsize=10,bbox=dict(boxstyle='round,pad=.35',fc='#fff1ee',ec=RED,lw=.7),zorder=12)
for x,y,name in [(45,75.8,'BARENTS SEA'),(85,76,'KARA SEA'),(126,76,'LAPTEV SEA'),(158,75,'EAST SIBERIAN SEA'),(181,73.7,'CHUKCHI SEA')]:
    main.text(x*scale,y,name,color='#688c9f',fontsize=9,ha='center',style='italic')
# Distance scale is exact horizontally at the stated standard parallel.
x0,y0=35*scale,64.2
main.plot([x0,x0+500/111.195],[y0,y0],color=NAVY,lw=2)
main.text(x0+250/111.195,y0+.35,'500 km at 70°N',ha='center',fontsize=8,color=NAVY)
handles=[Line2D([],[],marker='s',ls='',color=NAVY,markersize=10,label='Major/reference port*'),
 Line2D([],[],marker='o',ls='',color=TEAL,markersize=7,label='Other relay candidate'),
 Line2D([],[],marker='D',ls='',color=ORANGE,markersize=8,label='Industrial site — year-round staffing unverified'),
 Line2D([],[],color=TEAL,lw=2,label='Illustrative chain: ≤300 km'),
 Line2D([],[],color=RED,lw=4,label='Direct gap: >300 km'),
 Line2D([],[],color=ORANGE,lw=2,ls='--',label='Candidate detour: each leg ≤300 km')]
fig.legend(handles=handles,loc='upper left',bbox_to_anchor=(.032,.545),ncol=3,frameon=False,fontsize=11,columnspacing=2.7,handlelength=2)
fig.text(.035,.165,'DIRECT GAPS IN THE ILLUSTRATIVE CHAIN',fontsize=12,weight='bold',color=NAVY)
for i,r in enumerate(gaps):
    x=.035+i*.235
    fig.text(x,.143,f"{i+1}. {r['from_name']} → {r['to_name']}",fontsize=10.5,weight='bold',color=RED)
    fig.text(x,.123,f"{float(r['distance_km']):.1f} km  ·  intermediate relays required",fontsize=10,color='#536474')
fig.text(.035,.092,'Red shading marks long direct links; it is not an offshore coverage boundary. Inland detours are candidates, not confirmed operating routes.',fontsize=10,color=NAVY)
fig.text(.035,.073,'All 57 sites require site-level qualification. Electricity, permanent presence, access and aircraft range are not fully verified. Gyda–Dikson: 299.8 km (borderline).',fontsize=10,color=NAVY)
fig.text(.035,.051,'*Port symbols follow port labels in Arc_map_full.png; they do not assert a verified ranking by cargo volume. Sabetta is shown as a conditional industrial site.',fontsize=9,color='#536474')
fig.text(.035,.034,'Sources: relay-locations.csv; relay-chain-distances.csv; Arc_map_full.png (reference). Coastline: Natural Earth 1:110m land, public domain.',fontsize=9,color='#536474')
fig.text(.035,.018,'Coordinates: WGS84. Display: equidistant cylindrical, standard parallel 70°N; links drawn as great circles. Reported distances: existing WGS84 ellipsoidal calculations.',fontsize=9,color='#536474')
assert len(sites)==57 and len(gaps)==4
for suffix in ('png','pdf','svg'):
    out=ROOT/f'Arctic_relay_map.{suffix}'
    fig.savefig(out,dpi=170,facecolor=fig.get_facecolor())
    print(out)
