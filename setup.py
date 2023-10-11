from setuptools import setup, find_packages

# make sure the etl script outputs properly

setup(
    name="ETLpipelineTinaYi",
    version="0.1.0",
    description="ETLpipline",
    author="Tina Yi",
    author_email="tina.yi@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)
