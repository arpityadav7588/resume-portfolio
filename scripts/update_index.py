import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hero
    content = content.replace(
        'FastAPI &amp;<br/>\n            <span class="text-3d-orange py-2 block mt-4">AI Firmware Developer</span>',
        'Embedded Systems &amp;<br/>\n            <span class="text-3d-orange py-2 block mt-4">Robotics Engineer</span>'
    )
    content = content.replace(
        'Building the future of high-performance digital experiences where \n            <span class="text-primary font-extrabold border-b-4 border-primary/20">Generative AI</span> meets robust backend software architecture.',
        'Building the future of connected devices where \n            <span class="text-primary font-extrabold border-b-4 border-primary/20">Hardware</span> meets intelligent software architecture.'
    )

    # 2. About
    content = content.replace(
        '<img alt="arpit Yadav profile photo" class="w-full h-[620px] lg:h-[700px] object-cover grayscale group-hover:grayscale-0 transition-all duration-1000 scale-105 group-hover:scale-100" src="assets/c7774d6e-8c96-4dde-9e49-d24064189762.png"/>',
        '<img alt="arpit Yadav profile photo" class="w-full h-[620px] lg:h-[700px] object-cover grayscale group-hover:grayscale-0 transition-all duration-1000 scale-105 group-hover:scale-100" src="assets/img/arpit-profile.png"/>'
    )
    
    content = content.replace(
        'My Journey as a<br/><span class="text-3d-orange">Full-Stack &amp; Robotics Engineer</span>',
        'My Journey as a<br/><span class="text-3d-orange">Hardware &amp; Robotics Engineer</span>'
    )
    
    content = content.replace(
        'I build scalable backend systems in Python/FastAPI and integrate Large Language Models (LLMs) via OpenAI and LangChain. Combining clean database designs with intuitive frontend user interfaces is my primary focus.',
        'I build scalable embedded systems in C/C++ and integrate Internet of Things (IoT) devices with custom robotics platforms. Combining clean hardware designs with robust firmware algorithms is my primary focus.'
    )
    
    content = content.replace(
        '<h4 class="font-black text-xl text-on-background mb-1">1. Python Foundations</h4>\n                  <p class="text-base text-on-surface-variant leading-relaxed">Strong base in Python, OOP principles, and clean algorithm designs.</p>',
        '<h4 class="font-black text-xl text-on-background mb-1">1. Hardware Foundations</h4>\n                  <p class="text-base text-on-surface-variant leading-relaxed">Strong base in C/C++, circuit design, and microcontroller programming.</p>'
    )

    content = content.replace(
        '<h4 class="font-black text-xl text-on-background mb-1">2. Backend Development (FastAPI)</h4>\n                  <p class="text-base text-on-surface-variant leading-relaxed">Built scalable REST APIs, authentication flows, and PostgreSQL-backed systems.</p>',
        '<h4 class="font-black text-xl text-on-background mb-1">2. Embedded Systems (ESP32)</h4>\n                  <p class="text-base text-on-surface-variant leading-relaxed">Built custom PCB layouts, sensor integrations, and real-time operating systems.</p>'
    )
    
    content = content.replace(
        '<h4 class="font-black text-xl text-on-background mb-1">3. AI Integration &amp; SaaS</h4>\n                  <p class="text-base text-on-surface-variant leading-relaxed">Integrating custom RAG databases, parsing text with LangChain, and deploying SaaS dashboards.</p>',
        '<h4 class="font-black text-xl text-on-background mb-1">3. Robotics &amp; IoT Integration</h4>\n                  <p class="text-base text-on-surface-variant leading-relaxed">Integrating custom robotic platforms, connecting IoT sensors, and deploying edge computing solutions.</p>'
    )

    # 3. Skills
    skills_old = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Frontend -->
          <div class="tilt-card glass-panel p-8 rounded-[2.5rem] shadow-2xl transition-all duration-500 hover:border-primary/30 group">
            <div class="w-16 h-16 bg-3d-orange rounded-[1.25rem] flex items-center justify-center mb-7 text-white shadow-xl group-hover:-translate-y-2 transition-transform">
              <span class="material-symbols-outlined text-3xl">html</span>
            </div>
            <h3 class="font-headline text-[2rem] font-black mb-6">Frontend</h3>
            <div class="grid grid-cols-2 gap-3">
              <div class="skill-chip">React</div>
              <div class="skill-chip">Vite</div>
              <div class="skill-chip">JavaScript</div>
              <div class="skill-chip">HTML5</div>
              <div class="skill-chip">CSS3</div>
            </div>
          </div>
          <!-- Backend -->
          <div class="tilt-card glass-panel p-8 rounded-[2.5rem] shadow-2xl transition-all duration-500 hover:border-primary/30 group">
            <div class="w-16 h-16 bg-slate-900 rounded-[1.25rem] flex items-center justify-center mb-7 text-white shadow-xl group-hover:-translate-y-2 transition-transform">
              <span class="material-symbols-outlined text-3xl">database</span>
            </div>
            <h3 class="font-headline text-[2rem] font-black mb-6">Backend</h3>
            <div class="grid grid-cols-2 gap-3">
              <div class="skill-chip">Python</div>
              <div class="skill-chip">FastAPI</div>
              <div class="skill-chip">Django</div>
              <div class="skill-chip">PostgreSQL</div>
              <div class="skill-chip">Docker</div>
            </div>
          </div>
          <!-- AI/GenAI -->
          <div class="tilt-card glass-panel p-8 rounded-[2.5rem] shadow-2xl transition-all duration-500 hover:border-primary/30 group">
            <div class="w-16 h-16 bg-3d-orange-dark rounded-[1.25rem] flex items-center justify-center mb-7 text-white shadow-xl group-hover:-translate-y-2 transition-transform">
              <span class="material-symbols-outlined text-3xl">hub</span>
            </div>
            <h3 class="font-headline text-[2rem] font-black mb-6">AI Integration</h3>
            <div class="grid grid-cols-2 gap-3">
              <div class="skill-chip">OpenAI API</div>
              <div class="skill-chip">LangChain</div>
              <div class="skill-chip">RAG Systems</div>
              <div class="skill-chip">Vector DB</div>
              <div class="skill-chip">Prompts</div>
            </div>
          </div>
        </div>"""
    skills_new = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Hardware -->
          <div class="tilt-card glass-panel p-8 rounded-[2.5rem] shadow-2xl transition-all duration-500 hover:border-primary/30 group">
            <div class="w-16 h-16 bg-3d-orange rounded-[1.25rem] flex items-center justify-center mb-7 text-white shadow-xl group-hover:-translate-y-2 transition-transform">
              <span class="material-symbols-outlined text-3xl">memory</span>
            </div>
            <h3 class="font-headline text-[2rem] font-black mb-6">Hardware</h3>
            <div class="grid grid-cols-2 gap-3">
              <div class="skill-chip">Arduino</div>
              <div class="skill-chip">ESP32</div>
              <div class="skill-chip">Raspberry Pi</div>
              <div class="skill-chip">Sensors</div>
              <div class="skill-chip">PCB Design</div>
            </div>
          </div>
          <!-- Languages -->
          <div class="tilt-card glass-panel p-8 rounded-[2.5rem] shadow-2xl transition-all duration-500 hover:border-primary/30 group">
            <div class="w-16 h-16 bg-slate-900 rounded-[1.25rem] flex items-center justify-center mb-7 text-white shadow-xl group-hover:-translate-y-2 transition-transform">
              <span class="material-symbols-outlined text-3xl">code</span>
            </div>
            <h3 class="font-headline text-[2rem] font-black mb-6">Languages</h3>
            <div class="grid grid-cols-2 gap-3">
              <div class="skill-chip">C</div>
              <div class="skill-chip">C++</div>
              <div class="skill-chip">Python</div>
              <div class="skill-chip">Rust</div>
              <div class="skill-chip">Bash</div>
            </div>
          </div>
          <!-- Tools -->
          <div class="tilt-card glass-panel p-8 rounded-[2.5rem] shadow-2xl transition-all duration-500 hover:border-primary/30 group">
            <div class="w-16 h-16 bg-3d-orange-dark rounded-[1.25rem] flex items-center justify-center mb-7 text-white shadow-xl group-hover:-translate-y-2 transition-transform">
              <span class="material-symbols-outlined text-3xl">precision_manufacturing</span>
            </div>
            <h3 class="font-headline text-[2rem] font-black mb-6">Tools</h3>
            <div class="grid grid-cols-2 gap-3">
              <div class="skill-chip">Linux</div>
              <div class="skill-chip">Git</div>
              <div class="skill-chip">ROS</div>
              <div class="skill-chip">IoT</div>
              <div class="skill-chip">Robotics</div>
            </div>
          </div>
        </div>"""
    content = content.replace(skills_old, skills_new)

    # 4. Projects
    projects_old_1 = """            <div class="h-[240px] relative overflow-hidden">
              <img alt="Career AI project preview" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000" src="assets/image.png"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <div class="absolute bottom-6 left-6 flex gap-3">
                <span class="px-4 py-2 bg-3d-orange/90 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">AI MODEL</span>
                <span class="px-4 py-2 bg-white/20 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">Frontend</span>
              </div>
            </div>
            <div class="p-7">
              <h3 class="font-headline text-[1.8rem] font-black mb-3">Career AI</h3>
              <p class="font-body text-base text-on-surface-variant mb-6 leading-relaxed">
                AI-powered career guidance platform with personalized roadmaps, learning support, and skill-focused growth experiences.
              </p>
              <div class="flex items-center gap-4">
                <a class="flex-1 bg-3d-orange text-white px-6 py-3 rounded-full font-black text-sm flex items-center justify-center gap-3 btn-3d" href="projects/career-ai/index.html">
                  <span class="material-symbols-outlined text-xl">description</span> Case Study
                </a>
                <a class="p-3.5 bg-slate-100 rounded-full hover:bg-slate-200 transition-colors shadow-inner" href="https://career-ai-frontend.vercel.app/" target="_blank" rel="noopener">
                  <span class="material-symbols-outlined text-xl">rocket_launch</span>
                </a>
              </div>
            </div>"""
    projects_new_1 = """            <div class="h-[240px] relative overflow-hidden">
              <img alt="Autonomous Line Follower project preview" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000" src="assets/img/line-follower.png"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <div class="absolute bottom-6 left-6 flex gap-3">
                <span class="px-4 py-2 bg-3d-orange/90 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">HARDWARE</span>
                <span class="px-4 py-2 bg-white/20 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">ARDUINO</span>
              </div>
            </div>
            <div class="p-7">
              <h3 class="font-headline text-[1.8rem] font-black mb-3">Autonomous Line Follower</h3>
              <p class="font-body text-base text-on-surface-variant mb-6 leading-relaxed">
                A precise autonomous line follower robot with a custom PID control algorithm.
              </p>
              <div class="flex items-center gap-4">
                <a class="flex-1 bg-3d-orange text-white px-6 py-3 rounded-full font-black text-sm flex items-center justify-center gap-3 btn-3d" href="projects/career-ai/index.html">
                  <span class="material-symbols-outlined text-xl">description</span> Case Study
                </a>
                <a class="p-3.5 bg-slate-100 rounded-full hover:bg-slate-200 transition-colors shadow-inner" href="#" target="_blank" rel="noopener">
                  <span class="material-symbols-outlined text-xl">rocket_launch</span>
                </a>
              </div>
            </div>"""
    
    projects_old_2 = """            <div class="h-[240px] relative overflow-hidden">
              <img alt="Mobile Service Manager project preview" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000" src="assets/Screenshot 2026-03-15 211236.png"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <div class="absolute bottom-6 left-6 flex gap-3">
                <span class="px-4 py-2 bg-slate-900/90 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">Service Platform</span>
                <span class="px-4 py-2 bg-white/20 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">Management</span>
              </div>
            </div>
            <div class="p-7">
              <h3 class="font-headline text-[1.8rem] font-black mb-3">Mobile Service Manager</h3>
              <p class="font-body text-base text-on-surface-variant mb-6 leading-relaxed">
                A mobile service platform for managing service requests, technician assignments, and real-time tracking to improve operational efficiency.
              </p>
              <div class="flex items-center gap-4">
                <a class="flex-1 bg-slate-900 text-white px-6 py-3 rounded-full font-black text-sm flex items-center justify-center gap-3 hover:bg-slate-800 transition-all btn-3d !shadow-slate-400" href="projects/mobile-service-management/index.html">
                  <span class="material-symbols-outlined text-xl">description</span> Case Study
                </a>
                <a class="p-3.5 bg-slate-100 rounded-full hover:bg-slate-200 transition-colors shadow-inner" href="https://fa-mobiles.vercel.app/services" target="_blank" rel="noopener">
                  <span class="material-symbols-outlined text-xl">construction</span>
                </a>
              </div>
            </div>"""
    projects_new_2 = """            <div class="h-[240px] relative overflow-hidden">
              <img alt="Smart Ag Node project preview" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000" src="assets/img/smart-ag-node.png"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <div class="absolute bottom-6 left-6 flex gap-3">
                <span class="px-4 py-2 bg-slate-900/90 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">IOT</span>
                <span class="px-4 py-2 bg-white/20 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">SENSORS</span>
              </div>
            </div>
            <div class="p-7">
              <h3 class="font-headline text-[1.8rem] font-black mb-3">Smart Ag Node</h3>
              <p class="font-body text-base text-on-surface-variant mb-6 leading-relaxed">
                Remote agricultural data collection node using ESP32 to monitor soil and environmental conditions.
              </p>
              <div class="flex items-center gap-4">
                <a class="flex-1 bg-slate-900 text-white px-6 py-3 rounded-full font-black text-sm flex items-center justify-center gap-3 hover:bg-slate-800 transition-all btn-3d !shadow-slate-400" href="projects/mobile-service-management/index.html">
                  <span class="material-symbols-outlined text-xl">description</span> Case Study
                </a>
                <a class="p-3.5 bg-slate-100 rounded-full hover:bg-slate-200 transition-colors shadow-inner" href="#" target="_blank" rel="noopener">
                  <span class="material-symbols-outlined text-xl">construction</span>
                </a>
              </div>
            </div>"""
            
    projects_old_3 = """            <div class="h-[240px] relative overflow-hidden">
              <img alt="ETS2 Mod Stimilator project preview" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000" src="assets/Screenshot 2026-03-19 084814.png"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <div class="absolute bottom-6 left-6 flex gap-3">
                <span class="px-4 py-2 bg-orange-900/90 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">Secure Transfer</span>
                <span class="px-4 py-2 bg-white/20 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">ETS2</span>
              </div>
            </div>
            <div class="p-7">
              <h3 class="font-headline text-[1.8rem] font-black mb-3">ETS2 Launcher</h3>
              <p class="font-body text-base text-on-surface-variant mb-6 leading-relaxed">
                Secure mod file distribution system built to stop piracy using on-the-fly decryption and Backblaze B2 APIs.
              </p>
              <div class="flex items-center gap-4">
                <a class="flex-1 bg-orange-900 text-white px-6 py-3 rounded-full font-black text-sm flex items-center justify-center gap-3 hover:bg-orange-800 transition-all btn-3d" href="projects/ets2-launcher/index.html">
                  <span class="material-symbols-outlined text-xl">description</span> Case Study
                </a>
                <a class="p-3.5 bg-slate-100 rounded-full hover:bg-slate-200 transition-colors shadow-inner" href="https://www.linkedin.com/posts/arpityadav-727b0a219_backenddeveloper-react-fastapi-ugcPost-7440825775236329472-pl32/" target="_blank" rel="noopener">
                  <span class="material-symbols-outlined text-xl">link</span>
                </a>
              </div>
            </div>"""
    projects_new_3 = """            <div class="h-[240px] relative overflow-hidden">
              <img alt="Robo Soccer Player project preview" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000" src="assets/img/robo-soccer.png"/>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              <div class="absolute bottom-6 left-6 flex gap-3">
                <span class="px-4 py-2 bg-orange-900/90 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">ROBOTICS</span>
                <span class="px-4 py-2 bg-white/20 backdrop-blur-md rounded-xl text-[11px] font-black text-white tracking-widest uppercase">CONTROL</span>
              </div>
            </div>
            <div class="p-7">
              <h3 class="font-headline text-[1.8rem] font-black mb-3">Robo Soccer Player</h3>
              <p class="font-body text-base text-on-surface-variant mb-6 leading-relaxed">
                Competitive robotic soccer bot integrating vision processing and responsive drive control.
              </p>
              <div class="flex items-center gap-4">
                <a class="flex-1 bg-orange-900 text-white px-6 py-3 rounded-full font-black text-sm flex items-center justify-center gap-3 hover:bg-orange-800 transition-all btn-3d" href="projects/ets2-launcher/index.html">
                  <span class="material-symbols-outlined text-xl">description</span> Case Study
                </a>
                <a class="p-3.5 bg-slate-100 rounded-full hover:bg-slate-200 transition-colors shadow-inner" href="#" target="_blank" rel="noopener">
                  <span class="material-symbols-outlined text-xl">link</span>
                </a>
              </div>
            </div>"""
    content = content.replace(projects_old_1, projects_new_1)
    content = content.replace(projects_old_2, projects_new_2)
    content = content.replace(projects_old_3, projects_new_3)

    # 5. Schema replacement
    content = content.replace(
        '"image": "https://arpityadav.in/assets/c7774d6e-8c96-4dde-9e49-d24064189762.png"',
        '"image": "https://arpityadav.in/assets/img/arpit-profile.png"'
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done")

update_index()
