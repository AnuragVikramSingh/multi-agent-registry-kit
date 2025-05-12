"""
Setup script for the MultiAgentRegistryKit package.

This script configures the package for distribution and installation.
It reads metadata from README.md and requirements.txt to populate
package information and dependencies.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README.md for the long description
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = [
        line.strip() for line in f if line.strip() and not line.startswith("#")
    ]

setup(
    name="multi-agent-registry-kit",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "multi-agent-registry-kit=main:main",
        ],
    },
    python_requires=">=3.12",
    description="An extensible framework for building modular and intelligent multi-agent systems, with dynamic routing based on user intent.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anurag Vikram Singh",
    author_email="anuragvikramsingh@outlook.com",
    url="https://github.com/AnuragVikramSingh/multi-agent-registry-kit",
    project_urls={
        "Bug Tracker": "https://github.com/AnuragVikramSingh/multi-agent-registry-kit/issues",
        "Documentation": "https://github.com/AnuragVikramSingh/multi-agent-registry-kit#readme",
        "Source Code": "https://github.com/AnuragVikramSingh/multi-agent-registry-kit",
    },
    keywords="llm, agents, orchestration, routing, langchain, bedrock, claude, ai",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
)
