# Prompt Quality Scoring Agent

A simple local prompt evaluation tool that scores prompt quality using Ollama via LangChain.

## What it does

- Reads prompts from `input_prompts.txt`
- Sends each prompt through a local `qwen:7b` Ollama model
- Evaluates each prompt on:
  - Clarity
  - Specificity
  - Context
  - Output Format
  - Persona
- Writes scored results to `output_scores.txt`

## Requirements

- Python 3.14+
- A local Ollama runtime with a `qwen:7b` model available
- A virtual environment is strongly recommended

## Installation

1. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
python3 -m pip install langchain-core langchain-community langchain-ollama
```

## Usage

1. Add your prompts to `input_prompts.txt`, one prompt per line.
2. Run the script:

```bash
python3 agent.py
```

3. After completion, view the scored results in `output_scores.txt`.

## Files

- `agent.py` - main script that loads prompts, evaluates them, and saves results
- `input_prompts.txt` - input file containing prompts to score
- `output_scores.txt` - generated output file with prompt scores and explanations
- `README.md` - this file

## Notes

- The script uses `langchain_ollama.OllamaLLM` and a modern `RunnableSequence` pipeline.
- If the model output omits the `Suggestions:` section for a prompt, the saved result will reflect the model response.
- Update the prompt template or add fallback handling if you want stricter output formatting.

## License

This repository is provided as-is. Feel free to use or adapt it for your own prompt scoring workflows.
