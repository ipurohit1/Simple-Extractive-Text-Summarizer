import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else: # if no exception, this block is executed 
    ssl._create_default_https_context = _create_unverified_https_context
finally: 
    nltk.download('punkt')

