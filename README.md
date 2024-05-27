# Python IDLE 汉化

**支持版本: Python 3.8~3.13**（跟随 [cpython](https://github.com/python/cpython) 各分支最新源码）

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

## 开发资料

构建指南：[Build.md](https://github.com/zetaloop/IDLE-CN/blob/main/Build.md)<br>测试指南：[Test.md](https://github.com/zetaloop/IDLE-CN/blob/main/Test.md)

推荐搭配 [MapleMono NF SC](https://github.com/subframe7536/maple-font) 字体

## 项目进展
- [x] 汉化 turtledemo
- [x] 汉化 idlelib
- [x] 修复 IDLE 中文输入法误触问题
- [x] 制作 pip 汉化包
- [ ] 完整汉化 idle 文档
- [ ] 把界面变得更现代一些
