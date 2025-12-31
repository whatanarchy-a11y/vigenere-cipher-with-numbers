def encode(word, key):
    new_word = ""
    key = key.lower()
    l1 = list('!"#$%&()\'*+,-./')
    l2 = list(':;<=>?@')
    l3 = list('[\\]^_`')
    
    for i in range(len(word)):
        # 1. DO NOT encode spaces; keep them as is 
        if word[i] == ' ':
            new_word += ' '
            continue
            
        # 2. Handle other characters
        if word[i].isupper():
            stddisp = 65
            mod = 26
        elif word[i].islower():
            stddisp = 97
            mod = 26
        elif word[i].isdigit():
            stddisp = 48
            mod = 10
        elif word[i] in l1:
            stddisp = 33
            mod = 16
        elif word[i] in l2:
            stddisp = 58
            mod = 7
        elif word[i] in l3:
            stddisp = 32
            mod = 6
        else:
            # LEAVE other characters unchanged
            new_word += word[i]
            continue

        row = ord(word[i]) - stddisp
        col = ord(key[i % len(key)]) - stddisp
        new_word += chr(stddisp + (row + col) % mod)
            
    return new_word

def decode(word, key):
    decoded_word = ""
    key = key.lower()
    l1 = list('!"#$%&()\'*+,-./')
    l2 = list(':;<=>?@')
    l3 = list('[\\]^_`')
    
    for i in range(len(word)):
        # 1. DO NOT decode spaces; keep them as is
        if word[i] == ' ':
            decoded_word += ' '
            continue

        # 2. Handle other characters
        if word[i].isupper():
            stddisp = 65
            mod = 26
        elif word[i].islower():
            stddisp = 97
            mod = 26
        elif word[i].isdigit():
            stddisp = 48
            mod = 10
        elif word[i] in l1:
            stddisp = 33
            mod = 16
        elif word[i] in l2:
            stddisp = 58
            mod = 7
        elif word[i] in l3:
            stddisp = 32
            mod = 6
        else:
            decoded_word += word[i]
            continue
        
        row = ord(word[i]) - stddisp
        col = ord(key[i % len(key)]) - stddisp
        # Decoding formula
        decoded_word += chr(stddisp + (row - col) % mod)
            
    return decoded_word

def main():
    while True:
        print("----------------------")
        print("1: Encode plain text")
        print("2: Decode encrypted text")
        inpt = input("Enter choice: ")
        
        if inpt == "1":
            text = input("Enter text: ")
            keyword = input("Enter keyword: ")
            print("Encoded text: " + encode(text, keyword))
        elif inpt == "2":
            text = input("Enter text: ")
            keyword = input("Enter keyword: ")
            print("Decoded text: " + decode(text, keyword))
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()