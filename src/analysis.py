"""
This program calulates False Positive Rate + Compression Analysis experiments
Uses insert_words.txt and not_insert_words.txt
"""

from bloom_filter import BloomFilter
import random
import csv


def load_words(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]


def false_positive_overload_analysis():
    """
    False Positive Rate as function of inserted elements (overload test)
    """
    print("=== False Positive Rate Analysis (Point 8) === ")

    insert_words = load_words("data/inserted_words.txt")
    not_insert_words = load_words("data/not_inserted_words.txt")

    print(f"Loaded {len(insert_words):,} words for insertion")
    print(f"Loaded {len(not_insert_words):,} words for false positive testing")

    expected_n = 50000
    target_fp = 0.01
    results = []

    bf = BloomFilter(expected_elements=expected_n, false_positive_rate=target_fp)

    # Test at different load levels (including overload)
    test_points = [10000, 25000, 50000, 75000, 100000, 150000, 200000]

    for n_inserted in test_points:
        # Add more words up to n_inserted
        current_batch = insert_words[:n_inserted]
        bf.add_many(current_batch)

        # Measure FP rate using words that were NEVER inserted
        sample_size = min(10000, len(not_insert_words))
        fp_count = sum(1 for word in not_insert_words[:sample_size] if bf.contains(word))
        fp_rate = fp_count / sample_size

        fill_ratio = bf.get_info()['fill_ratio']

        results.append({
            "inserted": n_inserted,
            "fp_rate": round(fp_rate, 4),
            "fill_ratio": round(fill_ratio, 4),
            "bit_array_size": bf.size
        })

        print(f"Inserted: {n_inserted:6,} | FP Rate: {fp_rate:.4f} | Fill Ratio: {fill_ratio:.3f}")

    # Save results
    with open("fp_rate_analysis.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("False Positive analysis saved to fp_rate_analysis.csv")


def compression_rate_analysis():
    """
    Compression rate
    """
    print("=== Compression Rate Analysis (Point 9) ===")

    expected_list = [10000, 50000, 100000, 500000]
    fp_list = [0.001, 0.01, 0.05, 0.1]

    print("expected_n\tfp_rate\tbit_array_size\tbits_per_element")
    print("-" * 55)

    results = []
    for n in expected_list:
        for p in fp_list:
            bf = BloomFilter(expected_elements=n, false_positive_rate=p)
            bits_per_item = bf.size / n

            print(f"{n:7,}\t{p:.3f}\t{bf.size:10,}\t{bits_per_item:.2f}")

            results.append({
                "expected_n": n,
                "false_positive_rate": p,
                "bit_array_size": bf.size,
                "bits_per_element": round(bits_per_item, 3)
            })

    with open("compression_analysis.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("Compression analysis saved to compression_analysis.csv")


if __name__ == "__main__":
    random.seed(42)
    false_positive_overload_analysis()
    compression_rate_analysis()
    print("Analysis completed!")