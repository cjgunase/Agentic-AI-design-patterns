
# Brochure Generator with Python and OpenAI

## Overview
This project is a Python script that generates a humorous, pirate-themed brochure for a company by:
1. Scraping the company's website to extract text and links.
2. Filtering relevant links (e.g., "About Us" or "Careers").
3. Using OpenAI's language model to generate a markdown-formatted brochure based on the scraped content and filtered links.

### Key Features
- **Web scraping**: Extracts content and links from a webpage.
- **AI-powered content generation**: Creates entertaining brochures using OpenAI.
- **Modular design**: Breaks functionality into separate, reusable classes for better code organization.

---

## How It Works
The project follows these main steps:
1. Scrape the target website to get its text content and links.
2. Filter the links to identify relevant ones (e.g., links to company information or career pages).
3. Generate a user-friendly prompt combining the scraped content and filtered links.
4. Send the prompt to OpenAI's language model to create the brochure.
5. Save the generated brochure as a markdown file.

---

## Setup and Installation

### Prerequisites
Before running the code, ensure you have the following:
- Python 3.8 or higher installed.
- An OpenAI API key. [Sign up for OpenAI](https://platform.openai.com/signup/) to get an API key.

### Installing Required Libraries
Install the required Python libraries by running:

```bash
pip install requests beautifulsoup4 python-dotenv openai
```

### Setting Up the Environment
1. **Create a `.env` file**:
   The `.env` file stores sensitive information like your OpenAI API key. Create a `.env` file in the project directory and add the following:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Replace `your_openai_api_key_here` with your actual API key.

2. **Verify API Key**:
   Ensure your API key starts with `sk-` and is valid.

---

## How to Run the Script

1. Open your terminal or command prompt.
2. Run the script with the following command:

   ```bash
   python gen_brochure.py "Company Name" company_url
   ```

   - Replace `"Company Name"` with the name of the company (e.g., `"Example Corp"`).
   - Replace `company_url` with the URL of the company’s website (e.g., `https://example.com`).

   Example:

   ```bash
   python gen_brochure.py "Example Corp" https://example.com
   ```

3. The script will generate a markdown file named `company_name_brochure.md` in the same directory.

---

## Code Explanation
The code is divided into well-defined components. Below is a detailed breakdown:

### 1. `OpenAIStrategy`: Handles AI Interactions
This class manages all interactions with OpenAI's API.

- **Purpose**: Sends a prompt to OpenAI and retrieves the response.
- **Key Methods**:
  - `generate_response(system_prompt, user_prompt)`: Takes a system prompt and user prompt as input, sends them to OpenAI, and returns the AI's response.

Example:
```python
ai_strategy = OpenAIStrategy(api_key="your_key", model="gpt-4o-mini")
response = ai_strategy.generate_response("System prompt", "User prompt")
print(response)
```

---

### 2. `WebsiteScraper`: Extracts Content and Links
This class scrapes the provided webpage URL to extract:
- The title of the webpage.
- The main text content (ignoring irrelevant tags like `<script>` or `<style>`).
- Links found on the page.

- **Key Methods**:
  - `get_contents()`: Returns the webpage’s title and text content as a formatted string.

Example:
```python
scraper = WebsiteScraper("https://example.com")
print(scraper.get_contents())
print(scraper.links)
```

---

### 3. `LinkFilter`: Filters Relevant Links
This class filters links from the webpage to find those relevant for a brochure (e.g., "About Us" or "Careers").

- **Purpose**: Reduces noise by focusing only on links of interest.
- **Key Method**:
  - `filter_links(links)`: Takes a list of links and returns only those that are relevant.

Example:
```python
links = ["https://example.com/about", "https://example.com/contact", "https://example.com/careers"]
filtered_links = LinkFilter.filter_links(links)
print(filtered_links)  # Output: ["https://example.com/about", "https://example.com/careers"]
```

---

### 4. `BrochureGenerator`: Orchestrates the Workflow
This is the main class, acting as a **facade** to coordinate the entire process:
1. Scrape the website.
2. Filter links.
3. Generate a prompt.
4. Use OpenAI to create a brochure.
5. Save the brochure as a markdown file.

- **Key Methods**:
  - `create_brochure(company_name, url)`: Orchestrates the entire process, from scraping to saving the brochure.

Example:
```python
generator = BrochureGenerator(api_key="your_key", model="gpt-4o-mini")
brochure = generator.create_brochure("Example Corp", "https://example.com")
print(brochure)
```

---

## Detailed Workflow

1. **Scrape Website**:
   - Extract the title, text content, and links from the target webpage using `WebsiteScraper`.

2. **Filter Links**:
   - Use `LinkFilter` to find relevant links, such as "About Us" or "Careers".

3. **Generate Prompt**:
   - Combine the website’s text content and relevant links into a user prompt.
   - Add instructions for OpenAI to generate a humorous, pirate-themed brochure.

4. **Call OpenAI**:
   - Use `OpenAIStrategy` to send the prompt to OpenAI and retrieve the response.

5. **Save the Brochure**:
   - Save the generated markdown content to a file.

---

## Example Output
When you run the script, it generates a markdown file like the one below:

### File: `example_corp_brochure.md`
```markdown
# Ahoy, Mateys! Welcome to Example Corp!

## About Us
Example Corp be the finest ship in the sea of technology, building treasures for customers far and wide.

## Careers
Join our merry crew of tech-savvy pirates! Positions available in engineering, marketing, and more. Grab yer chance to sail the high seas of innovation!
```

---

## Advanced Tips

### Error Handling
- The script checks if the OpenAI API key is valid.
- You can extend error handling to catch issues like network failures or invalid URLs.

### Customizing the Prompt
- Modify `SYSTEM_PROMPT` in `BrochureGenerator` to adjust the tone or style of the brochure.

---

## Learning Outcomes
By studying this code, beginners will:
- Understand how to organize Python code using classes and methods.
- Learn how to interact with web scraping tools (BeautifulSoup).
- Use APIs like OpenAI for advanced natural language tasks.
- Apply design patterns such as **Facade** and **Prompt Engineering** for modular and maintainable code.

---

Feel free to use and adapt this code for other projects. Happy coding! 🚀
