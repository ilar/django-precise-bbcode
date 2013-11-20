from os.path import abspath
from os.path import dirname
from os.path import join
from setuptools import find_packages
from setuptools import setup


def read_relative_file(filename):
    """
    Returns contents of the given file, whose path is supposed relative
    to this module.
    """
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


setup(
    name='django-precise-bbcode',
    version=read_relative_file('VERSION').strip(),
    author='Morgan Aubert',
    author_email='morgan.aubert@zoho.com',
    packages=find_packages(),
    include_package_data=True,
    license='BSD license, see LICENSE file',
    description='A django BBCode integration..',
    long_description=open('README.rst').read(),
    zip_safe=False,
    install_requires=[
        "django",
        "south",
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
