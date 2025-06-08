# Python OpenAI examples

## For development

### Initialise python virtal environment

- `python -m venv .`
- `source ./bin/activate`

### Install packages

Prequisite: Have `pip` installed

- `pip install -r requirements.txt`

### Lint

- `python -m pylint src/`

### Style check

- `python -m black src/ --check --diff --verbose`

### All in one line

- `python -m pylint src/ && python -m black src/ --check --diff --verbose`

### To execute examples

- Ensure `OPENAI_API_KEY` is set in the environment: `export OPENAI_API_KEY=<key>`
- `python src/<filename>.py`
