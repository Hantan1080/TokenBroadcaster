# test_tokenbroadcaster.py
"""
Tests for TokenBroadcaster module.
"""

import unittest
from tokenbroadcaster import TokenBroadcaster

class TestTokenBroadcaster(unittest.TestCase):
    """Test cases for TokenBroadcaster class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenBroadcaster()
        self.assertIsInstance(instance, TokenBroadcaster)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenBroadcaster()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
