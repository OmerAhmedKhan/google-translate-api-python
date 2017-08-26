#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to provide unlimited tranlation from google tanslate api
"""
#core libraries
import json
import re
from subprocess import check_output
from urllib import urlencode
from distutils.sysconfig import get_python_lib
#core libraries
import requests # pylint: disable=import-error
from .languages import is_supported_lang, get_code

GOOGLE_TRANSLATION_URL = 'https://translate.google.com/translate_a/single'
DATA = {
    'client': 't',
    'sl': 'auto',
    'tl': 'en',
    'hl': 'en',
    'dt': ['at', 'bd', 'ex', 'ld', 'md', 'qca', 'rw', 'rm', 'ss', 't'],
    'ie': 'UTF-8',
    'oe': 'UTF-8',
    'otf': 1,
    'ssel': 0,
    'tsel': 0,
    'kc': 7,
    'q': 'Change me'
}

def translate(text, opts):  # pylint: disable=too-many-branches
    '''
    Translation core method
    param: text - Text to translate,
           opts - options to provide more control
    return: translated object
    '''
    opts = opts or {}

    if not isinstance(opts, dict):
        raise ValueError('Options should be in a dictionary')

    if not isinstance(text, basestring):
        raise ValueError('Text to translate should be in string')

    if not all([is_supported_lang(opts.get('to_lang')), is_supported_lang(opts.get('from_lang'))]):
        raise ValueError('Langauge is not supported')

    opts['from_lang'] = get_code(opts.get('from_lang'))
    opts['to_lang'] = get_code(opts.get('to_lang'))

    DATA['sl'] = opts.get('from_lang')
    DATA['tl'] = opts.get('to_lang')
    DATA['hl'] = opts.get('to_lang')
    DATA['q'] = text

    # This may seems amature way to do this, but this is the only way for now
    try:
        package_path = get_python_lib()
        print get_python_lib()
        token_file_path = '{}/google_translate_api_python/get_token.js'.format(package_path)
        token_obj = json.loads(check_output(['nodejs', token_file_path, text]))
    except Exception as e:
        print e
        raise Exception('Unable to get google API token')

    DATA[token_obj.get('name')] = token_obj.get('value')
    url = u'{}?{}'.format(GOOGLE_TRANSLATION_URL, urlencode(DATA, doseq=True))

    try:
        response = requests.get(url)
    except Exception as e:
        raise Exception(e)

    try:
        body = json.loads(response.content)
    except Exception:
        raise ValueError('Unable to load JSON')

    result = {
        'text': '',
        'from_lang': {
            'language': {
                'didYouMean': False,
                'iso': ''
            },
            'text': {
                'autoCorrected': False,
                'value': '',
                'didYouMean': False
            }
        },
        'raw': ''
    }

    if opts.get('raw'):
        result['raw'] = body

    for obj in body[0]:
        if obj[0]:
            result['text'] += obj[0]

    if body[2] == body[8][0][0]:
        result['from_lang']['language']['iso'] = body[2]
    else:
        result['from_lang']['language']['didYouMean'] = True
        result['from_lang']['language']['iso'] = body[8][0][0]

    if body[7] and body[7][0]:
        val = body[7][0]
        val = re.sub(r'<b><i>', '[', val)
        val = re.sub(r'<\/i><\/b>', ']', val)
        result['from_lang']['text']['value'] = val

        if body[7][5]:  # pylint: disable=simplifiable-if-statement
            result['from_lang']['text']['autoCorrected'] = True
        else:
            result['from_lang']['text']['didYouMean'] = True

    return result


def main():
    """
    Test/Console method
    """
    import argparse
    parser = argparse.ArgumentParser(\
        description='Script to provide unlimited tranlation from google tanslate api')
    parser.add_argument('-t', '--text', help='Text to translate', required=True)
    parser.add_argument('-i', '--in_lang', \
        help='Language name or code for text to translate in. e.g("ur", "en")', required=True)
    parser.add_argument('-f', '--from_lang', \
        help='Language name or code for provided text. e.g("ur", "en")', default='auto')
    parser.add_argument('-r', '--raw_response', \
        help='Language name or code for provided text. e.g("ur", "en")', default='')
    args = parser.parse_args()

    opts = {
        'to_lang': args.in_lang,
        'from_lang': args.from_lang,
        'raw': args.raw_response
    }
    text = args.text

    try:
        print translate(text, opts)
    except Exception as e:   # pylint: disable=broad-except
        print 'Something went wrong!'
        print e

if __name__ == '__main__':
    main()

# pylint 10.00/10
