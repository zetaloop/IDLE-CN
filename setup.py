from setuptools import setup
from pathlib import Path
import sys


def find_idcn_release_files():
    release_dir = Path("idcn/releases")
    release_files = []
    for file in release_dir.rglob("*"):
        if file.is_file():
            release_files.append(str(file.relative_to("idcn")))
    return release_files


def get_site_packages_dir():
    if sys.platform == "win32":
        return "lib/site-packages"
    else:
        return "lib/python{0}/site-packages".format(
            ".".join(str(i) for i in sys.version_info[:2])
        )


setup(
    name="idcn",
    version="1.0.1",
    author="zetaloop",
    author_email="zetaloop@outlook.com",
    description="IDLE Chinese Translation | IDLE 汉化包",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zetaloop/IDLE-CN",
    packages=["idcn"],
    package_data={"idcn": find_idcn_release_files()},
    data_files=[(get_site_packages_dir(), ["idcn.pth"])],
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
