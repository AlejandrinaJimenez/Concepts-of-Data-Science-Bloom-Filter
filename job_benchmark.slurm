#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=6G
#SBATCH --time=01:00:00
#SBATCH --job-name=bloom_filter
#SBATCH --output=%j_output.txt
#SBATCH --error=%j_error.txt

echo "=== Bloom Filter Job Started ==="
echo "Host: $(hostname)"
echo "Working directory: $(pwd)"
date

# ====================== Conda Setup ======================
module --force purge
module load conda

eval "$(conda shell.bash hook)"
conda activate base

echo "Using Python: $(which python3)"
python3 --version

# ====================== Prepare Data ======================
echo ""
echo "=== 1. Preparing data files ==="
python3 prepare_data.py

# ====================== Run Benchmark ======================
echo ""
echo "=== 2. Running Performance Benchmark (Point 7) ==="
time python3 benchmark.py

# ====================== Run Analysis ======================
echo ""
echo "=== 3. Running False Positive + Compression Analysis (Points 8 & 9) ==="
time python3 analysis.py

echo ""
echo "=== All tasks completed successfully! ==="
date