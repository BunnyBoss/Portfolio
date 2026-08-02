// All portfolio content from Poornachandra_G_Resume_v2.txt

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
  tagline: "Agentic AI Engineer",
  description:
    "I build enterprise GenAI applications — multi-agent systems, RAG pipelines, and LLM-powered solutions using LangChain, LangGraph, Azure AI Foundry, and more.",
};

export const aboutCards = [
  {
    title: "Multi-Agent Orchestration",
    icon: "🤖",
    description:
      "Designing complex workflows coordinating specialized agents, external tools, and contextual memory with human-in-the-loop validation.",
  },
  {
    title: "RAG & Retrieval Architect",
    icon: "🔍",
    description:
      "Building enterprise retrieval pipelines with vector stores, semantic search, optimized chunking, and golden dataset validation.",
  },
  {
    title: "GenAI Evaluation & QA",
    icon: "🎯",
    description:
      "Deploying automated CI/CD evaluation pipelines leveraging Promptfoo, DeepEval, and LLM-as-a-Judge to reduce defects by 30%.",
  },
  {
    title: "Responsible AI Governance",
    icon: "🛡️",
    description:
      "Establishing security, privacy, and red-team checkpoints for HIPAA-compliant, enterprise-ready GenAI deployments.",
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
      "Designed multi-agent orchestration workflows for vendor order management, coordinating specialized agents, external tools, and contextual memory with human-in-the-loop validation at critical decision points.",
      "Built enterprise RAG pipelines with LangChain and Azure AI Search, deploying them on Azure AI Foundry to automate knowledge discovery across biomedical literature and proprietary knowledge bases.",
      "Assessed vector store solutions (Chroma, Pinecone, Qdrant) for RAG retrieval, tuning chunking strategy and embedding configuration to improve retrieval precision and reduce hallucination rates.",
      "Created prompt libraries and AI evaluation pipelines with Promptfoo and DeepEval, integrating version-controlled prompts and benchmarks into CI/CD to validate retrieval accuracy, consistency, hallucination, and regression before release.",
      "Developed golden datasets and benchmark queries to continuously evaluate retrieval quality and response accuracy, reducing post-deployment defects by 30%.",
      "Established responsible AI governance, security, and privacy checkpoints, including red-team testing and release gates, to guarantee safe and production-ready GenAI deployments.",
      "Led AI enablement programs and mentored engineers on agentic AI, prompt engineering, GenAI solutions, and evaluation best practices, driving org-wide GenAI adoption.",
    ],
  },
  {
    title: "Senior Scientist, Reporting Manager",
    company_name: "Cellworks",
    icon: "📊",
    iconBg: "#0F1318",
    date: "2021 – 2024",
    points: [
      "Drove early adoption of LLM-assisted, RAG-based workflows for oncology therapy recommendations, integrating prompt engineering, knowledge indexing, and structured output evaluation.",
      "Designed an in-house ensemble-based ML variant reclassification pipeline, improving classification accuracy by 40%+; established reproducible ML workflows with MLflow for experiment tracking and model versioning.",
      "Built cloud-native data platforms on AWS and Databricks, engineering scalable ETL pipelines that feed ML and GenAI workloads.",
      "Built and led a technical team that conducted competitive technical analysis of market-leading healthcare AI/ML platforms while establishing core engineering standards.",
      "Delivered reusable documentation, SOPs, and training modules to standardize process adoption across teams.",
    ],
  },
  {
    title: "Senior Scientist, Clinical Translation",
    company_name: "Cellworks",
    icon: "🔬",
    iconBg: "#0F1318",
    date: "2018 – 2021",
    points: [
      "Built a machine learning pipeline using longitudinal time-series data to predict early disease relapse, applying feature engineering and model validation methodology.",
      "Developed and benchmarked high-throughput data processing pipelines, applying structured accuracy, performance, and reproducibility evaluation methodology across pipeline versions.",
      "Created a validation framework for an edge-clinical case category, defining acceptance criteria, structured quality checkpoints, and classification guidelines.",
      "Built graph analytics pipelines with NetworkX to pinpoint influential nodes and derive network-based insights for data-driven decision making.",
    ],
  },
  {
    title: "Scientist, Clinical Translation",
    company_name: "Cellworks",
    icon: "⚗️",
    iconBg: "#0F1318",
    date: "2017 – 2018",
    points: [
      "Engineered a Python rule-based variant classification framework to automate prioritization and standardize decision support.",
      "Developed an in-house variant annotation and filtering engine (Python, SQL), automating workflows and enabling downstream analytics.",
      "Implemented automated unit and integration tests with Pytest, increasing code reliability and enabling consistent validation of software releases through CI/CD.",
    ],
  },
  {
    title: "Associate Scientist",
    company_name: "Cellworks",
    icon: "🧪",
    iconBg: "#0F1318",
    date: "2015 – 2017",
    points: [
      "Automated report generation and ETL workflows using Python and SQL, reducing weekly processing time from ~15 hours to minutes.",
      "Standardized and automated large-scale data harmonization and ETL workflows across 500+ clinical cases and 10,000+ external records.",
      "Coordinated data standardization initiatives for data from multiple external partner institutions.",
    ],
  },
];

