# AI-Powered Customer Support Agent with LangGraph

This project implements an AI agent that automatically processes customer support emails using LangGraph for workflow management. The agent classifies emails, searches knowledge bases, drafts responses, escalates issues, and schedules follow-ups.

## Architecture

The agent uses LangGraph to define a stateful workflow graph:

1. **Classify Urgency**: Determines if the email is Low, Medium, or High urgency
2. **Classify Topic**: Categorizes into Account, Billing, Bug, Feature Request, or Technical Issue
3. **Search Knowledge Base**: Looks up answers in a predefined knowledge base
4. **Draft Response**: Generates an appropriate customer response
5. **Decide Escalation**: Determines if the issue should be escalated to a human
6. **Schedule Follow-up**: Schedules follow-ups for urgent or complex issues

## Workflow Graph

```
classify_urgency -> classify_topic -> search_kb -> draft_response -> decide_escalate -> [schedule_follow_up | END]
```

Conditional routing ensures follow-ups are only scheduled when escalation occurs.

## State Management

The workflow uses a `SupportState` TypedDict to maintain state across nodes:

- `email_content`: The input email text
- `urgency`: Classified urgency level
- `topic`: Classified topic
- `kb_answer`: Answer from knowledge base (if found)
- `response`: Drafted response text
- `escalate`: Boolean flag for escalation
- `follow_up`: Follow-up action (if any)

## Classification Logic

- **Urgency**: Analyzed using LLM based on keywords and context
- **Topic**: Categorized using LLM into predefined categories

## Escalation Logic

Escalates if:
- Urgency is High
- No knowledge base answer is found
- Topic is Technical Issue

## Follow-ups

Scheduled for:
- High urgency issues
- Technical issues

## Usage

### Command Line

#### Process a single email

```bash
python3 customer_support_agent.py --email "I was charged twice for my subscription!"
```

#### Process emails from a file

```bash
python3 customer_support_agent.py --file samples/emails.json --output results.json
```

### Web UI (Streamlit)

For an interactive demo, run the Streamlit app:

```bash
pip install streamlit
streamlit run app.py
```

This will open a web interface where you can:
- Enter customer email content
- Click "Process Email" to see classification, response, and actions
- Try sample emails with one-click buttons

## Requirements

- Python 3.8+
- LangChain and LangGraph (optional, falls back to simple implementation)
- Streamlit (for UI): `pip install streamlit`

## Files

- `customer_support_agent.py`: Main script with LangGraph workflow
- `samples/`: Sample emails and outputs
- `README.md`: This documentation

## Sample Output

For input: "I was charged twice for my subscription!"

```json
{
  "email_content": "I was charged twice for my subscription!",
  "urgency": "High",
  "topic": "Billing",
  "kb_answer": "If you were charged twice, please contact billing support at billing@company.com with your invoice number.",
  "response": "If you were charged twice, please contact billing support at billing@company.com with your invoice number.",
  "escalate": true,
  "follow_up": "Schedule follow-up in 3 days"
}
```