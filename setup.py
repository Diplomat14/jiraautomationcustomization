from setuptools import setup
import os

def readme():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/README.rst') as f:
        return f.read()

setup(
    name='jacustomization',
    version='0.1',
    description='jacustomization description',
    long_description=readme(),
    url='TBD',
    author='<todo_author_first_last_name>',
    author_email='<todo_author_email>',
    license='MIT', #TBD
    packages=['jacustomization'],
    install_requires=[],
    #dependency_links=['http://server/user/repo/tarball/master#egg=package-1.0'],
    entry_points = {
        'console_scripts':['jacustomization-main=jacustomization.console.command_line:main']
    },
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)