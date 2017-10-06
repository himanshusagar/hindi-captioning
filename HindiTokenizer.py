# -*- coding: utf-8 -*-	
import codecs
import re
class Tokenizer():
	

	def __init__(self,text=None):
		if text is  not None:
			self.text=text.decode('utf-8')
			self.clean_text()
		else:
			self.text=None
		self.sentences=[]
		self.tokens=[]
		self.stemmed_word=[]
		self.final_list=[]
		

	def generate_sentences(self):
		'''generates a list of sentences'''
		text=self.text
		self.sentences=text.split(u"।")

	def print_sentences(self,sentences=None):
		if sentences:
			for i in sentences:
				print i.encode('utf-8')
		else:
			for i in self.sentences:
				print i.encode('utf-8')


	def clean_text(self):
		'''not working'''
		text=self.text
		text=re.sub(r'(\d+)',r'',text)
		text=text.replace(u',','')
		text=text.replace(u'"','')
		text=text.replace(u'(','')
		text=text.replace(u')','')
		text=text.replace(u'"','')
		text=text.replace(u':','')
		text=text.replace(u"'",'')
		text=text.replace(u"‘‘",'')
		text=text.replace(u"’’",'')
		text=text.replace(u"''",'')
		text=text.replace(u".",'')
		text=text.replace(u"-",'')
		text=text.replace(u"।",'')
		self.text=text

	def remove_only_space_words(self):

		tokens=filter(lambda tok: tok.strip(),self.tokens)
		self.tokens=tokens
		
	def hyphenated_tokens(self):

		for each in self.tokens:
			if '-' in each:
				tok=each.split('-')
				self.tokens.remove(each)
				self.tokens.append(tok[0])
				self.tokens.append(tok[1])



	def tokenize(self):
		'''done'''
		if not self.sentences:
			self.generate_sentences()

		sentences_list=self.sentences
		tokens=[]
		for each in sentences_list:
			word_list=each.split(' ')
			tokens=tokens+word_list
		self.tokens=tokens
		#remove words containing spaces
		self.remove_only_space_words()
		#remove hyphenated words
		self.hyphenated_tokens()

	def print_tokens(self,print_list=None):
		'''done'''
		if print_list is None:
			for i in self.tokens:
				print i.encode('utf-8')
		else:
			for i in print_list:
				print i.encode('utf-8')


	def tokens_count(self):
		'''done'''
		return len(self.tokens)

	def sentence_count(self):
		'''done'''
		return len(self.sentences)

	def len_text(self):
		'''done'''
		return len(self.text)


if __name__=="__main__":
	t=Tokenizer("यह - - - - वाक्य हिन्दी में है।")
	t.generate_sentences()
	t.tokenize()
	t.remove_only_space_words()
	#t.print_tokens()
	#print t.tokens
	final_list=[x.encode('utf-8') for x in t.tokens]
	#for i in range(len(k)):
	#	print k[i]
	