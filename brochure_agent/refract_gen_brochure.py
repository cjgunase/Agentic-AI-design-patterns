import os
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)
API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-4o-mini'

# Utility class for interacting with OpenAI
class OpenAIStrategy:
    """Handles communication with the OpenAI API."""
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, system_prompt, user_prompt):
        """Generates a response using OpenAI's chat completion."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content

# Utility class for scraping and extracting data from websites
class WebsiteScraper:
    """Handles web scraping and content extraction."""
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    def __init__(self, url):
        self.url = url
        self.title = None
        self.text = None
        self.links = []
        self._scrape()

    def _scrape(self):
        response = requests.get(self.url, headers=self.HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for tag in soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

        self.links = [
            link.get('href') for link in soup.find_all('a') if link.get('href')
        ]

    def get_contents(self):
        """Returns the text content of the webpage."""
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"

# Class for filtering and classifying links
class LinkFilter:
    """Filters relevant links from a webpage."""
    @staticmethod
    def filter_links(links):
        """Filters links for relevance based on heuristic rules."""
        return [link for link in links if 'about' in link.lower() or 'careers' in link.lower()]

# Facade for generating company brochures
class BrochureGenerator:
    """Main entry point for generating brochures."""
    SYSTEM_PROMPT = (
        "You are an assistant that analyzes the contents of several relevant pages from a company website "
        "and creates a short humorous, entertaining, jokey brochure using pirate language about the company "
        "for prospective customers, investors, and recruits. Respond in markdown. "
        "Include details of company culture, customers, and careers/jobs if you have the information."
    )

    def __init__(self, api_key, model):
        self.ai_strategy = OpenAIStrategy(api_key, model)

    def create_brochure(self, company_name, url):
        # Scrape website and filter links
        scraper = WebsiteScraper(url)
        filtered_links = LinkFilter.filter_links(scraper.links)

        # Generate a user prompt
        user_prompt = self._generate_prompt(company_name, scraper, filtered_links)

        # Generate a brochure using OpenAI
        brochure_content = self.ai_strategy.generate_response(self.SYSTEM_PROMPT, user_prompt)

        # Save the brochure to a markdown file
        self._save_brochure(company_name, brochure_content)
        return brochure_content

    def _generate_prompt(self, company_name, scraper, links):
        """Constructs a detailed user prompt for brochure creation."""
        link_text = "\n".join(links)
        return (
            f"You are looking at a company called: {company_name}\n"
            f"Here are the contents of its landing page and other relevant pages:\n"
            f"{scraper.get_contents()}\n"
            f"Relevant links:\n{link_text}"
        )

    def _save_brochure(self, company_name, content):
        """Saves the generated brochure to a markdown file."""
        filename = f"{company_name.lower().replace(' ', '_')}_brochure.md"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Brochure has been saved to {filename}")

# Main execution
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python gen_brochure.py \"Company Name\" company_url")
        sys.exit(1)

    company_name = sys.argv[1]
    url = sys.argv[2]

    if not API_KEY:
        print("OpenAI API key is missing. Please set it in your environment variables.")
        sys.exit(1)

    generator = BrochureGenerator(API_KEY, MODEL)
    brochure = generator.create_brochure(company_name, url)
    print("Generated Brochure:\n", brochure)
