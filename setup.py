from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name="passerelle-imio-iile-1722",
    version=version,
    author="iMio",
    author_email="support-ts@imio.be",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
    ],
    url="https://github.com/IMIO/passerelle-imio-iile-1722",
    install_requires=[
        "django>=4.2",
    ],
    zip_safe=False,
)
