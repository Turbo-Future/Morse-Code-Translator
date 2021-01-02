ttm_dict = { 'a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

mtt_dict = {v:k for k,v in ttm_dict.items()}
question = input("Text to Morse or Morse to Text\nPlease type ttm for text to morse or type mtt for morse to text.\n")
if question == "ttm":
  encrypt_q = input("What would you like have be translated to Morse Code\n")
  # ' ' (single space, char separator
  # '  ' (double space) word separator
  morse = '  '.join([ ' '.join([ttm_dict[c] for c in word]) for word in encrypt_q.lower().split(' ')])
  print(morse)

elif question == "mtt":
  decrypt = input("What would you like to have be translated to English?\n")
  print(' '.join([''.join([mtt_dict[c] for c in word.split(' ')]) for word in decrypt.split('  ')]))

else:
  print("Invalid option")
