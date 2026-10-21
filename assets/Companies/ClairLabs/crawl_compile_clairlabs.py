import os
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin, urlparse
import time

base_url = "https://clairlabs.ai"
domain = "clairlabs.ai"

visited = set()
to_visit = [base_url]
content_dict = {}

h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = True

def is_internal(url):
    return domain in urlparse(url).netloc

# Keep track of pages to avoid infinite loops or massive scraping 
max_pages = 200

while to_visit and len(visited) < max_pages:
    url = to_visit.pop(0)
    if url in visited:
        continue
        
    visited.add(url)
    
    # Avoid crawling assets
    if any(url.lower().endswith(ext) for ext in ['.pdf', '.jpg', '.png', '.svg', '.css', '.js']):
        continue
        
    try:
        print(f"Crawling [{len(visited)}]: {url}")
        response = requests.get(url, timeout=10)
        
        # Ensure it's html
        if 'text/html' not in response.headers.get('Content-Type', ''):
            continue
            
        if response.status_code != 200:
            continue
            
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else url
        
        # Extract content
        main_content = soup.find('main')
        if not main_content:
            main_content = soup.body
            
        if main_content:
            # Remove scripts and styles for cleaner text
            for script in main_content(["script", "style", "nav", "footer", "header"]):
                script.decompose()
                
            md_text = h.handle(str(main_content))
            content_dict[url] = {
                'title': title.strip(),
                'text': md_text.strip()
            }
            
        # Find all links
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(base_url, href)
            # Normalize url (remove fragment)
            full_url = full_url.split('#')[0].rstrip('/')
            
            if is_internal(full_url) and full_url not in visited and full_url not in to_visit:
                to_visit.append(full_url)
                
    except Exception as e:
        print(f"Error crawling {url}: {e}")

# Now compile into a single organized file
output_file = "/Users/boss/Proyecto/Repos/Portfolio/clairlabs_deep_research.md"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# ClairLabs Deep Research Document\n\n")
    f.write("This document contains all scraped text from clairlabs.ai, compiled for deep research.\n\n")
    f.write("---\n\n")
    
    f.write("## Table of Contents\n")
    for url, data in content_dict.items():
        title = data['title']
        f.write(f"- {title} ({url})\n")
    f.write("\n---\n\n")
    
    for url, data in content_dict.items():
        title = data['title']
        text = data['text']
        f.write(f"# {title}\n")
        f.write(f"**Source URL:** {url}\n\n")
        f.write(text)
        f.write("\n\n---\n\n")
        
print(f"\nSuccessfully crawled {len(visited)} pages.")
print(f"Deep research file created at {output_file}")

