from setuptools import setup

# Get package metadata. To avoid loading the package __init__ we
# use exec instead.
with open('nuorder/_metadata.py') as fh:
    metadata = {}
    exec(fh.read(), globals(), metadata)

setup_kwargs = dict(
    name='nuorder',
    version=metadata['__version__'],
    description="Conveniently make requests to NuOrder's wholesale API",
    packages=['nuorder'],
    include_package_data=True,
    author='Jacob Magnusson',
    author_email='m@jacobian.se',
    url='https://github.com/jmagnusson/nuorder',
    license='BSD',
    platforms='any',
    install_requires=[
        'argh',
        'requests',
        'termcolor',
    ],
    extras_require={
        'test': {
            'coverage>=4.2',
            'flake8>=3.0.4',
            'pytest>=3.0.3',
            'responses>=0.5.1',
        },
    },
    entry_points={
        'console_scripts': [
            'nuorder = nuorder.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
)

if __name__ == '__main__':
    setup(**setup_kwargs)
