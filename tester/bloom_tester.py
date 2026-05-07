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


def run_tests():
    print("=== Starting Bloom Filter Tests ===\n")
    print("1. Basic correctness test")
    bf = BloomFilter(expected_elements=1000, false_positive_rate=0.05)
    test_items = ["cat", "dog", "bird", 42, "python"]
    bf.add_many(test_items)

    for item in test_items:
        assert bf.contains(item), f"Should contain {item}"
    print("All inserted items are detected\n")
    print("2. Testing with 3 different datasets (same filter parameters)")

    expected_n = 50000
    target_fp = 0.01
    bf = BloomFilter(expected_elements=expected_n, false_positive_rate=target_fp)

    words = ["apple", "banana", "cherry", "date", "elephant", "flower"] * 8000  # ~48k items
    words = list(set(words))  # make unique
    print(f"   Words dataset size: {len(words)}")

    random_strs = generate_random_strings(expected_n + 10000)

    dna = generate_dna_kmers(expected_n + 10000)

    datasets = [
        ("Natural Words", words[:expected_n]),
        ("Random Strings", random_strs[:expected_n]),
        ("DNA k-mers", dna[:expected_n])
    ]

    for name, data in datasets:
        print(f"\n   → Testing {name}")
        bf = BloomFilter(expected_elements=expected_n,
                         false_positive_rate=target_fp)  # fresh filter each time for fairness

        split = int(0.8 * len(data))
        inserted = data[:split]
        not_inserted = data[split:split + 10000]

        bf.add_many(inserted)

        fp_rate = measure_false_positive_rate(bf, inserted, not_inserted)
        print(f"Fill ratio: {bf.get_info()['fill_ratio']}")

    print("\nDataset tests completed")

    print("\n3. False positive rate when exceeding capacity")
    bf = BloomFilter(expected_elements=10000, false_positive_rate=0.01)
    items = generate_random_strings(30000)
    not_inserted = generate_random_strings(5000)

    fp_rates = []
    for i in range(0, len(items), 5000):
        batch = items[i:i + 5000]
        bf.add_many(batch)
        fp = measure_false_positive_rate(bf, items[:i + 5000], not_inserted)
        fp_rates.append((i + 5000, fp))

    print("FP rate increases as we overload the filter (expected behavior)")

    print("\n All tests finished!")


if __name__ == "__main__":
    random.seed(42)
    run_tests()