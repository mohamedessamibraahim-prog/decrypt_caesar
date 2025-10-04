def caesar_decrypt(text:str, shift:int):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isalpha() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

inp = input("Enter text: ")
shift = int(input("Enter shift value: "))
print(f"Decrypted text: {caesar_decrypt(inp, shift)}")