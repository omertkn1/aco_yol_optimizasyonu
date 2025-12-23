# Bursa Belediyesi Geri Donusum Araci Rota Optimizasyonu
## ÖMER TAŞKIN
## 2212721023
## Github Repo:
## Proje Tanitimi

Bursa Belediyesine bagli geri donusum araci, haftalik olarak 12 farkli liseden atik toplamaktadir. Bu proje, yakit ve zaman kazanci icin en verimli rotayi belirlemek amaciyla Karinca Kolonisi Optimizasyonu (Ant Colony Optimization - ACO) algoritmasini kullanir.

## Ozellikler

- Google Maps API ile gercek mesafe verileri
- Karinca Kolonisi Optimizasyonu (ACO) algoritmasi
- Interaktif Streamlit web uygulamasi
- Folium ile harita gorsellestirmesi
- Yakinlasma grafigi ile algoritma performans takibi
- API Key guvenlik yonetimi

## Proje Yapisi

```
omer/
├── .gitignore              # Guvenlik dosyalari
├── .streamlit/
│   └── secrets.toml        # API anahtari (gizli)
├── data/
│   └── coordinates.py      # Bursa okul listesi
├── core/
│   ├── matrix_utils.py     # Google Maps mesafe hesaplama
│   └── ant_algorithm.py    # ACO algoritmasi
├── figure/                 # Gorsel ciktilar
├── main.py                 # Streamlit uygulamasi
├── requirements.txt        # Gerekli kutuphaneler
└── README.md              # Proje dokumantasyonu
```

## Kurulum

### Gereksinimler

- Python 3.8 veya ustu
- Google Maps API Anahtari

### Adimlar

1. Gerekli kutuphaneleri yukleyin:

```bash
pip install -r requirements.txt
```

2. Google Maps API anahtarinizi `.streamlit/secrets.toml` dosyasina ekleyin:

```toml
google_maps_api_key = "SIZIN_API_ANAHTARINIZ"
```

**ONEMLI**: API anahtarinizi `.env` veya `.streamlit/secrets.toml` dosyasina yazin. Bu dosyalar `.gitignore` icinde oldugu icin GitHub'a yuklenmez.

## Kullanim

Uygulamayi baslatmak icin:

```bash
streamlit run main.py
```

### Uygulama Arayuzu

1. **Sol Panel (Ayarlar)**:
   - Google Maps API Key: API anahtarinizi girin
   - Karinca Sayisi: 10-200 arasi (varsayilan: 50)
   - Iterasyon: 10-500 arasi (varsayilan: 100)
   - Decay: 0.0-1.0 arasi (varsayilan: 0.95)
   - Alpha: 0.0-5.0 arasi (varsayilan: 1.0)
   - Beta: 0.0-5.0 arasi (varsayilan: 2.0)

2. **ROTAYI HESAPLA** butonuna basin

3. **Ana Ekran**:
   - Sol taraf: Interaktif harita uzerinde optimum rota
   - Sag taraf: Yakinlasma grafigi ve ziyaret sirasi

## Kullanilan Algoritmalar

### Ant Colony Optimization (ACO)

Karinca Kolonisi Optimizasyonu, karincalarin yemek ararken biraktiklari feromon izlerinden esinlenilmis bir optimizasyon algoritmasidir.

**Algoritma Adimlari**:

1. **Baslangic**: Tum kenarlara esit feromon dagilimi
2. **Karinca Gezileri**: Her karinca bir cozum (rota) olusturur
3. **Feromon Guncelleme**: Iyi rotalar daha fazla feromon birakir
4. **Buharlaşma**: Feromon seviyesi zamana gore azalir
5. **Tekrar**: Belirlenen iterasyon sayisi kadar tekrarlanir

**Parametreler**:
- `alpha`: Feromon onemi
- `beta`: Mesafe onemi
- `decay`: Feromon buharlaşma orani

## Kullanilan Okullar

Bursa'daki 12 farkli lise (+ 1 merkez):

1. Osmangazi Belediyesi (Merkez - Cikis Noktasi)
2. Tofas Fen Lisesi
3. Bursa Anadolu Lisesi
4. Ulubatli Hasan Anadolu Lisesi
5. Ahmet Erdem Anadolu Lisesi
6. Cinar Anadolu Lisesi
7. Osmangazi Gazi Anadolu Lisesi
8. Nilufer IMKB Fen Lisesi
9. Bursa Erkek Lisesi
10. Hurriyet Anadolu Lisesi
11. Cumhuriyet Anadolu Lisesi
12. Baris Anadolu Lisesi
13. Ali Karasu Anadolu Lisesi

## Guvenlik

- **API Anahtari Korumasi**: `.gitignore` ile hassas bilgiler repoya eklenmez
- **secrets.toml**: Streamlit'in guveli API key yonetimi


## GitHub Repo Baglantisi

Projeyi GitHub'a yuklemek icin:

```bash
git init
git add .
git commit -m "Bursa Belediyesi ACO Rota Optimizasyonu"
git remote add origin https://github.com/kullanici_adi/aco_yol_optimizasyonu
git push -u origin main
```

**Dikkat**: `.env` ve `.streamlit/secrets.toml` dosyalarina gercek API KEY yazmamalisiniz. Boylece hassas bilgiler repoya push edilmez.

## Lisans

Bu proje egitim amacli hazirlanmistir.

## ÇALIŞMA BİÇİMİ ##
Localde çalışıyor.**streamlit run mainpy** kodunu terminalde çalıştırdıktan sonra sitemize ulaşıyoruz.burada api keye göre giriş mümkün.