export const technologies = [
  { name: "Python", icon: "🐍" },
  { name: "LangChain", icon: "🦜" },
  { name: "PyTorch", icon: "🔥" },
  { name: "Azure", icon: "☁️" },
  { name: "AWS", icon: "🌩️" },
  { name: "Docker", icon: "🐳" },
  { name: "SQL", icon: "🗄️" },
  { name: "FastAPI", icon: "⚡" },
  { name: "MLflow", icon: "📈" },
  { name: "Neo4j", icon: "🕸️" },
  { name: "Anthropic", icon: "🧠" },
  { name: "OpenAI", icon: "🤖" },
  { name: "Promptfoo", icon: "🧪" },
  { name: "Git", icon: "🌿" },
  { name: "Databricks", icon: "🧱" },
  { name: "Cursor", icon: "🖱️" },
];

export const projects = [
  {
    name: "Inferverse",
    description:
      "Unified interface for discovery, categorization, proxy configuration, and benchmarking of open generative AI APIs (NVIDIA NIM, Mistral, Groq, OpenRouter, Ollama, PublicAI).",
    tags: [
      { name: "LiteLLM", color: "green-text-gradient" },
      { name: "Benchmarking", color: "amber-text-gradient" },
      { name: "Multi-Provider", color: "blue-text-gradient" },
    ],
    icon: "⚡",
    source_code_link: "https://github.com/",
  },
  {
    name: "PathoParse",
    description:
      "LLM-assisted and rule-based pipelines to extract structured clinical metadata from unstructured pathology reports with validation logic.",
    tags: [
      { name: "Document AI", color: "green-text-gradient" },
      { name: "Pathology", color: "amber-text-gradient" },
      { name: "Validation", color: "blue-text-gradient" },
    ],
    icon: "📄",
    source_code_link: "https://github.com/",
  },
  {
    name: "SQL Chat",
    description:
      "CrewAI multi-agent system translating natural-language queries into SQL, running statistical validation checks, and producing stakeholder-ready summaries.",
    tags: [
      { name: "Multi-Agent", color: "green-text-gradient" },
      { name: "CrewAI", color: "amber-text-gradient" },
      { name: "NL2SQL", color: "blue-text-gradient" },
    ],
    icon: "🗃️",
    source_code_link: "https://github.com/",
  },
];

export const publications = [
  {
    year: "2022",
    title: "Impact of mismatch repair deficiency on survival of temozolomide-treated glioblastoma patients",
    journal: "Neuro-Oncology. 2022;24(Suppl 7):vii116-vii117",
  },
  {
    year: "2021",
    title: "Combination chemotherapy versus temozolomide for patients with methylated MGMT glioblastoma",
    journal: "Journal of Neuro-Oncology. 2021;153(3):393-402",
  },
  {
    year: "2021",
    title: "Cellworks CBM to predict therapy response in gastric cancer patients",
    journal: "Journal of Clinical Oncology. 2021;39(15_suppl):e16024",
  },
  {
    year: "2021",
    title: "Biosimulation using CBM identifies novel biomarkers in refractory & relapsed AML patients",
    journal: "Blood. 2021;138(Suppl_1)",
  },
];

export const contactInfo = {
  email: "poornachandra.gedi@gmail.com",
  phone: "+91-7899 419758",
  linkedin: "https://linkedin.com/in/poornachandra-g",
  orcid: "https://orcid.org/0009-0009-1610-1205",
  location: "Bengaluru, India",
};
