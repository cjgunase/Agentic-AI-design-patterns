## LLM-Project Templates

A series of boilerplates to help you kick-start your LLM projects.

### Prerequisites
1. Python 3.6 or above
2. An OpenAI API Key

### Steps to run the application
**1. Clone the repository to your local machine:**
```shell
git clone https://github.com/krisograbek/llm-project-templates.git
```

**2. Navigate to the project directory:**
```shell
cd llm-project-templates
```

**3. Create a virtual environment and activate it:**

On macOS and Linux:
```shell
python3 -m venv myenv
source myenv/bin/activate
```

On Windows:
```shell
python -m venv myenv
.\myenv\Scripts\activate
```

**3a. Upgrade pip (optional but recommended)**
```shell
pip install --upgrade pip
```

**4. Install the necessary Python packages:**
```shell
pip install openai python-dotenv
```

**5. Create a .env file in the root directory of the project and add your OpenAI API key:**
```shell
echo OPENAI_API_KEY=your-api-key > .env
```
OR

```shell
cp .env.example .env
```

Please replace your-api-key with your actual OpenAI API key.

**6. Run the Python application:**
```shell
python app.py
```
Replace `app.py` with the actual script file you run.

**6. Run the Streamlit application.**

```shell
streamlit run app.py
```
Replace `app.py` with the actual script file you run.

