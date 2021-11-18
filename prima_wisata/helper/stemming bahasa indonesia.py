# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
# stemming process
sentence = 'HTMnya pantai tampora brp ya kak'
output   = stemmer.stem(sentence)
print(output)
