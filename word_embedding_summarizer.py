'''Extractive text summarizer that create a summary of a given text 
by compiling the sentences with highest sentence scores. The sentence score in this scenario 
indicates how similar a given sentence is to all the other sentences in the text. 
The sentence score is calculated by finding the sentence embedding for each sentence and using cosine similarity
to obtain a score that indicates how similar each sentence is to the other sentences. 
 '''



# nltk imports and downloads 
import nltk_modules
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

import numpy as np
from string import punctuation
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import argparse 
from load_glove import load_word_emb_binary

from math import floor

# global variables for Glove Model 
glove_file_path = 'glove.42B.300d.txt'
dim = 300 

def handle_args(): 
    '''Handle CL args by return contents of text file provided by user. If no file path is provided, 
    return default text '''
    parser = argparse.ArgumentParser(description = 'Parse file path from CL')
    parser.add_argument('--path', help = 'File path of .txt file containing text to be summarized', default = "text_files/Davis.txt")
    args = parser.parse_args() 

    f = open(args.path, "r")
    text = f.read() 
    return text 

stop_words = stopwords.words('english')


def loadGloveModel(gloveFile):
    '''Given the local path to the glove file, the function loads the word embeddings
    from the .vocab (txt file) and .npy (binary file)'''
    # word_embeddings = {}
    # f = open(gloveFile, encoding='utf-8')
    # for line in f:
    #     splitLines = line.split()
    #     word = splitLines[0]
    #     embedding = np.asarray(splitLines[1:], dtype='float32')
    #     word_embeddings[word] = embedding
    # f.close()
    # return word_embeddings
    return load_word_emb_binary(gloveFile)
 
def _remove_extraneous_words(sentence): 
    '''Removes extraneous words (stop words and punctuation) from input'''
    parsed_sentence = []
    for word in sentence.lower().split(): 
        if word not in stop_words and word not in punctuation: 
            parsed_sentence.append(word)

    parsed_str = ' '.join(parsed_sentence)
    return parsed_str

def clean_text(text): 
    ''' Iterates through text param by sentence and removes extraneous 
    words. Returns a list of clean sentences.'''
    sentences = sent_tokenize(text)
    processed_sentences = [_remove_extraneous_words(sentence) for sentence in sentences]
    return processed_sentences

# TODO: Make sure function is working correctly 
def calculate_sentence_embeddings(sentences, word_embeddings): 
    '''Takes in processed sentences and word_embeddings and returns a list
    of the sentence embeddings for each sentence '''  
    sentence_vectors = []
    sentence_embeddings = []
    avg = 0
    for sentence in sentences:
        if len(sentence) > 0: 

            for word in sentence.split(): 
                sentence_embeddings.append(word_embeddings.get(word, np.zeros((dim, ))))
               # print(sentence_embeddings)
            # for word in sentence.split(): 
            #     sentence_embeddings.append(word_embeddings.get(word, np.zeros((dim, ))))
            # get the word embedding from Glove, if not present return np array of 0s  
            avg = sum(sentence_embeddings)/len(sentence) 
        else: 
            avg = np.zeros((dim, ))

        sentence_vectors.append(avg)
        sentence_embeddings = []
    
    return sentence_vectors

def construct_similarity_matrix(sentence_vectors, sentences): 
    '''Takes in list of sentence vectors (size n) and constructs a n x n matrix
    that tracks the similarity (cosine distance) of each sentence to all other sentences '''
    matrix = np.zeros([len(sentence_vectors), len(sentence_vectors)])

    for i in range(len(sentences)): 
        for j in range(len(sentences)):
            if i != j:
                matrix[i][j] = cosine_similarity(sentence_vectors[i].reshape(1, dim), sentence_vectors[j].reshape(1, dim))

    matrix = np.round(matrix, 3)
    # print(matrix[2][3]) == print(matrix[3][2]), True, edit this function to reduce calls to cosine_similarity
    return matrix

def textrank(matrix, sentences):
    nx_graph = nx.from_numpy_array(matrix) 
    scores = nx.pagerank(nx_graph)
    
    ranked_sentences = sorted(((scores[i],i) for i,s in enumerate(sentences)), reverse=True)
    arranged_sentences = sorted(ranked_sentences[0:int(len(sentences)*0.5)], key=lambda x:x[1])
    print("\n".join([sentences[x[1]] for x in arranged_sentences]))



if __name__ == '__main__': 
    # load glove model 
    word_embeddings = loadGloveModel(glove_file_path)
    # print(word_embeddings.get('king'))

    text = handle_args()
    clean_text = clean_text(text) # returns a list of sentences without stop words and punctuation 
    sentence_vectors = calculate_sentence_embeddings(clean_text, word_embeddings) # sum all the word embeddings into one vector for each sentence 
    matrix = construct_similarity_matrix(sentence_vectors, clean_text)
    textrank(matrix, sent_tokenize(text))
    
    # calculate sentence embeddings 
    # construct similarity matrix
    # select highest scoring sentences and compile them into a summary