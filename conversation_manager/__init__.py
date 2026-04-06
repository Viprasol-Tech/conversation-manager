"""
conversation-manager - Manage multi-turn conversations and memory

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ConversationManager, manage, process, main

__all__ = ["ConversationManager", "manage", "process", "main"]
