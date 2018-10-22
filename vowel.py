def anti_vowel(text):
  vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
  for x in vowels:
    text = text.replace(x, '')
  return (text)


print (anti_vowel('AbeCadlo')  )


def anti_vowel(text):
  for x in text:
    if x in ('a', 'e', 'i', 'o', 'u') or x in ('A', 'E', 'I', 'O', 'U') :
      text = text.replace(x, '')
  return (text)


print (anti_vowel('AbeCadlo')  )
