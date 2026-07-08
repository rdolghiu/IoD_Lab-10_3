import regex as re
from sklearn.base import BaseEstimator, TransformerMixin

def clean_text(text):
    # reduce multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)
    # remove double quotes
    text = re.sub(r'"', '', text)
    return text.strip()

def convert_text(text):
    # lowercase
    text = text.lower()
    # remove punctuation
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # collapse spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

class preprocessor(TransformerMixin, BaseEstimator):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.apply(clean_text).apply(convert_text)
