# problem
"""Check if a string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters."""

# long method
def f(s):
    
    return [
        f'has alphanumeric? {any([c.isalnum() for c in s])}',
        f'has alphabetical? {any([c.isalpha() for c in s])}',
        f'has digits? {any([c.isdigit() for c in s])}',
        f'has lowercase? {any([c.islower() for c in s])}',
        f'has uppercase? {any([c.isupper() for c in s])}',
    ]

# test
s="982340yhr0"
print(*f(s))  # has alphanumeric? True has alphabetical? True has digits? True has lowercase? True has uppercase? False
