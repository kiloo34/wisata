import nltk

kalimat = 'Andi kerap melakukan transaksi rutin secara daring atau online'
tokens = nltk.tokenize.word_tokenize(kalimat)
print(tokens)
