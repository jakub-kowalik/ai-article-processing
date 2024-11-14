# Instalation
## Prerequisistes
- Python 3.12
- OpenAI API Key

## Instalation
1. Clone repository
2. Proceed to project directory
3. Create virtual environment\
    `python -m venv venv`
4. Activate virtual environment
   - Windows: `venv\Scripts\activate`
   - Linux: `source venv/bin/activate`
5. Install dependencies\
`pip install -r requirements.txt`
6. (Optional) Add OpenAI API key to environmental variables:
   - Windows: `setx OPENAI_API_KEY "API_KEY"`
   - Linux: `export OPENAI_API_KEY="API_KEY"`

# Running
Application requires an OpenAI API key. It can be provided in two ways:

- application will use API key from environmental variable `OPENAI_API_KEY`
- using `-ak` - application will use API key specified after this argument

Application also requires specifying path to input article, using `-i` argument.\
Example command for running application using environmental API key:

`python article_processor.py -i "./Zadanie dla JJunior AI Developera - tresc artykulu.txt" -m "gpt-4o"`

To check other command-line options, use `--help` argument.