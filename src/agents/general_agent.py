"""
General Agent - Specialized agent for handling general knowledge queries.

This module implements a general-purpose agent for handling a wide range of
knowledge questions, explanations, and conversational queries. It inherits from
the BaseAgent class and overrides the get_description method to provide a
description of its capabilities.
"""

from .base_agent import BaseAgent
from ..core.registry import register_agent


@register_agent
class GeneralAgent(BaseAgent):
    """
    Agent for handling general queries with multi-turn support.

    This agent serves as a fallback for queries that don't clearly match other
    specialized agents. It can handle a wide range of topics including:
    - General knowledge questions
    - Explanations of concepts
    - Conversational queries
    - Information requests
    - Assistance with various tasks

    The agent maintains context across multiple turns, allowing it to have
    coherent conversations with users.
    """

    def __init__(self, model):
        """
        Initialize the general agent with a specialized system prompt.

        Args:
            model: The LLM model to use for generating responses
        """
        system_prompt = """You are a helpful AI assistant. You can answer questions on a wide range of topics.
Provide accurate, helpful, and concise responses.

If you need additional information to answer a question completely, ask for it clearly.
Maintain context across the conversation and refer back to previous exchanges when relevant.
"""
        super().__init__(model, system_prompt)

    @classmethod
    def get_description(cls):
        """
        Return a description of what this agent handles.

        Returns:
            str: Description of the agent's general capabilities
        """
        return "Handles general knowledge questions, explanations, and conversational queries"
