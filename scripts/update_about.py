import re
import os

def update_about():
    filepath = 'about/index.html'
    if not os.path.exists(filepath):
        print(f"File {filepath} not found!")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Image
    content = content.replace(
        '../assets/c7774d6e-8c96-4dde-9e49-d24064189762.png',
        '../assets/img/arpit-profile.png'
    )

    # Who Am I
    content = content.replace(
        'I am a Python and FastAPI backend engineer specializing in custom full-stack SaaS systems and Generative AI pipelines. I write strict schemas using Pydantic, build asynchronous routing structures, set up Supabase databases, and build dashboards in React.',
        'I am a Hardware and Robotics Engineer specializing in embedded systems, IoT sensors, and autonomous robots. I write efficient C/C++ firmware, design custom PCBs, integrate sensors, and deploy intelligent algorithms for autonomous navigation.'
    )

    # Core Philosophy
    content = content.replace(
        'I prioritize structural validation at the database layer (using PostgreSQL triggers and foreign keys) and clear asynchronous logic in python, ensuring applications perform efficiently at scale.',
        'I prioritize power efficiency and real-time responsiveness at the hardware layer, ensuring devices perform reliably in edge environments.'
    )

    # Skills Stack
    skills_old = """              <span class="skill-chip">Python</span>
              <span class="skill-chip">FastAPI</span>
              <span class="skill-chip">Django</span>
              <span class="skill-chip">PostgreSQL</span>
              <span class="skill-chip">Supabase</span>
              <span class="skill-chip">React</span>
              <span class="skill-chip">Docker</span>
              <span class="skill-chip">LangChain</span>
              <span class="skill-chip">OpenAI API</span>"""
    skills_new = """              <span class="skill-chip">C/C++</span>
              <span class="skill-chip">Rust</span>
              <span class="skill-chip">Python</span>
              <span class="skill-chip">Arduino</span>
              <span class="skill-chip">ESP32</span>
              <span class="skill-chip">Raspberry Pi</span>
              <span class="skill-chip">ROS</span>
              <span class="skill-chip">Linux</span>
              <span class="skill-chip">PCB Design</span>"""
    content = content.replace(skills_old, skills_new)
    
    # Update linkedin
    content = content.replace(
        'https://www.linkedin.com/in/arpityadav-727b0a219',
        'https://linkedin.com/in/arpit-yadav-70367b342'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done about")

update_about()
