from setuptools import setup, find_packages

setup(
    name="leopa",
    version="0.1.0",
    description="Static site generator",
    author="Masahiko Hamazawa",
    author_email="ichigyo.zanmai@gmail.com",
    license="MIT",
    url="https://github.com/masahiko-ofgp/leopa",
    classifiers=[
        'License :: OSI Approved ::MIT License',
        'Programming Language :: Python 3.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
