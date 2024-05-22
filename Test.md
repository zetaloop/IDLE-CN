# Testing IDLE-CN

## Create environments

Use Anaconda/Miniconda to create testing environments for each Python version.
```bash
conda create -n pure_py38 python=3.8 -y
conda create -n pure_py39 python=3.9 -y
conda create -n pure_py310 python=3.10 -y
conda create -n pure_py311 python=3.11 -y
conda create -n pure_py312 python=3.12 -y
# conda create -n pure_py313 python=3.13 -y
#   ↑ Python 3.13 is not available yet
```

## Try IDLE-CN in each environment

Enter project directory, try IDLE-CN in each environment.
```bash
conda activate pure_py38
pip install .
python -m idlelib
conda deactivate
# Repeat for other python versions
```