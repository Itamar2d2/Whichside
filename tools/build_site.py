# Builds index.html from tools/whichside.html (the page as published on claude.ai).
import re,pathlib
src=pathlib.Path('tools/whichside.html').read_text(encoding='utf8')
link=re.search(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?',src)
src=src.replace(link.group(0),'')
ff=''
for w in (500,600,700,800,900):
    ff+='@font-face{font-family:"Outfit";font-weight:%d;font-display:swap;src:url("fonts/outfit-latin-%d-normal.woff2") format("woff2")}\n'%(w,w)
for w in (400,500,600,700,800,900):
    ff+='@font-face{font-family:"Heebo";font-weight:%d;font-display:swap;src:url("fonts/heebo-hebrew-%d-normal.woff2") format("woff2");unicode-range:U+0590-05FF,U+200C-2010,U+20AA,U+25CC,U+FB1D-FB4F}\n'%(w,w)
    ff+='@font-face{font-family:"Heebo";font-weight:%d;font-display:swap;src:url("fonts/heebo-latin-%d-normal.woff2") format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}\n'%(w,w)
head='<!doctype html><html lang="he"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#060b26"><link rel="icon" href="icon.png"><link rel="apple-touch-icon" href="icon.png"><meta property="og:title" content="WhichSide"><meta property="og:description" content="המאגר המקיף שעושה סדר בנושא"><meta property="og:image" content="https://itamar2d2.github.io/Whichside/og.png"><meta property="og:image:width" content="1080"><meta property="og:image:height" content="1350"><meta property="og:url" content="https://itamar2d2.github.io/Whichside/"><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image"><style>:root{color-scheme:dark}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}\n'+ff+'</style></head><body>'
pathlib.Path('index.html').write_text(head+src+'</body></html>',encoding='utf8')
print('index.html written',len(src))
