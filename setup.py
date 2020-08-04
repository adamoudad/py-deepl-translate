from setuptools import setup, find_packages
setup(
    name='py-deepl-translate',
    version='0.0.7',
    description='DeepL Translator using Selenium',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/adamoudad/py-deepl-translate',
    author='adamoudad',
    packages=find_packages(),
    python_requires='>=3.8',
    include_package_data=True,
    license='MIT',
    install_requires=['selenium==3.141'],
    entry_points={
        'console_scripts': [
            'deepl=deepl.main:main'
        ]
    }
)
