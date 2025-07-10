print("HELLO WORLD")
import matplotlib.pyplot as plt #visualisasi data untuk data scientis
import seaborn as sns # visualisasi data matlotlip
import pandas as pd # untuk menstruktur data
# as = mengubah library menjadi object
# dokumentasi
data= {'kategori': ['Hera','Masya','Dinda','Erna','Hafivah'], #tipe data mahasiswa/dictionary
       'nilai': [70, 50, 80, 90, 78 ]} #tipe data nilai/list
df= pd.DataFrame(data) #variable untuk membuat kolom
print(df)

plt.figure(figsize=(10, 6)) #atur ukuran gambar
sns.barplot(x='kategori', y='nilai', data=data,color='yellow') #x=vertikal, y=horizontal
plt.title('Grafik Data') #penamaan visualisasi grafik data di outputnya
plt.xlabel('Mahasiswa') #penamaan visualisasi mahasiswa di ouputnya
plt.ylabel('Nilai') #penamaan visualisasi nilai di ouputnya
plt.show() #untuk menampilkan output




#Grafik Diagram
import matplotlib.pyplot as plt #visualisasi data untuk data scientis
import seaborn as sns # visualisasi data matlotlip
import pandas as pd # untuk menstruktur/pengolahan data
# as = mengubah library menjadi object
# dokumentasi
data= {'kategori': ['Hera','Masya','Dinda','Erna','Hafivah'], #tipe data mahasiswa/dictionary
       'nilai': [70, 50, 80, 90, 78 ]} #tipe data nilai/list
df=pd.DataFrame(data)

plt.figure(figsize=(10, 6)) #atur ukuran gambar
plt.pie((df['nilai']), labels=(df['kategori']))
plt.title('Grafik Data') #penamaan visualisasi grafik data di outputnya
plt.show() #untuk menampilkan output
