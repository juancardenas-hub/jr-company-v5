import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

style_to_add = '''
                .sticky-stack {
                        position: sticky;
                        top: min(0px, calc(100vh - 100%));
                }
'''
if '.sticky-stack' not in content:
    content = content.replace('</style>', style_to_add + '</style>')

notch_regex = re.compile(r'\s*<div class="absolute top-0 left-0 w-full h-\[40px\].*?bg-([^ ]+).*?rounded-b-\[40px\].*?</div>')

def replace_notch(match):
    bg_color = match.group(1)
    # The bg_color could be slate-50, white, [#004AC6], etc.
    text_class = f'text-{bg_color}'
    if bg_color.startswith('['):
        text_class = f'text-{bg_color}'
        
    return f'''
                        <div class="absolute bottom-full left-0 w-full h-[16px] md:h-[24px] pointer-events-none z-20 flex justify-between">
                                <svg class="w-[16px] h-[16px] md:w-[24px] md:h-[24px] {text_class}" fill="currentColor" viewBox="0 0 24 24"><path d="M0 24V0c0 13.255 10.745 24 24 24H0z" /></svg>
                                <svg class="w-[16px] h-[16px] md:w-[24px] md:h-[24px] {text_class}" fill="currentColor" viewBox="0 0 24 24"><path d="M24 24V0c0 13.255-10.745 24-24 24h24z" /></svg>
                        </div>'''

content = notch_regex.sub(replace_notch, content)

sections = re.split(r'(<section\b[^>]*>)', content)
z_index = 10

new_content = ''
for part in sections:
    if part.startswith('<section'):
        if 'sticky-stack' not in part:
            class_match = re.search(r'class="([^"]*)"', part)
            if class_match:
                classes = class_match.group(1)
                classes = re.sub(r'z-\[[0-9]+\]|z-[0-9]+', '', classes)
                new_classes = f'{classes.strip()} sticky-stack z-[{z_index}]'
                part = part.replace(class_match.group(0), f'class="{new_classes}"')
            else:
                part = part.replace('<section', f'<section class="sticky-stack z-[{z_index}]"')
        z_index += 10
    new_content += part

# Finally, ensure footer has sticky-stack and correct z-index
footer_match = re.search(r'(<footer\b[^>]*class=")([^"]*)(")', new_content)
if footer_match:
    classes = footer_match.group(2)
    classes = re.sub(r'z-\[[0-9]+\]|z-[0-9]+', '', classes)
    new_classes = f'{classes.strip()} sticky-stack z-[{z_index}]'
    new_content = new_content.replace(footer_match.group(0), f'{footer_match.group(1)}{new_classes}{footer_match.group(3)}')

# Replace the footer notch
footer_notch_regex = re.compile(r'\s*<div class="absolute top-0 left-0 w-full h-\[40px\].*?bg-([^ ]+).*?rounded-b-\[40px\].*?</div>')
new_content = footer_notch_regex.sub(replace_notch, new_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done!')
