import re
import os

def update_services():
    filepath = 'services/index.html'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Heading
    content = content.replace(
        'Developer &amp; <span class="text-3d-orange">AI Services</span>',
        'Embedded &amp; <span class="text-3d-orange">Hardware Services</span>'
    )

    # Cards
    cards_old = """          <!-- Card 1 -->
          <div class="p-8 bg-white/70 rounded-3xl border border-slate-100 shadow-md">
            <span class="material-symbols-outlined text-4xl text-primary mb-4">dns</span>
            <h3 class="font-headline text-xl font-bold mb-3">FastAPI API Systems</h3>
            <p class="font-body text-sm text-on-surface-variant leading-relaxed">
              Design and execute asynchronous backend APIs in Python with Pydantic typing, authentication filters, and PostgreSQL relations.
            </p>
          </div>
          <!-- Card 2 -->
          <div class="p-8 bg-white/70 rounded-3xl border border-slate-100 shadow-md">
            <span class="material-symbols-outlined text-4xl text-primary mb-4">neurology</span>
            <h3 class="font-headline text-xl font-bold mb-3">Generative AI &amp; RAG</h3>
            <p class="font-body text-sm text-on-surface-variant leading-relaxed">
              Connect external large language models to custom contexts utilizing vector searches, prompt parsing, and LangChain memory loops.
            </p>
          </div>
          <!-- Card 3 -->
          <div class="p-8 bg-white/70 rounded-3xl border border-slate-100 shadow-md">
            <span class="material-symbols-outlined text-4xl text-primary mb-4">devices</span>
            <h3 class="font-headline text-xl font-bold mb-3">Full-Stack SaaS</h3>
            <p class="font-body text-sm text-on-surface-variant leading-relaxed">
              Deploy responsive frontends in React integrated with real-time Supabase database rows, payment systems, and audit ledgers.
            </p>
          </div>"""
          
    cards_new = """          <!-- Card 1 -->
          <div class="p-8 bg-white/70 rounded-3xl border border-slate-100 shadow-md">
            <span class="material-symbols-outlined text-4xl text-primary mb-4">memory</span>
            <h3 class="font-headline text-xl font-bold mb-3">Embedded Systems &amp; Firmware</h3>
            <p class="font-body text-sm text-on-surface-variant leading-relaxed">
              Develop efficient C/C++ firmware for microcontrollers like Arduino and ESP32 with RTOS and edge-level power optimization.
            </p>
          </div>
          <!-- Card 2 -->
          <div class="p-8 bg-white/70 rounded-3xl border border-slate-100 shadow-md">
            <span class="material-symbols-outlined text-4xl text-primary mb-4">sensors</span>
            <h3 class="font-headline text-xl font-bold mb-3">IoT Sensor Integration</h3>
            <p class="font-body text-sm text-on-surface-variant leading-relaxed">
              Deploy and integrate environmental sensors, actuators, and cloud communication protocols like MQTT for real-time monitoring.
            </p>
          </div>
          <!-- Card 3 -->
          <div class="p-8 bg-white/70 rounded-3xl border border-slate-100 shadow-md">
            <span class="material-symbols-outlined text-4xl text-primary mb-4">developer_board</span>
            <h3 class="font-headline text-xl font-bold mb-3">Custom PCB &amp; Hardware Design</h3>
            <p class="font-body text-sm text-on-surface-variant leading-relaxed">
              Design custom hardware solutions and PCB layouts for autonomous robots, smart agriculture, and edge devices.
            </p>
          </div>"""
    content = content.replace(cards_old, cards_new)

    # Footer LinkedIn URL
    content = content.replace(
        'https://www.linkedin.com/in/arpityadav-727b0a219',
        'https://linkedin.com/in/arpit-yadav-70367b342'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done services")

update_services()
