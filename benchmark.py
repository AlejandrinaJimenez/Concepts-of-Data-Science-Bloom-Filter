"""
Team Members: Alejandrina Jimenez and Joffre Sanchez
Benchmark script for Bloom Filter: Designed for HPC
This script times insert and search operations while increasing the number of elements.
It supports the 3 datasets and saves results to create plots later.
"""

import time
import random
import string
import csv
import os
import sys
from typing import List, Any, Optional
from bloom_filter import BloomFilter


def generate_random_strings(n: int, length: int = 12) -> List[str]:
    random.seed(42)
    chars = string.ascii_lowercase + string.digits
    return [''.join(random.choices(chars, k=length)) for _ in range(n)]


def generate_dna_kmers(n: int, k: int = 20) -> List[str]:
    random.seed(42)
    chars = "ACGT"
    return [''.join(random.choices(chars, k=k)) for _ in range(n)]


def load_words_from_file(filename: str = "data/words.txt", 
                        max_words: Optional[int] = None) -> List[str]:
    """
    Load natural language words from a text file (one word per line).
    """
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found. Using sample data instead.", 
              file=sys.stderr)
        # Fallback sample
        return ["apple", "banana", "cherry", "date", "elephant", "flower"] * 20000

    with open(filename, "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f if line.strip()]

    # If max_words is given, take only the first N words
    if max_words is not None and max_words > 0:
        words = words[:max_words]

    return words


def run_benchmark(dataset_name: str, data: List[Any], sizes: List[int], fp_rate: float = 0.01):
    print(f" === Benchmarking {dataset_name} ===")
    results = []

    for n in sizes:
        print(f"  Running with {n:,} elements...", flush=True)

        bf = BloomFilter(expected_elements=n, false_positive_rate=fp_rate)
        items = data[:n]

        # Time Insert
        start = time.perf_counter()
        bf.add_many(items)
        insert_time = time.perf_counter() - start

        # Time Search (limited to avoid very long runs)
        start = time.perf_counter()
        test_count = min(10000, len(items))
        for item in items[:test_count]:
            _ = bf.contains(item)
        search_time = time.perf_counter() - start

        results.append({
            "dataset": dataset_name,
            "num_elements": n,
            "insert_time_sec": round(insert_time, 6),
            "search_time_sec": round(search_time, 6),
            "bit_array_size": bf.size,
            "num_hashes": bf.num_hashes
        })

        print(f"    --> Insert: {insert_time:.4f}s | Search ({test_count} lookups): {search_time:.4f}s")

    # Save to CSV
    filename = f"benchmark_{dataset_name.lower().replace(' ', '_')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"  Results saved --> {filename}")
    return results


def main():
    print("=== Bloom Filter HPC Benchmark Started === ")

    test_sizes = [10000, 50000, 100000, 250000, 500000]

    # Natural Words
    print("Loading words...")
    words = load_words_from_file("data/words.txt", max_words=600000)
    run_benchmark("Natural_Words", words, test_sizes)

    # Random Strings
    print("Generating random strings...")
    random_strs = generate_random_strings(600000)
    run_benchmark("Random_Strings", random_strs, test_sizes)

    # DNA k-mers
    print("Generating DNA k-mers...")
    dna = generate_dna_kmers(600000)
    run_benchmark("DNA_kmers", dna, test_sizes)

    print("=== All Benchmarks Completed Successfully! ===")


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    main()