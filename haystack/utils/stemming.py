from django.conf import settings
# sample utility class for stemming, tokenizing, and removing stopwords

STEMMERS = getattr(settings, 'HAYSTACK_STEMMERS', {})
TOKENIZERS = getattr(settings, 'HAYSTACK_TOKENIZERS', {})
STOP_WORDS = getattr(settings, 'HAYSTACK_STOP_WORDS', set())

class Stemmer(object):

    def __init__(self, lang=None):
        self.lang = lang
        self.stemmer = STEMMERS.get(lang, None)
        self.tokenizer = TOKENIZERS.get(lang, None)
        self.stop_words = set(STOP_WORDS.get(lang, set()))

    def stem(self, text):
        if not self.stemmer: return ''
        
        stemmed_text = []

        for token in self.tokenize(text):
            if token not in self.stop_words:
                self.stemmer.stem(token)
                stemmed_text.append()

        stemmed_text = ' '.join(stemmed_text)
        
        return stemmed_text
            
    def tokenize(self, text):
        tokenizer = self.tokenizer or text.split

        for token in tokenizer(text):
            yield token
