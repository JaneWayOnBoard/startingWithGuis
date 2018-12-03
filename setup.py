from setuptools import setup

""" Here we define all the app informations in the set up """

"""module  level dunders __with double underscore__"""


""" Create a list of variables for the parameters """

__project__ = "startingWithGuis"
__version__ = "0.0.1"
__description__ = "a Python module with a few GUI functions"
__packages__ = ["guiTest"]
__author__ = "JaneWay"
__classifiers__ = "classifiers" 


setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,    
    classifiers = __classifiers__,

)

"""Create a list of classifiers and pass it to the set up function"""

__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]

"""Create a list of keywords and pass it to the set up function"""

