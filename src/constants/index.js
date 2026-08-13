// All portfolio content from Poornachandra_G_Resume_v5.0.txt

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
  tagline: "Bioinformatics & Multi-Omics Leader | Precision Oncology | AI-Augmented Data Science",
  description:
    "10+ years leading multi-omics R&D and biopharma technical delivery — integrating multi-omics, human genetics, knowledge graphs, and GenAI/RAG pipelines for target discovery and precision oncology.",
};

export const aboutSummary =
  "Bioinformatics and multi-omics leader with 10+ years in precision oncology, leading scientists and owning technical delivery across R&D, clinical, and biopharma collaborations, including Takeda, Genentech, Cleveland Clinic Florida and Bugworks. Translates complex biomedical data into decision-ready insights by integrating multi-omics with clinical, literature, and genetic evidence for target discovery and mechanism-of-action validation. Brings hands-on experience applying knowledge graphs to CRISPR-screen, drug-screen, and DepMap data, alongside LLM and RAG pipelines (LangChain, Azure AI Foundry) for literature mining and evidence integration.";

export const aboutCards = [
  {
    title: "Multi-Omics & Clinical Genomics",
    icon: "🧬",
    description:
      "Integrating WGS/WES/RNA-seq, single-cell, spatial transcriptomics, liquid biopsy, deconvolution, and biomarkers (MSI, HRD, TMB) for precision medicine.",
  },
  {
    title: "Target Discovery & Human Genetics",
    icon: "🎯",
    description:
      "Computational target prioritization, synthetic lethality, DepMap, CRISPR/drug-screen analytics, and NetworkX/Neo4j/PyG knowledge graphs.",
  },
  {
    title: "AI, RAG & Literature Mining",
    icon: "🤖",
    description:
      "Building biomedical LLM and RAG pipelines (LangChain, Azure AI Foundry), evaluation harnesses (Promptfoo, DeepEval), and knowledge graph extraction.",
  },
  {
    title: "Scientific Delivery & Leadership",
    icon: "🤝",
    description:
      "Technical roadmapping, team building, and leading cross-functional collaborations with biopharma partners (Takeda, Genentech, Bugworks, Cleveland Clinic).",
  },
];

export const experiences = [
  {
    title: "Lead Clinical Translation",
    company_name: "Cellworks",
    icon: "🧬",
    iconBg: "#0F1318",
    date: "2024 – Present",
    points: [
      "Own technical delivery of multi-omics and clinical-genomics programs for precision oncology, translating NGS, variant, and clinical evidence into decision-ready insights for pharma, clinical, and internal R&D stakeholders.",
      "Served as technical and data advisor for a target-indication assessment with Bugworks, leading computational analysis of TCGA and cell-line omics profiles alongside drug-resistance perturbation data, including resistant-cell-line sequencing and gene-knockdown screens, to develop an evidence-linked candidate target list and validate compound mechanisms of action.",
      "Lead the bioinformatics team's technical roadmap across R&D and clinical workstreams; recruit and mentor scientists, set delivery priorities, and align resources against concurrent partner commitments.",
      "Built and deployed LLM-powered RAG pipelines using LangChain and Azure AI Foundry to mine biomedical literature, retrieve relevant evidence, and construct biological networks.",
      "Designed analytical validation studies for a multi-omics predictive-response program in NSCLC, establishing acceptance criteria, validation protocols, and quality checkpoints for immunotherapy decision support.",
      "Established risk-management and quality practices for bioinformatics pipelines, identifying data-quality failure points and implementing mitigation strategies before downstream delivery.",
      "Designed AI evaluation pipelines with Promptfoo and DeepEval, using golden datasets to assess retrieval accuracy and reduce hallucination in GenAI-assisted biomedical workflows.",
    ],
  },
  {
    title: "Senior Scientist, Reporting Manager",
    company_name: "Cellworks",
    icon: "📊",
    iconBg: "#0F1318",
    date: "2021 – 2024",
    points: [
      "Built and led a bioinformatics team, owning recruitment, onboarding, mentoring, technical review, and day-to-day delivery of multi-omics interpretation work.",
      "Partnered directly with Takeda and Genentech stakeholders to deliver interpretation pipelines for clinical-trial datasets, translating genomic evidence into actionable therapy-response insights.",
      "Created input-agnostic workflows across FASTQ, BAM, and VCF formats and vendor data from 4BaseCare, Tempus, Caris, Foundation Medicine, and Alacris, aligning pipeline compatibility and data standards with external bioinformatics teams.",
      "Built cancer-driver and CNV-mRNA knowledge bases spanning 30+ cancer types from public multi-omics datasets, supporting evidence integration for target and biomarker assessment.",
      "Developed an Ensembl-based VUS reclassification pipeline that improved variant-classification accuracy by more than 40%, strengthening the genetic evidence available for clinical interpretation.",
      "Analyzed single-cell RNA-seq data from Human Protein Atlas normal-tissue samples with Seurat, Scanpy, and limma to establish in-silico control baselines for distinguishing cancer-specific expression signatures.",
      "Applied CIBERSORTx and MuSiC bulk RNA-seq deconvolution to resolve cancer-specific markers within heterogeneous tumor samples and improve multi-omics interpretation.",
      "Developed workflows for MSI, HRD, mutation signatures, TMB, and indel burden, connecting clinically relevant biomarkers to precision-oncology target and therapy decisions.",
    ],
  },
  {
    title: "Senior Scientist, Clinical Translation",
    company_name: "Cellworks",
    icon: "🔬",
    iconBg: "#0F1318",
    date: "2018 – 2021",
    points: [
      "Built ETL pipelines for DepMap multi-omics, CRISPR-screen, and drug-screen data, then applied knowledge-graph analytics and graph-based machine learning using NetworkX and PyTorch Geometric to identify essential genes and synthetic-lethal relationships.",
      "Led multi-omics analyses for MDS, AML, and MPN clinical studies to identify disease drivers, treatment-resistance and sensitivity biomarkers, progression signatures, and standard-of-care response predictors.",
      "Designed a custom liquid-biopsy panel and collaborated with Cleveland Clinic Florida stakeholders to develop an ML pipeline on longitudinal genomic data predicting early melanoma relapse.",
      "Developed multi-omics interpretation pipelines for 18,000+ Foundation Medicine cases, translating large-scale genomic data into structured clinical insights.",
      "Developed and benchmarked secondary-analysis pipelines using Illumina DRAGEN, NVIDIA Parabricks, and Sentieon, improving confidence in accuracy and turnaround-time performance.",
      "Compiled an inventory of NCCN-recommended and FDA-approved assays and tests spanning 88 cancer types to support clinical-genomics interpretation and downstream decision workflows.",
    ],
  },
  {
    title: "Scientist, Clinical Translation",
    company_name: "Cellworks",
    icon: "⚗️",
    iconBg: "#0F1318",
    date: "2017 – 2018",
    points: [
      "Curated evidence and rationale libraries for therapy-prediction workflows, reducing turnaround time for live oncology case analyses by more than 40%.",
      "Analyzed 200+ oncology cases, applying cancer and drug-interaction networks to support target selection and therapy-response interpretation.",
      "Benchmarked sequencing pipelines across DNAnexus and MedGenome to establish reproducibility and confidence in clinical-genomics outputs.",
      "Developed variant annotation, classification and filtering framework to automate prioritization and standardize decision support according to ACMG guidelines.",
      "Acted as a technical bridge between engineering R&D and core development teams, accelerating product delivery through rapid prototyping and the automation of scalable data processing pipelines.",
    ],
  },
  {
    title: "Associate Scientist",
    company_name: "Cellworks",
    icon: "🧪",
    iconBg: "#0F1318",
    date: "2015 – 2017",
    points: [
      "Harmonized karyotyping, aCGH, IHC, and mutation outputs for 500+ cases through automated ETL and data-harmonization pipelines, creating a consistent foundation for multi-omics analysis.",
      "Standardized genomic-data interpretation with academic collaborators at Columbia University, University of Florida, Cedars-Sinai, Mayo Clinic, Washington University, and MMRF-Michigan.",
      "Automated report-generation workflows that reduced preparation time from approximately 15 hours to minutes per week, accelerating delivery of stakeholder-ready clinical reports.",
    ],
  },
];

