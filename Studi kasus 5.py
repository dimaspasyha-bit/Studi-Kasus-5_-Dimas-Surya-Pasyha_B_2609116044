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

jenis_kendaraan = "motor"
jam_masuk = 7
jam_keluar = 14

durasi_parkir = jam_keluar - jam_masuk

total = biaya_parkir(jenis_kendaraan, durasi_parkir)

print("====== TARIF PARKIR ======")
print(f"Jenis kendaraan: {jenis_kendaraan}")
print(f"jam masuk: {jam_masuk}")
print(f"jam keluar: {jam_keluar}")
print(f"durasi parkir: {durasi_parkir}")
print(f"total biaya: {total}")
print("==========================")