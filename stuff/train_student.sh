#!/bin/bash

#SBATCH -t 48:00:00                 # Time limit: 48 hours
#SBATCH -J train_teacher_student    # Job name
#SBATCH -o train_student.out        # Output file
#SBATCH --mem-per-cpu=10000         # Memory per CPU
#SBATCH -p gpua100i                 # GPU partition
#SBATCH --gres=gpu:1                # Request 1 GPU

# Print the script content
cat $0

# Create and activate Python virtual environment
python -m venv myenv
source myenv/bin/activate

# Run the training script
python 8_train_student.py

# Deactivate virtual environment
deactivate
