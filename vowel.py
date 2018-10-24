def anti_vowel(text):
  vowels = 'aeiouAEIOU'
  for x in vowels:
    text = text.replace(x, '')
  return (text)


print(anti_vowel('AbeCadlo'))


def anti_vowel(text):
  for x in text:
    if x in ('aeiou') or x in ('AEIOU') :
      text = text.replace(x, '')
  return (text)


print(anti_vowel('AbeCadlo'))



def anti_vowel(characters):
  vow = 'aeiouAEIOU'
  for evrchar in vow:
    if evrchar in characters:
      characters = characters.replace(evrchar, '')
  return characters


print(anti_vowel('hkfsOEgiobmlaE'))

def anti_vowel(text):
  word = '' #variable for vowels 
  for char in text:
    if char in ('aeiouAEIOU'):
      word += char
      text = text.replace(char, '')
  print(word)
  return text


print(anti_vowel('gfdoELOAxhU'))

def anti_vowel(text):
  return text.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')


print(anti_vowel('fsdfoEAffoi'))

def anti_vowel(text):
  return ''.join(char for char in text if char not in ('aeiouAEIOU'))

print(anti_vowel('fsnjkoAEObjsfdoO'))


def anti_vowel(text): #return vowels only
  return ''.join(char for char in text if char in ('aeiouAEIOU'))

print(anti_vowel('fsnjkoAEObjsfdoO'))


def anti_vowel(text):
  result = list(text)
  for l in text:
    if l in "AEIOUaeiou":
      result.remove(l)
  return ''.join(result)
  
print(anti_vowel("ecureuil"))

































 
