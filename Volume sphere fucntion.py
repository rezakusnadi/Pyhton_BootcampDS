def volum_bola () :
    pi = 3.14
    try:
        radius=float(input('Masukkan nilai Radius : '))
    except ValueError:
        print('Work with number ONLY !')
    else:
        hasil = (4/3)*pi*(radius**3)
        print('volume bola : ',hasil)
volum_bola()