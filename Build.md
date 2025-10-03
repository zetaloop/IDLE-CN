# 构建 IDLE-CN

## 项目结构

汉化修改都在 base 中进行，然后移植回各个发行版。

```bash
idcn_build
│
├── cpython  # 从 python/cpython 储存库中提取的 IDLE 部分
│   ├── idlelib
│   └── turtledemo
│
└── IDLE-CN  # IDLE-CN 项目
    ├── idcn  # 汉化模块
    │   ├── releases
    │   │   ├── 3.9  # IDLE 3.9 汉化发布版
    │   │   │   ├── idlelib
    │   │   │   └── turtledemo
    │   │   └── ...  # 更多版本
    │   └── __init__.py
    │
    ├── base  # 最新汉化版本，基于 cpython@main
    │   ├── idlelib
    │   └── turtledemo
    │
    ├── Tools
    │   ├── make_release.py  # 自动移植脚本
    │   └── release_versions.txt  # 3.9 ~ 3.14
    │
    └── setup.py  # 安装脚本

```

## 手动构建

0.  请准备好 `git` 和 `python`。

    此外，还需安装 `git filter-repo` 用于从 cpython 中提取 IDLE 相关提交。

    ```bash
    pip install git-filter-repo
    ```

1.  克隆 IDLE-CN。

    ```bash
    mkdir idcn_build
    cd idcn_build

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

    比较方便的手动解决方法：从上游新建特定版本的 `3.xx-update` 分支，然后将旧的 `3.xx` 中的几个汉化提交摘取到新分支中，解决冲突，再将 `3.xx` 硬重置到新分支。

5.  打包与安装。

    本地安装：

    ```bash
    cd IDLE-CN
    pip install .
    cd ..
    ```

    打包上传至 PyPI：

    ```bash
    cd IDLE-CN
    python -m build
    twine upload dist/*
    cd ..
    ```


---

# Building IDLE-CN

## Project structure

Changes are made in the base directory, then backported to each version.

```bash
idcn_build
│
├── cpython  # Extracted IDLE from python/cpython
│   ├── idlelib
│   └── turtledemo
│
└── IDLE-CN  # IDLE-CN Project
    ├── idcn  # Translator Module
    │   ├── releases
    │   │   ├── 3.9  # IDLE 3.9 zh-CN Release
    │   │   │   ├── idlelib
    │   │   │   └── turtledemo
    │   │   └── ...  # More versions
    │   └── __init__.py
    │
    ├── base  # Patched newest IDLE source, based on cpython@main
    │   ├── idlelib
    │   └── turtledemo
    │
    ├── Tools
    │   ├── make_release.py  # Patching script
    │   └── release_versions.txt  # 3.9~3.14
    │
    └── setup.py  # Installation script
```

## Manual steps

0.  You need to have `git` and `python` installed.

    Additionally, install `git filter-repo` for extracting IDLE from cpython.

    ```bash
    pip install git-filter-repo
    ```

1.  Clone IDLE-CN.

    ```bash
    mkdir idcn_build
    cd idcn_build

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

    A convenient way to resolve conflicts manually: create a new `3.xx-update` branch from the upstream, then cherry-pick several translation commits from the old `3.xx` to the new branch, resolve conflicts, and hard reset `3.xx` to the new branch.

5.  Package and install.

    Local install:

    ```bash
    cd IDLE-CN
    pip install .
    cd ..
    ```

    Package and upload to PyPI:

    ```bash
    cd IDLE-CN
    python -m build
    twine upload dist/*
    cd ..
    ```
```