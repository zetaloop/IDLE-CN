# 构建 IDLE-CN

## 项目结构

汉化修改都在 base 中进行，然后移植回各个发行版。

```bash
idlecn_build
│
├── cpython  # 从 python/cpython 储存库中提取 IDLE 部分
│   ├── idlelib
│   └── turtledemo
│
└── IDLE-CN
    ├── base  # 最新汉化版本，基于 cpython@main
    │   ├── idlelib
    │   └── turtledemo
    │
    ├── 3.8  # cpython@3.8 的移植
    │   ├── idlelib
    │   └── turtledemo
    │
    ...  # 更多版本
    │
    ├── __init__.py
    └── setup.py
```

## 手动构建

0.  请准备好 `git` 和 `python`。

    此外，还需安装 `git filter-repo` 用于从 cpython 中提取 IDLE 相关提交。

    ```bash
    pip install git-filter-repo
    ```

1.  克隆 IDLE-CN。

    ```bash
    mkdir idlecn_build
    cd idlecn_build

    # 克隆 IDLE-CN
    git clone https://github.com/zetaloop/IDLE-CN.git
    cd IDLE-CN
    git submodule update --init --recursive
    cd ..
    ```

2.  克隆 cpython 并提取 IDLE。

    ```bash
    git clone https://github.com/python/cpython.git
    cd cpython
    git filter-repo --path Lib/idlelib --path Lib/turtledemo --path-rename Lib/idlelib:idlelib --path-rename Lib/turtledemo:turtledemo --force
    cd ..
    ```

3.  创建并应用补丁。

    ```bash
    python .\IDLE-CN\Tools\make_release.py
    ```

4.  查看所有产生的 `*.rej` 冲突文件，手动解决补丁冲突。

---

# Building IDLE-CN

## Project structure

Changes are made in the base directory, then backported to each version.

```bash
idlecn_build
│
├── cpython  # Extracted IDLE from python/cpython
│   ├── idlelib
│   └── turtledemo
│
└── IDLE-CN
    ├── base  # Patched newest IDLE, based on cpython@main
    │   ├── idlelib
    │   └── turtledemo
    │
    ├── 3.8  # cpython@3.8 backport
    │   ├── idlelib
    │   └── turtledemo
    │
    ...  # More versions
    │
    ├── __init__.py
    └── setup.py
```

## Manual steps

0.  You need to have `git` and `python` installed.

    Additionally, install `git filter-repo` for extracting IDLE from cpython.

    ```bash
    pip install git-filter-repo
    ```

1.  Clone IDLE-CN.

    ```bash
    mkdir idlecn_build
    cd idlecn_build

    # Clone IDLE-CN
    git clone https://github.com/zetaloop/IDLE-CN.git
    cd IDLE-CN
    git submodule update --init --recursive
    cd ..
    ```

2.  Clone cpython and extract IDLE.

    ```bash
    git clone https://github.com/python/cpython.git
    cd cpython
    git filter-repo --path Lib/idlelib --path Lib/turtledemo --path-rename Lib/idlelib:idlelib --path-rename Lib/turtledemo:turtledemo --force
    cd ..
    ```

3.  Create and apply patches.

    ```bash
    python .\IDLE-CN\Tools\make_release.py
    ```

4.  Read all `*.rej` files and resolve conflicts manually.
