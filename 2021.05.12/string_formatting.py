name = "Arushi Vohra"
age = 12
#introMessage = "I am "+name+" and i am "+ age+" years old"
introMessage1 = "I am {} and i am {} years old"
introMessage2 = "I am {1} and i am {0} years old"
introMessage3 = f'I am {name} and i am {age} years old'
print(introMessage1.format(name, age))
print(introMessage2.format(age, name))
print(introMessage3)