import re

import setuptools

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

# Inspiration: https://stackoverflow.com/a/7071358/6064135
with open('meeting_summarizer/_version.py', 'r') as version_file:
    version_groups = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_groups:
        version = version_groups.group(1)
    else:
        raise RuntimeError('Unable to find version string!')

REQUIREMENTS = [
    'slack_sdk == 3.*',
    'requests == 2.*',
]

DEV_REQUIREMENTS = [
    'bandit == 1.7.*',
    'black == 23.*',
    'flake8 == 6.*',
    'isort == 5.*',
    'mypy == 1.5.*',
    'types-requests',
]

setuptools.setup(
    name='meeting-summarizer',
    version=version,
    description='Summarize your meetings with the power of Recall AI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/meeting-summarizer',
    author='justintime50',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'meeting_summarizer': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'meeting-summarizer=meeting_summarizer.my_module:main',
        ]
    },
    python_requires='>=3.8, <4',
)
