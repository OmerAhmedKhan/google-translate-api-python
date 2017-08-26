=========================
 Google Translate API
=========================

.. image:: https://travis-ci.org/seanfisk/python-project-template.png
   :target: https://travis-ci.org/seanfisk/python-project-template

This project provides a way to get unlimited Google tranlate API without providing you API access keys. It removes all wories of limited API hit per day for free users and paying is not an option.

Project Setup
=============

Please follow these instructions to get this project running.

Instructions
------------

#. Clone the project ``google-translate-api-python``:

        git clone 
        cd google-translate-api-python


#. Install pip package through::

        pip install .

**Project setup is now complete!**


Using Google Translate API through CLI
---------
The tool ``google_translate`` provide you a cli interface which provide you results on fly, there are three actions that can be performed:
1. Supported Languages
2. Translate
3. Find and Translate

**Supported Languages**
It will display all supported languages and there codes for this API, which also include ``auto`` which means google will try to figure out the language itself


        google_translate supported_languages

**Translate Language**
It will translate provided text to a language provided through parameter, it is a fast method to translate to specific language as it will skip language guessing part.

        google_translate translate -t "Hello" -f "en" -i "ur"

The above command will translate ``Hello`` to urdu language which is ``ہیلو``. To get exact output from ``google-translate-api`` provide a opitional parameter ``-r`` which redirect raw output from Google translate API.

        google_translate translate -t "Hello" -i "ur" -r raw

**Find and Translate Language**
It is almost same as previous action translate, it just not required ``-f`` parameter and API will itself figure out the language of provided text. It also provide same optional raw parameter

        google_translate translate -t "Hello" -i "ur"



Using Google Translate API through Script
---------
TBD
 
Supported Python Versions
=========================

Google Translate API supports the following versions out of the box:

* Python 2.7


Licenses
========
TBD

Issues
======

Please report any bugs or requests that you have using the GitHub issue tracker!

Authors
=======

* Omer Ahmed Khan
