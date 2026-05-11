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
        if expected_elements <= 0:
            raise ValueError("expected_elements must be > 0")
        if not (0 < false_positive_rate < 1):
            raise ValueError("false_positive_rate must be between 0 and 1 (exclusive)")

        self.expected_elements = expected_elements
        self.false_positive_rate = false_positive_rate

        self.size = self._calculate_size()           # m = bit array size
        self.num_hashes = self._calculate_num_hashes()  # k = number of hashes

        self.bit_array = [False] * self.size

        print(f"BloomFilter created -> bits: {self.size:,} | hashes: {self.num_hashes} | "
              f"expected items: {expected_elements} | target FP: {false_positive_rate}")

    def _calculate_size(self) -> int:
        """
        Optimal bit array size m
        """
        m = (-self.expected_elements * math.log(self.false_positive_rate)) / (math.log(2) ** 2)
        return int(math.ceil(m))


    def _calculate_num_hashes(self) -> int:
        """
        Optimal number of hash functions k
        """
        k = (self.size/self.expected_elements)*math.log(2)
        return int(math.ceil(k))

    def _get_hash_positions(self, item: Any) -> List[int]:
        """
        Return list of positions in the bit array for this item
        """
        positions = []
        item_bytes = str(item).encode('utf-8')

        for i in range(self.num_hashes):
            # Different hash each time by adding salt i
            hash_obj = hashlib.md5(item_bytes + str(i).encode())
            hash_int = int(hash_obj.hexdigest(), 16)
            pos = hash_int % self.size
            positions.append(pos)
        
        return positions


    def add(self, item: Any) -> None:
        """
        Add an item to the filter
        """
        positions = self._get_hash_positions(item)
        for pos in positions:
            self.bit_array[pos] = True
        
        
    def contains(self, item: Any) -> bool:
        """
        Check if item is (probably) in the filter.
        Returns False -> definitely not present
        Returns True -> possibly present (may be false positive)
        """
        positions = self._get_hash_positions(item)
        for pos in positions:
            if not self.bit_array[pos]:
                return False
        return True


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
   # print("Contains 'orange'?", "orange" in bf)  

    words = ["python", "bloom", "filter", "hash", "test"]
    bf.add_many(words)

    print("\nFinal info:")
    print(bf)
    print(bf.get_info())