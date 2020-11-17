"""
Частотный анализ. Пример
"""
message = "alice good alice bad good good bag good bad"

d = {}
for word in message.split():
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

print(d)
