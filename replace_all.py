import os
import re

replacements = {
    r"arpit\b": "arpit",
    r"arpitbhuvan128@gmail\.com": "arpityadavarpit045@gmail.com",
    r"arpitv\.in": "arpityadav.in",
    r"arpit Yadav": "arpit Yadav",
    r"arpityadav": "arpityadav",
    r"arpityadav": "arpityadav",
    r"arpityadav": "arpityadav",
    r"arpit": "arpit",
    r"arpityadav7588": "arpityadav7588"
}

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    new_content = content
    # Order matters: more specific first
    for old, new in replacements.items():
        # Case insensitive replace for generic 'arpit' -> 'arpit'
        if old == r"arpit":
            new_content = re.sub(old, new, new_content, flags=re.IGNORECASE)
        else:
            new_content = re.sub(old, new, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk("."):
    if 'node_modules' in dirs: dirs.remove('node_modules')
    if '.git' in dirs: dirs.remove('.git')
    if '.venv' in dirs: dirs.remove('.venv')
    if 'assets' in dirs: dirs.remove('assets') # ignore images and compiled css

    for file in files:
        if file.endswith(('.html', '.xml', '.txt', '.js', '.py', '.json', '.md')):
            process_file(os.path.join(root, file))

