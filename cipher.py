# add your code here
def encode(text, shift):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encoded_text = ""
  for char in text.lower():
    if char in alphabet:
      encoded_text += alphabet[(alphabet.index(char) + shift) % 26]
    else:
      encoded_text += (char)
  return encoded_text


text = input('Enter text to encode: ')
shift = 5
encoded_text = encode(text, shift)
print('Encoded text: ' , encoded_text)
