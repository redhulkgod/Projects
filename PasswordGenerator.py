import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
#two Upper case letters
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#two Lower case letters
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
#two digits
digits1=chr(random.randint(47,57))
digits2=chr(random.randint(47,57))
#two punctuation
punct1=chr(random.randint(33,47))
punct2=chr(random.randint(33,47))

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digits1 + digits2 + punct1 + punct2
password = shuffle(password)

#Ouput
print(password)