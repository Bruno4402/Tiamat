#!/bin/bash

#SBATCH --job-name=rf_optuna

#SBATCH --partition=cpu

#SBATCH --nodes=1
#SBATCH --ntasks=1

#SBATCH --cpus-per-task=8

#SBATCH --mem=32G

#SBATCH --time=08:00:00

#SBATCH --output=rf_%j.out
#SBATCH --error=rf_%j.err

source ~/.bashrc

conda activate ilumpy

echo "===================="
echo "INICIO"
date
echo "===================="

python -u random_forest_optuna.py

echo "===================="
echo "FIM"
date
echo "===================="

