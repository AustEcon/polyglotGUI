from setuptools import find_packages, setup

with open('polyglotGUI/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='polyglotGUI',
    version=version,
    description='Bitcoin protocols made easy.',
    long_description=open('README.rst', 'r').read(),
    author='AustEcon',
    author_email='AustEcon0922@gmail.com',
    maintainer='AustEcon',
    maintainer_email='AustEcon0922@gmail.com',
    url='https://github.com/AustEcon/polyglotGUI',
    download_url='https://github.com/AustEcon/polyglotGUI/tarball/{}'.format(version),
    license='MIT',

    keywords=[
        'polyglotGUI',
        'metanet',
        'bitcoin sv',
        'bsv',
        'bitsv',
        'cryptocurrency',
        'payments',
        'tools',
        'wallet',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    install_requires=['bitsv', 'requests', 'pyqt5-tools', 'PyQt5'],
    extras_require={
        'cli': ('appdirs', 'click', 'privy', 'tinydb'),
        'cache': ('lmdb', ),
    },
    tests_require=['pytest'],
    packages=find_packages(),
)
