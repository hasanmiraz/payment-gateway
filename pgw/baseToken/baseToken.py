import secrets

s = secrets.token_urlsafe(512)
print(s)
print(len(s))
print(type(s))