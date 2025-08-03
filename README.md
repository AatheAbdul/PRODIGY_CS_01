Caesar Cipher Encryption and Decryption | Aatheka Abdul Kadar

This is a simple Python-based implementation of the classic **Caesar Cipher**, a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

## 🔐 Features

- Encrypt plaintext using a key (shift value)
- Decrypt ciphertext using a key
- Handles both uppercase and lowercase letters
- Preserves non-alphabetic characters (spaces, punctuation, numbers)
- Input validation for both menu and key entries
- User-friendly command-line interface

---

## 🧠 How It Works

The Caesar Cipher works by shifting each letter of the alphabet by a fixed number (`key`). For example, using a key of 3:
Plain: A B C D E F ...
Cipher: D E F G H I ...

- For encryption: `(original_index + key) % 26`
- For decryption: `(original_index - key) % 26`

---
