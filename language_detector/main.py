"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here
    text = text.lower()
    count = {}
    for i, val in enumerate(LANGUAGES):
        ct=0
        for word in text.split(' '):
            if word in LANGUAGES[i]['common_words']:
                ct +=1
        count[LANGUAGES[i]['name']]= ct
    return max(count, key=count.get)