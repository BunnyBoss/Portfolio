// All portfolio content from Poornachandra_G_Resume_v6.0

export const navLinks = [
  { id: "about", title: "About" },
  { id: "experience", title: "Experience" },
  { id: "tech", title: "Skills" },
  { id: "works", title: "Projects" },
  { id: "contact", title: "Contact" },
];

export const heroContent = {
  greeting: "Hi, I'm",
  name: "Poornachandra G.",
  tagline: "The scientist who thinks like an engineer and leads like a human.",
  description:
    "10+ years in bioinformatics, deep expertise in NGS secondary analysis, and a systems-builder mindset. I bring AI and biology together to build smarter workflows, turn complex science into scalable solutions, and help teams do their best work—with curiosity, collaboration, and a little fun along the way.",
};

export const aboutSummary =
  "Bioinformatics Scientist and AI Systems Developer with 10+ years of experience in precision oncology, clinical genomics, and production-grade NGS and multi-omics pipelines. Combines deep expertise in biomarker discovery, variant interpretation, and translational research with hands-on development of AI-powered applications, RAG pipelines, and multi-agent systems. Experienced in reproducible workflow engineering, machine learning, and systematic AI evaluation, with a focus on biological relevance, scientific validity, and reliable, traceable computational workflows.";

export const aboutCards = [
  {
    title: "Clinical NGS & Multi-Omics Pipelines",
    icon: "🧬",
    description:
      "Productionizing end-to-end WGS, WES, RNA-Seq, scRNA-Seq, and spatial omics pipelines with automated QC and turnaround time optimization.",
  },
  {
    title: "Clinical Variant Interpretation & Biomarkers",
    icon: "🎯",
    description:
      "Architecting variant annotation and prioritization (ACMG/AMP/ASCO/CAP), MSI, HRD, TMB, CNV, and phenotype-based rare disease gene prioritization.",
  },
  {
    title: "AI, LLMs & Agentic Systems",
    icon: "🤖",
    description:
      "Engineering multi-agent frameworks, RAG workflows, PEFT fine-tuning, and robust observability & evaluation (Promptfoo, DeepEval, Ragas).",
  },
  {
    title: "Bioinformatics Leadership & Delivery",
    icon: "🤝",
    description:
      "10+ years growing bioinformatics teams, technical roadmapping, regulatory compliance (HIPAA), and cross-functional biopharma delivery (Takeda, Genentech).",
  },
];

