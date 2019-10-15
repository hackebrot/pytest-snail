import pathlib
import setuptools


def read(*args):
    file_path = pathlib.Path(__file__).parent.joinpath(*args)
    return file_path.read_text("utf-8")


setuptools.setup(
    name="pytest-snail",
    version="0.1.0.dev1",
    author="Raphael Pierzina",
    author_email="raphael@hackebrot.de",
    maintainer="Raphael Pierzina",
    maintainer_email="raphael@hackebrot.de",
    license="MIT License",
    url="https://github.com/hackebrot/pytest-snail",
    project_urls={
        "Repository": "https://github.com/hackebrot/pytest-snail",
        "Issues": "https://github.com/hackebrot/pytest-snail/issues",
    },
    description="Plugin for adding a marker to slow running tests. 🐌",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=["pytest>=5.0.1"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["snail = pytest_snail.plugin"]},
    keywords=["pytest"],
)
