import os
import requests
from bs4 import BeautifulSoup
import html2text

urls = {
    "Company": [
        "https://clairlabs.ai/about-us",
        "https://clairlabs.ai/careers",
        "https://clairlabs.ai/contact-us"
    ],
    "Impactomics": [
        "https://clairlabs.ai/impactomics",
        "https://clairlabs.ai/impactomics/rare-disease-genomics-solutions",
        "https://clairlabs.ai/impactomics/translational-oncology-intelligence"
    ],
    "Solutions": [
        "https://clairlabs.ai/gen-ai-solutions",
        "https://clairlabs.ai/multi-omics-intelligence-management-solutions",
        "https://clairlabs.ai/bioinformatics-solutions"
    ],
    "Services": [
        "https://clairlabs.ai/ai-services",
        "https://clairlabs.ai/cloud-engineering",
        "https://clairlabs.ai/data-engineering-and-governance",
        "https://clairlabs.ai/software-product-engineering",
        "https://clairlabs.ai/api-and-integration",
        "https://clairlabs.ai/transformative-consulting",
        "https://clairlabs.ai/ai-powered-digital-operations-healthcare",
        "https://clairlabs.ai/ai-clinical-trial-services",
        "https://clairlabs.ai/rwd-rwe-evidence-services"
    ],
    "Insights": [
        "https://clairlabs.ai/cognition-hub"
    ],
    "Home": [
        "https://clairlabs.ai/"
    ]
}

base_dir = "/Users/boss/Proyecto/Repos/Portfolio/clairlabs_info"
os.makedirs(base_dir, exist_ok=True)

h = html2text.HTML2Text()
h.ignore_links = False

for category, links in urls.items():
    cat_dir = os.path.join(base_dir, category)
    os.makedirs(cat_dir, exist_ok=True)
    
    for url in links:
        try:
            print(f"Fetching {url}...")
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to find the main content to avoid header/footer noise
            main_content = soup.find('main')
            if not main_content:
                main_content = soup.body
                
            if main_content:
                markdown_text = h.handle(str(main_content))
                
                # Create a safe filename
                filename = url.strip('/').split('/')[-1]
                if not filename or filename == 'clairlabs.ai':
                    filename = 'home'
                
                filepath = os.path.join(cat_dir, f"{filename}.md")
                with open(filepath, 'w') as f:
                    f.write(f"# {url}\n\n")
                    f.write(markdown_text)
                print(f"Saved to {filepath}")
            else:
                print(f"No content found for {url}")
                
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

