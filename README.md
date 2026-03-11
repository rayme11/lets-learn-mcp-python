# Let's Learn MCP with Python - Tutorial Series

A comprehensive guide to understanding and building Model Context Protocol (MCP) Servers for Python developers through interactive learning experiences.

**Watch the video** walkthrough on YouTube here: [Let's Learn MCP Python Live](https://www.youtube.com/watch?v=qQZFvz4BTCY&t=2858s)

Code from the **AI Engineer Paris** Talk can be found here: [Building MCP Servers for VS Code](https://github.com/microsoft/lets-learn-mcp-python/tree/main/ai-engineer-25)

## What You'll Build

By the end of this tutorial series, you'll have:

1. **🐍 Python Study Buddy App** - An interactive console application that uses a custom MCP server to help developers learn Python concepts at beginner, intermediate, and expert levels
2. **🧠 AI Research Learning MCP Server** - Your own advanced MCP server that helps AI assistants find the latest AI/ML research papers, highlight top discoveries, and create personalized study plans

## Tutorial Structure

### [Part 1: Setup and Core Concepts](#quick-start)

<img src="./images/mcp-core-concepts.png" alt="mcp-core-concepts" width="900" height="600">

**⏱️ Time: 15-20 minutes**

Set up your development environment and understand MCP fundamentals:
- Install VS Code, Python 3.12+, and Python extension
- Learn what Model Context Protocol is and why it matters
- Understand the client-server architecture


* Note for a more in depth 'Getting Started' with MCP Demo check out [mcp-python-demo](https://github.com/pamelafox/mcp-python-demo)

---

### [Part 2: Using MCP Servers - Python Study Buddy](part2-study-buddy.md)
**⏱️ Time: 20-35 minutes**

<img src="./images/study_buddy_app.png" alt="study-buddy-app" width="900" height="600">

**Key Learning Objectives:**
1. Create a basic MCP server in Python
2. Use prompts with MCP
3. Use basic tools with MCP

**Outcomes:**
Building an interactive Python learning companion:
- Configure a custom Python Learning MCP server
- Create Python models for learning concepts using dataclasses
- Build an interactive study session with progress tracking
- Generate personalized coding challenges and explanations
- Understand how AI assistants can enhance learning experiences

**Example of what you'll create**:
```
🐍 Python Study Buddy - Interactive Learning Session
===================================================
Level: Intermediate
Topic: List Comprehensions
Progress: 3/10 concepts mastered

Challenge: Create a list comprehension that filters even numbers...
💡 Hint: Use the modulo operator (%) to check for even numbers
🎯 Your mission: Write code that demonstrates understanding!
```

**Continue to**: [Part 2: Python Study Buddy →](part2-study-buddy.md)

---

### [Part 3: Building Your Own MCP Server - AI Research Learning Hub](part3-ai-researcher.md)
**⏱️ Time: 20-35 minutes**

**Key Learning Objectives:**
1. Find and use external MCP servers 
2. Add resources with MCP
3. Automate Tasks with MCP 

**Outcomes:**
Build an advanced MCP server that helps you keep up with the latest AI Research:
- Create an AI/ML research paper discovery service
- Implement tools for finding trending papers and breakthroughs
- Build personalized study plan generation capabilities
- Create intelligent content summarization and ranking
- Store daily AI Research Learning Notes in a Github Repo

**What you'll build**:
- `search_research_papers()` - Find latest AI/ML research by topic
- `get_trending_papers()` - Discover what's hot in AI research
- `create_study_plan()` - Generate personalized learning roadmaps
- `summarize_paper()` - Create digestible summaries of complex research
- `track_learning_progress()` - Monitor study achievements and goals
- `send_research_learning()` - Send study daily study note to the user 

**Continue to**: [Part 3: AI Research Learning Hub →](./part3-ai-researcher.md)

---

## Quick Start

If you're ready to dive in immediately:

### 1. Visual Studio Code
- Download and install [VS Code](https://code.visualstudio.com/)
- Essential for MCP development and integration

### 2. Python 3.12+
- Install Python 3.12 or later from [Python.org](https://www.python.org/downloads/)
- Verify installation: `python --version` or `python3 --version`
- Ensure pip is installed: `pip --version` or `pip3 --version`

### 3. Python Extension for VS Code
- Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension
- Provides comprehensive Python development support
- Includes IntelliSense, debugging, and virtual environment management

### 4. Install UV
To install UV, run the following command in the terminal:

```bash
pip install uv 
```

### 5. Create Virtual Environment

```bash
# Pin Python version used by uv for this project
uv python pin 3.13

# Create the virtual environment
uv venv --python 3.13 mpc-env

# Activate on macOS/Linux
source mpc-env/bin/activate

# Activate on Windows
mpc-env\Scripts\activate
```

### 6. Install packages 

```bash
uv sync --active
```

### 6. Walk through the core concepts in the terminal 

```bash
python part-1-concepts.py
```

### 7. Build your first MCP app

2. **Choose your path**:
   - 🐍 **Want to learn Python with MCP?** Jump to [Part 2: Python Study Buddy](part2-study-buddy.md)
   - 🧠 **Ready to build AI research tools?** Go to [Part 3: AI Research Hub](part3-ai-researcher.md)

## Additional Resources

- 📖 [MCP Official Documentation](https://modelcontextprotocol.io/)
- 🛠️ [Python MCP SDK Repository](https://github.com/modelcontextprotocol/python-sdk)
- 🐍 [Python MCP Examples](https://github.com/modelcontextprotocol/servers)
- 🧠 [Quick Start Python MCP Demo](https://github.com/pamelafox/mcp-python-demo)
- 📚 [ArXiv API Documentation](https://arxiv.org/help/api/user-manual)
- 🔬 [Papers With Code API](https://paperswithcode.com/api/v1/docs/)

## Contributing

This tutorial is open source! Feel free to:
- 🐛 Submit improvements and corrections
- 💡 Add more examples and use cases
- 🤝 Share your own MCP server implementations
- 💬 Help others in the discussions

----

*Happy learning! 🐍🧠*
