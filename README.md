# Bloom Filter Project

**Course:** Concepts of Data Science  
**Team Members:** Alejandrina Jimenez Guzman and Joffre Sanchez

## Project Overview

This project implements a **Bloom Filter** using an **Object-Oriented approach** in Python.  
A Bloom Filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set.

## Repository Structure

```text
bloom-filter-project/
├── README.md
├── Bloom_Filter_Implementation.ipynb
├── src/                    # Source code
│   ├── bloom_filter.py
│   ├── test_bloom.py
│   ├── prepare_data.py
│   ├── benchmark.py
│   └── analysis.py
├── data/                   # Input datasets
│   ├── insert_words.txt
│   └── not_insert_words.txt
├── HPC_scripts/                   # HPC job scripts
│   └── job_benchmark.slurm
├── results/                # Benchmark outputs from HPC
│   ├── benchmark_*.csv
│   ├── fp_rate_analysis.csv
│   └── compression_analysis.csv
```

## How to Run

### Locally

```bash
cd src
python3 test_bloom.py           # Correctness tests
python3 prepare_data.py         # Prepare insert/not_insert files
python3 benchmark.py            # Performance test
python3 analysis.py             # False positive & compression analysis
```

### On HPC (VSC)

```bash
sbatch jobs/job_benchmark.slurm
```

## Implementation

The Bloom Filter is implemented as a class in `src/bloom_filter.py`.

Key features:

- Automatic calculation of optimal bit array size (`m`) and number of hash functions (`k`)
- Multiple hash functions using salted MD5
- Support for `add()`, `contains()`, and `add_many()`

## Time and Space Complexity

### Space Complexity

- Main memory usage comes from the bit array of size **m**.
- Formula:

  **m ≈ (-n × ln(p)) / (ln(2))²**

- **Asymptotic**: **O(m)**
- For typical parameters (p = 0.01), this gives approximately **9.6 bits per expected element**.

### Time Complexity

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `add(item)` / `insert` | **O(k)** ≈ **O(1)** | Compute k hashes + set k bits |
| `contains(item)` | **O(k)** ≈ **O(1)** | Compute k hashes + check k bits |
| `add_many(N items)` | **O(N × k)** | Repeat single add for each item |

- **k** is small (usually 5–10), making operations effectively constant time.
- Time complexity is **independent** of the current number of elements stored (a major advantage of Bloom Filters).

## Datasets Used

- **Natural Language Words** (`insert_words.txt`)
- **Random Strings** (generated)
- **DNA k-mers** (generated)

Tested with at least two different data types as required.

## Results

### Performance Benchmarks

- Executed on **VSC Genius** cluster using SLURM.
- Insert and search times measured for up to 500,000 elements.
- Results available in `results/benchmark_*.csv`

### False Positive Rate

- Analyzed how FP rate changes when exceeding designed capacity.
- Results in `results/fp_rate_analysis.csv`

### Compression Rate

- Bits per element for different `n` and `p`.
- Results in `results/compression_analysis.csv`

See `notebooks/plots.ipynb` for all visualizations and detailed analysis.

## Conclusions

- The implementation behaves as expected from theory: near-constant operation time and excellent space efficiency.
- False positive rate stays close to the target when not overloaded and increases predictably beyond capacity.
- Different data types (natural words, random strings, DNA) show consistent performance.
- All project requirements have been fulfilled, including HPC benchmarking, multiple datasets, and thorough testing.

## References

- Bloom Filter theory (Wikipedia + course materials)
- VSC HPC documentation for SLURM and conda

---


