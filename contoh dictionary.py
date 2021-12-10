nilai_ipa= {'andri':8,'darius':6,'muldoko':4,'henry':6,'bari':9,'dona':5,'karin':2,'danang':6,'latifa':7}
nama=input('masukkan nama siswa : ')
if nama in nilai_ipa :
    print('nilai ipa : ', nama,'adalah',nilai_ipa[nama])
else :
    print('data siswa tidak di temukan')
    print('berikut nama-nama siswa : ')
    for namasiswa in nilai_ipa.keys() :
        print(namasiswa)