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

def measure_false_positive_rate(bf: BloomFilter, inserted: List[Any], not_inserted: List[Any]) -> float:
    false_positives = 0
    for item in not_inserted:
        if bf.contains(item):
            false_positives += 1

    fp_rate = false_positives / len(not_inserted) if not_inserted else 0
    print(f"False Positive Rate: {fp_rate:.4f}  ({false_positives}/{len(not_inserted)})")
    return fp_rate

