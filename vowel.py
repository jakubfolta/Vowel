def anti_vowel(text):
  vowels = 'aeiouAEIOU'
  for x in vowels:
    text = text.replace(x, '')
  return (text)


print (anti_vowel('AbeCadlo'))


def anti_vowel(text):
  for x in text:
    if x in ('aeiou') or x in ('AEIOU') :
      text = text.replace(x, '')
  return (text)


print (anti_vowel('AbeCadlo'))
 
