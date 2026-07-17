import os
import shutil

# 1. Update projects/index.html
def update_projects_index():
    filepath = 'projects/index.html'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the grid with new cards
    old_grid_start = '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">'
    new_grid_start = '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-12">'

    content = content.replace(old_grid_start, new_grid_start)
    
    # We will replace the entire content between the grid start and the end of the grid.
    # It's easier to just do a string replacement of the old cards.
    
    old_cards = """          <!-- Project 1 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/image.png" alt="Career AI Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">Career AI</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">AI Roadmaps &amp; Resumes</p>
              <a class="bg-3d-orange text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="career-ai/index.html">
                View Case Study
              </a>
            </div>
          </div>
          
          <!-- Project 2 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/Screenshot 2026-03-15 211236.png" alt="Mobile Repair Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">Mobile Repair CRM</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">SaaS &amp; Repair Operations</p>
              <a class="bg-slate-900 text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="mobile-service-management/index.html">
                View Case Study
              </a>
            </div>
          </div>

          <!-- Project 3 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/Screenshot 2026-03-19 084814.png" alt="ETS2 Launcher Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">ETS2 DRM Launcher</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">DRM &amp; File Encryption</p>
              <a class="bg-3d-orange text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="ets2-launcher/index.html">
                View Case Study
              </a>
            </div>
          </div>"""
          
    new_cards = """          <!-- Project 1 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/img/line_follower_1784211899753.png" alt="Line-follower Robot Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">Line-following Robot</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">PID &amp; Infrared Sensors</p>
              <a class="bg-3d-orange text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="line-follower/index.html">
                View Details
              </a>
            </div>
          </div>
          
          <!-- Project 2 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/img/smart_ag_node_1784211912785.png" alt="Smart Ag Node Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">Smart Agricultural Node</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">ESP32 &amp; MQTT</p>
              <a class="bg-slate-900 text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="smart-ag-node/index.html">
                View Details
              </a>
            </div>
          </div>

          <!-- Project 3 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/img/robo_soccer_1784211926326.png" alt="Robo Soccer Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">Robo-Soccer Bot</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">Bluetooth &amp; Dual Motor</p>
              <a class="bg-3d-orange text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="robo-soccer/index.html">
                View Details
              </a>
            </div>
          </div>
          
          <!-- Project 4 -->
          <div class="group relative bg-white rounded-[2rem] overflow-hidden shadow-xl border border-slate-100 hover:shadow-2xl transition-all duration-300">
            <div class="h-[180px] overflow-hidden relative">
              <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src="../assets/img/iot_environment_1784211938527.png" alt="IoT Environmental Monitor Preview"/>
            </div>
            <div class="p-6">
              <h3 class="font-headline text-2xl font-bold mb-2">IoT Environmental Monitor</h3>
              <p class="text-xs text-slate-500 mb-4 uppercase font-bold tracking-wider">Raspberry Pi &amp; Grafana</p>
              <a class="bg-slate-900 text-white px-6 py-2.5 rounded-full font-bold text-sm btn-3d w-full block text-center" href="iot-environment/index.html">
                View Details
              </a>
            </div>
          </div>"""
    
    content = content.replace(old_cards, new_cards)
    
    # Update linkedin
    content = content.replace(
        'https://www.linkedin.com/in/arpityadav-727b0a219',
        'https://linkedin.com/in/arpit-yadav-70367b342'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
def scaffold_project(name, title):
    base_html = f'''<!DOCTYPE html>
<html class="light" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>{title} | arpit Yadav</title>
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
  <style>
    body {{ font-family: 'Inter', sans-serif; background-color: #f2f7fe; color: #2a2f35; }}
    .font-plus-jakarta-sans {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    .glass-panel {{ background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.5); }}
  </style>
</head>
<body class="antialiased">
  <div class="container mx-auto px-6 max-w-4xl py-24 text-center">
    <div class="glass-panel p-16 rounded-[3rem] shadow-2xl">
      <h1 class="font-plus-jakarta-sans text-4xl font-black mb-6">{title}</h1>
      <p class="text-on-surface-variant mb-12">Case study details coming soon. Check back later for in-depth insights into this project.</p>
      <a href="../index.html" class="inline-block bg-slate-900 text-white px-8 py-3 rounded-full font-bold text-sm shadow-xl hover:scale-105 transition-transform">Back to Projects</a>
    </div>
  </div>
</body>
</html>'''
    os.makedirs(f'projects/{name}', exist_ok=True)
    with open(f'projects/{name}/index.html', 'w', encoding='utf-8') as f:
        f.write(base_html)

# Delete old
shutil.rmtree('projects/career-ai', ignore_errors=True)
shutil.rmtree('projects/ets2-launcher', ignore_errors=True)
shutil.rmtree('projects/mobile-service-management', ignore_errors=True)

# Update index
update_projects_index()

# Scaffold new
scaffold_project('line-follower', 'Line-following Robot')
scaffold_project('smart-ag-node', 'Smart Agricultural Node')
scaffold_project('robo-soccer', 'Robo-Soccer Bot')
scaffold_project('iot-environment', 'IoT Environmental Monitor')

print("Done projects")
