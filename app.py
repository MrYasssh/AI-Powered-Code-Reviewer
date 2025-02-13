# app.py
import streamlit as st
import ast
import re
from main import CodeReviewer

# Initialize the Code Reviewer
reviewer = CodeReviewer()

# Streamlit UI Enhancements
st.set_page_config(page_title="AI Code Reviewer", page_icon="🚀", layout="wide")
st.title("🔍 AI-Powered Code Reviewer")
st.markdown("## Improve your Python code with AI-powered suggestions!")

# Text area for user input
code_input = st.text_area("✍️ Paste your Python code here:", height=200, help="Enter your Python script for analysis.")

if st.button("🚀 Review Code"):
    if code_input.strip():
        suggestions = reviewer.review_code(code_input)
        
        # Split the code into lines for detailed analysis
        code_lines = code_input.split("\n")
        analyzed_lines = {i + 1: [] for i in range(len(code_lines))}
        general_suggestions = []
        
        # Extract issues related to specific lines
        for suggestion in suggestions:
            match = re.search(r"line (\d+)", suggestion)
            if match:
                line_number = int(match.group(1))
                if line_number in analyzed_lines:
                    analyzed_lines[line_number].append(suggestion)
            else:
                general_suggestions.append(suggestion)  # General suggestions
        
        # Layout for side-by-side display
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📜 Code Analysis")
            for i, line in enumerate(code_lines, start=1):
                if analyzed_lines[i]:
                    st.markdown(f"**Line {i}:** `{line.strip()}`")
                    for comment in analyzed_lines[i]:
                        st.warning(comment)
                else:
                    st.text(f"{i}: {line}")
        
        with col2:
            st.subheader("💡 General Suggestions")
            if general_suggestions:
                for suggestion in general_suggestions:
                    st.info(suggestion)
            else:
                st.success("No general suggestions! Your code looks good.")
    else:
        st.warning("⚠️ Please enter some code before clicking review.")

# Sidebar Info
st.sidebar.header("ℹ️ About")
st.sidebar.write(
    "This AI-powered code reviewer analyzes Python code and provides suggestions on naming conventions, structure, and improvements line-by-line."
)

# Footer Section
st.markdown("---")
st.markdown("👨‍💻 **Project Owner:** Yash Khatri")
st.markdown("📌 Developed with ❤️ using Streamlit and AI.")
