"""
TIPE DATA DICTIONARY

"""

kamus_ind_eng = {}
kamus_ind_eng['anak'] = 'son'
kamus_ind_eng['istri'] = 'wife'
kamus_ind_eng['ayah'] = 'father'
kamus_ind_eng['ibu'] = 'mother'

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\ndata ini di kirimkan oleh server gojek')
data_dari_server_gojek = {
    'tanggal': '2021-02-03',
    'driver_list': [
        {'nama': 'a', 'jarak': 10}, {'nama': 'b', 'jarak': 100}, {'nama': 'c', 'jarak': 300},
        {'nama': 'd', 'jarak': 150}]
}
print(data_dari_server_gojek)
print(f"driver di sekitar sini'{data_dari_server_gojek['driver_list']}")
print(f"driver #1'{data_dari_server_gojek['driver_list'][0]}")
print(f"driver #1'{data_dari_server_gojek['driver_list'][3]}")
print(f"Driver Terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

