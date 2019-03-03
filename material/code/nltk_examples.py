Example 1: Sentence tokenization
================================

from nltk.tokenize import sent_tokenize
sent_tokenize("This is just a sentence tokenizing example. Let us see how it works!")

Example 2: Word tokenization
============================

from nltk.tokenize import word_tokenize
word_tokenize("This is just a sentence tokenizing example.")

Example 3: Word tokenization & punctuation
==========================================

word_tokenize("What's up?")

from nltk.tokenize import wordpunct_tokenize
wordpunct_tokenize("What's up?")

Example 4: Part-of-Speech tagging
=================================

words = word_tokenize("The little dog barked at the cat.")
from nltk.tag import pos_tag
pos_tag(words)

Example 5: Chunking
===================

import nltk
grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = nltk.RegexpParser(grammar)
sentence = "The little dog barked at the cat."
words = nltk.tokenize.word_tokenize(sentence)
tags = nltk.tag.pos_tag(words)
tree = parser.parse(tags)
tree.draw()

Example 6: Text classification
==============================

# Names ending in a, e and i are likely to be female, while names ending in k, o, r, s and t are likely to be male

# First we define a feature extractor

def gender_features(word):
return{'last letter': word[-1]}

# Example
gender_features('Shrek')
gender_features('Fiona')

# Create a list of (correctly annotated individuals)
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] + 
 [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

# Create a training/test set
featuresets = [(gender_featuresNo, g) for (n, g) in names]
trainset, testset = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(trainset)

# Try the classifier
classifier.classify(gender_features("Neo"))
classifier.classify(gender_features("Trinity"))

# Test the classifier accuracy
print nltk.classify.accuracy(classifier, testset)

# Determine most informative features
classifier.show_most_informative_features(5)