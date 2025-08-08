from bitcrypt import BitCrypt

bit= BitCrypt()
if __name__ == "__main__":
    bitcrypt = BitCrypt()
    plaintext = (b"cybersecurity")
    encrypted = bitcrypt.encrypt(plaintext)
    print("Encrypted:", encrypted.hex())
    try:
        decrypted = bitcrypt.decrypt(encrypted)
        print("Decryption:", decrypted)
    except ValueError as e:
        print("Decryption failed:", e)