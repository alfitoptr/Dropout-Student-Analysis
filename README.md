# Proyek Akhir: Prediksi Dropout Mahasiswa

## Business Understanding
Dalam dunia pendidikan tinggi, dropout mahasiswa menjadi salah satu tantangan utama yang harus diatasi oleh institusi pendidikan. Dropout dapat disebabkan oleh berbagai faktor, termasuk latar belakang akademik, faktor sosial-ekonomi, dan performa akademik mahasiswa selama perkuliahan.

### Permasalahan Bisnis
Institusi pendidikan ingin mengurangi angka dropout mahasiswa dengan cara mendeteksi mahasiswa yang berisiko lebih awal. Dengan demikian, mereka dapat mengambil tindakan preventif yang tepat, seperti memberikan bimbingan akademik atau bantuan keuangan.

### Cakupan Proyek
Proyek ini bertujuan untuk:
1. Membuat model klasifikasi untuk mendeteksi apakah mahasiswa akan dropout atau tidak.
2. Mengembangkan aplikasi berbasis Streamlit untuk mempermudah deteksi dropout mahasiswa.
3. Membuat Student Dashboard untuk memantau profil dan kondisi mahasiswa saat ini.

### Persiapan

**Sumber Data:** Dataset diambil dari Dicoding Academy yang mencakup berbagai informasi mahasiswa terkait jalur akademik, demografi, dan faktor sosial-ekonomi.

**Setup environment:**
```
pip install -r requirements.txt
```

## Student Dashboard
Student Dashboard dibuat untuk membantu pemantauan kondisi mahasiswa berdasarkan data yang tersedia. Dashboard ini memungkinkan institusi pendidikan melihat pola dropout mahasiswa dan mengambil tindakan yang diperlukan.
Link Dashboard: [Klik di sini](https://lookerstudio.google.com/reporting/0467acad-0b62-4c25-a3f9-08bd4aba6e78)

## Menjalankan Sistem Machine Learning
Jalankan aplikasi Streamlit untuk mendeteksi dropout mahasiswa dengan perintah berikut:
```
streamlit run app.py
```
Atau dapat langsug mengakses link online berikut: [streamlit](https://dropout-student-analysis.streamlit.app/)

Repositori ini berisi beberapa file utama:
- **model/**: Folder yang berisi model.pkl dan scaler.pkl.
- **notebook.ipynb**: Notebook yang digunakan untuk pembuatan model.
- **app.py**: Aplikasi Streamlit untuk mendeteksi dropout mahasiswa.
- **data.csv**: Dataset yang digunakan dalam proyek ini.
- **columns.txt**: Daftar kolom yang digunakan dalam model.
- **requirements.txt**: File daftar package Python yang digunakan.

## Conclusion
Model klasifikasi yang dikembangkan telah mencapai akurasi yang tinggi dengan Random Forest Tuned mencapai 91.46%. Namun, masih ada ruang untuk perbaikan guna meningkatkan kinerja model.

Dari hasil analisis, ditemukan bahwa faktor utama penyebab dropout adalah:
- 22% mahasiswa yang dropout adalah seorang debitur, dibandingkan dengan hanya 6% pada mahasiswa yang tidak dropout.
- 32% mahasiswa yang dropout mengalami keterlambatan pembayaran biaya pendidikan, sedangkan hanya 2,5% dari mahasiswa yang tidak dropout yang mengalami hal serupa.

Hasil ini menunjukkan bahwa faktor finansial memiliki pengaruh besar terhadap kemungkinan mahasiswa mengalami dropout. Oleh karena itu, langkah-langkah intervensi perlu difokuskan pada aspek finansial serta pendampingan akademik.

### Rekomendasi Action Items
- Menyediakan program bantuan keuangan atau skema pembayaran fleksibel untuk mahasiswa dengan risiko finansial tinggi.
- Mengembangkan sistem peringatan dini bagi mahasiswa yang mengalami keterlambatan pembayaran agar mereka dapat diberikan solusi sebelum kondisi memburuk.
- Menyediakan layanan konsultasi keuangan bagi mahasiswa agar mereka dapat mengelola keuangan dengan lebih baik.
- Mengoptimalkan pemanfaatan data dari Student Dashboard untuk memberikan rekomendasi intervensi lebih awal kepada mahasiswa yang berisiko dropout.
- Menggunakan model ini sebagai bagian dari sistem pemantauan akademik untuk memberikan bimbingan lebih awal kepada mahasiswa yang memiliki risiko akademik tinggi.