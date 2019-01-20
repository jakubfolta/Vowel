def removeVowels(text):
  vowels = 'aeiouAEIOU'
  for x in vowels:
    text = text.replace(x, '')
  return (text)


print(removeVowels('AbeCadlo'))


def removeVowels(text):
  for x in text:
    if x in ('aeiou') or x in ('AEIOU') :
      text = text.replace(x, '')
  return (text)


print(removeVowels('AbeCadlo'))



def removeVowels(characters):
  vow = 'aeiouAEIOU'
  for evrchar in vow:
    if evrchar in characters:
      characters = characters.replace(evrchar, ' ')
  return characters


print(removeVowels('hkfsOEgiobmlaE'))

def removeVowels(text):
  vowelsVar = '' 
  for char in text:
    if char in ('aeiouAEIOU'):
      vowelsVar += char
      text = text.replace(char, '')
  print(vowelsVar)
  return text


print(removeVowels('gfdoELOAxhU'))

def removeVowels(text):
  return text.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')


print(removeVowels('fsdfoEAffoi'))

def removeVowels(text):
  return ''.join(char for char in text if char not in ('aeiouAEIOU'))

print(removeVowels('fsnjkoAEObjsfdoO'))


def returnOnlyVowels(text):
  return ''.join(char for char in text if char in ('aeiouAEIOU'))

print(returnOnlyVowels('fsnjkoAEObjsfdoO'))


def removeVowelsFromTextCopy(text):
  result = list(text)
  for l in text:
    if l in "AEIOUaeiou":
      result.remove(l)
  return ''.join(result)
  
print(removeVowelsFromTextCopy("ecureuil"))


def removeVowelsFromCopy(text):
  textCopy = list(text)
  for x in text:
    if x in 'aeiouAEIOU':
      textCopy.remove(x)
  return ''.join(textCopy)

print(removeVowelsFromCopy('fsnjkoAEObjsfdoOfsnjkoAEObjsfdoO'))












