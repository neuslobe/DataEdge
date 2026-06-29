# test_dataedge.py
"""
Tests for DataEdge module.
"""

import unittest
from dataedge import DataEdge

class TestDataEdge(unittest.TestCase):
    """Test cases for DataEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataEdge()
        self.assertIsInstance(instance, DataEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
