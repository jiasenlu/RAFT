from setuptools import setup, find_packages

setup(
    name="raft_flow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.6.0",
        "numpy",
        "opencv-python",
        "Pillow",
        "matplotlib",
        "tensorboard",
        "scipy"
    ],
    author="Princeton Vision Lab (Packaged by You)",
    author_email="your.email@example.com",
    description="A pip-installable version of RAFT optical flow",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/raft_flow",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)