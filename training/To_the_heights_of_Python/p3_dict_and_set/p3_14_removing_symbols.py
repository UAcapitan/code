
from unicodedata import normalize, combining
import string

def shave_marks(txt):
    nfd_str = normalize("NFD", txt)
    shaved = ''.join(c for c in nfd_str if not combining(c))
    return normalize("NFC", shaved)
