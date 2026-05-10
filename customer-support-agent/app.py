import streamlit as st
import json
from customer_support_agent import process_email

st.title("AI Customer Support Agent")

st.markdown("""
This app demonstrates the AI-powered customer support agent.
Enter an email content below and see how it's classified, responded to, and handled.
""")

if 'email_input' not in st.session_state:
    st.session_state.email_input = ""

email_input = st.text_area(
    "Enter customer email content:",
    height=150,
    key="email_input",
)

if st.button("Process Email"):
    if email_input.strip():
        with st.spinner("Processing email..."):
            result = process_email(email_input)

        st.success("Email processed successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Classification")
            st.write(f"**Urgency:** {result['urgency']}")
            st.write(f"**Topic:** {result['topic']}")

        with col2:
            st.subheader("Actions")
            st.write(f"**Escalate:** {'Yes' if result['escalate'] else 'No'}")
            st.write(f"**Follow-up:** {result['follow_up'] or 'None'}")

        st.subheader("Response")
        st.write(result['response'])

        st.subheader("Raw Result")
        st.json(result)
    else:
        st.error("Please enter some email content.")

st.markdown("---")
st.markdown("**Sample emails to try:**")
samples = [
    "How do I reset my password?",
    "I was charged twice for my subscription!",
    "The export feature crashes when I select PDF format.",
    "Can you add dark mode to the mobile app?",
    "Our API integration fails intermittently with 504 errors."
]

for sample in samples:
    if st.button(f"Try: {sample[:50]}..."):
        st.session_state.email_input = sample
        st.rerun()