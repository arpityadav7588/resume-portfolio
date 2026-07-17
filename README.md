# Arpit Yadav - Personal Brand Portfolio

Welcome to the repository of my personal portfolio and brand platform. This website showcases my technical projects, engineering services, achievements, and professional journey as an **Embedded Systems, IoT & Robotics Engineer**.

The website is designed with a premium, responsive glassmorphism aesthetic, featuring optimized layouts, smooth transitions, custom 3D visual tokens, and an interactive resume.

---

## 🚀 Live Demo & Local Development

### 1. Prerequisite
Make sure you have Node.js installed on your machine.

### 2. Install Dependencies
Install Tailwind and image-processing modules:
```bash
npm install
```

### 3. Start Local Development Server
Launch the lightweight node development server:
```bash
npm run dev
```
The server will be active at **[http://localhost:3000/](http://localhost:3000/)**.

### 4. Build or Watch CSS
To compile and optimize the custom Tailwind stylesheet:
- **Build CSS**: `npm run build:css`
- **Watch Changes**: `npm run watch:css`

---

## 🛠️ Technology Stack

- **Core Structure & Logic**: Semantic HTML5, Vanilla JavaScript.
- **Styling & Theming**: Vanilla CSS variables (Design System) + Tailwind CSS (Layout & Utility classes).
- **Fonts & Symbols**: Google Fonts (*Plus Jakarta Sans* & *Inter*), Google Material Symbols.
- **Contact API**: Vercel/Node Serverless handler using the [Resend API](https://resend.com/) to process and dispatch messages.
- **Development Tooling**: Custom Node.js http static server, Sharp for visual asset compression.

---

## 📂 Repository Structure

```
├── .agents/               # Agent workflow rules and workspace controls
├── .vscode/               # Workspace settings and configurations
├── about/                 # "About Me" page with detail of skills & philosophy
├── api/                   # Serverless function handlers
│   └── contact.js         # Contact form POST handler using Resend
├── assets/                # Design assets
│   ├── css/               # Core CSS and compiled Tailwind styles
│   └── img/               # Optimized profile photo and project preview images
├── blog/                  # Technical blog homepage (Coming Soon)
├── certifications/        # Verified achievements, competition wins, and hackathons
├── projects/              # Detailed technical case studies and previews
│   ├── line-follower/     # Autonomous Line-following robot case study
│   ├── smart-ag-node/     # Smart Agricultural Node case study
│   ├── robo-soccer/       # Bluetooth Robo-Soccer Bot case study
│   └── iot-environment/   # IoT Environment Monitor case study
├── resume/                # Interactive Curriculum Vitae page (with Print option)
├── scripts/               # Helper tools
│   ├── dev-server.js      # Lightweight local HTTP server with mock contact API
│   └── optimize-images.js # Automated image-optimization pipeline using Sharp
├── src/                   # Tailwind CSS directives input file
├── index.html             # Homepage / Main portfolio hub
├── feed.xml               # Technical projects RSS Feed
├── sitemap.xml            # SEO sitemap definition
└── tailwind.config.js     # Tailwind compilation parameters
```

---

## 📁 Key Projects Featured

1. **Autonomous Line-following Robot**: A high-speed tracking robot integrating IR sensors and a custom-tuned PID loop on Arduino.
2. **Smart Agricultural Node**: Remote ESP32-based node monitoring soil temperature/humidity and pushing low-power MQTT telemetry.
3. **Robo-Soccer Bot**: Dual-motor Bluetooth-controlled bot engineered for high agility and reinforced for combat.
4. **IoT Environmental Monitor**: Raspberry Pi climate tracking station visualized via Grafana dashboards.

---

## 💡 Contact API Configuration
To enable the production contact form, configure the environment variable `RESEND_API_KEY` on your deployment platform (e.g., Vercel environment variables). The contact API endpoint is located in `api/contact.js` and sends form data to `arpityadavarpit045@gmail.com`.
