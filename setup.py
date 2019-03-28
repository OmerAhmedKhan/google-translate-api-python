""" Sets up Unlimited Google Translate API """
from setuptools import setup, find_packages

VERSION = '0.1.01'

setup(
    name='google_translate_api',
    version=VERSION,
    description='Kafka Admin Api',
    long_description='Unlimited Google Translate API',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'    #TODO:Change it
    ],
    keywords='oak google-translate unlimited free api',
    author='Omer Ahmed Khan',
    author_email='omerahmed122@gmail.com',
    url='https://elastica.net',
    license='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['get_token.js']},
    install_requires=['requests', 'urllib3'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'google_translate=google_translate_api_python:google_translate_api_cli'
        ]
    }
)
