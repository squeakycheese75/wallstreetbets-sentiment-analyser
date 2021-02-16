from setuptools import setup, find_packages

# Get package requirements
with open("requirements.txt", "r") as fd:
    requirements = fd.read().strip().split("\n")

 
# See note below for more information about classifiers
classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Education',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='wallstreetBetsAnalyser',
  version='0.1.0',
  description='A tool for extracting post from the wallstreetbets reddit group and running them through a sentiment analyser (vadar).',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/squeakycheese75/wallstreetbets-sentiment-analyser',  # the URL of your package's home page e.g. github link
  author='Jamie Wooltorton',
  author_email='james_wooltorton@hotmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='wallstreetbets reddit sentiment analyser',
  packages = find_packages(exclude=['tests*']),
  include_package_data=True,
  install_requires=requirements,
)