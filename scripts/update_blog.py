import os
import shutil
import re

def update_blog_index():
    filepath = 'blog/index.html'
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update description text
    content = content.replace(
        'Guides, post-mortems, and concepts in backend Python APIs, database schema design, and Large Language Model applications.',
        'Articles, updates, and deep-dives into Embedded Systems, Robotics, IoT, and hardware engineering.'
    )

    # We need to replace the grid of articles with a simple coming soon message
    # Let's find the grid start and the closing tag
    
    # We will just replace everything from <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12"> 
    # down to the end of the grid.
    
    start_str = '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">'
    start_idx = content.find(start_str)
    
    # Find the closing tag of the grid. It should be before </div>\n        </div>\n    </div>\n  </main>
    # Since it's a bit risky to regex the end, I'll just look for a known structure after it, like '</div>\n\n      </div>\n    </div>\n  </main>'
    # Or just replace the whole section manually using regex.
    
    pattern = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">.*?</div>\n\n      </div>', re.DOTALL)
    
    new_grid = '''<div class="mt-12 text-center py-20 bg-white/50 rounded-3xl border border-slate-100 shadow-inner">
          <span class="material-symbols-outlined text-6xl text-slate-300 mb-4 block">article</span>
          <h3 class="font-headline text-2xl font-bold mb-2 text-slate-500">Coming Soon</h3>
          <p class="text-sm text-slate-400">Blog posts are currently being written. Check back later!</p>
        </div>
        
      </div>'''
      
    content = pattern.sub(new_grid, content)

    # Update linkedin
    content = content.replace(
        'https://www.linkedin.com/in/arpityadav-727b0a219',
        'https://linkedin.com/in/arpit-yadav-70367b342'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Delete old blog subdirs
subdirs = [
    'building-ai-powered-web-applications',
    'building-mobile-service-management-platform',
    'how-i-built-career-ai-using-fastapi',
    'lessons-learned-while-building-saas-products',
    'my-journey-learning-fastapi',
    'using-ai-to-accelerate-software-development'
]

for d in subdirs:
    shutil.rmtree(os.path.join('blog', d), ignore_errors=True)

update_blog_index()

print("Done blog")
