# Position: Intern for Cyber Security
# Company: Prodigy InfoTech

def caesar_cipher(text, shift, choice):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                if choice == 'E':
                    shifted = chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    shifted = chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                if choice == 'E':
                    shifted = chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    shifted = chr((ord(char) - 65 - shift) % 26 + 65)

            result += shifted
        else:
            result += char
    return result

def main():
  choice = input("Enter E or e perform encryption \n Enter D or d decryption \n Enter exit for Exit : ")
  while(True):
    if choice == 'E' or choice=='e':
        text = input("Input the text you want to encrypt: ")
    elif choice == 'D' or choice=='d':
        text = input("Input the text you want to decrypt: ")
    elif choice == 'exit':
      print("Thanks for using Cipher")
      return
    else:
        print("Invalid input. Terminating program...")
        return

    shift = int(input("Enter a positive shift value: "))
    print("Original text: " + text)
    print("New text: " + caesar_cipher(text, shift, choice))

if __name__ == "__main__":
    main()