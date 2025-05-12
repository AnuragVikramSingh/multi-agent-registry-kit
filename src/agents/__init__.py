"""
Agent package initialization.

This package contains specialized agent implementations:
- MathAgent: Handles mathematical problems and calculations
- CodingAgent: Addresses programming questions and code generation
- GeneralAgent: Responds to general knowledge queries
"""
from .base_agent import BaseAgent
from .math_agent import MathAgent
from .coding_agent import CodingAgent
from .general_agent import GeneralAgent

__all__ = ['BaseAgent', 'MathAgent', 'CodingAgent', 'GeneralAgent']
