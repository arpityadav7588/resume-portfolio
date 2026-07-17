import re
import os

def update_resume():
    filepath = 'resume/index.html'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Experience section replacement -> Key Projects & Experience
    exp_old = """            <h2 class="font-headline text-2xl font-black mb-4 border-b pb-2">Experience</h2>
            <div class="mb-6">
              <div class="flex justify-between items-start mb-2">
                <h3 class="font-bold text-lg">Full-Stack &amp; Robotics Engineer (Freelance)</h3>
                <span class="text-xs font-black bg-slate-100 px-3 py-1 rounded-full text-slate-500">Nov 2023 - Present</span>
              </div>
              <ul class="list-disc pl-5 text-sm text-on-surface-variant space-y-2">
                <li><strong>Career AI:</strong> Developed asynchronous resume parser backend API using Python/FastAPI and LangChain structure validations.</li>
                <li><strong>ETS2 DRM Launcher:</strong> Implemented mod decryption processes binding file requests to Backblaze B2 transient urls.</li>
                <li><strong>Mobile repair CRM:</strong> Created database operations triggers and ledger registers inside Supabase.</li>
              </ul>
            </div>"""
            
    exp_new = """            <h2 class="font-headline text-2xl font-black mb-4 border-b pb-2">Key Projects</h2>
            <div class="mb-6">
              <ul class="list-disc pl-5 text-sm text-on-surface-variant space-y-4">
                <li>
                  <div class="flex justify-between items-start mb-1">
                    <strong class="text-lg text-slate-900">Line-following Robot</strong>
                  </div>
                  Developed a high-speed line-following robot using PID Controllers, Infrared Sensors array, and an Arduino for precise tracking.
                </li>
                <li>
                  <div class="flex justify-between items-start mb-1">
                    <strong class="text-lg text-slate-900">Smart Agricultural Node</strong>
                  </div>
                  Built an IoT node using ESP32, Soil Moisture, and Temp/Humidity sensors, pushing data to the cloud via MQTT for real-time monitoring.
                </li>
                <li>
                  <div class="flex justify-between items-start mb-1">
                    <strong class="text-lg text-slate-900">Robo-Soccer Bot</strong>
                  </div>
                  Designed and assembled a Bluetooth-controlled soccer bot with dual motor drivers and a reinforced chassis for state-level competitions.
                </li>
                <li>
                  <div class="flex justify-between items-start mb-1">
                    <strong class="text-lg text-slate-900">IoT Environmental Monitor</strong>
                  </div>
                  Created a Raspberry Pi based environment monitor using Python, collecting sensor data and visualizing it on a Grafana Dashboard.
                </li>
              </ul>
            </div>"""
    content = content.replace(exp_old, exp_new)

    # Certifications Section
    cert_old = """            <h2 class="font-headline text-2xl font-black mb-4 border-b pb-2">Certifications</h2>
            <div class="space-y-3 text-sm">
              <p><strong>IBM Full Stack IoT Developer Professional Certification</strong> (April 2024)</p>
              <p><strong>Django REST Framework Complete Course</strong> (January 2024)</p>
              <p><strong>Developing Backend with Node.js and Express</strong> (February 2024)</p>
            </div>"""
    cert_new = """            <h2 class="font-headline text-2xl font-black mb-4 border-b pb-2">Achievements</h2>
            <div class="space-y-3 text-sm">
              <p><strong>Winner of State-Level Robotics Competition</strong> (2024)</p>
              <p><strong>Smart India Hackathon Finalist</strong> (2024)</p>
            </div>"""
    content = content.replace(cert_old, cert_new)

    # Skills Section
    skills_old = """            <div class="flex flex-wrap gap-2 text-xs">
              <span class="skill-chip">Python</span>
              <span class="skill-chip">FastAPI</span>
              <span class="skill-chip">Django</span>
              <span class="skill-chip">PostgreSQL</span>
              <span class="skill-chip">Supabase</span>
              <span class="skill-chip">Docker</span>
              <span class="skill-chip">React</span>
              <span class="skill-chip">Vite</span>
              <span class="skill-chip">LangChain</span>
              <span class="skill-chip">OpenAI API</span>
            </div>"""
    skills_new = """            <div class="flex flex-wrap gap-2 text-xs">
              <span class="skill-chip">C/C++</span>
              <span class="skill-chip">Rust</span>
              <span class="skill-chip">Python</span>
              <span class="skill-chip">Arduino</span>
              <span class="skill-chip">ESP32</span>
              <span class="skill-chip">Raspberry Pi</span>
              <span class="skill-chip">ROS</span>
              <span class="skill-chip">Linux</span>
              <span class="skill-chip">PCB Design</span>
            </div>"""
    content = content.replace(skills_old, skills_new)

    # Contact Section
    content = content.replace(
        '<p><strong>Email:</strong> arpitv@example.com</p>',
        '<p><strong>Email:</strong> arpityadavarpit045@gmail.com</p>'
    )
    content = content.replace(
        '<p><strong>GitHub:</strong> github.com/arpityadav7588</p>',
        '<p><strong>GitHub:</strong> github.com/arpityadav7588</p>'
    )
    content = content.replace(
        '<p><strong>LinkedIn:</strong> linkedin.com/in/arpityadav-727b0a219</p>',
        '<p><strong>LinkedIn:</strong> linkedin.com/in/arpit-yadav-70367b342</p>'
    )
    # The first email replacement might fail since it's already arpityadavarpit045@gmail.com, but that's fine.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done resume")

update_resume()
