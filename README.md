# Poornachandra G. | Lead Bioinformatics Scientist

**Precision Oncology • NGS Architecture & Agentic AI Systems**

Welcome to my professional portfolio repository. This website showcases my **10+ years of experience** in bioinformatics, precision medicine, and clinical genomics, combined with expertise in building **agentic AI systems** and full-stack applications. It highlights my journey from an Associate Scientist to a Lead Bioinformatics Scientist, along with my independent AI projects, key research publications, and innovative technology stack.

## 🔗 [Live Portfolio Website](https://bunnyboss.github.io/Portifolio/)

---

## 📂 Portfolio Overview

This portfolio is organized into the following sections:

### 1. **Professional Summary**
A snapshot of my background in building end-to-end NGS pipelines, architecting variant annotation workflows, and leading bioinformatics R&D teams.

### 2. **Experience Timeline**
A detailed career journey through my roles at **Cellworks**:
- **Lead Bioinformatician (2024–Present)**: Leading Bioinformatics R&D, defining technical roadmap, recruiting and mentoring scientists, and driving project prioritization.
- **Senior Scientist, Reporting Manager (2021–2024)**: Developed workflows for MSI, HRD, TMB; built high-throughput variant calling stacks on AWS; led team of 4 scientists.
- **Senior Scientist, Bioinformatics (2018–2021)**: Benchmarked secondary analysis pipelines (DRAGEN, Parabricks, Sentieon); designed liquid-biopsy panels; managed Panel of Normals workflow.
- **Scientist, Clinical Translation (2017–2018)**: Curated rationale libraries; analyzed 200+ cancer cases; benchmarked sequencing pipelines.
- **Associate Scientist (2015–2017)**: Harmonized multi-omics data for >500 cases; automated ETL pipelines; standardized data interpretation from multiple partners.

### 3. **Skills and Technologies**
My technical expertise spans 10 distinct categories:
- **NGS & Clinical-omics**: WGS, WES, TES, RNA-Seq, scRNA-Seq, Variant Interpretation (ACMG/AMP/ASCO/CAP), MSI, HRD, TMB, CNV, SV.
- **Bioinformatics & Pipeline Engineering**: GATK, Sentieon, DRAGEN, NVIDIA Parabricks, DeepVariant, Nextflow, Kallisto, Salmon, DESeq2, Seurat, Scanpy, GSEA.
- **Machine Learning & AI**: Supervised/Unsupervised Learning, Feature Engineering, LightGBM, XGBoost, PyTorch, TensorFlow, scikit-learn, AutoML, PySpark, SHAP.
- **LLMs & Agentic Systems**: LangChain, LangGraph, Multi-Agent Systems, RAG Pipelines, Fine-Tuning, Quantization, LoRA/QLoRA, OpenAI/Anthropic/Gemini APIs, MCP, W&B.
- **NLP, OCR & Document AI**: Hugging Face Transformers, LayoutLMv3, BioBERT, scispaCy, Tesseract, EasyOCR, PyMuPDF, Docling, OpenCV.
- **Programming & Engineering**: Python, Bash, R, FastAPI, SQLite, REST APIs, Uvicorn, Git, CI/CD.
- **Cloud, Platforms & Infrastructure**: AWS (EC2, S3, Batch, HealthOmics), DNAnexus, BaseSpace, Galaxy, Terra/FireCloud, Docker, Conda/Mamba, Jupyter, HPC, MLOps.
- **Visualization & UI**: Streamlit, Gradio, Plotly, Matplotlib, Seaborn.
- **GenAI Developer Tools**: Claude Code, GitHub Copilot, Cursor, Windsurf, Continue, Cline, Aider, Goose.
- **Leadership & Delivery**: Team Building, Hiring, Mentoring, Technical Roadmapping, HIPAA Compliance, Agile, Scrum, Risk Management, JIRA.

### 4. **AI Projects & Innovations**
I have independently developed production-ready AI and clinical genomics engineering projects:

**Clinical & Bioinformatics AI:**
- **VarEffex**: Multi-agent framework that autonomously searches biomedical literature to extract variant-function associations, functional impacts, and biomarker evidence under ACMG/AMP criteria.
- **PathoParse**: LLM-assisted and rule-based pipelines extracting structured clinical metadata and biomarker stages from unstructured pathology and histology reports.
- **SQL Chat**: Multi-agent Streamlit application translating natural language clinical queries to SQL with automated statistical testing and interpretable summaries.
- **Phenotype-Driven Rare Disease Prioritization Pipeline**: End-to-end tertiary analysis pipeline for phenotype-based gene prioritization, variant selection, and clinical reporting in rare genetic disorders. Awarded Top Rank at Bangalore Tech Summit (BTS 2025).

### 5. **Publications**
A collection of **10+ research contributions** in peer-reviewed journals and conference abstracts (2018–2022):
- **2022**: Impact of mismatch repair deficiency on survival in glioblastoma (Neuro-Oncology)
- **2021**: Combination chemotherapy vs. temozolomide predictions; CBM-based biomarker identification in AML; therapy response assessment (Journal of Neuro-Oncology, Blood, JCO)
- **2020**: Superior LGG therapy predictions; ATO/ATRA resistance prediction in APL patients (JCO, Blood)
- **2018**: MDS/AML clonal analysis; azacitidine response prediction (Blood)

