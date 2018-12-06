def anty_vowel(text):
  vowels = 'aeiouAEIOU'
  for char in vowels:
    if char in text:
      text = text.replace(char, '')
  return text

print(anty_vowel('abeeeOIFREdhtuuiyuikfl'))


def antvowel(letters):
  return letters.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print(antvowel('abecdeEOIoithkl'))


def antyv(text):
  word = list(text)
  for char in text:
    if char in 'aeiou' or char in 'AEIOU':
      word.remove(char)
  return ''.join(word)

print(antyv('abfetyUOEihfgto'))


def ant_vow(text):
  for char in text:
    if char in 'aeiouAEIOU':
      text = text.replace(char, '')
  return text

print(ant_vow('abecedeOouUtjIEo'))


def anty_vowel(text):
  return ''.join(char for char in text if char not in ('aeiouAEIOU'))

print(anty_vowel('abeCEDOUikglto'))
