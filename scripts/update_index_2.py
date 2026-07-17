import re

def update_index2():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Certifications Section Replacement
    cert_old = """          <!-- Cert 1 -->
          <a class="group glass-panel p-9 rounded-[2.25rem] shadow-2xl border-white/60 transition-all duration-500 hover:-translate-y-2 tilt-card block" href="https://www.coursera.org/account/accomplishments/professional-cert/THK2H91LBK12" rel="noreferrer" target="_blank">
            <div class="cert-icon-panel mb-8 shadow-inner">
              <div class="cert-icon-badge bg-orange-500"><span class="material-symbols-outlined text-5xl">cloud</span></div>
            </div>
            <div class="flex items-start justify-between mb-6">
              <div class="w-[4.5rem] h-[4.5rem] rounded-[1.6rem] bg-orange-500 flex items-center justify-center text-white shadow-xl"><span class="material-symbols-outlined text-3xl">cloud</span></div>
              <span class="px-4 py-2 bg-orange-100 text-orange-700 rounded-full text-xs font-black tracking-[0.18em] uppercase">April 2024</span>
            </div>
            <p class="text-xs font-black uppercase tracking-[0.24em] text-on-surface-variant mb-4">IBM - Coursera</p>
            <h3 class="font-headline text-3xl font-black text-on-background mb-2">Full Stack IoT Developer Professional</h3>
          </a>
          <!-- Cert 2 -->
          <a class="group glass-panel p-9 rounded-[2.25rem] shadow-2xl border-white/60 transition-all duration-500 hover:-translate-y-2 tilt-card block" href="https://www.coursera.org/account/accomplishments/verify/OA4UT59PX4OI" rel="noreferrer" target="_blank">
            <div class="cert-icon-panel mb-8 shadow-inner">
              <div class="cert-icon-badge bg-slate-900"><span class="material-symbols-outlined text-5xl">webhook</span></div>
            </div>
            <div class="flex items-start justify-between mb-6">
              <div class="w-[4.5rem] h-[4.5rem] rounded-[1.6rem] bg-slate-900 flex items-center justify-center text-white shadow-xl"><span class="material-symbols-outlined text-3xl">webhook</span></div>
              <span class="px-4 py-2 bg-slate-900/10 text-slate-900 rounded-full text-xs font-black tracking-[0.18em] uppercase">January 2024</span>
            </div>
            <p class="text-xs font-black uppercase tracking-[0.24em] text-on-surface-variant mb-4">IBM - Coursera</p>
            <h3 class="font-headline text-3xl font-black text-on-background mb-2">Django REST Framework Complete</h3>
          </a>
          <!-- Cert 3 -->
          <a class="group glass-panel p-9 rounded-[2.25rem] shadow-2xl border-white/60 transition-all duration-500 hover:-translate-y-2 tilt-card block" href="https://www.coursera.org/account/accomplishments/verify/3VMU1S1GJM0Y" rel="noreferrer" target="_blank">
            <div class="cert-icon-panel mb-8 shadow-inner">
              <div class="cert-icon-badge bg-3d-orange-dark"><span class="material-symbols-outlined text-5xl">dns</span></div>
            </div>
            <div class="flex items-start justify-between mb-6">
              <div class="w-[4.5rem] h-[4.5rem] rounded-[1.6rem] bg-3d-orange-dark flex items-center justify-center text-white shadow-xl"><span class="material-symbols-outlined text-3xl">dns</span></div>
              <span class="px-4 py-2 bg-orange-900/10 text-orange-800 rounded-full text-xs font-black tracking-[0.18em] uppercase">February 2024</span>
            </div>
            <p class="text-xs font-black uppercase tracking-[0.24em] text-on-surface-variant mb-4">IBM - Coursera</p>
            <h3 class="font-headline text-3xl font-black text-on-background mb-2">Node.js and Express Backend</h3>
          </a>"""
          
    cert_new = """          <!-- Cert 1 -->
          <a class="group glass-panel p-9 rounded-[2.25rem] shadow-2xl border-white/60 transition-all duration-500 hover:-translate-y-2 tilt-card block" href="#" rel="noreferrer" target="_blank">
            <div class="cert-icon-panel mb-8 shadow-inner">
              <div class="cert-icon-badge bg-orange-500"><span class="material-symbols-outlined text-5xl">emoji_events</span></div>
            </div>
            <div class="flex items-start justify-between mb-6">
              <div class="w-[4.5rem] h-[4.5rem] rounded-[1.6rem] bg-orange-500 flex items-center justify-center text-white shadow-xl"><span class="material-symbols-outlined text-3xl">emoji_events</span></div>
              <span class="px-4 py-2 bg-orange-100 text-orange-700 rounded-full text-xs font-black tracking-[0.18em] uppercase">2024</span>
            </div>
            <p class="text-xs font-black uppercase tracking-[0.24em] text-on-surface-variant mb-4">Achievement</p>
            <h3 class="font-headline text-3xl font-black text-on-background mb-2">Winner of State-Level Robotics Competition</h3>
          </a>
          <!-- Cert 2 -->
          <a class="group glass-panel p-9 rounded-[2.25rem] shadow-2xl border-white/60 transition-all duration-500 hover:-translate-y-2 tilt-card block" href="#" rel="noreferrer" target="_blank">
            <div class="cert-icon-panel mb-8 shadow-inner">
              <div class="cert-icon-badge bg-slate-900"><span class="material-symbols-outlined text-5xl">lightbulb</span></div>
            </div>
            <div class="flex items-start justify-between mb-6">
              <div class="w-[4.5rem] h-[4.5rem] rounded-[1.6rem] bg-slate-900 flex items-center justify-center text-white shadow-xl"><span class="material-symbols-outlined text-3xl">lightbulb</span></div>
              <span class="px-4 py-2 bg-slate-900/10 text-slate-900 rounded-full text-xs font-black tracking-[0.18em] uppercase">2024</span>
            </div>
            <p class="text-xs font-black uppercase tracking-[0.24em] text-on-surface-variant mb-4">Achievement</p>
            <h3 class="font-headline text-3xl font-black text-on-background mb-2">Smart India Hackathon Finalist</h3>
          </a>"""

    content = content.replace(cert_old, cert_new)
    
    # Resume / CV PDF replacement
    content = content.replace(
        '<span class="font-label text-sm tracking-[0.2em] uppercase font-black text-on-surface-variant">Last Updated: Jun 2026</span>',
        '<span class="font-label text-sm tracking-[0.2em] uppercase font-black text-on-surface-variant">Last Updated: Sep 2026</span>'
    )
    
    # Let's adjust grid-cols in certifications section to grid-cols-1 md:grid-cols-2 instead of md:grid-cols-3
    content = content.replace(
        '<div class="grid grid-cols-1 md:grid-cols-3 gap-8">\n          <!-- Cert 1 -->',
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">\n          <!-- Cert 1 -->'
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done 2")

update_index2()
