#percobaan pertama
stack =[1,2,3,4,5]
print ('Tumpukan sekarang:',stack)

stack.append(6)
print('tumpukan masuk:',6)
print('tumpukan sekarang:',stack)

stack.append(7)
print('tumpukan masuk:',7)
print('tumpukan sekarang:',stack)

out = stack.pop()
print('tumpukan keluar:',out)
print('tumpukan sekarang:',stack)

#percobaan kedua
queue=([1,2,3,4,5])
print('antrian sekarang:',queue)

queue.append(6)
print('antrian masuk:',6)
print('antrian sekarang:',queue)

queue.append(7)
print('antrian masuk:',7)
print('antrian sekarang:',queue)

out=queue.popleft()
print('antrian keluar:',out)
print('antrian sekarang:',queue)

#percobaan ketiga
def reverse_sentence(sentence):
    stack =[]
    reversed_sentence=""

    for word in sentence.split():
        stack.append(word)

    while len(stack)>0:
        reversed_sentence +=stack.pop()+""
        return reversed_sentence.strip()
sentence="Selamat pagi, bagaimana kabar anda?"
print(reverse_sentence(sentence))

#percobaan keempat
stack = []

def tambah_barang(stack, barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru}berhasil ditambahakan ke dalam stack.")

def hapus_barang_terakhir(stack):
    if len(stack) ==0:
        print("stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        barang_terakhir=stack.pop()
        print(f"{barang_terakhir}berhasil dihapus dari stack.")

def tampilkan_barang_teratas(stack):
    if len(stack) ==0:
        print("Stack kosong, tidak ada barang yang ditampilkan.)
    else:
        barang_teratas = stack[-1]
        print(f"barang teratas didalam stack adalah {barang_teratas}")
        