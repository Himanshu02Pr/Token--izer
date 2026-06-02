import re

#Character Tokenizer
class CharTokenizer:
  def tokenize(self, text):
    return list(text)

#Word Tokenizer  
class WordTokenizer:
  def tokenize(self, text):
    return re.findall(r"\b[\w']+\b", text.lower())
  
#Ngram Tokenizer
class NgramTokenizer:
  def ngtokenizer(self, text, n=2):
    tokenizer = WordTokenizer()
    tokens = tokenizer.tokenize(text)
    return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
