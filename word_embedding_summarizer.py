'''Extractive text summarizer that create a summary of a given text 
by compiling the sentences with highest sentence scores. The sentence score in this scenario 
indicates how similar a given sentence is to all the other sentences in the text. 
The sentence score is calculated by finding the sentence embedding for each sentence and using cosine similarity
to obtain a score that indicates how similar each sentence is to the other sentences. 
 '''

import numpy as np
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import argparse 

glove_file_path = '/Users/ishaanpurohit/Documents/ML_Projects/Pretrained_Models/glove.42B.300d.txt'
dim = 300 

def handle_args(): 
    '''Handle CL args by return contents of text file provided by user. If no file path is provided, 
    return default text '''
    parser = argparse.ArgumentParser(description = 'Parse file path from CL')
    parser.add_argument('--path', help = 'File path of .txt file containing text to be summarized', default = None)
    args = parser.parse_args() 

    if args.path: 
        f = open(args.path, "r")
    else: 
        f = open("text_files/Davis.txt", "r")

    text = f.read() 
    return text 

stop_words = stopwords.words('english')

def convert_text_file_to_str(text_file_path): 
    '''Given the path to a text file, the function returns a
    str of the text.'''
    pass 

def loadGloveModel(gloveFile):
    '''Given the local path to the glove file, the function stores the
    embedding values for each word into a Python dictionary '''
    word_embeddings = {}
    f = open(gloveFile, encoding='utf-8')
    for line in f:
        splitLines = line.split()
        word = splitLines[0]
        embedding = np.asarray(splitLines[1:], dtype='float32')
        word_embeddings[word] = embedding
    f.close()
    return word_embeddings
 
# TODO: Currently iterating through sentence/words twice, reduce to one iteration
def remove_extraneous_words(sentence): 
    '''Removes extraneous words (stop words and punctuation) from input'''
    parsed_sentence = []
    for word in sentence.lower().split(): 
        if word not in stop_words and word not in punctuation: 
            parsed_sentence.append(word)

    parsed_str = ' '.join(parsed_sentence)
    return parsed_str

def clean_text(text): 
    '''Takes in text to process and tokenizes using NLTK. Then 
    iterates through the text by sentence and removes extraneous 
    words '''
    sentences = sent_tokenize(text)
    processed_sentences = [remove_extraneous_words(sentence) for sentence in sentences]
    return processed_sentences

# TODO: Make sure function is working correctly 
def calculate_sentence_embeddings(sentences, word_embeddings): 
    '''Takes in processed sentences and word_embeddings and returns a list
    of the sentence embeddings for each sentence '''  
    list_of_scores = []
    sum = 0
    for sentence in sentences: 
        for word in sentence.split(): 
            sum += word_embeddings.get(word)
        list_of_scores.append(sum)
        sum = 0

if __name__ == '__main__': 
    

    text = handle_args()
  
    # load glove model 
    # word_embeddings = loadGloveModel(glove_file_path)
    # clean the text (text is either local to program or from text file)
    # calculate sentence embeddings 
    # construct similarity matrix
    # select highest scoring sentences and compile them into a summary