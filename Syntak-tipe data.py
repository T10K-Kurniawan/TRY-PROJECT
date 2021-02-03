#tipe data skala = tipe data sederhana
anak1 = 'a'
anak2 = 'b'
anak3 = 'c'
anak4 = 'd'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list = tipe data daftar/array')
anak = ['a', 'b', 'c', 'd']
print(anak)
anak.append('e')
print(anak)

print('\nsapa anak 2')
print(f'hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nsapa semua anak ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]}')