"""
В чем преимущество кортежей?
Часто кортежи используются для транспортировки данных внутри программы
"""
lst = ["Alice"] * 10000 # ["Alice"] + ["Alice"] + ["Alice"] ....
tpl = ("Alice", ) * 10000
st = set(["Alice" + str(x) for x in range(1, 10000)])

print("List Size:", lst.__sizeof__(), "Bytes")
print("Tuple Size:", tpl.__sizeof__(), "Bytes")
print("Set Size:", st.__sizeof__(), "Bytes")