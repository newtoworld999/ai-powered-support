from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Connect to local Ollama model
llm = OllamaLLM(
    model="qwen:7b",
    temperature=0.2
)

# Prompt scoring template
template = """
You are a Prompt Quality Scoring Agent.

Evaluate the prompt using:

1. Clarity (0–10)
2. Specificity (0–10)
3. Context (0–10)
4. Output Format (0–10)
5. Persona (0–10)

Rules:
- Be strict and consistent
- Final score = average

Return EXACT format - DO NOT DEVIATE:

Clarity: X/10
Specificity: X/10
Context: X/10
Output Format: X/10
Persona: X/10

Final Score: X/10

Explanation:
[Your explanation here]

REQUIRED - Suggestions (you MUST provide exactly 3 actionable suggestions):
1. [First suggestion]
2. [Second suggestion]
3. [Third suggestion]

Prompt:
{user_prompt}
"""

prompt = PromptTemplate(
    input_variables=["user_prompt"],
    template=template
)

chain = prompt | llm
# -----------------------------
# File paths
# -----------------------------
INPUT_FILE = "input_prompts.txt"
OUTPUT_FILE = "output_scores.txt"

# -----------------------------
# Read prompts from file
# -----------------------------
def load_prompts(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]
# -----------------------------
# Write results to file
# -----------------------------
def save_results(results, file_path):
    with open(file_path, "w") as f:
        for i, (prompt, result) in enumerate(results, 1):
            f.write(f"\n==============================\n")
            f.write(f"PROMPT {i}: {prompt}\n")
            f.write(f"------------------------------\n")
            f.write(result)
            f.write("\n")

# -----------------------------
# Run evaluation
# -----------------------------
def evaluate_prompt(user_prompt):
    return chain.invoke({"user_prompt": user_prompt})

# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":

    prompts = load_prompts(INPUT_FILE)
    results = []

    print("\nEvaluating prompts...\n")

    for p in prompts:
        print(f"Processing: {p}")
        result = evaluate_prompt(p)
        results.append((p, result))

    save_results(results, OUTPUT_FILE)

    print(f"\nDone! Results saved to {OUTPUT_FILE}\n")
