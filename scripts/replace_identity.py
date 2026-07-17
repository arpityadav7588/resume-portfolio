import os
import re

replacements = {
    "arpit Yadav": "arpit Yadav",
    "arpityadav.in": "arpityadav.in",
    "FastAPI, Python &amp; AI Developer": "Embedded Systems, IoT &amp; Robotics Engineer",
    "FastAPI, Python & AI Developer": "Embedded Systems, IoT & Robotics Engineer",
    "FastAPI Developer": "Embedded Systems Engineer",
    "Python Developer": "IoT Engineer",
    "AI Developer": "Robotics Engineer",
    "Full Stack Developer": "Full Stack IoT Developer",
    "Backend Developer": "Hardware Developer",
    "SaaS Developer": "Firmware Developer",
    "Generative AI Developer": "Control Systems Engineer",
    "arpityadavarpit045@gmail.com": "arpityadavarpit045@gmail.com",
    "https://www.linkedin.com/in/arpityadav-ai": "https://linkedin.com/in/arpit-yadav-70367b342",
    "https://github.com/arpityadav7588": "https://github.com/arpityadav7588",
    "@arpityadav": "@arpityadav",
    "https://hashnode.com/@arpitv": "https://github.com/arpityadav7588",
    "https://medium.com/@arpitv": "https://github.com/arpityadav7588",
    "https://dev.to/arpit_v": "https://github.com/arpityadav7588"
}

def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in replacements.items():
                    new_content = new_content.replace(old, new)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    process_html_files(".")
