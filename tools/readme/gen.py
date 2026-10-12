import colorsys
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.abspath(_os.path.join(HERE, "..", ".."))
BG="#0B0D0F";PN="#111419";ST="#2A2D31";BONE="#E9E5DC";GR="#8E8A82";VER="#B62B32";RULE="#4D5156"
MONO="JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS="Inter, Segoe UI, Arial, sans-serif"
ROSE="#D45B54";LAV="#5462D4"
DEFS=f'''<defs>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#FFFFFF" stroke-opacity=".035"/></pattern>
<filter id="blur"><feGaussianBlur stdDeviation="22"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
<linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9E5DC" stop-opacity=".10"/><stop offset="1" stop-color="#E9E5DC" stop-opacity=".03"/></linearGradient>
<linearGradient id="tonal" x1="0" x2="1"><stop offset="0" stop-color="{LAV}"/><stop offset=".5" stop-color="#8E5FA8"/><stop offset="1" stop-color="{ROSE}"/></linearGradient>
</defs>'''
def t(x,y,s,size=12,fill=GR,font=MONO,w=600,anchor="start",ls=0,op=1):
    s=s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<text xml:space="preserve" x="{x}" y="{y}" font-family="{font}" font-size="{size}px" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{s}</text>'
def frame(w,h,label,tag,rx=16):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{DEFS}'
      f'<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="{rx}" fill="{BG}" stroke="{ST}"/>'
      f'<rect x="3" y="3" width="{w-6}" height="{h-6}" rx="{rx}" fill="url(#grid)"/>'
      + (t(28,34,label,12,GR,ls=2) + t(w-30,34,tag,10,VER,anchor="end",ls=2) if label else ""))
def card(x,y,w,h,k,v,sub,vc=BONE):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{PN}" stroke="{ST}"/>'
      + t(x+16,y+22,k,10,GR,ls=2) + t(x+16,y+53,v,18,vc,SANS,700) + t(x+16,y+78,sub,11,GR,w=400))
def folder(x,y,w,c,op=1):
    h=w*0.72; tab=w*0.38
    return (f'<g opacity="{op}"><path d="M{x} {y+h*0.14} q0 -{h*0.14} {w*0.06} -{h*0.14} h{tab-w*0.1} l{w*0.06} {h*0.08} h{w-tab-w*0.08} q{w*0.06} 0 {w*0.06} {h*0.08} v{h*0.06} z" fill="{c}" opacity=".75"/>'
      f'<rect x="{x}" y="{y+h*0.16}" width="{w}" height="{h*0.84}" rx="{w*0.06}" fill="{c}"/>'
      f'<rect x="{x+w*0.03}" y="{y+h*0.2}" width="{w*0.94}" height="{h*0.035}" rx="2" fill="#FFFFFF" opacity=".7"/></g>')
import json as _j
_SHI=_j.load(open(_os.path.join(HERE,"shi.json")))["d"]
def seal(cx,y,size,fill=VER):
    k=size/1000; tx=cx-502*k
    return f'<path d="{_SHI}" fill="{fill}" transform="translate({tx:.2f} {y}) scale({k} {-k})"/>'
out={}
# HERO
s=frame(1200,360,"","")
s+=f'<ellipse cx="900" cy="170" rx="300" ry="170" fill="url(#tonal)" opacity=".28" filter="url(#blur)"/>'
# window mock
s+=f'<rect x="690" y="62" width="440" height="250" rx="14" fill="#15171B" stroke="{ST}"/>'
s+=f'<rect x="690" y="62" width="120" height="250" rx="14" fill="url(#glass)"/><line x1="810" y1="62" x2="810" y2="312" stroke="{ST}"/>'
for i,yy in enumerate(range(96,230,22)):
    s+=f'<rect x="704" y="{yy}" width="{80 if i else 92}" height="10" rx="3" fill="{BONE}" opacity="{.5 if i==0 else .14}"/>'
