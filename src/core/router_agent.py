"""
MultiAgentRegistryKit Router - Intelligent query routing system.

This module implements the Router Agent pattern for routing user queries to specialized
agents based on the query content. It uses a language model to analyze the query intent
and select the most appropriate agent to handle it.
"""
from langchain_core.messages import SystemMessage, HumanMessage

from .registry import agent_registry as AgentRegistry
from .discovery import AgentDiscovery
from .llm_model import LLMModelProvider
from src.config.model_config import DEFAULT_REGION, DEFAULT_MODEL_ID

class RouterAgent:
    """
    Router agent that routes queries to specialized agents.
    
    This class acts as a central router that analyzes user queries and directs them
    to the most appropriate specialized agent. It uses a language model to determine
    the query intent and maintains a registry of available agents.
    """
    def __init__(self, region_name=DEFAULT_REGION, model_id=DEFAULT_MODEL_ID):
        """
        Initialize the router agent with specialized agents.
        
        This constructor:
        1. Creates an LLM model for routing decisions
        2. Discovers all available agents
        3. Initializes instances of all registered agents
        4. Generates a routing prompt based on agent descriptions
        
        Args:
            region_name (str): AWS region name for Bedrock
            model_id (str): Model ID to use for the language model
        """
        # Create LLM model using the LLMModelProvider class
        model_provider = LLMModelProvider(
            region_name=region_name,
            model_id=model_id
        )
        self.model = model_provider.create_model()
        
        # Discover all agents using the AgentDiscovery class
        self.agent_discovery = AgentDiscovery()
        self.agent_discovery.discover_agents()
        
        # Initialize all registered agents
        self.agent_instances = {}
        for name, agent_class in AgentRegistry.get_all_agents().items():
            self.agent_instances[name] = agent_class(self.model)
        
        # Generate routing prompt
        self.routing_prompt = self._generate_routing_prompt()
    
    def _generate_routing_prompt(self):
        """
        Generate a routing prompt based on registered agents.
        
        This method creates a system prompt for the routing model that includes
        descriptions of all registered agents. The prompt instructs the model to
        select the most appropriate agent based on the query content.
        
        Returns:
            str: The generated routing prompt
        """
        prompt = """You are a router agent that routes user queries to specialized agents.
Based on the query content, determine which of the following agents should handle it:

"""
        # Add each agent's description to the prompt
        for name, agent_class in AgentRegistry.get_all_agents().items():
            prompt += f"- {name}: {agent_class.get_description()}\n"
        
        prompt += """
Respond with ONLY the name of the appropriate agent. If none of the specialized agents are suitable,
respond with 'GeneralAgent'.
"""
        return prompt
    
    def route_query(self, query):
        """
        Determine which agent should handle the query.
        
        This method uses the language model to analyze the query content and
        determine which specialized agent is best suited to handle it.
        
        Args:
            query (str): The user's query
            
        Returns:
            str: The name of the selected agent
        """
        messages = [
            SystemMessage(content=self.routing_prompt),
            HumanMessage(content=query)
        ]
        
        response = self.model.invoke(messages)
        return response.content.strip()
        
    def get_agent(self, name):
        """
        Get an agent instance by name.
        
        This method retrieves the agent instance with the specified name.
        If the requested agent doesn't exist, it falls back to the GeneralAgent.
        
        Args:
            name (str): The name of the agent to retrieve
            
        Returns:
            BaseAgent: The requested agent instance or GeneralAgent as fallback
        """
        return self.agent_instances.get(name, self.agent_instances.get('GeneralAgent'))
