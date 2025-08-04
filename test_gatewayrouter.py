# test_gatewayrouter.py
"""
Tests for GatewayRouter module.
"""

import unittest
from gatewayrouter import GatewayRouter

class TestGatewayRouter(unittest.TestCase):
    """Test cases for GatewayRouter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GatewayRouter()
        self.assertIsInstance(instance, GatewayRouter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GatewayRouter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
