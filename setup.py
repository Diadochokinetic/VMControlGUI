import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read()

setuptools.setup(
    name="VMControlGUI-Diadochokinetic",
    version="0.0.1",
    author="Fabian Eckstein",
    author_email="diadochokinetic@gmail.com",
    description="A little GUI to start and stop my Virtual Machines with macro keys",
    long_description=long_description,
    python_requires='>3.6',
    install_requires=requirements,
    packages=['vmcontrol', 'vmcontrol.*']
)
