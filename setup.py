from setuptools import setup, find_packages

setup(
    name="ProofReader",
    version="1.0.0",
    description="A proofreader of English texts",
    author="Julian Dosch",
    author_email="Dosch@bio.uni-frankfurt.de",
    packages=find_packages(),
    entry_points={
        'console_scripts': ["proofread = proofreader.proofread:main"],
    },
    license="GPL-3.0",
)
