Week 3 - Multi-File Context Agent

Project Overview

The Multi-File Context Agent is a Python-based project that organizes tasks across multiple modules. It includes an AI agent, context builder, calculator, editor, executor, and language model integration.

Features

- Multi-file context building
- AI agent integration
- Calculator operations
- File editing and task execution
- Language model integration
- Automated calculator testing

Technologies Used

- Python
- Large Language Models (LLMs)
- Pytest
- Modular programming

Project Structure

Week3-Multi-File-Context-Agent/
├── logs/
├── .env.example
├── .gitignore
├── README.md
├── ai_agent.py
├── calculator.py
├── context_builder.py
├── editor.py
├── executor.py
├── llm.py
├── main.py
├── requirements.txt
└── test_calculator.py

Installation and Setup

1. Clone the Repository

git clone https://github.com/KonikiPoojitha/Week3-Multi-File-Context-Agent.git
cd Week3-Multi-File-Context-Agent

2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Check ".env.example" and configure the environment variables required by your project.

Run the Project

python3 main.py

Run Tests

pytest test_calculator.py

Security Note

Never commit your ".env" file or expose API keys, passwords, or other secrets in GitHub repositories, screenshots, or demonstrations.

SkillAudit.ai Week 3 Checklist

- [ ] Multi-file project structure
- [ ] Context builder implementation
- [ ] AI agent integration
- [ ] Calculator functionality
- [ ] File editing and execution
- [ ] Language model integration
- [ ] Calculator tests
- [ ] README documentation

Mark each item as complete only after verifying that it works in your project.

Learning Outcomes

- Understanding modular Python applications
- Working with multiple files and context
- Integrating AI-related components
- Managing dependencies and environment variables
- Writing and running automated tests
