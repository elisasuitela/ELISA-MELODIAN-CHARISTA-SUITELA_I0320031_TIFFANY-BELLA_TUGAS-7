input_nama = str(input("Nama :"))
input_ttl = input("Tempat, Tanggal Lahir: ")
input_alamat = input("Alamat: ")
input_status = input("Status (Kawin/Belum Kawin): ")
input_hobi = input("Hobi: ")

#fungsi 1
judul_awal = "biodata"
judul = judul_awal.upper()

#fungsi 2
judul_akhir = judul.center(50,'=')

#fungsi 3
nama = input_nama.capitalize()
ttl = input_ttl.capitalize()
alamat = input_alamat.capitalize()
status_kapital = input_status.capitalize()
print(status_kapital)
hobi = input_hobi.capitalize()

#fungsi 4
if status_kapital == "Kawin":
    status = status_kapital.replace("Kawin", "Menikah")
elif status_kapital == "Belum kawin":
    status = status_kapital.replace("kawin", "Menikah")


print(judul_akhir,"\n", "Nama: ", nama,"\n","Tempat & Tanggal Lahir: ",ttl, "\n","Alamat: ",alamat, "\n", "Status: ",status, "\n", "Hobi: ",hobi)

