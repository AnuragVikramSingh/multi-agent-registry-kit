"""
Agent Discovery - Automatic discovery and loading of agent modules.

This module provides functionality to dynamically discover and import agent modules
from the agents package. It handles the automatic registration of agents with the
registry when their modules are imported.
"""

import importlib
import os
import pkgutil
from typing import List, Optional, Set


class AgentDiscovery:
    """
    Class responsible for discovering and importing agent modules.

    This class scans the agents package directory, imports all agent modules
    (except those explicitly excluded), and triggers their registration with
    the agent registry through the import process.
    """

    def __init__(self, excluded_modules: Optional[List[str]] = None):
        """
        Initialize the agent discovery class.

        Args:
            excluded_modules: List of module names to exclude from discovery.
                             Default excludes 'base_agent' as it's not a concrete agent.
        """
        self.excluded_modules = excluded_modules or ["base_agent"]
        self.discovered_modules: Set[str] = set()

    def discover_agents(self) -> Set[str]:
        """
        Import all agent modules to trigger registration with the registry.

        This method scans the agents package directory and imports all modules
        except those in the excluded_modules list. The import process triggers
        the @register_agent decorator, which registers the agent classes with
        the registry.

        Returns:
            Set[str]: Set of module names that were successfully imported
        """
        # Get the directory of the agents package
        from .. import agents

        package_dir = os.path.dirname(agents.__file__)

        # Import all modules in the package to trigger registration
        for _, module_name, _ in pkgutil.iter_modules([package_dir]):
            # Skip excluded modules
            if module_name not in self.excluded_modules:
                try:
                    importlib.import_module(f"src.agents.{module_name}")
                    self.discovered_modules.add(module_name)
                except ImportError as e:
                    print(f"Error importing agent module {module_name}: {e}")

        return self.discovered_modules

    def get_discovered_modules(self) -> Set[str]:
        """
        Get the set of module names that were successfully discovered.

        Returns:
            Set[str]: Set of discovered module names
        """
        return self.discovered_modules
