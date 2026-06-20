"""PostwingSDK - Python SDK for Postwing email service API."""

from .sdk import PostwingSdk
from .exceptions import PostwingSdkException

__version__ = "1.0.0"
__all__ = ["PostwingSdk", "PostwingSdkException"]
