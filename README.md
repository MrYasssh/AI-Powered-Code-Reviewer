# AI-Powered Code Reviewer 🔍

An intelligent Python code review tool that provides automated suggestions for code improvements, style checks, and best practices using AI technology.

## Features ✨

- Real-time Python code analysis
- Line-by-line code review suggestions
- Naming convention checks (snake_case compliance)
- Code structure analysis and modularization suggestions
- AI-powered code improvement recommendations
- Clean and intuitive Streamlit interface

## Prerequisites 📋

Before running this application, make sure you have the following installed:

```bash
- Python 3.7+
- pip (Python package manager)
```

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage 💻

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Paste your Python code in the text area

4. Click the "Review Code" button to get AI-powered suggestions

## How It Works 🔨

The application consists of two main components:

### 1. Code Reviewer Engine (main.py)
- Implements naming convention checks using regex patterns
- Analyzes code structure using Python's AST (Abstract Syntax Tree)
- Utilizes the BART-large-CNN model for generating improvement suggestions
- Provides a comprehensive review combining multiple analysis techniques

### 2. Web Interface (app.py)
- Built with Streamlit for a responsive and user-friendly experience
- Displays code analysis in a side-by-side layout
- Separates line-specific suggestions from general improvements
- Includes helpful tooltips and clear error messages

## Features in Detail 🎯

1. **Naming Convention Check**
   - Ensures variables follow Python's snake_case convention
   - Provides specific suggestions for non-compliant variable names

2. **Code Structure Analysis**
   - Identifies opportunities for code modularization
   - Detects syntax errors and provides warnings

3. **AI-Powered Suggestions**
   - Generates context-aware code improvement recommendations
   - Uses state-of-the-art natural language processing

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Requirements 📝

```
streamlit
transformers
torch
regex
ast
```

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author ✍️

**Yash Khatri**

## Acknowledgments 🙏

- Built using Streamlit framework
- Powered by Hugging Face Transformers
- Uses Facebook's BART-large-CNN model for text generation

---

Made with ❤️ using Python and AI
