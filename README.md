# Python IDLE 汉化

![Pypi 总下载量](https://img.shields.io/pepy/dt/idcn?label=Pypi%20总下载量) ![GitHub 总下载量](https://img.shields.io/github/downloads/zetaloop/idle-cn/total?label=GitHub%20总下载量)


**支持版本: Python 3.8~3.13 的最新版本**（跟随 [cpython](https://github.com/python/cpython) 各分支最新源码）

<img src="https://github.com/zetaloop/IDLE-CN/assets/36418285/16f3d1a4-6e77-44d7-8a66-a396539b38d0" alt="First Image" style="width: 48%;">
<img src="https://github.com/zetaloop/IDLE-CN/assets/36418285/281674c1-69a1-4383-ba31-fdc612d7395b" alt="Second Image" style="width: 48%;">

<br>将 IDLE 的界面变为中文。

同时，修复了中文输入法下输入某些字母时误触发快捷键的问题。

## 使用方法

### 安装

打开您的命令提示符或终端，输入以下命令：
```bash
pip install idcn
# 如果连接速度比较慢的话，请在后边加上 -i https://mirrors.aliyun.com/pypi/simple
```
安装完成后，打开您的 IDLE，界面即为中文。

### 卸载

同样输入以下命令卸载：
```bash
pip uninstall idcn
```
卸载 idcn 之后您的 IDLE 将恢复原版英文。

## 遇到问题

如果在安装汉化之后 IDLE 闪退：

<details><summary>Python 版本过旧：<code>ImportError: cannot import name '_setup_dialog` from 'tkinter.simpledialog'</code></summary>
遇到这个报错，是因为 Python 版本太旧。<br>
以 Python 3.9 为例，最新的 IDLE 3.9 所使用的 _setup_dialog 函数是在 Python 3.9.5 添加的。<br>
如果您的 Python 3.9 版本比 3.9.5 更旧，就会导致 IDLE 找不到这个函数，启动闪退。<br>
要解决这个问题，请安装最新的 Python。（只需要小版本号最新即可，比如更新到 <a href="https://www.python.org/downloads/release/python-3913/">Python 3.9.13</a>）
</details>

<details><summary>配置文件编码问题：<code>UnicodeDecodeError: 'gbk' codec can't decode byte 0x83 in position 289</code></summary>
IDLE 打不开，可能是因为旧的 IDLE 配置文件的编码类型和新的（UTF-8）不一样。<br>
只需把旧的配置文件删除，然后应该就可以打开了。<br>
Windows：<code>C:\Users\%username%\.idlerc</code> 文件夹<br>
Linux/macOS：<code>~/.idlerc</code> 文件夹
</details>

如果汉化仍然闪退，请将 IDLE 的报错内容和 Python 版本告诉我（[创建议题](https://github.com/zetaloop/IDLE-CN/issues/new) / [电子邮件](mailto:zetaloop@outlook.com)），我去修复。

您可先 [卸载汉化](#卸载)，一切应该会恢复原样。<br>（如果还是闪退，参考上面配置文件编码问题，删除配置文件，现在应该真的恢复原样了）

## 开发资料

构建指南：[Build.md](https://github.com/zetaloop/IDLE-CN/blob/main/Build.md)<br>测试指南：[Test.md](https://github.com/zetaloop/IDLE-CN/blob/main/Test.md)

推荐搭配 [MapleMono NF SC](https://github.com/subframe7536/maple-font) 字体

## 项目进展
- [x] 汉化 turtledemo
- [x] 汉化 idlelib
- [x] 修复 IDLE 中文输入法误触问题
- [x] 制作 pip 汉化包
- [ ] 汉化 idle 附带的文档
- [ ] 把界面变得更现代一些
