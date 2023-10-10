
def generate_key(string, key):
    
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return key

def original_text(string, key):
    text = []
    for i in range(len(string)):
        orig = (ord(string[i]) - ord('A') - key[i]) % 26
        orig += ord('A')
        text.append(chr(orig))
    return ("".join(text))

string = input("> ")
zork = [25, 14, 17, 10]
key = generate_key(string, zork)
orig_txt = original_text(string, key)

print(orig_txt)