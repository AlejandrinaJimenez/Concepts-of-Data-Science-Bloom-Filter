#!/bin/bash
#SBATCH --job-name=bloom_benchmark
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4          
#SBATCH --mem=8G                   # memory limit
#SBATCH --time=02:00:00            # max 2 hours 
#SBATCH --output=bloom_%j.out
#SBATCH --error=bloom_%j.err

# === Important: How to use conda on VSC (common pattern) ===
module --force purge                # clean environment
module load conda                   

# Activate conda
eval "$(conda shell.bash hook)"
conda activate base                 

# Go to project directory
cd $SLURM_SUBMIT_DIR

# Run the benchmark
python benchmark.py

echo "Benchmark job finished at $(date)"