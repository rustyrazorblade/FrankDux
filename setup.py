from distutils.core import setup
from setuptools import find_packages

setup(
        name='FrankDux',
        version='0.1',
        packages=['frankdux'],
        url='https://github.com/rustyrazorblade/FrankDux',
        license='License :: OSI Approved :: BSD License',
        author='Jon Haddad',
        author_email='jon@jonhaddad.com',
        description='Framework for ZeroMQ and CapnProto',
        entry_points={
            'console_scripts': [
                'frankdux=frankdux.cli:main'
            ]
        },

)
