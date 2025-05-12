"""
Math Agent - Specialized agent for handling mathematical queries.

This module implements a specialized agent for handling mathematical problems,
calculations, equations, and numerical analysis. It inherits from the BaseAgent
class and overrides the get_description method to provide a description of its
capabilities.
"""

from .base_agent import BaseAgent
from ..core.registry import register_agent


@register_agent
class MathAgent(BaseAgent):
    """
    Agent for handling math queries with multi-turn support.

    This agent specializes in mathematical problems and calculations. It can:
    - Solve equations and systems of equations
    - Perform arithmetic operations
    - Handle calculus problems (derivatives, integrals)
    - Work with statistics and probability
    - Analyze numerical data

    The agent maintains context across multiple turns, allowing it to build on
    previous interactions when solving complex problems.
    """

    def __init__(self, model):
        """
        Initialize the math agent with a specialized system prompt.

        Args:
            model: The LLM model to use for generating responses
        """
        system_prompt = """You are a mathematical expert. You excel at solving mathematical problems.
When presented with a math problem:
1. If you need additional information, ask for it clearly
2. Once you have all required information, break down the problem step by step
3. Show your work clearly
4. Verify your answer

For problems like "find sum of two numbers" or similar operations where values aren't provided:
- First ask for the first number
- Then ask for the second number
- Once you have both numbers, perform the calculation and show the result

Maintain context across the conversation. If the user has already provided some values, don't ask for them again.
Only respond to math questions. If the query is not about math, politely decline and explain that you're a math specialist.
"""
        super().__init__(model, system_prompt)

    @classmethod
    def get_description(cls):
        """
        Return a description of what this agent handles.

        Returns:
            str: Description of the agent's mathematical capabilities
        """
        return "Handles mathematical problems, calculations, equations, and numerical analysis"
