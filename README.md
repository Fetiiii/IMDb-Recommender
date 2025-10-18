# IMDb TV Series Recommender

Bu proje, IMDb'den çekilen TV dizileri için bir öneri sistemi sunar. Sistem, dizilerin başlıkları ve türleri üzerinden benzerlik hesaplayarak öneriler yapar.

## Özellikler

- IMDb'den TV dizisi verilerini otomatik çekme
- Gelişmiş öneri sistemi (Sentence Transformers tabanlı)
- Konsol ve web arayüzü seçenekleri
- Türkçe dizi adları desteği

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Veri setini güncelleme (opsiyonel):
```bash
python src/scraping/scraper.py
```

## Kullanım

### Konsol Uygulaması

```bash
python src/recommendation.py
```

### Web Arayüzü

```bash
streamlit run src/app.py
```

## Proje Yapısı

```
IMDb ML/
├── src/
│   ├── scraping/
│   │   └── scraper.py        # IMDb veri çekme
│   ├── recommendation.py     # Öneri sistemi
│   └── app.py               # Streamlit web arayüzü
├── data/
│   └── imdb_data.json       # IMDb veri seti
├── requirements.txt         # Bağımlılıklar
└── README.md
```

## Teknik Detaylar

- **Veri Toplama**: Selenium ile IMDb web scraping
- **Öneri Sistemi**: Sentence Transformers ile metin benzerliği
- **Web Arayüzü**: Streamlit ile interaktif arayüz

## Gereksinimler

- Python 3.8+
- Detaylı gereksinimler için `requirements.txt` dosyasına bakın

## Lisans

MIT License