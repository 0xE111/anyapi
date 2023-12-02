from pathlib import Path

from setuptools import find_packages, setup

# # allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='anyapi2',
    version='0.0.6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests<=3.0', 'tenacity<=9.0'],
    license='MIT',
    description='Boilerplate code for api integrations',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type="text/markdown",
    url='https://github.com/c0ntribut0r/anyapi',
    keywords='requests api',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
