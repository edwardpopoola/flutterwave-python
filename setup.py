from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flutterwave',

    version='1.0.0',

    description='Flutterwave',
    long_description=long_description,

    url='https://github.com/Flutterwave/flutterwave-python',

    author='Obinna Isintume',
    author_email='ibonobij@gmail',

    classifiers=[
        # Maturity
        'Development Status :: 5 - Production/Stable',
        
        # Audience
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Topic :: Software Development :: Libraries :: Python Modules'

        # License
        'License :: Freely Distributable',

        # Python version
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='Payments, Payment-integration, Payment-API, Flutterwave',

    packages=find_packages(exclude=[]),

    install_requires=['requests', 'Crypto', 'hashlib'],

    entry_points={}
)