title = input('Please enter your name or preferred title: ')
print('Hello', title + '.', 'I am ORACLE. Your automated personal assistant.')
print('Please exercise patience. I have only recently been created and am incomplete.')
print('Allow me a moment to prepare...') # added this line so users know ORACLE is booting
print('Importing nltk...') # This and following lines were added to more clearly show what went wrong if ORACLE fails
import nltk
print('Importing libraries...')
import numpy as np
import random
import string # to process standard python strings
print('Importing operating systems...')
import threading
import queue
import os
print('Loading definitions...')
def email():
    os.startfile("outlook")

print('Thank you for your patience. ORACLE standing by.') # Added to alert users ORACLE is ready for use
command = input(">>>")
while command != "exit":
    if command == "email":
        email()
    if command == "Open the pod bay doors, Oracle.":
        print("I'm sorry," + title, ".", "I'm afraid I can't do that.")
    command = input(">>>")


# EVERYTHING BELOW THIS LINE IS BROKEN/INCOMPLETE, REMOVE COMMENTS ONLY IF YOU'RE TRYING TO FIX IT

# GREETING_KEYWORDS = ("hello", "hi", "greetings", "attention",)

# GREETING_RESPONSES = ["A good day to you.", "Hello.", "ORACLE standing by."]

# def check_for_greetings(sentence):
#    """If any of the words in the user's sentence was a greeting, return a greeting response"""
#    for word in sentence.words:
#        if word.lower() in GREETING_KEYWORDS:
#            return random.choice(GREETING_RESPONSE)
