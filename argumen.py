def berikan_selamat(*args):
    print("Mari berikan selamat kepada: ")
    for i, x in enumerate(args):
        print("%s. %s" % (i+1, x))

berikan_selamat("ihfazh", "sakinah", "fufu","rasya")

# Mari berikan selamat kepada:
# 1. ihfazh
# 2. sakinah
# 3. fufu
# 4. rasya
print ""
def daftar_key_val(**kwargs):
    for key in kwargs:
        print("%s : %s" % (key, kwargs[key]))

daftar_key_val(nama='aryo',telp='1243546436')
# nama : aryo
# telp : 1243546436

# definisi fungsi
def beri_selamat(dari, ke):
    print("%s memberikan selamat kepada %s" % (dari, ke))
print ""
beri_selamat('rasya', 'ubay')
# ihfazh memberikan selamat kepada sufyan

 # memanggil fungsi 2 dengan menggunakan list didahului bintang
alist = ["ihfazh", "sufyan"]
beri_selamat(*alist)
# ihfazh memberikan selamat kepada sufyan

# panggil fungsi dengan keyword argument biasa
beri_selamat(ke="sufyan1", dari="ihfazh1")
# ihfazh memberikan selamat kepada sufyan

adict = {"ke": "sufyan", "dari": "ihfazh"}
beri_selamat(**adict)
# ihfazh memberikan selamat kepada sufyan