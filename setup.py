from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''Returns a list of requirements'''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]
        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
    return requirement


setup(
name='MlProject',
version='0.0.1',
author='Manish',
author_email='manishsoni94601@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)