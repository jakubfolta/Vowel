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
  print (word)
  return text


print(anti_vowel('gfdoELOAxhU'))






































 
