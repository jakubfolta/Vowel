def vowel(text):
  return ''.join(char for char in text if char not in 'aeiouAEIOU')

print(vowel('akeoOIifjookrtg'))


def antvowel(text):
  vowels = 'aeiouAEIOU'
  for letter in text:
    if letter in vowels:
      text = text.replace(letter, '')
  return text

print(antvowel('hftreuoouhfgOEAk'))


def vowel(text):
  letters = list(text)
  for character in text:
    if character in 'aeiouAEIOU':
      letters.remove(character)
  return ''.join(letters)

print(vowel('agtehtoIOfgtU'))
  
