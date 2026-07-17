import os

# Define file-specific replacements
file_replacements = {
    'index.html': {
        'familyName": "V"': 'familyName": "Yadav"',
        'jobTitle": "FastAPI & AI Web Developer"': 'jobTitle": "Embedded Systems & Robotics Engineer"',
        'description": "arpit Yadav is a Python Backend Engineer, FastAPI specialist, and AI SaaS Builder based in India. He builds scalable REST APIs, integrates Large Language Models via OpenAI and LangChain, and deploys full-stack web applications and SaaS platforms."': 'description": "Arpit Yadav is an Embedded Systems and Robotics Engineer based in India. He builds efficient microcontroller firmware, custom PCB layouts, and integrates IoT sensor arrays with edge devices."',
        'knowsAbout": [\n          "Python", "FastAPI", "Django", "PostgreSQL", "Supabase",\n          "Docker", "React", "Vite", "OpenAI API", "LangChain",\n          "RAG Systems", "Generative AI", "Backend Development",\n          "Full Stack Development", "SaaS Architecture"\n        ]': 'knowsAbout": [\n          "C", "C++", "Python", "Rust", "Arduino", "ESP32",\n          "Raspberry Pi", "Sensors", "PCB Design", "ROS",\n          "Linux", "Git", "IoT", "Robotics", "Control Systems"\n        ]',
        'description": "Official portfolio of arpit Yadav — FastAPI & Robotics Engineer. Explore projects, certifications, and services."': 'description": "Official portfolio of Arpit Yadav — Embedded Systems & Robotics Engineer. Explore projects, achievements, and services."',
        'text": "arpit Yadav is a backend developer, Python/FastAPI engineer, and AI specialist focused on building full-stack web applications, secure DRM launchers, and SaaS repair management portals. He is available for freelance and full-time opportunities."': 'text": "Arpit Yadav is an Embedded Systems and Robotics Engineer focused on building microcontroller firmware, custom PCB designs, and autonomous robots. He is available for freelance and full-time opportunities."',
        'text": "arpit Yadav designs and builds high-performance Python/FastAPI backends, integrates Generative AI (OpenAI, LangChain, RAG), and ships full-stack SaaS products. He also writes technical articles on Hashnode, Medium, and Dev.to about AI engineering and backend development."': 'text": "Arpit Yadav designs and builds efficient C/C++ firmware, custom PCBs, and autonomous robotic control systems. He also writes technical articles about embedded systems and robotics."',
        'text": "Notable projects by arpit Yadav include: (1) Career AI – an AI-powered career guidance platform using OpenAI and LangChain RAG pipelines; (2) ETS2 Launcher – a secure DRM mod-distribution system using FastAPI and Backblaze B2 with on-the-fly decryption; (3) SaaS Repair Management Portal – a full-stack service management platform with customer dashboards and real-time status tracking."': 'text": "Notable projects by Arpit Yadav include: (1) Autonomous Line Follower – high-speed line-tracking robot with custom PID; (2) Smart Ag Node – ESP32 IoT node monitoring environmental metrics; (3) Robo Soccer Bot – competitive dual-motor Bluetooth-controlled bot; (4) IoT Environmental Monitor – Raspberry Pi climate tracker visualized on Grafana."',
        'text": "His primary skills are Python, FastAPI, Django, PostgreSQL, Supabase, Docker, React, Vite, OpenAI APIs, and LangChain."': 'text": "His primary skills are C/C++, Rust, Python, Arduino, ESP32, Raspberry Pi, ROS, Linux, and custom PCB Design."',
        'text": "arpit Yadav is active across multiple platforms: Portfolio at arpityadav.in, LinkedIn as arpityadav-ai, GitHub as arpityadav7588, X/Twitter as @arpityadav, Hashnode as @arpitv, Medium as @arpitv, Dev.to as arpit_v, and Stack Overflow as arpityadav."': 'text": "Arpit Yadav is active across multiple platforms: Portfolio at arpityadav.in, LinkedIn as arpit-yadav-70367b342, and GitHub as arpityadav7588."',
        'Official portfolio of arpit Yadav - specialized Python &amp; Embedded Systems Engineer, AI SaaS Builder, and Backend Engineer. Explore case studies on Career AI, secure DRM launchers, and SaaS repair platforms.': 'Official portfolio of Arpit Yadav - specialized Embedded Systems, IoT &amp; Robotics Engineer. Explore case studies on Line-following Robot, Smart Agricultural Node, Robo-Soccer, and IoT Environmental Monitor.',
        'Explore the portfolio of arpit Yadav. FastAPI backends, Generative AI applications, and custom SaaS builds.': 'Explore the portfolio of Arpit Yadav. Embedded systems, IoT devices, robotics, and custom hardware designs.',
        'FastAPI backend systems and Python applications integrated with OpenAI, LangChain, and RAG architectures.': 'Embedded systems, IoT, and custom robotics platforms integrated with robust firmware and hardware architectures.',
        'Python, FastAPI, AI Systems': 'C/C++, Embedded Systems, IoT',
        'w-[8rem] h-[8rem] rounded-[2.5rem] overflow-hidden grayscale hover:grayscale-0 transition-all duration-500 shadow-xl border border-white/60 mb-8': 'w-[8rem] h-[8rem] rounded-[2.5rem] overflow-hidden hover:grayscale-0 transition-all duration-500 shadow-xl border border-white/60 mb-8',
        'FastAPI &amp; AI Web Developer': 'Embedded Systems &amp; Robotics Engineer',
        'FastAPI & AI Web Developer': 'Embedded Systems & Robotics Engineer',
        'assets/img/profile-800w.webp': 'assets/img/arpit-profile.webp',
        'assets/img/Arpit-profile.webp': 'assets/img/arpit-profile.webp',
    },
    'about/index.html': {
        'Discover the professional background of arpit Yadav. From building robust backend services in FastAPI to launching generative AI integrations and SaaS products.': 'Discover the professional background of Arpit Yadav, specializing in embedded systems firmware, IoT devices, and robotics.',
        'Python, FastAPI &amp; Robotics Engineer': 'Embedded Systems &amp; Robotics Engineer',
        '../assets/img/Arpit-profile.png': '../assets/img/arpit-profile.webp',
        '../assets/img/Arpit-profile.webp': '../assets/img/arpit-profile.webp',
    },
    'services/index.html': {
        'Python, FastAPI &amp; AI Engineering': 'Embedded Systems &amp; Robotics Engineering',
        'Professional developer services by arpit Yadav. Specializing in secure FastAPI backend development, LLM &amp; LangChain AI integrations, vector search systems, and custom SaaS products.': 'Professional engineering services by Arpit Yadav. Specializing in C/C++ firmware development, IoT sensor integration, and custom PCB / hardware design.',
        'View engineering services offered by arpit Yadav. Standard packages, API design, RAG, and custom SaaS builds.': 'View engineering services offered by Arpit Yadav, including firmware development, IoT solutions, and custom hardware.',
    },
    'resume/index.html': {
        'Python &amp; Embedded Systems Engineer': 'Embedded Systems &amp; Robotics Engineer',
        'View the professional curriculum vitae of arpit Yadav. Focused on Python, FastAPI backend architectures, Supabase DB design, and custom AI SaaS systems.': 'View the professional resume and CV of Arpit Yadav. Focused on embedded firmware, C/C++ development, IoT sensor integration, and robotics engineering.',
        'Review experience history, technical credentials, and code qualifications of arpit Yadav.': 'Review experience history, technical credentials, and robotics qualifications of Arpit Yadav.',
    },
    'projects/index.html': {
        'Explore detailed engineering case studies by arpit Yadav, including Career AI roadmap engine, Mobile repair operations CRM, and the secure ETS2 DRM launcher.': 'Explore detailed engineering projects by Arpit Yadav, including Line-following robot, Smart Agricultural Node, and Robo-Soccer Bot.',
        'In-depth developer case studies covering Python, FastAPI backend architectures, Supabase DB systems, and GenAI models.': 'In-depth case studies covering C/C++ firmware, ESP32/Arduino, IoT sensor networks, and autonomous robotics.',
    },
    'blog/index.html': {
        'Read engineering articles by arpit Yadav. Focused on FastAPI development, Supabase integrations, LLM workflows, LangChain prompt designs, and building SaaS.': 'Read technical articles by Arpit Yadav. Focused on embedded firmware, C/C++ development, IoT systems, and robotics.',
    },
    'certifications/index.html': {
        'Certifications &amp; Credentials': 'Achievements &amp; Credentials',
        'Certifications & Credentials': 'Achievements & Credentials',
        'View the verified backend, full-stack, and container credentials earned by arpit Yadav, including certifications from IBM and LinkedIn Learning.': 'View the robotics achievements and technical credentials earned by Arpit Yadav, including state-level competition awards and hackathon finalist certificates.',
        'Verified professional developer credentials earned by arpit Yadav in Python, Django, APIs, and Docker.': 'Verified achievements and technical credentials earned by Arpit Yadav in robotics and hardware engineering.',
    },
    'feed.xml': {
        'Developer insights and step-by-step guides on Python backends, FastAPI APIs, AI applications, and SaaS engineering.': 'Engineering insights and updates on Embedded Systems, Robotics, IoT, and hardware design.',
        'How I Built Career AI Using FastAPI': 'Developing a PID Controller for a Line-following Robot',
        'An in-depth architectural breakdown of processing resumes, running LLM extraction chains, and streaming roadmaps in FastAPI.': 'An in-depth breakdown of designing a custom PID feedback loop for precise differential-drive control.',
        'https://arpityadav.in/blog/how-i-built-career-ai-using-fastapi/': 'https://arpityadav.in/projects/line-follower/',
        'My Journey Learning FastAPI: From Scripting to Scale': 'Building a Smart Agricultural Node with ESP32 & MQTT',
        'Takeaways migrating to FastAPI: managing async context, writing Pydantic validation models, Depends injection, and Docker builds.': 'Implementing low-power sleep modes, calibrating capacitive moisture sensors, and streaming telemetry over MQTT.',
        'https://arpityadav.in/blog/my-journey-learning-fastapi/': 'https://arpityadav.in/projects/smart-ag-node/',
    }
}

