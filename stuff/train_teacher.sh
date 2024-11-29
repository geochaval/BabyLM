#!/bin/bash
#SBATCH -t 48:00:00

#SBATCH -J train_teacher_gpt

#SBATCH -o train_gpt.out

#SBATCH --mem-per-cpu=10000

#SBATCH -p gpua100i
#SBATCH --gres=gpu:1

cat $0

python -m venv myenv
source myenv/bin/activate

python 7_train_teachers.py

deactivate
