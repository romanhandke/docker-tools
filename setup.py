from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r') as req:
        contents = req.read()
        requirements = contents.split('\n')

    return requirements


with open('LICENSE') as f:
    license = f.read()

setup(name='docker-tools',
      version='0.1',
      author='Roman Handke',
      author_email='roman.handke@online.de',
      description='A collection of scripts simplifying tasks around docker',
      packages=find_packages(),
      install_requires=read_requirements(),
      license=license,
      entry_points={'console_scripts': ['dt=docker_tools.main:cli']})
