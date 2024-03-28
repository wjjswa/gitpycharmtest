#!/bin/bash

# set the number of nodes
#SBATCH --nodes=1

# set max wall-clock time
#SBATCH --time=00:01:00

# set name of job
#SBATCH --job-name=test1
# set number of GPUs
#SBATCH --gres=gpu:1

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=jw840@sussex.ac.uk

# load the module for python or anaconda if needed
# module load python/3.8.5 
# run the application
python test.py