export const experiences = [
  {
    title: "Lead Scientist Bioinformatics",
    company_name: "Cellworks",
    icon: "🧬",
    iconBg: "#0F1318",
    date: "2024 – Present",
    points: [
      "Led the Bioinformatics R&D team: defined technical roadmap, recruited and mentored scientists, drove project prioritization, and aligned strategy with executive leadership.",
      "Partnered with executive leadership to align strategy and communicate progress, while providing team members with the broader context needed to execute effectively.",
      "Built multi-stage annotation and prioritization pipelines applying AMP/ASCO/CAP guidelines across public and proprietary annotation sources.",
      "Used AlphaGenome to identify candidate TERT promoter variants with potentially significant effects on gene expression and functional relevance in cancer.",
      "Designed and implemented input ingestion, monitoring, and reporting frameworks that reduced manual review time by 20%.",
      "Established risk management practices for bioinformatics pipelines — identified potential failure points, data-quality risks, and downstream repercussions, and implemented mitigation strategies.",
      "Designed structured upskilling sessions leveraging supplemental projects beyond core deliverables, improving engagement, critical thinking, and problem-solving across team members.",
      "Leveraged technical competitive intelligence and published methodologies to develop and benchmark an in-house bioinformatics pipeline inspired by Foundation Medicine (FM).",
    ],
  },
  {
    title: "Senior Scientist, Reporting Manager",
    company_name: "Cellworks",
    icon: "📊",
    iconBg: "#0F1318",
    date: "2021 – 2024",
    points: [
      "Developed comprehensive workflows for microsatellite instability (MSI), homologous recombination deficiency (HRD), mutational signatures, tumor mutational burden (TMB), and indel burden.",
      "Built high-throughput variant calling stacks on AWS following GATK best practices, including mutation and CNV calling, and biomarker extraction.",
      "Built and led the bioinformatics team: recruited, trained, mentored, and reviewed the work of team members; created custom training protocols that accelerated onboarding and competency development.",
      "Designed input-agnostic workflows supporting multiple formats (FASTQ, BAM, VCF, HDF5, structured reports) across diverse commercial vendors (4BC, Tempus, Caris, Foundation Medicine, Alacris) and research workflows.",
      "Built cancer driver and copy number variation (CNV) vs. mRNA expression correlation databases for 30+ cancer types using public datasets and computational tools.",
      "Developed automated multi-omics interpretation pipelines for high-impact clinical trial datasets from biopharma partners including Takeda and Genentech.",
      "Created an in-house Variant of Uncertain Significance (VUS) reclassification pipeline using an Ensembl-based approach, improving classification accuracy by >40%.",
      "Analyzed single-cell RNA-seq data from Human Protein Atlas normal-tissue samples with Seurat, Scanpy, and limma to establish in-silico control baselines for distinguishing cancer-specific expression signatures.",
    ],
  },
  {
    title: "Senior Scientist, Bioinformatics",
    company_name: "Cellworks",
    icon: "🔬",
    iconBg: "#0F1318",
    date: "2018 – 2021",
    points: [
      "Developed and benchmarked secondary analysis pipelines (Illumina DRAGEN, NVIDIA Parabricks, Sentieon), optimized for turnaround time, resource cost, and variant calling accuracy.",
      "Led custom panel design for liquid-biopsy samples; collaborated with Cleveland Clinic Florida to build a machine learning pipeline using longitudinal genomic data to predict early relapse in Melanoma.",
      "Built an analytical framework to process pediatric cancer cases; served as primary domain owner for pediatric hematological malignancies.",
      "Designed and implemented a Panel of Normals (PoN) workflow for CNV and mutation calling, improving support for tumor-only clinical analyses.",
      "Created multiple tertiary analysis workflows (GSEA, pathway enrichment, PCA, statistical models, ML pipelines) for biomarker discovery and treatment-response characterization.",
      "Developed multi-omics interpretation pipelines for the Foundation Medicine clinical genomic dataset (18,000+ patient cases).",
      "Compiled a comprehensive diagnostic assay and genomic test inventory across 88 cancer types based on NCCN, FDA, and international clinical guidelines.",
    ],
  },
  {
    title: "Scientist, Clinical Translation",
    company_name: "Cellworks",
    icon: "⚗️",
    iconBg: "#0F1318",
    date: "2017 – 2018",
    points: [
      "Curated therapeutic rationale libraries to support computational biology predictions, reducing turnaround time for live clinical case analyses by >40%.",
      "Analyzed 200+ complex cancer cases, gaining deep expertise in target selection using biological network models and drug interaction mechanisms in precision oncology.",
      "Conducted rigorous benchmarking of external sequencing pipelines (DNAnexus, BeOne, MedGenome) to establish analytical validity, confidence, and cross-platform reproducibility.",
      "Developed an in-house somatic variant annotation and filtering pipeline with custom tier classification, eliminating recurring external software fees and improving clinical interpretability.",
    ],
  },
  {
    title: "Associate Scientist",
    company_name: "Cellworks",
    icon: "🧪",
    iconBg: "#0F1318",
    date: "2015 – 2017",
    points: [
      "Processed, interpreted, and harmonized multi-omics outputs (karyotyping, aCGH, IHC, somatic variants) for >500 cases, translating insights into automated data-harmonization ETL pipelines.",
      "Curated and automated retrospective in-house dataset creation by integrating patient and cell-line data for >10,000 cases from various sources like COSMIC, TCGA, cBioportal, GEO, SRA and published clinical studies.",
      "Standardized genomic data interpretation from external medical partners including Columbia University, University of Florida, Cedars-Sinai, Mayo Clinic, and Washington University.",
      "Automated report-generation workflows using reproducible pipelines and templates, reducing preparation time from ~15 hours to just minutes per week.",
    ],
  },
];