s+=f'<rect x="700" y="90" width="102" height="22" rx="6" fill="{ROSE}" opacity=".25"/>'
cols=[LAV,"#8E5FA8",ROSE]
for r in range(2):
    for c in range(4):
        col=cols[(r*4+c)%3] if False else (LAV if (r*4+c)<3 else ("#8E5FA8" if (r*4+c)<5 else ROSE))
        s+=folder(836+c*72,100+r*92,56,col)
s+=f'<line x1="38" y1="35" x2="112" y2="35" stroke="{RULE}"/><line x1="38" y1="35" x2="38" y2="76" stroke="{RULE}"/>'
s+=f'<line x1="38" y1="325" x2="112" y2="325" stroke="{RULE}"/><line x1="38" y1="284" x2="38" y2="325" stroke="{RULE}"/>'
s+=t(58,77,"DFN / 01",13,GR,ls=3)
s+=t(58,140,"D O L P H I N",44,BONE,SANS,700,ls=8)
s+=t(58,188,"F I N D E R · N O C T A L I A",22,BONE,SANS,500,ls=4,op=.85)
s+=t(60,222,"A FINDER-STYLE DOLPHIN FOR HYPRLAND + NOCTALIA",13,GR,ls=2)
s+=t(60,252,"DARKLY  ·  GLASS  ·  MACTAHOE  ·  TONAL FOLDERS  ·  FISH",12,BONE,w=400,ls=1)
s+=t(60,310,"MAIOLO / SYSTEMS LAB",11,GR,ls=2)
s+=seal(1150,300,22)
s+=t(1150,322,"TONAL FIELD",9,GR,anchor="middle",ls=2,w=500)
for i,c in enumerate([LAV,"#8E5FA8",ROSE]): s+=f'<circle cx="{700+i*16}" cy="44" r="3" fill="{c}"/>'
out["hero"]=s+"</svg>"
# AT A GLANCE
s=frame(1200,185,"01 / AT A GLANCE","SYSTEM PROFILE")
for i,(k,v,sub) in enumerate([("QT STYLE","Darkly","per-widget translucency"),("ICONS","MacTahoe-dark","macOS Tahoe icon set"),("PALETTE","Noctalia M3","wallpaper → tonal roles"),("COMPOSITOR","Hyprland","Lua config · blur on")]):
    s+=card(28+i*287,58,275,96,k,v,sub)