export const technologies = [
  { name: "Python", icon: "🐍" },
  { name: "R", icon: "📊" },
  { name: "LangChain", icon: "🦜" },
  { name: "Azure AI", icon: "☁️" },
  { name: "PyTorch (PyG)", icon: "🔥" },
  { name: "Nextflow", icon: "🔄" },
  { name: "DRAGEN / GATK", icon: "🧬" },
  { name: "Neo4j / NetworkX", icon: "🕸️" },
  { name: "Seurat / Scanpy", icon: "🔬" },
  { name: "Promptfoo / DeepEval", icon: "🧪" },
  { name: "AWS", icon: "🌩️" },
  { name: "Docker", icon: "🐳" },
  { name: "SQL", icon: "🗄️" },
  { name: "Databricks", icon: "🧱" },
  { name: "Git", icon: "🌿" },
];

export const projects = [
  {
    name: "VarEffex",
    description:
      "Multi-agent scientific literature-mining framework that extracts variant–function associations and links biomedical evidence to variant interpretation and computational target discovery.",
    tags: [
      { name: "Multi-Agent", color: "green-text-gradient" },
      { name: "Literature Mining", color: "amber-text-gradient" },
      { name: "Target Discovery", color: "blue-text-gradient" },
    ],
    icon: "🧬",
    source_code_link: "https://github.com/",
  },
  {
    name: "PathoParse",
    description:
      "LLM-assisted and rule-based pipelines to convert unstructured pathology reports into structured clinical metadata, supporting downstream biomedical data analysis and evidence integration.",
    tags: [
      { name: "LLMs / RAG", color: "green-text-gradient" },
      { name: "Pathology NLP", color: "amber-text-gradient" },
      { name: "Clinical Metadata", color: "blue-text-gradient" },
    ],
    icon: "📄",
    source_code_link: "https://github.com/",
  },
  {
    name: "SQLChat",
    description:
      "Multi-agent clinical data interface that translates natural-language questions into SQL, performs statistical checks, and returns interpretable summaries for research and stakeholder decision-making.",
    tags: [
      { name: "Multi-Agent", color: "green-text-gradient" },
      { name: "NL2SQL", color: "amber-text-gradient" },
      { name: "Clinical Data", color: "blue-text-gradient" },
    ],
    icon: "🗃️",
    source_code_link: "https://github.com/",
  },
];

export const publications = [
  {
    year: "Co-Author",
    title: "9 peer-reviewed oncology publications and conference abstracts in J Neurooncol, J Clin Oncol, and Blood/ASCO",
    journal: "Computational biomarker modeling, AML/MDS biosimulation, and therapy-response modeling (ORCID: 0009-0009-1610-1205)",
  },
];

export const contactInfo = {
  email: "poornachandra.gedi@gmail.com",
  phone: "+91-7899 419758",
  linkedin: "https://linkedin.com/in/poornachandra-g",
  orcid: "https://orcid.org/0009-0009-1610-1205",
  location: "Bengaluru, India",
};

