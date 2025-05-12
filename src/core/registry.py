"""
Agent Registry - A central registry for agent classes using the Singleton pattern.

This module implements the Registry pattern for agent management, allowing dynamic
registration and discovery of agent implementations. It provides a decorator for
easy agent registration and methods to retrieve registered agents.
"""

from typing import Dict, Optional, Any

# Forward declaration of BaseAgent type to avoid circular imports
# Using Any to prevent circular import issues with BaseAgent
BaseAgentType = Any


class AgentRegistry:
    """
    Registry for agent classes with automatic discovery.

    This class implements the Singleton pattern to ensure only one registry
    exists throughout the application. It stores agent classes by name and
    provides methods to register and retrieve them.
    """

    # Singleton instance
    _instance = None

    def __new__(cls):
        """
        Ensure only one instance of the registry exists (Singleton pattern).

        Returns:
            AgentRegistry: The singleton instance
        """
        if cls._instance is None:
            cls._instance = super(AgentRegistry, cls).__new__(cls)
            cls._instance._agents = {}
        return cls._instance

    def register_agent(self, agent_class=None):
        """
        Register an agent class with the registry.

        This method can be used as a decorator in two forms:
        1. @register_agent
        2. @register_agent()

        Args:
            agent_class: The agent class to register (when used as @register_agent)

        Returns:
            callable: Decorator function that registers the agent class
        """

        def decorator(agent_cls):
            # Register the agent using its class name as the key
            self._agents[agent_cls.__name__] = agent_cls
            return agent_cls

        # Handle both @register_agent and @register_agent() forms
        if agent_class is not None:
            return decorator(agent_class)
        return decorator

    def get_agent(self, name: str) -> Optional[BaseAgentType]:
        """
        Get an agent class by name.

        Args:
            name: The name of the agent class to retrieve

        Returns:
            Optional[BaseAgentType]: The agent class if found, None otherwise
        """
        return self._agents.get(name)

    def get_all_agents(self) -> Dict[str, BaseAgentType]:
        """
        Get all registered agent classes.

        Returns:
            Dict[str, BaseAgentType]: Dictionary mapping agent names to agent classes
        """
        return self._agents.copy()  # Return a copy to prevent modification


# Create a singleton instance
agent_registry = AgentRegistry()

# For decorator usage
register_agent = agent_registry.register_agent
