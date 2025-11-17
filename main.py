
print('-----------------------')
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('  5. modular \t [%]')
print('-----------------------')


operasi = input("Pilih operasi (1, 2, 3, 4, 5): ")
a = int(input("masukkan angka pertama: "))
b = int(input("masukkan angka kedua: "))


if operasi == '1':
    hasil = a + b
    print(f'Hasil: {a} + {b} = {hasil}')
elif operasi == '2':
    hasil = a - b
    print(f'Hasil: {a} - {b} = {hasil}')
elif operasi == '3':
    hasil = a * b
    print(f'Hasil: {a} * {b} = {hasil}')
elif operasi == '4':
    hasil = a / b
    print(f'Hasil: {a} / {b} = {hasil}')
elif operasi == '5':
    hasil = a % b
    print(f'Hasil: {a} % {b} = {hasil}')
else:
    print('Operasi tidak dikenali')

