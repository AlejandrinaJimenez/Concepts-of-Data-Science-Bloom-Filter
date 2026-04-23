"""
Bloom Filter Implementation - Object-Oriented Approach
Team Members: Alejandrina Jimenez and Joffre Sanchez
"""

import hashlib
import math
from typing import List, Any


class BloomFilter:
    """
    Simple Bloom Filter using multiple hash functions.
    """

    def __init__(self, expected_elements: int, false_positive_rate: float = 0.01):
        """
        Create a new Bloom Filter.

        Parameters:
            expected_elements (int): Number of items you expect to add (n)
            false_positive_rate (float): Desired false positive probability (e.g. 0.01 = 1%)
        """


    def _calculate_size(self):
        """
        Optimal bit array size m
        """
        pass


    def _calculate_num_hashes(self):
        """
        Optimal number of hash functions k
        """
        pass

    def _get_hash_positions(self, item: Any):
        """
        Return list of positions in the bit array for this item
        """
        pass

    def add(self, item: Any):
        """
        Add an item to the filter
        """
        pass
        

    def contains(self, item: Any):
        """
        Check if item is (probably) in the filter.
        Returns False -> definitely not present
        Returns True -> possibly present (may be false positive)
        """
        pass

  

    def add_many(self, items: List[Any]):
        """
        Add a list of items efficiently
        """
        

    def get_info(self):
        """
        Return current state information
        """
        pass

    def __str__(self):
        pass



if __name__ == "__main__":
    print("=== Bloom Filter Quick Demo ===\n")

    bf = BloomFilter(expected_elements=10000, false_positive_rate=0.01)

    bf.add("apple")
    bf.add("banana")
    bf.add(12345)

    print("Contains 'apple'?", bf.contains("apple"))
    print("Contains 'orange'?", "orange" in bf)  

    words = ["python", "bloom", "filter", "hash", "test"]
    bf.add_many(words)

    print("\nFinal info:")
    print(bf)
    print(bf.get_info())