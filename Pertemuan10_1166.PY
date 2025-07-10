print("HELLO WORLD")
import matplotlib.pyplot as plt #visualisasi data untuk data scientis
import seaborn as sns #visualisasi data matlotlib
import pandas as pd #untuk pengolahan data
# as = mengubah library menjadi object
# dokumentasi
data = {'mahasiswa': ['siti', 'hawa', 'adam', 'uri', 'isa'],  #tipe data dictionary
        'nilai': [20, 35, 30, 25, 40]} #tipe data list
df = pd.DataFrame(data) #df: variabel untuk menyimpan  #dataframe untuk membuat kolom
# print(df) #menampilkan output dari variabel df

plt.figure(figsize=(10, 6))  # Atur ukuran gambar
plt.pie((df['nilai']),labels=(df['kategori']))#diagram pie
#sns.barplot(x='kategori', y='nilai', data=data, color='purple') #x: vertikal y: horizontal color: untuk merubah warna bar
plt.title('Grafik Data') #penamaan visualisasi grafik data
plt.xlabel('mahasiswa') #penamaan visualisasi mahasiswa
plt.ylabel('Nilai') #penamaan visualisasi nilai
plt.show() #untuk menampilkan output