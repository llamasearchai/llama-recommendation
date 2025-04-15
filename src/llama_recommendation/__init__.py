"""
llama_recommender - A privacy-preserving multi-modal recommendation system.

This package provides a comprehensive suite of tools for building and deploying
privacy-preserving recommendation systems that support multi-modal content,
graph-based recommendation, causal inference, and ethical considerations.
"""

__version__ = "0.1.0"

import os

from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Import key components for easy access
from llama_recommender.core.models import (
    BaseModel,
    CausalModel,
    GraphModel,
    MultiModalModel,
)
from llama_recommender.recommender import RecommenderSystem

# Verify required environment variables
required_env_vars = ["LLAMA_API_KEY", "LLAMA_ENCRYPTION_KEY"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    import warnings

    warnings.warn(
        f"Missing required environment variables: {', '.join(missing_vars)}. "
        "Some functionality may not work properly.",
        RuntimeWarning,
    )

# Package metadata
__author__ = "Nik Jois"
__email__ = "nikjois@llamasearch.ai" = "Nik Jois"
__email__ = "nikjois@llamasearch.ai" = "Nik Jois"
__email__ = "nikjois@llamasearch.ai"
__license__ = "MIT"
