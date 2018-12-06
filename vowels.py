def get_vowels(text):
  vowels = ''
  for letter in text:
    if letter in 'aeiouAEIOU':
      vowels += letter
  return vowels

print(get_vowels('abedeOSUkil'))


def noVowels(letters):
  sec_letters = list(letters)
  vowels = 'aeiouAEIOU'
  for character in letters:
    if character in vowels:
      sec_letters.remove(character)
  return ''.join(sec_letters)

print(noVowels('abdeOUghtjuel'))


def noVowels(text):
  return text.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print(noVowels('adeloUOFgEb'))
