def satrni_hisobla(satr):
    harflar_soni = sum(1 for harf in satr if harf.isalpha())
    raqamlar_soni = sum(1 for harf in satr if harf.isdigit())
    bo'sh_joylar_soni = sum(1 for harf in satr if harf.isspace())
    return harflar_soni, raqamlar_soni, bo'sh_joylar_soni

satr = input("Istalgan satrni kiriting: ")
harflar_soni, raqamlar_soni, bo'sh_joylar_soni = satrni_hisobla(satr)
print(f"Harflar soni: {harflar_soni}")
print(f"Raqamlar soni: {raqamlar_soni}")
print(f"Bo'sh joylar soni: {bo'sh_joylar_soni}")
```

Kodni ishlatish uchun quyidagicha amal qilishingiz mumkin:

1. Kodni yozuvchi faylga saqlang.
2. Faylni oching va satrni kiriting.
3. Dastur harflar, raqamlar va bo'sh joylar sonini hisoblaydi va ekranga chiqaradi.
