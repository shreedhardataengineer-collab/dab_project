from setuptools import setup, find_packages


setup(
    name="citibike_etl",
    version="0.0.2 ",
    description="This contains the code in the ./src directory of the project",
    author="Shreedhar Nara",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
    entry_points={
        "packages": [
            "main=dab_project.main:main"
        ]
    }
)