from setuptools import setup, find_packages

setup(
    name="AircasLogger",          # 包名（pip install 时使用的名字）
    version="0.1.0",            # 版本号
    author="Chao Qin",
    description="A Logger",
    long_description=open("README.md").read(),  # 长描述（通常是README）
    long_description_content_type="text/markdown",
    url="https://github.com/XevenQC/AircasLogger",  # 项目地址
    packages=find_packages(),    # 自动查找所有包
    classifiers=[                # 分类信息（PyPI使用）
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',    # Python版本要求
    install_requires=[          # 依赖库（自动安装）
    ],
)
