punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str1):
    for i in str1:
        if i in punctuation_chars:
            str1 = str1.replace(i, "")
    return str1

        
var1 = 'in.cred..ible!'
var2 = '#Amazing'
var3 = 'wow!'
var4 = 'wonderful'

print(strip_punctuation(var1))
print(strip_punctuation(var2))
print(strip_punctuation(var3))
print(strip_punctuation(var4))

