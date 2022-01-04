def caesarCipher(s, k):
    # Write your code here
    # s = s.lower()
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()
    newString = ""
    for char in s:
        ind = -1
        try:
            if not char.isupper():
                ind = alphabet_lower.index(char)
            else:
                ind = alphabet_upper.index(char)
        except:
            newString += char
            continue

        if not char.isupper():
            if ind + k < len(alphabet_lower):
                newString += alphabet_lower[ind + k]
            else:
                newString += alphabet_lower[(ind + k) % len(alphabet_lower)]
        else:
            if ind + k < len(alphabet_upper):
                newString += alphabet_upper[ind + k]
            else:
                newString += alphabet_upper[(ind + k) % len(alphabet_upper)]
    return newString


if __name__ == '__main__':
    print(caesarCipher("middle-Outz", 2))
