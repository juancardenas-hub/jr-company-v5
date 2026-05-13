"""
Substitui icones inadequados do footer (Material Symbols genericos)
por SVGs apropriados das marcas: Facebook, Instagram, LinkedIn, WhatsApp.
Aplica em todos os HTMLs do diretorio.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

# SVGs em currentColor (herdam a cor do <a>, mantendo hover existente)
SVG_FB = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
          'fill="currentColor" class="w-5 h-5" aria-hidden="true">'
          '<path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.86.24-1.45 1.48-1.45H16.5V4.5'
          'c-.27-.04-1.2-.12-2.28-.12-2.26 0-3.81 1.38-3.81 3.91V10.5H8v3h2.41V21h3.09Z"/></svg>')

SVG_IG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
          'fill="currentColor" class="w-5 h-5" aria-hidden="true">'
          '<path d="M12 2.2c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38'
          '.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23'
          '-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07'
          's-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38'
          'c-.16-.42-.36-1.06-.41-2.23C2.21 15.58 2.2 15.2 2.2 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23'
          '.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.21 8.8 2.2 12 2.2Z'
          'M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63a5.92 5.92 0 0 0-2.13 1.39A5.92 5.92 0 0 0 .62 4.15'
          'c-.3.76-.5 1.64-.55 2.9C.01 8.33 0 8.74 0 12c0 3.26.01 3.67.07 4.95.06 1.27.26 2.14.55 2.9'
          '.32.84.74 1.55 1.4 2.21a5.92 5.92 0 0 0 2.12 1.4c.76.29 1.64.49 2.9.55C8.33 23.99 8.74 24 12 24'
          's3.67-.01 4.95-.07c1.27-.06 2.14-.26 2.9-.55a6.16 6.16 0 0 0 3.52-3.52c.29-.76.49-1.64.55-2.9'
          '.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.14-.55-2.9a5.92 5.92 0 0 0-1.4-2.13'
          'A5.92 5.92 0 0 0 19.85.62c-.76-.3-1.64-.5-2.9-.55C15.67.01 15.26 0 12 0Z'
          'M12 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32Zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8Z'
          'M19.85 5.59a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0Z"/></svg>')

SVG_IN = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
         'fill="currentColor" class="w-5 h-5" aria-hidden="true">'
         '<path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.95v5.66H9.36V9h3.41v1.56h.05'
         'a3.74 3.74 0 0 1 3.36-1.85c3.6 0 4.27 2.37 4.27 5.45v6.29ZM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12Z'
         'M7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45C23.2 24 24 23.23 24 22.27V1.73C24 .77 23.2 0 22.22 0Z"/></svg>')

SVG_WA = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
         'fill="currentColor" class="w-5 h-5" aria-hidden="true">'
         '<path d="M.06 24l1.69-6.16A11.88 11.88 0 0 1 .15 11.9C.15 5.34 5.5 0 12.07 0a11.84 11.84 0 0 1 8.42 3.49 11.81 11.81 0 0 1 3.48 8.42c0 6.56-5.35 11.9-11.9 11.9-2 0-3.95-.5-5.69-1.45L.06 24Zm6.6-3.8.36.22a9.87 9.87 0 0 0 5.04 1.38c5.45 0 9.89-4.43 9.89-9.89A9.83 9.83 0 0 0 19.05 4.93a9.83 9.83 0 0 0-6.99-2.9c-5.46 0-9.9 4.44-9.9 9.89 0 1.86.52 3.68 1.5 5.26l.24.37-1 3.66 3.76-.99Zm11.39-6.7c-.07-.12-.27-.2-.56-.34-.3-.15-1.76-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48a9.07 9.07 0 0 1-1.66-2.07c-.18-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.21-.24-.58-.49-.5-.67-.51l-.57-.01a1.1 1.1 0 0 0-.8.37c-.27.3-1.04 1.02-1.04 2.49s1.07 2.88 1.22 3.08c.15.2 2.1 3.21 5.1 4.5.7.3 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41Z"/></svg>')

# Padroes Material Symbols a substituir.
# Usamos regex multiline pois alguns spans estao quebrados em duas linhas.
RE_FB  = re.compile(r'<span\s+class="material-symbols-outlined text-\[20px\]"\s*>\s*facebook\s*</span>',     re.DOTALL)
RE_IG  = re.compile(r'<span(?:\s+class="material-symbols-outlined text-\[20px\]"|\s+class="material-symbols-outlined text-\[20px\]"\s*)\s*>\s*photo_camera\s*</span>', re.DOTALL)
RE_IG2 = re.compile(r'<span\s*\n?\s*class="material-symbols-outlined text-\[20px\]"\s*>\s*photo_camera\s*</span>', re.DOTALL)
RE_IN  = re.compile(r'<span\s+class="material-symbols-outlined text-\[20px\]"\s*>\s*work\s*</span>',         re.DOTALL)
# WhatsApp: chat usado APENAS no contexto do whatsapp; restringimos pelo bg-green
# (evita mexer em outros 'chat' do site, se houver). Procuramos o bloco inteiro.
RE_WA = re.compile(
    r'(<div[^>]*bg-green-50[^>]*>\s*)<span\s+class="material-symbols-outlined text-\[20px\]"\s*>\s*chat\s*</span>',
    re.DOTALL,
)

def fix(html: str) -> tuple[str, int]:
    n = 0
    new, c = RE_FB.subn(SVG_FB, html);   n += c
    new, c = RE_IG.subn(SVG_IG, new);    n += c
    new, c = RE_IG2.subn(SVG_IG, new);   n += c
    new, c = RE_IN.subn(SVG_IN, new);    n += c
    new, c = RE_WA.subn(r'\1' + SVG_WA, new); n += c
    return new, n

def main():
    files = sorted(p for p in ROOT.glob("*.html"))
    total = 0
    for f in files:
        original = f.read_text(encoding="utf-8")
        updated, n = fix(original)
        if n:
            f.write_text(updated, encoding="utf-8")
            print(f"  {f.name}: {n} icones substituidos")
            total += n
        else:
            print(f"  {f.name}: (sem alteracoes)")
    print(f"\nTotal: {total} substituicoes em {len(files)} arquivos.")

if __name__ == "__main__":
    main()
