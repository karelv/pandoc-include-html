from setuptools import setup
from os import path

version = '0.0.0'

repo_base_dir = path.abspath(path.dirname(__file__))

# Long description
readme = path.join(repo_base_dir, 'README.md')
with open(readme) as f:
    long_description = f.read()

setup(
    name='pandoc-include-html',
    version=version,
    description='Pandoc filter to allow raw html file includes',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='karelv',
    license='MIT',
    url='https://github.com/karelv/pandoc-include-html',

    install_requires=['panflute>=1'],
    # Add to lib so that it can be included
    py_modules=['pandoc_include_html'],
    entry_points={
        'console_scripts': [
            'pandoc-include-html = pandoc_include_html:main'
        ]
    },

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License'
    ]
)
