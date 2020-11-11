
while True:
    password1 = input()
    password2 = input()
    if len(password1) < 10:
        print("СЛИШКОМ КОРОТКИЙ ПАРОЛЬ!")
    elif password1 != password2:
        print("ПАРОЛИ РАЗЛИЧАЮТСЯ!")
    else:
        print("ВСЕ ПРАВИЛЬНО!")
        break 

print("Done!")
# Чтобы проверить вхождение символов "abcd" в пароль password1 => "abcd" in password1
