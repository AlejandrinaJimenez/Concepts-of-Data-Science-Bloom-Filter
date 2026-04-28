#Script for tester

from bloom_filter_1 import BloomFilter
import random
import string
import time
from typing import List, Any

def generate_random_strings(n: int, length: int = 12) -> List[str]:
    chars = string.ascii_lowercase + string.digits
    return [''.join(random.choices(chars, k=length)) for _ in range(n)]

def generate_dna_kmers(n: int, k: int = 20) -> List[str]:
    chars = "ACGT"
    return [''.join(random.choices(chars, k=k)) for _ in range(n)]
