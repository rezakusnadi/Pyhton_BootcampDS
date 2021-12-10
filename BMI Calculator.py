nama=input('masukkan nama anda : ')
print('panjang nama anda sebanyak', len(nama), 'karakter')

angka=input('masukkan angka : ')
angka=int(angka)+10 ##declare bahwa yang di input ada angka
print('hasil anda setelah + 10 adalah : ',angka)

angka=input('masukkan angka : ')
angka=float(angka)+10 ##declare angka pecahan lebih aman di gunakan jika user masukkan angka pecahan
print('hasil anda setelah + 10 adalah : ',angka)

def hitungbmi(tinggi,berat) :
    tinggi=float(input('masukkan tinggi : '))
    berat=float(input('masukkan berat : '))
    hasil=berat/(tinggi*tinggi)
    print('hasil BMI : ',hasil)
hitungbmi(tinggi,berat)