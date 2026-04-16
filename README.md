# Bloom Filter Implementation

**Course Project** – Object-Oriented Data Structures  
**Team Members:**  
- Alejandrina Jimenez Guzman
- Joffre Sanchez

## Project Overview

This project implements a **Bloom Filter** using an Object-Oriented approach in Python.  
A Bloom Filter is a space-efficient probabilistic data structure that allows fast membership testing (checking whether an element is in a set) with a controllable false positive rate.

### Key Features
- Object-Oriented design (`BloomFilter` class)
- Calculation of bit array size (`m`) and number of hash functions (`k`)
- Correctness testing with 3 different datasets
- Performance benchmarks designed for HPC
- Analysis of false positive rate and compression

## Repository Structure
bloom_filter_project/
├── bloom_filter.py          # Main Bloom Filter class (OOP)
├── test_bloom.py            # Correctness tests + 3 datasets
├── benchmark.py             # Performance benchmarks for HPC
├── job_benchmark.slurm      # SLURM job script for VSC
├── data/
│   └── words.txt            # Natural language words (download separately)
├── benchmark_*.csv          # Generated benchmark results
├── README.md                # This file
└── requirements.txt         # (optional) Python dependencies

## How to Run

### 1. Quick Demo
```bash
python bloom_filter.py
```

### 2. Run Correctness Tests
```bash
python test_bloom.py
```

### 3. Run Benchmarks (on your laptop first with small sizes)
```bash
python benchmark.py
```

### 4. Run on HPC (VSC)
```bash
sbatch job_benchmark.slurm
```

## Implementation Details

### BloomFilter Class
- **Constructor**: `BloomFilter(expected_elements: int, false_positive_rate: float = 0.01)`
- Calculates optimal `m` (bit array size) and `k` (number of hashes) automatically
- Uses `hashlib.md5` with salt for the family of hash functions

### Supported Datasets (Point 5)
We tested with **three different data types** to evaluate hash function behavior:

1. **Natural Language Words** – Real English words (good distribution)
2. **Random Strings** – Uniform random alphanumeric strings (stress test)
3. **DNA k-mers** – Fixed-length strings from alphabet {A,C,G,T}

## Time and Space Complexity (Point 6)

### Space Complexity
- **O(m)** where `m ≈ (-n × ln(p)) / (ln(2))²`
- Approximately **8–10 bits per expected element** (for p = 0.01)
- Memory usage stays constant regardless of how many items are actually inserted

### Time Complexity

| Operation              | Time Complexity       | Explanation                              |
|------------------------|-----------------------|------------------------------------------|
| `add(item)` / `insert` | **O(k)** ≈ **O(1)**   | k hash computations + k bit settings     |
| `contains(item)`       | **O(k)** ≈ **O(1)**   | k hash computations + k bit checks       |
| `add_many(N items)`    | **O(N × k)**          | Repeat single add for each item          |

- **k** is usually small (5–10), so operations are effectively constant time.
- Time does **not** depend on the current number of elements in the filter.

## Testing & Benchmarking

- **Correctness**: All basic operations tested + false positive behavior verified.
- **Hash Functions**: Tested on all 3 datasets (as required).
- **Performance**: Timed on increasing sizes (10k → 500k elements) using HPC.
- **False Positive Rate** (Point 8): Measured as function of inserted elements. Rate stays close to target when `n` is respected, but increases when the filter is overloaded.
- **Compression Rate** (Point 9): Demonstrated through theoretical formulas and empirical bit usage.

## Files Included for HPC

- `benchmark.py` – Generates timing results for insert and search
- `job_benchmark.slurm` – SLURM script to run on VSC
- CSV output files with raw benchmark data

## Conclusions

- The Bloom Filter provides excellent **time and space efficiency** at the cost of allowing a small false positive probability.
- Our implementation behaves as expected from theory: near-constant operation time and very low memory usage.
- Different datasets affect the observed false positive rate slightly, but the theoretical calculations remain valid.
- The OOP design makes the code clean, reusable, and easy to extend.

## How to Reproduce

1. Clone the repository
2. Download a large word list and place it in `data/words.txt`
3. Run `test_bloom.py` for correctness
4. Submit `job_benchmark.slurm` on the VSC cluster
5. Use the generated CSV files to create plots in Jupyter
