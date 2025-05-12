"""
Model configuration settings for the MultiAgentRegistryKit framework.

This module contains configuration constants for language models used in the application.
These settings control which model is used, which region it's accessed from, and
parameters that affect the model's behavior.
"""

# Default AWS region for Bedrock services
DEFAULT_REGION = "us-east-1"

# Default model ID for Amazon Bedrock
# Claude 3 Haiku is used as the default model due to its balance of performance and cost
DEFAULT_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

# Default model configuration parameters
MODEL_CONFIG = {
    # Temperature controls randomness in the output (0.0 = deterministic, 1.0 = creative)
    "temperature": 0.0,
    
    # Maximum number of tokens to generate in the response
    "max_tokens": 1024,
}