def clean_file(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content

    # Apply file-specific replacements first
    basename = os.path.relpath(filepath, '.').replace('\\', '/')
    if basename.startswith('./'):
        basename = basename[2:]
        
    if basename in file_replacements:
        for old, new in sorted(file_replacements[basename].items(), key=lambda x: len(x[0]), reverse=True):
            new_content = new_content.replace(old, new)

    # 1. Replace logo initials BV -> AY
    new_content = new_content.replace('text-white text-xs">BV</span>', 'text-white text-xs">AY</span>')
    new_content = new_content.replace('text-white text-xs">BV', 'text-white text-xs">AY')
    new_content = new_content.replace('text-white">BV', 'text-white">AY')
    
    # 2. Replace old image placeholder in og:image metadata
    new_content = new_content.replace('assets/c7774d6e-8c96-4dde-9e49-d24064189762.png', 'assets/img/arpit-profile.webp')
    
    # 3. Capitalize Arpit yadav / arpit Yadav -> Arpit Yadav
    new_content = new_content.replace('arpit yadav', 'Arpit Yadav')
    new_content = new_content.replace('arpit Yadav', 'Arpit Yadav')
    new_content = new_content.replace('Arpit yadav', 'Arpit Yadav')
    
    # 4. Standard name replacements for "arpit" -> "Arpit"
    new_content = new_content.replace('© 2026 arpit Yadav', '© 2026 Arpit Yadav')
    new_content = new_content.replace('© 2026 arpit', '© 2026 Arpit')
    new_content = new_content.replace('arpit\'s', 'Arpit\'s')
    new_content = new_content.replace('arpit\'', 'Arpit\'')
    new_content = new_content.replace('About arpit', 'About Arpit')
    new_content = new_content.replace('by arpit', 'by Arpit')
    new_content = new_content.replace('of arpit', 'of Arpit')
    new_content = new_content.replace('for arpit', 'for Arpit')
    new_content = new_content.replace('earned by arpit', 'earned by Arpit')
    new_content = new_content.replace('>arpit Yadav', '>Arpit Yadav')
    new_content = new_content.replace('>arpit ', '>Arpit ')
    new_content = new_content.replace(' arpit ', ' Arpit ')
    new_content = new_content.replace('"arpit"', '"Arpit"')
    new_content = new_content.replace('"name": "arpit', '"name": "Arpit')
    new_content = new_content.replace('"givenName": "arpit"', '"givenName": "Arpit"')
    
    # 5. Fix uppercase domains
    new_content = new_content.replace('Arpityadav.in', 'arpityadav.in')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned up: {filepath}")

# Walk directories
for root, dirs, files in os.walk('.'):
    if 'node_modules' in dirs: dirs.remove('node_modules')
    if '.git' in dirs: dirs.remove('.git')
    if '.venv' in dirs: dirs.remove('.venv')
    if 'assets' in dirs: dirs.remove('assets')
    
    for file in files:
        if file.endswith(('.html', '.xml', '.txt')):
            clean_file(os.path.join(root, file))
