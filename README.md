# Simple-Extractive-Text-Summarizer
Create an extractive text summarizer that concatenates that most important sentences from text to produce a summary of a given number of sentences. 

## Project Status
A simple extractive method for summarizing texts is complete. Given a piece of text, the program parses through it and finds the normalized frequency of each word, while ignoring common stop words and punctuation. It then scores each sentence by summing the frequency of each word that it contains. The sentences with the highest score are selected and combined to create a summary. 

There are definitely ways to build on and expand the current solution. First, it's possible to read in files of text rather than just strings that are locally assigned in the program. Secondly, the method to rank/score the sentences can be expanded and take into account other factors. Finally, I could look into an abstractive approach where the program uses its own vocabulary in order to summarize the given text. 

## Requirements 
- Python3 
- Spacy (Version 3.0.3 on my machine)

## Reflection 
This was a small side project I wanted to develop after learning about being introduced to NLP and NLP programming libraries. The method used to summarize text is extractive and attempts to score the sentences based on how many "important" words they contain. There are some shortcomings with this apporach, particularly pieces of text that are sequential/narrative where each sentence relies on the one before it for context. On the other hand, informative texts that discuss each a variety of topics at length are likely to work well with this method.   

## References 
https://medium.com/sciforce/towards-automatic-text-summarization-extractive-methods-e8439cd54715
https://medium.com/luisfredgs/automatic-text-summarization-with-machine-learning-an-overview-68ded5717a25
https://www.youtube.com/watch?v=9PoKellNrBc&t=543s