export const technologies = [
  { name: "Python", icon: "🐍" },
  { name: "Nextflow", icon: "🔄" },
  { name: "GATK / DRAGEN", icon: "🧬" },
  { name: "LangChain / Graph", icon: "🦜" },
  { name: "Multi-Agent Systems", icon: "🤖" },
  { name: "PyTorch / ML", icon: "🔥" },
  { name: "R / Bioconductor", icon: "📊" },
  { name: "AWS HealthOmics", icon: "🌩️" },
  { name: "Docker", icon: "🐳" },
  { name: "Promptfoo / Evals", icon: "🧪" },
  { name: "Seurat / Scanpy", icon: "🔬" },
  { name: "cBioPortal / TCGA", icon: "🗄️" },
  { name: "AlphaGenome", icon: "🧬" },
  { name: "Streamlit / Plotly", icon: "📈" },
  { name: "Git / CI/CD", icon: "🌿" },
  { name: "Claude Code / Cursor", icon: "⚡" },
];

export const projects = [
  {
    name: "Portal Intelligence",
    description:
      "Enterprise multi-agent orchestration workflow for vendor order management, coordinating specialized agents, external tools, and contextual memory with human-in-the-loop validation. Implemented golden evaluation datasets with DeepEval and LangSmith for hallucination reduction and retrieval quality benchmarking.",
    tags: [
      { name: "LangGraph", color: "green-text-gradient" },
      { name: "Multi-Agent", color: "amber-text-gradient" },
      { name: "DeepEval", color: "blue-text-gradient" },
      { name: "RBAC", color: "pink-text-gradient" },
    ],
    icon: "🤖",
    source_code_link: "https://github.com/",
  },
  {
    name: "Phenotype-Driven Rare Disease Pipeline",
    description:
      "End-to-end tertiary analysis pipeline for phenotype-based gene prioritization, variant selection, and clinical reporting in rare genetic disorders. Awarded Top Rank at Bangalore Tech Summit 2025 as an independent researcher.",
    tags: [
      { name: "Rare Disease", color: "green-text-gradient" },
      { name: "HPO", color: "amber-text-gradient" },
      { name: "ACMG", color: "blue-text-gradient" },
      { name: "BTS Top Rank", color: "pink-text-gradient" },
    ],
    icon: "🧬",
    source_code_link: "https://github.com/",
  },
  {
    name: "JobAIder",
    description:
      "AI-driven career platform integrating resume and Obsidian vault parsing, job description analysis, profile-to-role gap assessment, personalized upskilling plans, ATS-optimized resume generation, and role-specific mock interviews.",
    tags: [
      { name: "Agentic AI", color: "green-text-gradient" },
      { name: "Resume Parser", color: "amber-text-gradient" },
      { name: "ATS Optimization", color: "blue-text-gradient" },
      { name: "Mock Interview", color: "pink-text-gradient" },
    ],
    icon: "💼",
    source_code_link: "https://github.com/",
  },
  {
    name: "HealthForge",
    description:
      "AI-powered personalized health planning platform combining health profile ingestion, context-aware LLM interactions, tailored wellness plan generation, and WhatsApp automated reminders into an end-to-end application.",
    tags: [
      { name: "LLM API", color: "green-text-gradient" },
      { name: "Context Management", color: "amber-text-gradient" },
      { name: "Full-Stack", color: "blue-text-gradient" },
      { name: "Automation", color: "pink-text-gradient" },
    ],
    icon: "🏥",
    source_code_link: "https://github.com/",
  },
];

export const honorsAndAwards = [
  {
    title: "Bangalore Tech Summit 2025 Top Rank (Independent Research)",
    year: "2025",
    description:
      "Awarded Top Rank at Bangalore Tech Summit 2025 as an independent researcher for architecting a phenotype-based gene prioritization and tertiary analysis pipeline for rare disease diagnostics.",
  },
];

export const publications = [
  {
    year: "Co-Author",
    title:
      "9 peer-reviewed oncology publications and conference abstracts in J Neurooncol, J Clin Oncol, and Blood/ASCO",
    journal:
      "Computational biomarker modeling, AML/MDS biosimulation, and therapy-response modeling (ORCID: 0009-0009-1610-1205)",
  },
];

export const education = {
  degree: "B.Tech in Biotechnology",
  institution: "JNTUA College of Engineering Pulivendula (JNTUA CEP)",
  year: "2015",
};

export const contactInfo = {
  email: "poornachandra.gedi@gmail.com",
  phone: "+91-7899 419758",
  linkedin: "https://linkedin.com/in/poornachandra-g",
  orcid: "https://orcid.org/0009-0009-1610-1205",
  location: "Bengaluru, India",
};
