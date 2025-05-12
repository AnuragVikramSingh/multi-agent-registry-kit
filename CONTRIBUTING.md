# Contributing to MultiAgentRegistryKit

Thank you for your interest in contributing to the MultiAgentRegistryKit project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

1. A clear, descriptive title
2. A detailed description of the issue
3. Steps to reproduce the bug
4. Expected behavior
5. Actual behavior
6. Any relevant logs or error messages
7. Your environment (OS, Python version, etc.)

### Suggesting Enhancements

We welcome suggestions for enhancements! Please create an issue with:

1. A clear, descriptive title
2. A detailed description of the proposed enhancement
3. Any relevant examples or use cases
4. If applicable, references to similar features in other projects

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add or update tests as necessary
5. Ensure all tests pass
6. Update documentation as needed
7. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AnuragVikramSingh/multi-agent-registry-kit.git
   cd multi-agent-registry-kit
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

4. Run tests:
   ```bash
   python -m unittest discover tests
   ```

## Coding Standards

- Follow PEP 8 style guidelines
- Write docstrings for all functions, classes, and modules
- Include type hints where appropriate
- Write unit tests for new functionality

## Adding a New Agent

To add a new specialized agent:

1. Create a new file in the `src/agents` directory
2. Define a class that inherits from `BaseAgent`
3. Use the `@register_agent` decorator
4. Implement the required methods, especially `get_description`
5. Add tests for the new agent
6. Update the documentation

Example:

```python
# src/agents/travel_agent.py
from src.agents.base_agent import BaseAgent
from src.core.registry import register_agent

@register_agent
class TravelAgent(BaseAgent):
    """Specialized agent for travel-related queries."""
    
    def __init__(self, model):
        system_prompt = """You are a travel expert specialized in:
- Flight and hotel recommendations
- Destination information
- Travel planning
- Local attractions and activities"""
        super().__init__(model, system_prompt)
    
    @classmethod
    def get_description(cls):
        return "Handles travel planning, destination information, and recommendations"
```

## Contact

If you have any questions or need help, please contact:
- Anurag Vikram Singh
  - Email: anuragvikramsingh@outlook.com
  - LinkedIn: https://www.linkedin.com/in/anuragvikramsingh/
- Open an issue on GitHub

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.
