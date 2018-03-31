class Pegawai:
    def __init__(self, nama, gaji=0):
        self.nama=nama
        self.gaji=gaji

    def tunjangan(self, persen):
        self.gaji=self.gaji + (self.gaji * persen)

    def kerja(self):
        print(self.nama, "Pekerjaannya")

    def __repr__(self):
        return "<Pegawai: nama = %s, gaji = %s>" % \
        (self.nama, self.gaji)

class Koki(Pegawai):
    def __init__(self,nama):
        Pegawai.__init__(self,nama,100000)
    def kerja(self):
        print(self.nama, "Membuat Masakan")

class PizzaRobot(Koki):
    def __init__(self, nama):
        Koki.__init__(self, nama)
    def kerja(self):
        print(self.nama, "Membuat Pizza")

class Koki_Sendiri():
    # def __init__(self):
    def kerja(self):
        print("Koki_Sendiri Membuat Masakan")

# Program Utama
if __name__ == "__main__":
    agus=Koki("Agus")
    print(agus)
    agus.kerja()

    # kk=Koki('patub')
    # kk=kk.kerja()
    print
    for kelas in Pegawai, Koki, PizzaRobot:
        objek=kelas(kelas.__name__)
        objek.kerja()
    print"----"
    objek=(Koki.__name__)
    print objek

    # koki_sdr=Koki_Sendiri()
    # hsl = koki_sdr.kerja()