out["at-a-glance"]=s+"</svg>"
# CAPABILITIES
s=frame(1200,330,"02 / CAPABILITIES","WHAT CHANGES")
caps=[("GLASS SIDEBAR","Sidebar + toolbar at 55%","Darkly opacity, Hyprland blur"),
("VIBRANT VIEW","File area at 80%","less black, wallpaper bleeds in"),
("TONAL FOLDERS","Folders follow Noctalia","post_hook recolours 18 SVGs"),
("MINIMAL CHROME","No menu, lean toolbar","◀ ▶ · view · path · search"),
("PER-FOLDER ICONS","folder-icons.tsv","written to .directory files"),
("SAFE INSTALL","install.fish","timestamped *.bak-* backups")]
for i,(k,v,sub) in enumerate(caps):
    x=28+(i%3)*384; y=58+(i//3)*128
    s+=f'<rect x="{x}" y="{y}" width="372" height="114" rx="12" fill="{PN}" stroke="{ST}"/>'
    s+=f'<circle cx="{x+20}" cy="{y+22}" r="3.5" fill="{VER if i!=2 else ROSE}"/>'
    s+=t(x+32,y+26,k,10,GR,ls=2)+t(x+20,y+62,v,18,BONE,SANS,700)+t(x+20,y+90,sub,12,GR,w=400)
out["capabilities"]=s+"</svg>"
# SHOWCASE tonal pipeline
s=frame(1200,330,"03 / TONAL PIPELINE","LIVE RECOLOUR")
steps=[("WALLPAPER","noctalia-wallpaper"),("M3 SCHEME","primary · primary.light"),("palette.json","~/.local/state/…"),("RECOLOUR","mactahoe-recolor.py"),("ICONS","places/scalable × 18")]
for i,(k,v) in enumerate(steps):
    x=28+i*232
    s+=f'<rect x="{x}" y="58" width="212" height="70" rx="12" fill="{PN}" stroke="{ST}"/>'
    s+=t(x+14,y:=82,k,11,BONE,w=700,ls=1)+t(x+14,110,v,11,GR,w=400)
    if i<4: s+=f'<path d="M{x+214} 93 h14" stroke="{VER}" stroke-width="1.5"/><path d="M{x+224} 89 l5 4 -5 4" fill="none" stroke="{VER}" stroke-width="1.5"/>'
s+=t(28,164,"HUE ← primary.light   ·   SATURATION ← max(both), capped at MAX_SAT 0.60   ·   LIGHTNESS = 0.58",11,GR,w=500,ls=1)
for j,(name,a,b,res) in enumerate([("Lavender scheme","#BCC2FF","#535A92",LAV),("Rose scheme","#FFB3AE","#904A46",ROSE)]):
    x=28+j*586; y=186
    s+=f'<rect x="{x}" y="{y}" width="558" height="116" rx="12" fill="{PN}" stroke="{ST}"/>'
    s+=t(x+16,y+24,name.upper(),10,GR,ls=2)
    for k,(c,l) in enumerate([(a,"primary"),(b,"primary.light")]):
        s+=f'<rect x="{x+16+k*120}" y="{y+40}" width="104" height="40" rx="8" fill="{c}"/>'+t(x+16+k*120,y+98,f"{l} {c.lower()}",10,GR,w=400)
    s+=t(x+262,y+66,"→",22,VER,SANS,700)
    s+=folder(x+300,y+36,64,res)+t(x+300,y+98,f"folder {res.lower()}",10,BONE,w=600)
    s+=t(x+400,y+60,"default",10,GR,w=400)+folder(x+400,y+68,34,"#006EFD",.55)+t(x+444,y+92,"#006efd",10,GR,w=400)
out["tonal-pipeline"]=s+"</svg>"
# CONTROL SURFACE
s=frame(1200,300,"05 / CONTROL SURFACE","TUNING KNOBS")
def knob(x,y,w,key,val,frac,note,col=VER):
    r=f'<rect x="{x}" y="{y}" width="{w}" height="64" rx="10" fill="{PN}" stroke="{ST}"/>'
    r+=t(x+14,y+22,key,11,BONE,w=600)+t(x+w-14,y+22,val,11,col,anchor="end",w=700)
    r+=f'<rect x="{x+14}" y="{y+34}" width="{w-28}" height="4" rx="2" fill="{ST}"/><rect x="{x+14}" y="{y+34}" width="{(w-28)*frac}" height="4" rx="2" fill="{col}"/>'
    r+=t(x+14,y+54,note,10,GR,w=400)
    return r
s+=t(28,66,"mactahoe-recolor.py",10,GR,ls=2)+t(612,66,"~/.config/darklyrc",10,GR,ls=2)
s+=knob(28,78,560,"LIGHTNESS","0.58",.58,"lower = darker folder · Finder ≈ 0.50",ROSE)
s+=knob(28,152,560,"MAX_SAT","0.60",.60,"0.3 discreet tonal · 0.8 vivid",ROSE)
for i,(k,v,n) in enumerate([("DolphinSidebarOpacity","55",.55),("ToolBarOpacity","55",.55),("DolphinViewOpacity","80",.80),("MenuOpacity","90",.90)]):
    x=612+(i%2)*284; y=78+(i//2)*74
    s+=knob(x,y,272,k,v,n,["40 glassier · 70 solid","toolbar glass","85–90 for light walls","context menus"][i])
s+=t(28,258,"$ python3 ~/.config/noctalia/scripts/mactahoe-recolor.py ['#rrggbb']",12,BONE,w=500)
s+=t(28,280,"$ ./install.fish [--no-deps]",12,BONE,w=500)
out["control-surface"]=s+"</svg>"
# ARCHITECTURE
s=frame(1200,360,"07 / ARCHITECTURE","REPO → SYSTEM")
rows=[("install.fish","orchestrates every step below","—"),
("noctalia/templates/mactahoe/palette.json","Noctalia template (primary, primary.light)","~/.config/noctalia/templates/mactahoe/"),
("noctalia/scripts/mactahoe-recolor.py","post_hook · recolours folders","~/.config/noctalia/scripts/"),
("noctalia/config.snippet.toml","[theme.templates.user.mactahoe]","~/.config/noctalia/config.toml"),
("config/darklyrc","glass opacities, no focus line","~/.config/darklyrc"),
("config/folder-icons.tsv","per-folder Icon= entries","~/<folder>/.directory"),
("kxmlgui/dolphinui.rc","lean toolbar layout","~/.local/share/kxmlgui5/dolphin/"),
("hypr/dolphin.lua","window rules (manual copy)","your Hyprland config")]
s+=t(28,64,"SOURCE",10,GR,ls=2)+t(470,64,"ROLE",10,GR,ls=2)+t(800,64,"TARGET",10,GR,ls=2)
for i,(a,b,c) in enumerate(rows):
    y=78+i*34
    s+=f'<line x1="28" y1="{y}" x2="1172" y2="{y}" stroke="{ST}"/>'
    s+=f'<circle cx="34" cy="{y+18}" r="3" fill="{VER if i==0 else (ROSE if "noctalia" in a else GR)}"/>'
    s+=t(46,y+22,a,12,BONE,w=600)+t(470,y+22,b,11,GR,w=400)+t(800,y+22,c,11,GR,w=400)
s+=f'<line x1="28" y1="{78+len(rows)*34}" x2="1172" y2="{78+len(rows)*34}" stroke="{ST}"/>'
out["architecture"]=s+"</svg>"
# FAILURE MODES
s=frame(1200,330,"08 / FAILURE MODES","SYMPTOM → CAUSE → FIX")
fm=[("Blur stops near the bottom / right edge","monitor scale < 1 (e.g. 0.9375)","scale = \"1\"",True),
("Folders keep their old colour","post_hook not run / python3 missing","run mactahoe-recolor.py by hand",True),
("Capacity bars under devices","Dolphin draws them, no toggle","hide the device from Places",False),
("\"16 folders\" in English","untranslated upstream strings","nothing to configure",False),
("\"cannot remove\" on reinstall","existing files in the icon tree","harmless",False)]
s+=t(28,64,"SYMPTOM",10,GR,ls=2)+t(470,64,"CAUSE",10,GR,ls=2)+t(860,64,"FIX",10,GR,ls=2)
for i,(a,b,c,hot) in enumerate(fm):
    y=78+i*46
    s+=f'<rect x="28" y="{y}" width="1144" height="38" rx="8" fill="{PN}" stroke="{ST}"/>'
    s+=f'<rect x="28" y="{y}" width="4" height="38" rx="2" fill="{VER if hot else RULE}"/>'
    s+=t(46,y+24,a,12,BONE,w=600)+t(470,y+24,b,11,GR,w=400)+t(860,y+24,c,11,VER if hot else GR,w=600)
out["failure-modes"]=s+"</svg>"
# PROVENANCE
s=frame(1200,200,"09 / PROVENANCE","UPSTREAM")
for i,(k,v,sub) in enumerate([("ICONS","MacTahoe","vinceliuice · GPL-3.0"),("QT STYLE","Darkly","Bali10050"),("SHELL","Noctalia","templates engine"),("THIS REPO","MIT","scripts + configs")]):
    s+=card(28+i*287,58,275,96,k,v,sub,BONE if i<3 else VER)
s+=t(28,180,"MacTahoe is downloaded at install time — not redistributed here.",11,GR,w=400)
out["provenance"]=s+"</svg>"
for k,v in out.items(): open(_os.path.join(ROOT,"assets/readme",f"{k}.svg"),"w").write(v)
print(list(out))
