# Bloom Filter Implementation

**Course Name** – Concepts of Data Science
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
```text
├── bloom_filter.py          # Main Bloom Filter class (OOP)
├── test_bloom.py            # Correctness tests + 3 datasets
├── benchmark.py             # Performance benchmarks for HPC
```

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

### 4. Run on HPC
```

## Implementation Details

### BloomFilter Class
- **Constructor**: `BloomFilter(expected_elements: int, false_positive_rate: float = 0.01)`
- Calculates optimal `m` (bit array size) and `k` (number of hashes) automatically

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


## Testing & Benchmarking


## Files Included for HPC

## Conclusions

## How to Reproduce

1. Clone the repository
2. Download a large word list and place it in `data/words.txt`
3. Run `test_bloom.py` for correctness
