"""
Coding Agent - Specialized agent for handling programming queries.

This module implements a specialized agent for handling programming questions,
code generation, debugging, and software development. It inherits from the BaseAgent
class and overrides the get_description method to provide a description of its
capabilities.
"""

from .base_agent import BaseAgent
from ..core.registry import register_agent


@register_agent
class CodingAgent(BaseAgent):
    """
    Agent for handling coding queries with multi-turn support.

    This agent specializes in programming and software development. It can:
    - Write code in various programming languages
    - Debug existing code
    - Explain programming concepts
    - Suggest best practices and design patterns
    - Help with algorithm design and optimization

    The agent maintains context across multiple turns, allowing it to build on
    previous interactions when working on complex programming tasks.
    """

    def __init__(self, model):
        """
        Initialize the coding agent with a specialized system prompt.

        Args:
            model: The LLM model to use for generating responses
        """
        system_prompt = """You are a coding expert. You excel at writing clean, efficient code.
When asked to write code:
1. If you need additional information about requirements, ask for it clearly
2. Once you have all required information, choose appropriate data structures and algorithms
3. Write clean, well-documented code
4. Explain your implementation

Maintain context across the conversation. If the user has already provided some requirements or preferences, don't ask for them again.
Only respond to coding questions. If the query is not about coding, politely decline and explain that you're a coding specialist.
"""
        super().__init__(model, system_prompt)

    @classmethod
    def get_description(cls):
        """
        Return a description of what this agent handles.

        Returns:
            str: Description of the agent's programming capabilities
        """
        return "Handles programming questions, code generation, debugging, and software development"
