"""
Core package for the MultiAgentRegistryKit framework.

This package contains the core components of the framework:
- Registry: Agent registration system
- Discovery: Automatic agent discovery
- Router Agent: Main routing agent
- LLM Model: Language model provider
- Conversation State: Conversation history management
"""

from src.core.registry import agent_registry as AgentRegistry, register_agent
from src.core.discovery import AgentDiscovery
from src.core.router_agent import RouterAgent
from src.core.llm_model import LLMModelProvider, create_llm_model
from src.core.conversation_state import ConversationState

__all__ = [
    'AgentRegistry', 
    'register_agent', 
    'AgentDiscovery',
    'RouterAgent', 
    'LLMModelProvider',
    'create_llm_model',
    'ConversationState'
]
