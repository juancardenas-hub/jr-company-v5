import os

old_css_start = '/* Nova textura Chevron aplicada a todos os blocos de fundo globais */'
old_css_end = 'background-image: none !important;\n        }'

new_css = '''
        /* Nova textura Chevron aplicada a todos os blocos de fundo globais */
        body, section, main, footer, nav, header, .bg-white, .bg-slate-50, .bg-slate-100, .bg-surface, .bg-surface-container-lowest, .bg-surface-container-low {
            background-image: url("data:image/svg+xml,%3Csvg width='1440' height='1000' viewBox='0 0 1440 1000' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='rgba(0,0,0,0.04)' stroke-width='1.5'%3E%3Cpath d='M400 -500 L1350 450 Q1400 500 1350 550 L400 1500'/%3E%3Cpath d='M200 -500 L1150 450 Q1200 500 1150 550 L200 1500'/%3E%3Cpath d='M0 -500 L950 450 Q1000 500 950 550 L0 1500'/%3E%3Cpath d='M-200 -500 L750 450 Q800 500 750 550 L-200 1500'/%3E%3Cpath d='M-400 -500 L550 450 Q600 500 550 550 L-400 1500'/%3E%3C/g%3E%3C/svg%3E");
            background-attachment: fixed;
            background-size: cover;
            background-position: right center;
            background-repeat: no-repeat;
        }
        
        /* Override para fundos escuros, para a textura ficar branca */
        .bg-slate-950, .bg-on-surface, footer {
            background-image: url("data:image/svg+xml,%3Csvg width='1440' height='1000' viewBox='0 0 1440 1000' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='rgba(255,255,255,0.05)' stroke-width='1.5'%3E%3Cpath d='M400 -500 L1350 450 Q1400 500 1350 550 L400 1500'/%3E%3Cpath d='M200 -500 L1150 450 Q1200 500 1150 550 L200 1500'/%3E%3Cpath d='M0 -500 L950 450 Q1000 500 950 550 L0 1500'/%3E%3Cpath d='M-200 -500 L750 450 Q800 500 750 550 L-200 1500'/%3E%3Cpath d='M-400 -500 L550 450 Q600 500 550 550 L-400 1500'/%3E%3C/g%3E%3C/svg%3E") !important;
            background-attachment: fixed !important;
            background-size: cover !important;
            background-position: right center !important;
            background-repeat: no-repeat !important;
        }
        
        /* Remover a textura blueprint antiga para evidenciar a nova */
        .blueprint-bg, .blueprint-bg-dark {
            background-image: none !important;
        }
'''

directory = '.'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_css_start in content:
            # Find the start and end indices
            start_idx = content.find(old_css_start)
            end_idx = content.find(old_css_end) + len(old_css_end)
            
            # Replace the old CSS block with the new one
            content = content[:start_idx] + new_css.strip() + '\n' + content[end_idx:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filename}')
        else:
            print(f'Not found in {filename}')
