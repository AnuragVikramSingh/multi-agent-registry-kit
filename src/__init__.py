"""
MultiAgentRegistryKit - A modular, extensible framework for routing user queries to specialized AI agents.

This package contains:
- Core framework components for agent registration, discovery, and routing
- Specialized agent implementations for different domains
- Utility functions and helpers
"""

from src.core import AgentRegistry, register_agent, AgentDiscovery, RouterAgent, LLMModelProvider, create_llm_model, ConversationState
from src.agents import BaseAgent, MathAgent, CodingAgent, GeneralAgent
from src.config import MODEL_CONFIG, DEFAULT_REGION, DEFAULT_MODEL_ID
from src.main import main

__all__ = [
    'AgentRegistry',
    'register_agent', 
    'AgentDiscovery',
    'RouterAgent',
    'BaseAgent',
    'MathAgent',
    'CodingAgent',
    'GeneralAgent',
    'LLMModelProvider',
    'create_llm_model',
    'MODEL_CONFIG',
    'DEFAULT_REGION',
    'DEFAULT_MODEL_ID',
    'ConversationState',
    'main'
]
