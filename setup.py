from setuptools import setup, find_packages

try:
    long_description = open('README.md').read()
except (IOError, UnicodeError):
    long_description = ''

setup(
    name='Uber movements',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Amar',
    author_email='amar.zlojic@gmail.com',
    packages=find_packages(),
    python_requires='>=3.8',
    url='https://github.com/',
    description='Uber movements data lake',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='',
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    license='',
    platforms=['any'],
    install_requires=[
        'python-dotenv==0.17.1',
        'mongoengine==0.23.0',
        'click==7.1.2',
    ],
)