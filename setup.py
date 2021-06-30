import sys
import time
from setuptools import setup, find_packages

if '--release' in sys.argv:
  IS_RELEASE = True
  sys.argv.remove('--release')
else:
  # Build a nightly package by default.
  IS_RELEASE = False

# Environment-specific dependencies.
extras = {
    'jax': ['jax==0.2.14', 'jaxlib==0.1.67', 'dm-haiku==0.0.4', 'optax==0.0.8'],
    'torch': ['torch', 'torchvision', 'dgl', 'dgllife']
}


# get the version from deepchem/__init__.py
def _get_version():
  with open('deepchem/__init__.py') as fp:
    for line in fp:
      if line.startswith('__version__'):
        g = {}
        exec(line, g)
        base = g['__version__']
        if IS_RELEASE:
          return base
        else:
          # nightly version : .devYearMonthDayHourMinute
          if base.endswith('.dev') is False:
            # Force to add `.dev` if `--release` option isn't passed when building
            base += '.dev'
          return base + time.strftime("%Y%m%d%H%M%S")

    raise ValueError('`__version__` not defined in `deepchem/__init__.py`')


setup(
    name='deepchem',
    version=_get_version(),
    url='https://github.com/deepchem/deepchem',
    maintainer='DeepChem contributors',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT',
    description='Deep learning models for drug discovery, \
        quantum chemistry, and the life sciences.',
    keywords=[
        'deepchem',
        'chemistry',
        'biology',
        'materials-science',
        'life-science',
        'drug-discovery',
    ],
    packages=find_packages(exclude=["*.tests"]),
    project_urls={
        'Documentation': 'https://deepchem.readthedocs.io/en/latest/',
        'Source': 'https://github.com/deepchem/deepchem',
    },
    install_requires=[
        'joblib',
        'numpy',
        'pandas',
        'scikit-learn',
        'scipy',
    ],
    extras_require=extras,
    python_requires='>=3.5')
