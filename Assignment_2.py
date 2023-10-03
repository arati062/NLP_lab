##Assignment No.02##
#Name:Rahane Arati Bhagwat
##Roll No:46
#Batch:B3
#Title:Assignment to implement Bag of Words and TFIDF using Gensim library.
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess


text1 = ["""India ia my country
         Maharashtra is my state."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)


print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

text = ["""India ia my country
         Maharashtra is my state."""]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])
    
##OUTPUT##
'''
The dictionary has: 4 tokens

{'India': 0, 'Maharashtra': 1, 'country': 2, 'my': 3}
Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 2)]]
Dictionary : 
[['India', 1], ['Maharashtra', 1], ['country', 1], ['my', 2]]
'''