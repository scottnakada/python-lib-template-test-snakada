from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="python-lib-template-test-snakada",
    description="Testing python-lib-template ",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Scott Nakada",
    url="https://github.com/scottnakada/python-lib-template-test-snakada",
    project_urls={
        "Issues": "https://github.com/scottnakada/python-lib-template-test-snakada/issues",
        "CI": "https://github.com/scottnakada/python-lib-template-test-snakada/actions",
        "Changelog": "https://github.com/scottnakada/python-lib-template-test-snakada/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["python_lib_template_test_snakada"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
