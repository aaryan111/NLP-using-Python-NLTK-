from nltk.tokenize import word_tokenize
import pandas as pd

comment = input ("Enter your comment")
tokens=comment.split(" ")
print ("tokens are:",tokens)
stopwords=["this","is","a"]
poswords=["good","nice","awesome","very good","so good"]
negwords=["worst product","bad","poor","ugly","very bad"]
for word in list(tokens):
    if(word in stopwords):
        tokens.remove(word)
pflag=False
nflag=False
for item in tokens:
    if(item in poswords):
        pflag=True
    if (item in negwords):
        nflag=False

if (pflag==True and nflag==True):
    print ("Its Neutral")
elif (pflag):
    print("Its+ve")
elif(nflag):
    print("Its -ve")
else:
    print("It can't be analysed!")




'''
stopw=pd.read_csv("woords.txt")
print(stopw)
stopwords=list(stopw["words"])
print(stopwords)
for word in list(tokens):
    if(word in stopwords): #The square bracket is for
        tokens.remove(word)

print(tokens)
'''