#Topic Modeling of several thousands of emails from
#my Gmail account with Latent Dirichlet Allocation (LDA)

# https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
# https://www.linkedin.com/pulse/email-archive-analysis-kaveh-piroozram/

import re

import numpy as np
import pandas as pd

from pprint import pprint

import mailbox

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import spacy

import pyLDAvis
import pyLDAvis.gensim

import matplotlib.pyplot as plt

import logging
#%matplotlib inline


logging.basicConfig(format= '%(asctimes)s : %(levelname)s : %(message)s',
                    level=logging.ERROR)
logging.basicConfig(filename='lda_model.log', format='%(asctime)s : %(levelname)s : %(message)s', 
                    level=logging.INFO)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

from nltk.corpus import  stopwords

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

##############################
mboxfile = mailbox.mbox('/home/fish/PycharmProjects/untitled1/Android.mbox')

print(len(mboxfile))
#print (mbox[0].keys())

messages = []
mail_chunks=[]

def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets


def handleerror(errmsg, emailmsg,cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    #Walk through the parts of the email to find the text body.    
    if msg.is_multipart():    
        for part in msg.walk():

            # If part is multipart, walk through the subparts.            
            if part.is_multipart(): 

                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        # Get the subpart payload (i.e the message body)
                        body = subpart.get_payload(decode=True) 
                        #charset = subpart.get_charset()
                        

            # Part isn't multipart so get the email body
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                #charset = part.get_charset()

    # If this isn't a multi-part message then get the payload (i.e the message body)
    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True) 

   # No checking done to match the charset with the correct part. 
    for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.",msg,charset)
        except AttributeError:
             handleerror("AttributeError: encountered" ,msg,charset)
    return body    



#print(mboxfile)

for thisemail in mailbox.mbox('/home/fish/PycharmProjects/untitled1/Android.mbox'):
    body = getbodyfromemail(thisemail)
    
    
    #body= re.sub('\S*@\S*\s?', '', body)
    body= re.sub("\S*http\S*\s?", " ", str(body))
    body= body.replace('=', '')
    body= body.replace('\'', '')
    body= body.replace(':', '')
    body= body.replace(',', '')
    body= body.replace('!', '')
    body= body.replace('?', '')
    body= body.replace('-', '')
    body= body.replace('~', '')   
    body= body.replace(')', '') 
    body= body.replace('(', '')
    body= body.replace(']', '') 
    body= body.replace('[', '') 
    body= body.replace('}', '') 
    body= body.replace('{', '') 
    body= body.replace('&', '') 
    body= body.replace('$', '') 
    body= body.replace('\r', '')
    body= body.replace('\n', '')

    mail_chunks.append(body)
    #print(body[0:10000])

#print(mail_chunks)
df = pd.DataFrame(messages,columns=mail_chunks)

df.info(verbose=True)
#print(df)


##############################
#df.columns.values().toli
data=df.columns.values.tolist()

#for m in mbox:
    
#    print(m['subject'])

print ('1')
# Remove distracting single quotes. zero '
#data = [re.sub("\'", "", sent) for sent in str(data)]

def sentence_to_words(sentences):
    for i in sentences:
        yield(gensim.utils.simple_preprocess(str(i), deacc=True)) #returns a generator(1 time use)
                        # ^ list of str

print ('passed sentence_to_words')

data_words = list(sentence_to_words(data))
#print(data_words[:1])
print ('data_words')

# Build the bigram and trigram models
bigram= gensim.models.Phrases(data_words,min_count=5, threshold=100)
print ('bigram')
# higher threshold fewer phrases.
trigram= gensim.models.Phrases(bigram[data_words], threshold=100)
print ('trigram')
# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod= gensim.models.phrases.Phraser(bigram)
trigram_mod= gensim.models.phrases.Phraser(trigram)

print ('mod_ram')
#print(trigram_mod[bigram_mod[data_words[1]]])

print ('before remove_stopwords')


# Define functions for stopwords, bigrams, trigrams and lemmatization

########################################################################
def remove_stopwords(texts):
        return[
                [word for word in simple_preprocess(str(doc)) if word not in stop_words]
                 for doc in texts  
              ]
####################################
def make_bigrams(texts):
        return [ bigram_mod[doc] for doc in texts ]

####################################
def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

####################################
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []

    # Initialize spacy 'en' model, keeping only tagger component (for efficiency)
    nlp=spacy.load('en', disable=['parser', 'ner'])
    nlp.add_pipe(nlp.create_pipe('sentencizer'))

    print ('load spacy')

    for sent in texts:  ##CPU intensive! why?? A lot of nouns here.. not verbs..
     
        doc = nlp (" ".join(sent)) 
        
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        #print ('lem:', sent)
    return texts_out    

########################################################################

data_words_nostops= remove_stopwords(data_words)
print('169')

# Form Bigrams
data_words_bigrams= make_bigrams(data_words_nostops)

# Do lemmatization keeping only noun, adj, vb, adv
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

print(data_lemmatized[:1])

# Create Dictionary
id2word = corpora.Dictionary(data_lemmatized)

# Create Corpus
texts = data_lemmatized

# Term Document Frequency
#counts the number of occurrences of each distinct word, 
# converts the word to its integer word id and returns the result as a sparse vector.
corpus= [id2word.doc2bow(text) for text in texts]

#id2word[0]

#view
print(corpus[:1])

print(id2word[1])

# Human readable format of corpus (term-frequency)
[[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]]
print('196')

#words that are not indicative are going to be omitted. 
# phi_value is another parameter that steers this process - it is 
# a threshold for a word treated as indicative or not.
# Build LDA model
# which one is amount of sampling? reduce it to 1..5
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=2, #touchy s  tuff!
                                           random_state=1000,

                                           #determines how often the model parameters should be updated 
                                           #bigger values are faster but not quality
                                           #too low and it will not capture the nuances of the data well enough
                                           update_every=10,
                                           
                                           #the number of documents to be used in each training chunk  
                                           chunksize=10, #touchy stuff!
                                           #total number of training passes
                                           passes=10, #touchy stuff! bigger values, better quality take longer times.
                                           
                                           alpha='auto',
                                           per_word_topics=True)


# Print the Keyword in the 10 topics
#lda_model.show_topics()
print('215')
pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]

print('219')
# Compute Perplexity
print('\nPerplexity: ', lda_model.log_perplexity(corpus))  # a measure of how good the model is. lower the better.

# Compute Coherence Score
#coherence='u_mass' or 'c_v' ?
coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Scorez: ', coherence_lda)

#gensim.models.    

# Visualize the topics
#pyLDAvis.enable_notebook()
# takes too much CPU! try with smaller dataset
#The red bars represent the frequency of a term in a given topic, 
# ==> (proportional to p(term | topic)), and the blue bars represent 
# a term's frequency across the entire corpus


lda_display = pyLDAvis.gensim.prepare(lda_model, corpus, id2word,  sort_topics=False)

# problem                               ^                  ^ 
#pyLDAvis.display(lda_display)
pyLDAvis.save_html(lda_display, 'z.html')
