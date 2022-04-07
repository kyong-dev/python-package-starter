import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.6',
    install_requires=["aiohttp", "another_project_name[extras_require_key]"],
    extras_require={
        'PDF': ["ReportLab>=1.2", "RXP"],
        'reST': ["docutils>=0.3"],
    },
    entry_points={
        'console_scripts': ['shortcut1 = package.module:func', ],
        'gui_scripts': ['shortcut2 = package.module:func', ]
    },
    test_suite=['tests.test_module.suite'],
)
