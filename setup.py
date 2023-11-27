from setuptools import setup, find_packages

__version__ = "0.6.1a999"


setup(name='ebrains-drive',
      version=__version__,
      license='Apache-2.0 License',
      description='Python client interface for EBRAINS Collaboratory Seafile storage',
      author='EBRAINS, CNRS',
      author_email='support@ebrains.eu',
      url='https://github.com/HumanBrainProject/ebrains-drive/',
      platforms=['Any'],
      packages=find_packages(),
      install_requires=['requests', 'tqdm'],
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      )
