""" Command-line invocation helper """
# --- core python imports
import argparse
# --- core python imports
# --- local imports
from .languages import is_supported_lang, LANGUAGES
from .translate import translate as translate_method
# --- local imports
# --- globals
# --- globals


def google_translate_api_cli():
    """ Google Translate API CLI Invocation Facility """
    msg = 'Failed to exectue API'
    parser = argparse.ArgumentParser(description='Google Translate API')

    actions = parser.add_subparsers(dest='action', help='supported Google Translate API actions')

    find_and_translate = actions.add_parser('find_and_translate', \
        help='Found the language origin and then tranlate it')
    translate = actions.add_parser('translate', help='Tranlate from provided language origin')
    supported_langs = actions.add_parser('supported_languages', help='List all supported languages')

    supported_langs.add_argument('-l', '--list', \
        help='List all supported langugaes', default='')

    find_and_translate.add_argument('-t', '--text', help='Text to translate', required=True)
    find_and_translate.add_argument('-i', '--in_lang', \
        help='Language name or code for text to translate in. e.g("ur", "en")', required=True)
    find_and_translate.add_argument('-f', '--from_lang', \
        help='Language name or code for provided text. e.g("ur", "en")', default='auto')
    find_and_translate.add_argument('-r', '--raw_response', \
        help='Language name or code for provided text. e.g("ur", "en")', default='')

    translate.add_argument('-t', '--text', help='Text to translate', required=True)
    translate.add_argument('-i', '--in_lang', \
        help='Language name or code for text to translate in. e.g("ur", "en")', required=True)
    translate.add_argument('-f', '--from_lang', \
        help='Language name or code for provided text. e.g("ur", "en")', required=True)
    translate.add_argument('-r', '--raw_response', \
        help='Language name or code for provided text. e.g("ur", "en")', default='')

    args = parser.parse_args()
    if args.action == 'supported_languages':
        print LANGUAGES
        return

    text = getattr(args, 'text', None)
    to_lang = getattr(args, 'in_lang', None)
    from_lang = getattr(args, 'from_lang', 'auto')

    if not isinstance(text, basestring):
        raise ValueError('Text to translate should be in string')

    if not all([is_supported_lang(to_lang), is_supported_lang(from_lang)]):
        raise ValueError('Langauge is not supported')

    result = translate_method(text, {'from_lang': from_lang, 'to_lang':to_lang, 'raw':getattr(args, 'raw_response', None)})

    if getattr(args, 'raw_response', None):
        print result.get('raw', 'something went wrong')
    else:
        print result.get('text', 'something went wrong')


# pylint 10.00/10.00
