def biaya_parkir (jenis_kendaraan, durasi_parkir):
    jenis = jenis_kendaraan

    if jenis == "mobil":
        tarif_perjam = 5000
    elif jenis == "motor":
        tarif_perjam = 3000
    else:
        return False

    total_biaya = tarif_perjam * durasi_parkir

    return total_biaya

jenis_kendaraan = input("Masukkan jenis kendaraan anda: ")
jam_masuk = int(input("masukkan jam anda masuk keparkiran: "))
jam_keluar = int(input("masukkan jam anda keluar parkiran: "))

durasi_parkir = jam_keluar - jam_masuk

total = biaya_parkir(jenis_kendaraan, durasi_parkir)

print("====== TARIF PARKIR ======")
print(f"Jenis kendaraan: {jenis_kendaraan}")
print(f"jam masuk: {jam_masuk}")
print(f"jam keluar: {jam_keluar}")
print(f"durasi parkir: {durasi_parkir}")
print(f"total biaya: {total}")
print("==========================")