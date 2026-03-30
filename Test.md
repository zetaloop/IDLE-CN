# 测试 IDLE-CN

## 在虚拟环境里手动测试 IDLE-CN

我们使用 [uv](https://docs.astral.sh/uv) 在每个 Python 发行版中试用 IDLE-CN。
```bash
uv run --python 3.14 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.13 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.12 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.11 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.10 --isolated --with idcn --no-editable -- python -m idlelib
```

---

# Testing IDLE-CN

## Try IDLE-CN in isolated environments

Use [uv](https://docs.astral.sh/uv) to try IDLE-CN in each Python version.
```bash
uv run --python 3.14 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.13 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.12 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.11 --isolated --with idcn --no-editable -- python -m idlelib
uv run --python 3.10 --isolated --with idcn --no-editable -- python -m idlelib
```