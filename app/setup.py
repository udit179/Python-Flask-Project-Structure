from setuptools import setup

# Package - A folder/directory that contains __init__.py file.
# Module - A valid python file with .py extension.
# Distribution - How one package relates to other packages and modules.

with open("/home/dev2/Desktop/ERP/requirements.txt", 'r') as f:
    long_description = f.read()

setup(
    name='app',
    # version='1.0',
    # description='A useful module',
    license = "BSD",
    long_description=long_description,
    # author='',
    # author_email='foomail@foo.com',
    url="https://pypi.org/ERP",
    # packages=[''],  #same as name
    # install_requires=['pandas', 'numpy'], #external packages as dependencies
    # scripts=[
    #             'scripts/cool',
    #             'scripts/skype',
    #         ]
)