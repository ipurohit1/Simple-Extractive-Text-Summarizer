import codecs 
import numpy as np 
import sys 
import argparse

def handle_args(): 
    parser = argparse.ArgumentParser(description = 'Parse file path from CL')
    parser.add_argument('path', help = 'File path of .txt file containing Glove Vectors')
    args = parser.parse_args() 
    
    return args.path

def convert_to_binary(embedding_path):
    f = codecs.open(embedding_path, 'r', encoding='utf-8')
    wv = []

    with codecs.open(embedding_path + ".vocab", "w", encoding='utf-8') as vocab_write:
        count = 0
        for line in f:
            splitlines = line.split()
            vocab_write.write(splitlines[0].strip())
            vocab_write.write("\n")
            wv.append([float(val) for val in splitlines[1:]])
        count += 1

    np.save(embedding_path + ".npy", np.array(wv))

def load_word_emb_binary(embedding_file_name_w_o_suffix):
    print("Loading binary word embedding from {0}.vocab and {0}.npy".format(embedding_file_name_w_o_suffix))

    with codecs.open(embedding_file_name_w_o_suffix + '.vocab', 'r', 'utf-8') as f_in:
        index2word = [line.strip() for line in f_in]

    wv = np.load(embedding_file_name_w_o_suffix + '.npy')
    word_embedding_map = {}
    for i, w in enumerate(index2word):
        word_embedding_map[w] = wv[i]

    return word_embedding_map

if __name__ == '__main__': 
    path = handle_args()

    # convert_to_binary(path)
    map = load_word_emb_binary(path)
    print(map['king'])