"""
Base Agent - Foundation class for all specialized agents.

This module provides the base class for all specialized agents in the system.
It handles common functionality such as conversation state management and
query processing, allowing specialized agents to focus on their specific domains.
"""
from typing import Optional
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from ..core.conversation_state import ConversationState

class BaseAgent:
    """
    Base agent class with conversation state management.
    
    This class provides the foundation for all specialized agents in the system.
    It handles common functionality such as:
    - Maintaining conversation history
    - Processing queries with context
    - Generating responses using the language model
    
    Specialized agents should inherit from this class and override the
    get_description class method to provide a description of their capabilities.
    """
    def __init__(self, model, system_prompt):
        """
        Initialize the agent with a model and system prompt.
        
        Args:
            model: The LLM model to use for generating responses
            system_prompt (str): The system prompt that defines the agent's behavior
                                and specialization
        """
        self.model = model
        self.system_prompt = system_prompt
        self.conversation_state = ConversationState()
    
    def process_query(self, query):
        """
        Process a query with conversation history.
        
        This method:
        1. Creates a message list with the system prompt
        2. Adds the conversation history
        3. Adds the current query
        4. Invokes the language model to generate a response
        5. Updates the conversation history with the query and response
        
        Args:
            query (str): The user's query
            
        Returns:
            str: The agent's response
        """
        messages = [SystemMessage(content=self.system_prompt)]
        
        # Add conversation history
        for message in self.conversation_state.message_history:
            messages.append(message)
        
        # Add current query
        messages.append(HumanMessage(content=query))
        
        response = self.model.invoke(messages)
        
        # Update conversation history
        self.conversation_state.add_message(HumanMessage(content=query))
        self.conversation_state.add_message(AIMessage(content=response.content))
        
        return response.content
    
    def reset_conversation(self):
        """
        Reset the conversation history.
        
        This method clears the conversation history, allowing a fresh start
        for a new conversation.
        """
        self.conversation_state.reset()
        
    @classmethod
    def get_description(cls):
        """
        Return a description of what this agent handles.
        
        This method should be overridden by subclasses to provide
        a description of the agent's capabilities. This description is used
        by the orchestrator to route queries to the appropriate agent.
        
        Returns:
            str: Description of the agent's capabilities
        """
        return "A generic agent"
