# Bioinformatics & Multi-Omics Leader | 3D Interactive Portfolio

A premium, interactive 3D portfolio highlighting 10+ years of experience in Bioinformatics, Multi-Omics Data Science, Precision Oncology, Target Discovery, Knowledge Graphs, and AI-Augmented Pipelines (LLMs, RAG, Multi-Agent Systems). 

This portfolio features a scroll-driven 3D environment with a realistic moon texture that dynamically moves and shifts lighting as you navigate through the content.

## 🚀 Features

- **Lunar Elegance Theme:** Soft moonlight palette (`#A8C4D4`, `#D4A574`, `#0F1318`) with Outfit headings and warm gold accents.
- **Dynamic 3D Scroll Animations:** Uses `framer-motion-3d` to map scroll position directly to the 3D canvas. A moon model smoothly scales, translates across sections, and rotates as you scroll.
- **Interactive Timelines & Physics Cursors:** Includes a scroll-synced glowing beam in the experience timeline and a custom trailing cursor.
- **Precision Oncology & Multi-Omics Focus:** Showcases work in NGS pipelines, single-cell RNA-seq, spatial transcriptomics, target discovery, DepMap knowledge graphs, and biopharma technical delivery (Takeda, Genentech, Bugworks, Cleveland Clinic).

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
