"""
LLM Model Provider - Factory for language model instances.

This module provides a factory class for creating and configuring language models
for use with agents. It abstracts the details of model creation and configuration,
allowing the rest of the application to work with language models without knowing
the specifics of their implementation.
"""
import boto3
from langchain_aws import ChatBedrock

from src.config.model_config import DEFAULT_REGION, DEFAULT_MODEL_ID, MODEL_CONFIG


class LLMModelProvider:
    """
    Factory class for creating and configuring language models.
    
    This class is responsible for creating language model instances with the
    specified configuration. It handles the details of connecting to AWS Bedrock
    and configuring the model parameters.
    """
    
    def __init__(
        self,
        region_name: str = DEFAULT_REGION,
        model_id: str = DEFAULT_MODEL_ID,
        temperature: float = MODEL_CONFIG["temperature"],
        max_tokens: int = MODEL_CONFIG["max_tokens"]
    ):
        """
        Initialize the model provider with configuration parameters.
        
        Args:
            region_name (str): AWS region name for Bedrock
            model_id (str): Model ID to use (e.g., Claude model identifier)
            temperature (float): Temperature setting for the model (0.0-1.0)
                                Lower values make output more deterministic
            max_tokens (int): Maximum tokens to generate in the response
        """
        self.region_name = region_name
        self.model_id = model_id
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._client = None
    
    @property
    def client(self):
        """
        Lazily initialize and return the Bedrock client.
        
        This property implements lazy initialization of the Bedrock client,
        creating it only when needed and reusing it for subsequent calls.
        
        Returns:
            boto3.client: Configured Bedrock runtime client
        """
        if self._client is None:
            self._client = boto3.client(
                service_name="bedrock-runtime",
                region_name=self.region_name
            )
        return self._client
    
    def create_model(self):
        """
        Create and configure a language model for use with agents.
        
        This method creates a LangChain ChatBedrock model with the specified
        configuration parameters. The model can be used by agents to generate
        responses to user queries.
        
        Returns:
            ChatBedrock: Configured LangChain ChatBedrock model
        """
        return ChatBedrock(
            client=self.client,
            model_id=self.model_id,
            model_kwargs={
                "temperature": self.temperature,
                "max_tokens": self.max_tokens
            }
        )


# For backward compatibility and standalone usage
def create_llm_model(
    region_name: str = DEFAULT_REGION, 
    model_id: str = DEFAULT_MODEL_ID,
    temperature: float = MODEL_CONFIG["temperature"], 
    max_tokens: int = MODEL_CONFIG["max_tokens"]
):
    """
    Create and configure a language model for use with agents.
    
    This function is a convenience wrapper around the LLMModelProvider class
    for backward compatibility and standalone usage.
    
    Args:
        region_name (str): AWS region name for Bedrock
        model_id (str): Model ID to use (e.g., Claude model identifier)
        temperature (float): Temperature setting for the model (0.0-1.0)
        max_tokens (int): Maximum tokens to generate in the response
        
    Returns:
        ChatBedrock: Configured LangChain ChatBedrock model
    """
    provider = LLMModelProvider(
        region_name=region_name,
        model_id=model_id,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return provider.create_model()
