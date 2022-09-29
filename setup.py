from setuptools import find_packages, setup

setup(
    name='Packagename',
    packages=find_packages(include=['Packagename', 'Packagename.*']),
    version='0.1.1',
    description='smt',
    author='smo',
    # license='MIT',
    install_requires=[]
)
