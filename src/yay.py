sirname, first_name = input("Enter your names: ").split()
print(f"My sirname is {sirname} and my first name is {first_name}")

text_string = input("Enter a long string to play with: ")
#declaring the sample string


'''the following are a series of operations on the string.
meant to test the functionality of string operations'''

print("Split: " + str(text_string.split()))
#string cantenation requires strings thus I first convert the list from split() to a string using str()
print("Index of 'three': " + str(text_string.find('three')))
#find() returns an integer so I employ the str() function again to make it compatible for cantenation

print("Uppercase: " + text_string.upper())
print("Lowercase: " + text_string.lower())
print("Titlecase: " + text_string.title())

print("Strip: " + text_string.strip('one').strip('TEN').strip())
#Here, the resultant string from the first strip() then acts as the input for the next.
#Thus the operations can be done in quick succession.

print("Does it start with 'one'? " + str(text_string.startswith('one')).replace("True","Yes").replace("False","No!"))
#Check if it starts with one, then convert the boolean to a string, then replace with an appropriate reply.
#Luckily, if the term we're trying to replace is non-existent, the replace() method is ignored

print(f"If only the spaces were commas ^-^: {text_string.replace(' ',',').replace(text_string[0],text_string[0].upper(),1)}{text_string[-1]*10}")
'''
    Now, WHAT THE HELL IS HAPPENING HERE???!!!

Allow me to explain:
    Firstly, we're replacing all spaces with commas.
    Then, we're capitalizing the first letter of the string. (replacing the letter with it capital form)
    Finally, we're looking at the last character and duplicating it 10 times.
    On top of all that, we're using f-string formating to insert the result of these operations into the print-out string.
It may be alot, but it's convenient to be able to do this in one line.
'''
def hello (*args):
    print("hello,",*args )
hello(first_name,sirname)    
