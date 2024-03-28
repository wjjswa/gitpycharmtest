#!/bin/bash

# set the number of nodes
#SBATCH --nodes=1

# set max wall-clock time
#SBATCH --time=10:00:00

# set name of job
#SBATCH --job-name=job123

# set number of GPUs
#SBATCH --gres=gpu:1

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=john.brown@gmail.com

# load the module for python or anaconda if needed
# module load python/3.8.5 or something similar

# run the application
python test.py
