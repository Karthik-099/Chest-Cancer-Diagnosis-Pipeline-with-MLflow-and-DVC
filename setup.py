import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chest-Cancer-Diagnosis-Pipeline-with-MLflow-and-DVC"
AUTHOR_USER_NAME = "Karthik-099"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "kumarkarthik09925@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An end-to-end pipeline for chest cancer diagnosis using machine learning. This project employs MLflow for experiment tracking and DVC for data versioning, ensuring efficient data management and reproducibility. Features include data preprocessing, model training, evaluation, and deployment within an MLOps framework." ,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)