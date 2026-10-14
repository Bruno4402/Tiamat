#!/bin/bash

#SBATCH --job-name=gb_optuna

#SBATCH --partition=cpu

#SBATCH --nodes=1
#SBATCH --ntasks=1

#SBATCH --cpus-per-task=8

#SBATCH --mem=32G

#SBATCH --time=08:00:00

#SBATCH --output=gb_%j.out
#SBATCH --error=gb_%j.err

source ~/.bashrc

echo "===================="
echo "INICIO"
date
echo "===================="

python -u gradient_boosting_optuna.py

echo "===================="
echo "FIM"
date
echo "===================="
