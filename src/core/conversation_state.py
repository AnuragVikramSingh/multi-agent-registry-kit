"""
Conversation State - Manages conversation history for multi-turn interactions.

This module provides a data class for storing and managing conversation history
between users and agents. It supports adding messages and resetting the conversation.
"""
from dataclasses import dataclass, field
from typing import List

@dataclass
class ConversationState:
    """
    Data class to store conversation state.
    
    This class manages the conversation history for agents, providing
    methods to add messages and reset the conversation. It uses a simple
    list to store the message history in chronological order.
    
    Attributes:
        message_history (List): List of messages in the conversation
    """
    message_history: List = field(default_factory=list)
    
    def add_message(self, message):
        """
        Add a message to the conversation history.
        
        This method appends a new message to the conversation history.
        Messages can be of any type, but are typically LangChain message
        objects (HumanMessage, AIMessage, etc.).
        
        Args:
            message: The message to add to the history
        """
        self.message_history.append(message)
        
    def reset(self):
        """
        Reset the conversation history.
        
        This method clears the conversation history by replacing the
        message_history list with an empty list.
        """
        self.message_history = []
