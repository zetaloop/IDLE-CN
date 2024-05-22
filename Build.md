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

3.  Create backport patches from `base`.

    ```bash
    cd IDLE-CN
    cd base
    git remote add upstream ../../cpython
    git fetch upstream
    git format-patch upstream/main
    cd ../..
    ```
4.  Set up each backport version, then apply patches.

    ```bash
    # For version 3.8
    cd IDLE-CN
    mkdir 3.8
    cd 3.8
    git init
    git remote add upstream ../../cpython
    git fetch upstream
    git checkout -t upstream/3.8
    git am ../base/*.patch
    cd ../..

    # Repeat the above steps for each additional version
    ```
