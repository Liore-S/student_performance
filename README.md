# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah besar bagi sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberikan bimbingan khusus.

### Cakupan Proyek
Membuat sebuah aplikasi machine learning yang dapat memprediksi siswa yang akan melakukan dropout, membuat sebuah business dashboard yang dapat memberikan insight kepada pihak institusi, dan melakukan analisis terhadap faktor-faktor yang mempengaruhi siswa melakukan dropout. Data yang digunakan hanya data yang fokus pada faktor-faktor internal yang berada dibawah kendali langsung institusi pendidikan, daripada faktor eksternal seperti latar belakang orang tua.

### Persiapan

Sumber data: [GitHub](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)
Hardware: GPU NVIDIA Volta™ or higher with compute capability 7.0+. ([list](https://developer.nvidia.com/cuda-gpus))<br>
Software:
- Docker
- Visual Studio Code

#### Setup environment:

Docker Container:
- Metabase Container: <u>metabase/metabase:v0.49.6</u> **(Docker Hub)**
- Rapids Notebook Container: <u>nvcr.io/nvidia/rapidsai/notebooks:24.04-cuda12.2-py3.11</u> **(Nvidia NGC)**

```bash
docker run -d -p 4000:3000 --name metabase metabase/metabase:v0.49.6

# Ubah parameter --gpus sesuai dengan GPU ID yang digunakan
docker run -d --name rapids-vs --gpus '"device=7"' -v ~/student_performance:/home/rapids/student_performance nvcr.io/nvidia/rapidsai/notebooks:24.04-cuda12.2-py3.11
```

Python Libraries:
```bash
pip install -r requirements.txt
```

## Business Dashboard
```
# Metabase Account
Email: root@mail.com
Password: root123
```
### Dashboard Preview
![Dasbor Screenshot](liore-s-dashboard.png)

### Penjelasan


## Machine Learning App
Aplikasi ini dibuat menggunakan Streamlit. Aplikasi sudah dilakukan deployment di Streamlit Cloud berikut urlnya [Streamlit](https://student-analyzer.streamlit.app/) 

Untuk menjalan aplikasi ini secara lokal, jalankan perintah berikut:
```bash
streamlit run app.py
```
### App Preview
![App Screenshot](liore-s-MlApp.png)


## Conclusion
Berdasarkan analisis yang dilakukan terdapat beberapa faktor yang dapat mengindikan kelulusan/dropout pelajar pada Jaya Jaya Insitut. Beberapa faktor tersebut antara lain:
- Nilai
  - Pelajar yang mendapatkan nilai rendah pada semester awal cenderung melakukan dropout. Ini bisa disebabkan oleh beberapa faktor seperti kurangnya pemahaman materi, kurangnya minat, atau faktor lainnya.
- Umur
  - Pelajar yang berumur lebih tua cenderung melakukan dropout. Hal ini bisa disebabkan oleh beberapa faktor seperti kesibukan, pekerjaan, atau faktor lainnya.
- GDP, Inflation, Unemployment
  - Faktor ekonomi juga mempengaruhi kelulusan/dropout pelajar. Pelajar yang berasal dari keluarga dengan kondisi ekonomi yang kurang baik cenderung melakukan dropout.

### Rekomendasi Action Items

- Bimbingan
  - Memberikan bimbingan khusus kepada pelajar yang mendapatkan nilai rendah pada semester awal. Bimbingan ini bisa berupa bimbingan akademik, bimbingan psikologi, atau bimbingan lainnya.
  - Memberikan bimbingan khusus kepada pelajar yang berumur lebih tua. Bimbingan ini bisa berupa bimbingan akademik, bimbingan karir, atau bimbingan lainnya.
- Beasiswa
  - Memberikan beasiswa kepada pelajar yang berasal dari keluarga dengan kondisi ekonomi yang kurang baik. Beasiswa ini bisa berupa beasiswa penuh, beasiswa sebagian, atau beasiswa lainnya. Beasiswa ini bisa membantu pelajar untuk tetap melanjutkan pendidikannya. Selain itu, beasiswa ini juga bisa membantu pelajar untuk fokus pada pendidikannya tanpa harus bekerja. Hal ini juga terbukti dengan analisis yang menunjukkan bahwa pelajar dengan beasiswa cenderung menyelesaikan pendidikannya.
