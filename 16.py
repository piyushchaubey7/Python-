
text = "piyush, chaubey"

try:
    
    index = text.index('piyush')

   
    print("Index of 'piyush':", index)

except ValueError:
    print("'piyush' not found in the string.")