Complete publication list available on [ORCID](https://orcid.org/0009-0009-1610-1205).

---

## 🚀 Job Application Engine & Workflow

This repository serves as the **single source of truth and end-to-end automation toolkit** for job applications, structured across 4 modular steps:

```text
[1. Master Profile] ──> [2. JD & Company Analysis] ──> [3. Resume Tailoring & PDF] ──> [4. Vercel Branch Deployment]
(data/master_profile)     (scripts/analyze_jd.py)        (scripts/tailor_resume.py)      (scripts/deploy_branch.py)
```

### 1. Section-Agnostic Master Profile Table (`data/`)
- [master_table.tsv](data/master_table.tsv): The foundational Single Source of Truth (SSOT). Captures all 60+ career records in a standardized, section-agnostic tabular schema:
  - `id`: Unique slug identifier
  - `title`: Initiative or project name
  - `description`: Technical narrative detailing accomplishments, scope, and methodologies
  - `technologies`: Semicolon-delimited tools, frameworks, and libraries
  - `start_date` / `end_date`: Timeline
  - `organization`: Company, partner, or institution (`Cellworks`, `Cleveland Clinic Florida`, `Independent`, `JNTUA CEP`)
  - `engagement_type`: Relationship context (`Corporate`, `Strategic Collaboration`, `Independent R&D`, `Academic`, `Honor`)
  - `domain_tags`: Semicolon-delimited query tags (`bioinformatics`, `ai`, `leadership`, `clinical`, `pipeline`)
  - `impact`: Quantified outcome, performance metric, or milestone
- [compile_master.py](scripts/compile_master.py): Pandas-based compiler that validates the table and compiles it into:
  - [master_profile.json](data/master_profile.json): Machine-readable catalog with parsed skills inventory and tag index for downstream automation.
  - [master_profile.md](data/master_profile.md): Comprehensive Markdown career dossier for human reading.

### 2. JD & Company Decomposition (`scripts/analyze_jd.py`)
- Analyzes JD text/file against your master profile.
- Detects role archetype (`Bioinformatics Lead`, `Agentic AI Engineer`, `AI Program Lead`, `Multi-Omics Leader`).
- Identifies matching skills, potential gaps, and ranks the most relevant portfolio projects.
- Saves structured reports in `applications/<company>-<role>/`.

### 3. Tailored Resume Refinement (`scripts/tailor_resume.py`)
- Automatically generates ATS-optimized [resume.md](applications/) aligning summaries, selected highlights, and skills matrix with the JD.
- Compiles high-resolution, print-ready PDF using `WeasyPrint` via [generate_pdf.py](scripts/generate_pdf.py).
- Stages documents into `docs/assets/documents/` and `assets/documents/`.

### 4. Branch-Based Vercel Portfolio Deployment (`scripts/deploy_branch.py`)
- Customizes [docs/index.html](docs/index.html) with target company badge, subtitle, and direct link to that version's tailored PDF.
- Creates dedicated Git branch: `apply/<company_slug>-<role_slug>`.
- Deploys static site via Vercel ([vercel.json](vercel.json)) by pushing to GitHub (`git push -u origin apply/<branch>`), triggering an isolated Vercel preview URL (e.g. `https://portfolio-git-apply-<company>-<role>-bunnyboss.vercel.app`).

---

### 💻 Unified CLI Usage (`apply.py`)

Run the complete pipeline end-to-end or step-by-step:

```bash
# 1. Run all 4 steps in one command (Analyze -> Tailor Resume & PDF -> Create Branch & Customize Site):
python apply.py all --company "Genentech" --role "Lead Bioinformatics Scientist" --jd path/to/jd.txt --push

# 2. Or run individual steps:
# Step 2: Analyze JD & Company context
python apply.py analyze --company "Anthropic" --role "AI Systems Engineer" --jd path/to/jd.txt

# Step 3: Refine tailored Markdown & PDF resume
python apply.py tailor --company "Anthropic" --role "AI Systems Engineer"

# Step 4: Create branch, customize portfolio, and trigger Vercel deployment
python apply.py branch --company "Anthropic" --role "AI Systems Engineer" --push
```

---

## 🛠️ Repository Structure & Local Development

This repository follows a clean, modular architecture separating the public portfolio website from Python tooling and research assets:

```text
Portfolio/
├── apply.py                        # Master CLI for the 4-step application engine
├── vercel.json                     # Vercel static deployment configuration
├── data/
│   ├── master_profile.json         # Single source of truth (Skills, Projects, Experience, Pubs)
│   └── master_profile.md           # Markdown master profile reference
├── scripts/
│   ├── analyze_jd.py               # Step 2: JD & company context decomposition
│   ├── tailor_resume.py            # Step 3: ATS-tailored resume generation
│   ├── generate_pdf.py             # WeasyPrint PDF compilation
│   └── deploy_branch.py            # Step 4: Branch creation & Vercel deployment
├── applications/                   # Generated tailored resumes, analyses & PDFs per application
├── docs/                           # Static portfolio website (Vercel & GitHub Pages)
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/documents/
├── assets/                         # Company research & document backups
├── Versions/                       # Historical resume drafts
└── requirements.txt                # Python environment dependencies
```

### Setup & PDF Generation

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Generate updated resume PDF:**
   ```bash
   python3 scripts/generate_pdf.py
   ```
   *Generates styled PDFs in both `assets/documents/` and `docs/assets/documents/`.*

---

## 📬 Contact Information

I am always open to discussing new opportunities, collaborations, or connecting with fellow professionals in the field.

- **Email**: [poornachandra.gedi@gmail.com](mailto:poornachandra.gedi@gmail.com)
- **LinkedIn**: [linkedin.com/in/poornachandra-g](https://linkedin.com/in/poornachandra-g)
- **ORCID**: [0009-0009-1610-1205](https://orcid.org/0009-0009-1610-1205)

---

> *This portfolio showcases my evolution from precision medicine to agentic AI systems, demonstrating end-to-end technical leadership and product ownership across clinical bioinformatics and modern AI engineering.*
