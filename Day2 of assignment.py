Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String practice
>>> #To print a value
>>> print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> print('30 days 30 hour challenge')
30 days 30 hour challenge
>>> #In python we can use both single and double quotes
>>> #Assigning String to variable
>>> Hours="thirty"
>>> print(Hours)
thirty
>>> #Indexing using string
>>> Days="Thirty days"
>>> print(Days[0])
T
>>> print(Days[5])
y
>>> print(Days[8])
a
>>> print(Days[9])
y
>>> print(Days[10])
s
>>> #print the particular character from certain text
>>> Challenge="I will win"
>>> print(challenge[8:10])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(challenge[8:10])
NameError: name 'challenge' is not defined
>>> print(Challenge[8:10])
in
>>> print(Challenge[5:10])
l win
>>> print(Challenge[3:10])
ill win
>>> #print the length of character
>>> Challenge="I will win"
>>> print(len(Challenge))
10
>>> #convert string into lower case
>>> print(Challenge.lower())
i will win
>>> #convert string into upper
>>> print(Challenge.upper())
I WILL WIN
>>> #String concatenation-joined two strings
>>> a='30 Days'
>>> b='30 hours'
>>> c=a+b
>>> print(c)
30 Days30 hours
>>> #adding spaces during concatenation
>>> c=a+""+b
>>> print(c)
30 Days30 hours
>>> c=a+" "+b
>>> print(c)
30 Days 30 hours
>>> #casefold usage- It is similar to lower() method
>>> text='THirty Days Thirty HOUr Challenge"
SyntaxError: EOL while scanning string literal
>>> text="THirty Days Thirty HOUr Challenge"
>>> x=text.casefold()
>>> print(x)
thirty days thirty hour challenge
>>> #capitalize- It is used to change the first character of the string into upper case.
>>> x=text.capitalize()
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> x=text.capitalize()
>>> print(x)
Thirty days thirty hour challenge
>>> #find usage
>>> x=text.find("Hour")
>>> print(x)
-1
>>> x=text.find("Days")
>>> print(x)
7
>>> #isalpha usage
>>> x=text.isalpha()
>>> print(x)
False
>>> y='hello'
>>> y=text.isalpha()
>>> print(y)
False
>>> y="Hello"
>>> y=text.isalpha()
>>> print(y)
False
>>> #isalnum usage
>>> z="n54"
>>> z=text.isalnum()
>>> print(z)
False
>>> z="no54"
>>> z=text.isalnum()
>>> print(z)
False
>>> print(y.isalpha())
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(y.isalpha())
AttributeError: 'bool' object has no attribute 'isalpha'
>>> y="hello"
>>> print(y.isalpha())
True
>>> z="n090"
>>> print(z.isalnum())
True
>>> v="9o"
>>> print(v.isnumeric())
False
>>> v="90"
>>> print(v.isnumeric())
True
>>> 