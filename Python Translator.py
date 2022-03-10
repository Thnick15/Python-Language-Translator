#write a program that allows users to translate text from English to one of
#the following two languages: Spanish, and Arabic.

from textblob import TextBlob

#prompt user instructions
print ("Hello, enter a statement in English and I will translate it for you.")

#Ask the user to enter text here
userInput = input("Type here: ")
blob = TextBlob(userInput)

sentiment = TextBlob(userInput)

#get length of English input
lengthEnglish = len(userInput)

#ask the user to select the language to translate to
selectLanguage = input ("Would you like me to translate to Spanish or German? ")

#spanish translation
if selectLanguage == "Spanish" or selectLanguage == "spanish":
    translationSpanish = blob.translate(to='es')
    #display the translated sentence  
    print ("'",userInput,"'","in Spanish is: ", translationSpanish)
    lengthSpanish = len(translationSpanish)
    #display length of the non-english sentence
    print ("The length in Spanish is: ", lengthSpanish)

#german translation
elif selectLanguage == "German" or selectLanguage == "german":
    translationGerman = blob.translate(to='de')
    #display the translated sentence
    print ("'",userInput,"'","in German is: ", translationGerman)
    lengthGerman = len(translationGerman)
    #display length of the non-english sentence
    print ("The length in German is: ", lengthGerman)

#display length of the original english sentence
print("The length in English is: ", lengthEnglish)

#display sentiment level of the english text
print("Sentiment level of the english text: ", sentiment.sentiment.polarity)
    
