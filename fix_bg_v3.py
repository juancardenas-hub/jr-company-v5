import os
import re

new_css = """
        /* Nova textura Chevron aplicada a todos os blocos de fundo globais */
        body, section, main, footer, nav, header, .bg-white, .bg-slate-50, .bg-slate-100, .bg-surface, .bg-surface-container-lowest, .bg-surface-container-low {
            background-image: 
                url("data:image/svg+xml,%3Csvg width='1440' height='1000' viewBox='0 0 1440 1000' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='rgba(0,0,0,0.04)' stroke-width='1.5'%3E%3Cpath d='M400 -500 L1350 450 Q1400 500 1350 550 L400 1500'/%3E%3Cpath d='M200 -500 L1150 450 Q1200 500 1150 550 L200 1500'/%3E%3Cpath d='M0 -500 L950 450 Q1000 500 950 550 L0 1500'/%3E%3Cpath d='M-200 -500 L750 450 Q800 500 750 550 L-200 1500'/%3E%3Cpath d='M-400 -500 L550 450 Q600 500 550 550 L-400 1500'/%3E%3Ccircle cx='1400' cy='500' r='600' /%3E%3Ccircle cx='200' cy='800' r='400' /%3E%3Ccircle cx='800' cy='100' r='250' /%3E%3Ccircle cx='-100' cy='100' r='500' /%3E%3C/g%3E%3C/svg%3E"),
                radial-gradient(circle 800px at 85% 15%, rgba(0, 74, 198, 0.05) 0%, rgba(0, 74, 198, 0) 100%),
                radial-gradient(circle 600px at 15% 75%, rgba(0, 74, 198, 0.04) 0%, rgba(0, 74, 198, 0) 100%),
                radial-gradient(circle 900px at 50% 100%, rgba(0, 74, 198, 0.03) 0%, rgba(0, 74, 198, 0) 100%);
            background-attachment: fixed, fixed, fixed, fixed;
            background-size: cover, 100vw 100vh, 100vw 100vh, 100vw 100vh;
            background-position: right center, top left, top left, top left;
            background-repeat: no-repeat, no-repeat, no-repeat, no-repeat;
        }
        
        /* Override para fundos escuros, para a textura ficar branca */
        .bg-slate-950, .bg-on-surface, footer {
            background-image: 
                url("data:image/svg+xml,%3Csvg width='1440' height='1000' viewBox='0 0 1440 1000' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='rgba(255,255,255,0.05)' stroke-width='1.5'%3E%3Cpath d='M400 -500 L1350 450 Q1400 500 1350 550 L400 1500'/%3E%3Cpath d='M200 -500 L1150 450 Q1200 500 1150 550 L200 1500'/%3E%3Cpath d='M0 -500 L950 450 Q1000 500 950 550 L0 1500'/%3E%3Cpath d='M-200 -500 L750 450 Q800 500 750 550 L-200 1500'/%3E%3Cpath d='M-400 -500 L550 450 Q600 500 550 550 L-400 1500'/%3E%3Ccircle cx='1400' cy='500' r='600' /%3E%3Ccircle cx='200' cy='800' r='400' /%3E%3Ccircle cx='800' cy='100' r='250' /%3E%3Ccircle cx='-100' cy='100' r='500' /%3E%3C/g%3E%3C/svg%3E"),
                radial-gradient(circle 800px at 85% 15%, rgba(0, 74, 198, 0.15) 0%, rgba(0, 74, 198, 0) 100%),
                radial-gradient(circle 600px at 15% 75%, rgba(0, 74, 198, 0.1) 0%, rgba(0, 74, 198, 0) 100%),
                radial-gradient(circle 900px at 50% 100%, rgba(0, 74, 198, 0.08) 0%, rgba(0, 74, 198, 0) 100%) !important;
            background-attachment: fixed, fixed, fixed, fixed !important;
            background-size: cover, 100vw 100vh, 100vw 100vh, 100vw 100vh !important;
            background-position: right center, top left, top left, top left !important;
            background-repeat: no-repeat, no-repeat, no-repeat, no-repeat !important;
        }
        
        /* Remover a textura blueprint antiga para evidenciar a nova */
        .blueprint-bg, .blueprint-bg-dark {
            background-image: none !important;
        }
"""

directory = '.'
# Match from "/* Nova textura Chevron..." until right before "</style>" or another specific block
# Because the previous regex might match too much, let's just do a string replace since we know the exact content of index.html

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        start_marker = "/* Nova textura Chevron aplicada a todos os blocos de fundo globais */"
        end_marker = "background-image: none !important;\n        }"
        
        if start_marker in content and end_marker in content:
            start_idx = content.find(start_marker)
            end_idx = content.find(end_marker) + len(end_marker)
            
            new_content = content[:start_idx] + new_css.strip() + content[end_idx:]
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {filename}')
            else:
                print(f'No change in {filename}')
        else:
            print(f'Markers not found in {filename}')
