"""
D3:R solution
"""
n = int(input())
words = set() # множество уже названных слов

for _ in range(n): # 0, 1, 2, 3
    current_word = input()
    words.add(current_word)

new_word = input()
if new_word in words:
    print("НЕ ЗАСЧИТАНО")
else:
    print("ЗАСЧИТАНО")