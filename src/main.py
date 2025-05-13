#!/usr/bin/env python3
"""
MultiAgentRegistryKit - Main Application

This script runs the interactive router agent that routes queries to specialized agents.
It provides a command-line interface for users to interact with the multi-agent system.
"""

from src.core.router_agent import RouterAgent
from src.config.model_config import DEFAULT_REGION, DEFAULT_MODEL_ID


def main():
    """
    Run the interactive router agent.

    This function:
    1. Creates a router agent
    2. Enters an interactive loop to process user queries
    3. Routes queries to specialized agents based on content
    4. Maintains conversation state across multiple turns
    5. Handles special commands like 'exit' and 'reset'
    6. Automatically detects intent changes and reroutes to appropriate agents

    Returns:
        None
    """
    # Initialize the router agent with default configuration
    router = RouterAgent(region_name=DEFAULT_REGION, model_id=DEFAULT_MODEL_ID)
    current_agent = None
    current_agent_name = None

    # Display welcome message and instructions
    print("Welcome to MultiAgentRegistryKit!")
    print(
        "Seamlessly route user queries to specialized AI agents with intelligent intent detection"
    )
    print("Type 'exit' to quit or 'reset' to start a new conversation.")

    # Main interaction loop
    while True:
        # Get user input
        query = input("\nYou: ")

        # Handle special commands
        if query.lower() == "exit":
            break
        elif query.lower() == "reset":
            print("Starting a new conversation.")
            if current_agent:
                current_agent.reset_conversation()
                current_agent = None
                current_agent_name = None
            continue

        # Check if intent has changed by asking router to analyze the query
        new_agent_name = router.route_query(query)
        
        # If this is a new conversation or intent has changed, route to appropriate agent
        if not current_agent or new_agent_name != current_agent_name:
            # If we're switching agents, reset the previous agent's conversation
            if current_agent:
                current_agent.reset_conversation()
                print(f"Intent change detected. Switching from {current_agent_name} to {new_agent_name}")
            else:
                print(f"Routing to {new_agent_name}")
                
            current_agent = router.get_agent(new_agent_name)
            current_agent_name = new_agent_name

        # Process the query with the current agent
        response = current_agent.process_query(query)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    main()
