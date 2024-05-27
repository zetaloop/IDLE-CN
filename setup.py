from setuptools import setup
from pathlib import Path
import os


def find_idlecn_release_files():
    release_dir = Path("idlecn/releases")
    release_files = []
    for file in release_dir.rglob("*"):
        if file.is_file():
            release_files.append(str(file.relative_to("idlecn")))
    return release_files


setup(
    name="idlecn",
    version="1.0.0",
    author="zetaloop",
    author_email="zetaloop@outlook.com",
    description="IDLE Chinese Translation | IDLE 汉化包",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zetaloop/IDLE-CN",
    packages=["idlecn"],
    package_data={"idlecn": find_idlecn_release_files()},
    data_files=[("Lib/site-packages", ["idlecn.pth"])],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)
