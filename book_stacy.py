stack = []

def add_book(stack, name_book, name_author):
    new_book = [name_book, name_author]
    stack.append(new_book)
    print(f"{new_book} berhasil ditambahkan ke dalam stack")

def delete_book_last(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat dihapus")
    else:
        last_book = stack.pop()
        print(f"{last_book} berhasil dihapus dari stack")

def show_top_book(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat ditampilkan")
    else:
        top_book = stack[-1]
        print(f"Buku teratas di dalam stack adalah {top_book}")

while True:
    print("\nTumpukan buku saat ini:", stack)
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan anda (1/2/3/4): ")

    if pilihan == "1":
        name_book = input("Masukkan nama buku yang ditambahkan: ")
        name_author = input("Masukkan nama pengarang yang ditambahkan: ")
        add_book(stack, name_book, name_author)
    elif pilihan == "2":
        delete_book_last(stack)
    elif pilihan == "3":
        show_top_book(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini. Semoga membantu!")
        break
    else:
        print("Pilihan tidak valid, silakan masukkan pilihan yang benar.")

        
    

