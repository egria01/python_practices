single_quote = 'Hello'
double_quote = "Hello"
triple_single_quote = """multi-line 
string"""
print(single_quote)
print(double_quote)
print(triple_single_quote)

python_string = "Python Programming"
print(python_string[0])         # First character
print(python_string[-1])        # last character
print(python_string[0:5])       # slice 0 to 4
print(python_string[:6])        # start to 5
print(python_string[7:])        # 7 to end

name ="bob the builder "

print(len(name))            # Length of string with white space
print(name.strip())        # Remove whitespace   
print(name.upper())         # Uppercase
print(name.lower())         # Lowercase
print(name.title())         # Title Case
print(name.replace("bob","jane"))  # Replace

name    = "John Doe"
age     =30 
message_1 = f"My name is {name} and I am {age} years old." # f-string
message_2 = "My name is {} and I am {} years old".format(name,age) # str.format()
message_3 = "My name is %s and I am %d years old." % (name, age) # % format
print(message_1)
print(message_2)
print(message_3)

text = """Python is a powerful programming language. It's easy to learn
and versatile!You  can  use  Python  for  web  development,  data  science,  andautomation. The syntax is clean and readable.This makes Python perfect for beginners and experts alike."""

import re
print(text)
text_count_character=len(text.strip())    # Length without leading/trailing whitespace
text_count_character_spaces=(len(text))    # Length with whitespace
text_count_words=len(re.findall("[a-zA-Z_]+", text))
text_count_sentences=len(re.findall("[.!?]+", text))

print("Character count (no spaces):", text_count_character)
print("Character count (with spaces):", text_count_character_spaces)
print("Word count:", text_count_words)
print("Sentence count:", text_count_sentences)