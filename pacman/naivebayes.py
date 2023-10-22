'''Basic code for implementing a Naive Bayes classifier
Please edit to create a working classifier'''

import pandas as pd
from nltk.tokenize import word_tokenize 
import math 

def get_dataframes():
	'''reads in the training and test sets and returns two data frames, one for each'''
	'''make sure to update file names or paths, depending on where you have the data stored'''
	trainset = pd.read_csv('IMDB_train.csv')
	testset = pd.read_csv('IMDB_test.csv')
	return trainset, testset

pos_counts = dict() #count of each word in the positive class
neg_counts = dict() #count of each word in the negative class
vocab = set() #set containing each word that appears in the training set in each class


def process_dataframe(df):
	'''loops over each row of the data frame'''
	'''currently tokenizes the review and prints out the list of tokens followed by the class'''
	'''should be updated to properly update vocab, pos_counts, neg_counts'''
	for i in range(len(df)):
		tokens = word_tokenize(df.loc[i, 'review'])
		for token in tokens:
			if df.loc[i,'sentiment'] == 'pos':
				if token in pos_counts:
					pos_counts[token]+= 1
				else:
					pos_counts[token] = 1
			else:
				if token in neg_counts:
					neg_counts[token]+= 1
				else:
					neg_counts[token] = 1
			vocab.add(token)
		#REPLACE THE REST OF THIS LOOP
		#print(tokens)
		#print(df.loc[i,'sentiment'])

train, test = get_dataframes()
process_dataframe(train)

def calculate_probabilities(smoothing=False):
	'''based on the counts dictionaries, calculate P(w|+) and P(w|-) for each word in the vocab'''
	'''how probabilities are calculated will depend on whether smoothing is used'''
	pos_prob = dict()
	neg_prob = dict()
	#CALCULATE PROBABILITIES HERE
	pos_tot = len(pos_counts)
	neg_tot = len(neg_counts)
	tot = len(vocab)
	if smoothing:
		for token in pos_counts.keys():
			pos_prob[token] = (pos_counts[token]+1)/(pos_tot+tot)
		for token in neg_counts.keys():
			neg_prob[token] = (neg_counts[token]+1)/(neg_tot+tot)
	else:
		for token in pos_counts.keys():
			pos_prob[token] = pos_counts[token]/pos_tot
		for token in neg_counts.keys():
			neg_prob[token] = neg_counts[token]/neg_tot
	return pos_prob, neg_prob

smoothing = True
pos_prob, neg_prob = calculate_probabilities(smoothing)

def find_accuracy():
	'''loops over the test set and classifies each review'''
	'''you will need to implement your own code for actually calculating accuracy, as this currently always returns 0'''
	accuracy = 0
	for i in range(len(test)):
		pred_class = classify_review(test.loc[i, 'review'])
		true_class = test.loc[i, 'sentiment']
		#UPDATE ACCURACY HERE
		if pred_class == true_class:
			accuracy+=1
	
	return accuracy/len(test)

def classify_review(review):
	'''Given a review as a string, tokenizes it and uses the Naive Bayes approach to determine whether it is positive or negative'''
	'''Currently always returns positive'''
	tokens = word_tokenize(review)
	#USE NAIVE BAYES TO DETERMINE CORRECT CLASS
	pos = 0
	neg = 0
	if smoothing:
		null_pos = 1/(len(pos_counts)+len(vocab))
		null_neg = 1/(len(neg_counts)+len(vocab))
	else:
		null_pos = 1
		null_neg = 1
		
	for token in tokens:
		if token in pos_prob:
			pos += math.log(pos_prob[token])
		else:
			pos += math.log(null_pos)

		if token in neg_prob:
			neg += math.log(neg_prob[token])
		else:
			neg += math.log(null_neg)
	#given prob of neg and pos snts is .5
	neg += math.log(.5)
	neg += math.log(.5)
	if pos>neg:
		return 'pos'
	else:
		return 'neg'

print('accuracy is', find_accuracy())