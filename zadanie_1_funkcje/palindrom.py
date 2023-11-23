def is_palindrom(text: str) -> bool:
    comparison = ''.join(ch.upper() for ch in text if ch.isalnum())
    return comparison == comparison[::-1]


text = '   na psa logiki,- golas pan'
print(is_palindrom(text))
