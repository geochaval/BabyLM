#!/bin/bash
#SBATCH -t 48:00:00

#SBATCH -J train_teacher_student

#SBATCH -o train_student.out

#SBATCH --mem-per-cpu=10000

#SBATCH -p gpua100i
#SBATCH --gres=gpu:1

cat $0

python -m venv myenv
source myenv/bin/activate

python 8_train_student.py

deactivate
