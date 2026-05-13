import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to add an intersection observer script for the border animation
script_to_add = '''
                <script>
                document.addEventListener('DOMContentLoaded', () => {
                    const sections = document.querySelectorAll('.sticky-stack');
                    
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            const borderLine = entry.target.querySelector('.animated-border-line');
                            if (borderLine) {
                                if (entry.isIntersecting && entry.intersectionRatio > 0.1) {
                                    borderLine.style.transform = 'scaleX(1)';
                                    borderLine.style.opacity = '1';
                                } else if (entry.intersectionRatio < 0.1 && entry.boundingClientRect.top > 0) {
                                    borderLine.style.transform = 'scaleX(0)';
                                    borderLine.style.opacity = '0';
                                }
                            }
                        });
                    }, { threshold: [0, 0.1, 0.5, 1.0] });

                    sections.forEach(sec => observer.observe(sec));
                    
                    // Also add scale down effect to previous sections
                    window.addEventListener('scroll', () => {
                        sections.forEach((sec, index) => {
                            const rect = sec.getBoundingClientRect();
                            // If this section is sticky at the top, and the NEXT section is overlapping it
                            if (rect.top <= 0) {
                                const nextSec = sections[index + 1];
                                if (nextSec) {
                                    const nextRect = nextSec.getBoundingClientRect();
                                    const overlap = Math.max(0, window.innerHeight - nextRect.top);
                                    const progress = Math.min(1, overlap / window.innerHeight);
                                    
                                    // Scale down and fade out slightly
                                    const scale = 1 - (progress * 0.05); // shrink to 0.95
                                    const brightness = 1 - (progress * 0.4); // darken
                                    
                                    // Apply to the first child or an inner wrapper to avoid breaking sticky
                                    // Wait, applying transform to the sticky element itself can break position: sticky.
                                    // We must apply it to its visual content container.
                                }
                            }
                        });
                    });
                });
                </script>
'''

if 'animated-border-line' not in content:
    # First, let's inject the animated line into the notches container
    def inject_animated_line(match):
        # match is the <div class="absolute bottom-full ...">...</div>
        full_match = match.group(0)
        
        # We add a div for the animated line between the SVGs
        # The line will expand from the center
        animated_line = '<div class="animated-border-line absolute bottom-0 left-[16px] md:left-[24px] right-[16px] md:right-[24px] h-[1px] md:h-[2px] bg-gradient-to-r from-transparent via-[#374BFF] to-transparent transform scale-x-0 opacity-0 transition-all duration-1000 ease-out origin-center z-30"></div>'
        
        # Insert the animated line just before the closing </div> of the notch wrapper
        return full_match.replace('</div>', f'\n{animated_line}\n</div>')

    notch_container_regex = re.compile(r'<div class="absolute bottom-full left-0 w-full h-\[16px\] md:h-\[24px\] pointer-events-none z-20 flex justify-between">.*?</div>', re.DOTALL)
    
    new_content = notch_container_regex.sub(inject_animated_line, content)
    
    # Add the script just before </body>
    new_content = new_content.replace('</body>', script_to_add + '\n</body>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Added border animation successfully.")
else:
    print("Border animation already exists.")
