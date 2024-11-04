# 测试 IDLE-CN

## 创建虚拟环境

我们使用 Anaconda/Miniconda 为每个 Python 发行版创建测试环境。
```bash
conda create -n py38 python=3.8 -y
conda create -n py39 python=3.9 -y
conda create -n py310 python=3.10 -y
conda create -n py311 python=3.11 -y
conda create -n py312 python=3.12 -y
conda create -n py313 python=3.13 -y
```

## 在每个环境里手动测试 IDLE-CN

进入项目文件夹，在每个测试环境中试用 IDLE-CN。
```bash
conda activate py38
pip install .
python -m idlelib
conda deactivate
# 剩余版本重复上述步骤
```

---

# Testing IDLE-CN

## Create environments

Use Anaconda/Miniconda to create testing environments for each Python version.
```bash
conda create -n py38 python=3.8 -y
conda create -n py39 python=3.9 -y
conda create -n py310 python=3.10 -y
conda create -n py311 python=3.11 -y
conda create -n py312 python=3.12 -y
conda create -n py313 python=3.13 -y
```

## Try IDLE-CN in each environment

Enter project directory, try IDLE-CN in each environment.
```bash
conda activate py313
pip install .
python -m idlelib
conda deactivate
# Repeat for other python versions
```