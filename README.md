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
![Dasbor Screenshot]()

### Penjelasan


## Menjalankan Sistem Machine Learning
Untuk menggunakan model prediksi *Dropout* mahasiswa, Anda dapat menjalankan kode berikut:

```py
python predict.py
```


## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
