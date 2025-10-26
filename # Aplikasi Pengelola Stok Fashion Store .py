# Aplikasi Pengelola Stok Fashion Store (Versi Fixed)
# Aplikasi sederhana untuk mengelola stok produk fashion menggunakan Python.
# Mengimplementasikan: If Statement, For/While Statement, Function, dan OOP.
# Perbaikan: Error handling input, pilihan produk dinamis, validasi lebih ketat.

class Product:
    """
    Kelas OOP untuk merepresentasikan produk fashion.
    Atribut: nama (str), harga (float), stok (int).
    """
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = max(0, stok)  # Pastikan stok tidak negatif
    
    def update_stok(self, jumlah):
        """
        Function untuk memperbarui stok produk.
        Menggunakan if statement untuk memvalidasi input (tidak boleh negatif).
        """
        if jumlah < 0:
            print("Error: Jumlah tidak boleh negatif!")
            return False
        self.stok = max(0, self.stok + jumlah)  # Pastikan tidak negatif
        print(f"Stok {self.nama} berhasil diperbarui menjadi {self.stok}.")
        return True
    
    def is_low_stock(self, batas_minimal=5):
        """
        Function untuk memeriksa apakah stok rendah.
        Menggunakan if statement untuk kondisi low stock.
        """
        if self.stok < batas_minimal:
            return True
        return False
    
    def __str__(self):
        status = " (LOW STOCK!)" if self.is_low_stock() else ""
        return f"{self.nama} - Harga: Rp{self.harga:,.0f} - Stok: {self.stok}{status}"

class Inventory:
    """
    Kelas OOP untuk mengelola inventaris (daftar produk).
    """
    def __init__(self):
        self.produk_list = []
    
    def tambah_produk(self, nama, harga, stok):
        """
        Function untuk menambahkan produk baru ke inventaris.
        """
        if not nama.strip():  # Validasi nama tidak kosong
            print("Error: Nama produk tidak boleh kosong!")
            return False
        produk_baru = Product(nama, harga, stok)
        self.produk_list.append(produk_baru)
        print(f"Produk '{nama}' berhasil ditambahkan.")
        return True
    
    def tampilkan_stok(self):
        """
        Function untuk menampilkan daftar stok.
        Menggunakan for statement untuk iterasi daftar produk.
        """
        if not self.produk_list:
            print("Inventaris kosong! Tambahkan produk terlebih dahulu.")
            return
        
        print("\n=== DAFTAR STOK PRODUK ===")
        total_stok = 0
        for i, produk in enumerate(self.produk_list, 1):  # Enumerate untuk index user-friendly
            print(f"{i}. {produk}")
            total_stok += produk.stok
        print(f"\nTotal stok keseluruhan: {total_stok}")
    
    def peringatan_low_stock(self):
        """
        Function untuk menampilkan peringatan stok rendah.
        Menggunakan for statement untuk iterasi, dan while untuk konfirmasi.
        """
        low_stock_count = 0
        low_stock_produk = []
        for produk in self.produk_list:
            if produk.is_low_stock():
                print(f"PERINGATAN: Stok {produk.nama} rendah ({produk.stok})!")
                low_stock_produk.append(produk)
                low_stock_count += 1
        
        if low_stock_count == 0:
            print("Tidak ada stok rendah.")
            return
        
        # While loop untuk konfirmasi (lebih robust)
        while True:
            jawab = input("Apakah ingin menambahkan stok untuk produk low stock? (y/n): ").lower().strip()
            if jawab == 'y':
                if low_stock_produk:
                    self.tampilkan_stok()  # Tampilkan daftar untuk pilih
                    try:
                        index = int(input("Pilih nomor produk (1-based): ")) - 1
                        if 0 <= index < len(self.produk_list):
                            jumlah = self.get_valid_int("Jumlah tambahan: ")
                            self.produk_list[index].update_stok(jumlah)
                        else:
                            print("Index tidak valid!")
                    except ValueError:
                        print("Input tidak valid!")
                break
            elif jawab == 'n':
                print("OK, peringatan ditutup.")
                break
            else:
                print("Masukkan 'y' atau 'n' saja!")
    
    def get_valid_int(self, prompt):
        """
        Helper function untuk input integer valid (dengan try-except).
        """
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Error: Masukkan angka bulat yang valid!")

    def get_valid_float(self, prompt):
        """
        Helper function untuk input float valid (dengan try-except).
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Masukkan angka yang valid!")

def main_menu(inventory):
    """
    Function utama untuk menu interaktif.
    Menggunakan while statement untuk loop menu hingga user keluar.
    """
    while True:
        print("\n=== APLIKASI PENGELOLA STOK FASHION STORE ===")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Stok")
        print("3. Periksa Peringatan Low Stock")
        print("4. Update Stok Produk")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            nama = input("Nama produk: ").strip()
            harga = inventory.get_valid_float("Harga (Rp): ")
            stok = inventory.get_valid_int("Stok awal: ")
            inventory.tambah_produk(nama, harga, stok)
        
        elif pilihan == '2':
            inventory.tampilkan_stok()
        
        elif pilihan == '3':
            inventory.peringatan_low_stock()
        
        elif pilihan == '4':
            if not inventory.produk_list:
                print("Tidak ada produk! Tambahkan dulu.")
                continue
            inventory.tampilkan_stok()
            try:
                index = int(input("Pilih nomor produk untuk update (1-based): ")) - 1
                if 0 <= index < len(inventory.produk_list):
                    jumlah = inventory.get_valid_int("Jumlah tambahan: ")
                    inventory.produk_list[index].update_stok(jumlah)
                else:
                    print("Index tidak valid!")
            except ValueError:
                print("Input tidak valid!")
        
        elif pilihan == '5':
            print("Terima kasih! Aplikasi ditutup.")
            break
        
        else:
            print("Pilihan tidak valid! Pilih 1-5.")

# Inisialisasi dan jalankan aplikasi (mulai kosong)
if __name__ == "__main__":
    inventory = Inventory()
    main_menu(inventory)
