from setuptools import setup, find_packages

setup(
    name="vertex-xgb-fraud",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "xgboost",
        "joblib"
    ]
)
