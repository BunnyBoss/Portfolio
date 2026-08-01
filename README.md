# Agentic AI Engineer Portfolio

A premium, highly interactive 3D portfolio designed to showcase projects and experience in Agentic AI, Multi-Agent Systems, RAG architecture, and Machine Learning. 

This portfolio breaks away from standard web templates by integrating a persistent, scroll-driven 3D environment featuring a hyper-realistic moon that dynamically changes phases as you explore the content.

## 🚀 Features

- **Dynamic 3D Scroll Animations:** Uses `framer-motion-3d` to map the user's scroll position directly to the 3D canvas. A high-resolution moon smoothly scales, translates across sections, and rotates as you scroll.
- **Procedural Lighting (Moon Phases):** As you reach the bottom of the page, the directional lighting dynamically orbits the moon, plunging the craters into shadow and creating a razor-thin, realistic crescent moon.
- **Cyberpunk / Deep Space Aesthetic:** A stark monochrome black/grey palette (`#030303`, `#111111`) accented with glowing neon cyan (`#00e5ff`) drop-shadows and rim lights.
- **Interactive Timelines & Physics Cursors:** Includes a scroll-synced glowing laser beam in the experience timeline and a custom physics-based trailing cursor.
- **Procedural AI Background:** A Three.js neural network visualization representing AI/ML engineering expertise.

## 🛠️ Technology Stack

- **Framework:** React 18 + Vite
- **3D Graphics:** Three.js, `@react-three/fiber`, `@react-three/drei`
- **Animations:** Framer Motion, `framer-motion-3d`, React Vertical Timeline
- **Styling:** TailwindCSS
- **Deployment:** Vercel / GitHub Pages ready

## 💻 Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Portfolio
   ```

2. **Install dependencies:**
   ```bash
   npm install --legacy-peer-deps
   ```
   *(Note: `--legacy-peer-deps` is required due to standard versioning strictness between `@react-three/fiber` and `framer-motion-3d`)*

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Build for production:**
   ```bash
   npm run build
   ```

## 📄 License
MIT License
