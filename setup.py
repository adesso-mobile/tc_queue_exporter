import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tc_queue_exporter",  # Replace with your own username
    version="0.1.2",
    author="adesso mobile solutions GmbH",
    author_email="it-operations@adesso-mobile.de",
    description="Export teamcity queue data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adesso-mobile/tc_queue_exporter",
    project_urls={
        "Bug Tracker": "https://github.com/adesso-mobile/tc_queue_exporter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests","prometheus_client"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={  
        "console_scripts": [
            "tc_queue_exporter=tc_queue_exporter:run",
        ],
    },
)
