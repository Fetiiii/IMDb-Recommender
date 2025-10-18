# IMDb TV Series Recommender

[English](#english) | [Türkçe](#türkçe)

## English

This project provides a recommendation system for TV series from IMDb. The system makes recommendations by calculating similarities based on series titles and genres.

### Features

- Automatic TV series data scraping from IMDb
- Advanced recommendation system (Sentence Transformers based)
- Console and web interface options
- Support for Turkish series titles

### Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Update dataset (optional):
```bash
python src/scraping/scraper.py
```

### Usage

#### Console Application

```bash
python src/recommendation.py
```

#### Web Interface

```bash
streamlit run src/app.py
```

### Project Structure

```
IMDb ML/
├── src/
│   ├── scraping/
│   │   └── scraper.py        # IMDb data scraping
│   ├── recommendation.py     # Recommendation system
│   └── app.py               # Streamlit web interface
├── data/
│   └── imdb_data.json       # IMDb dataset
├── requirements.txt         # Dependencies
└── README.md
```

### Technical Details

- **Data Collection**: IMDb web scraping with Selenium
- **Recommendation System**: Text similarity with Sentence Transformers
- **Web Interface**: Interactive interface with Streamlit

### Requirements

- Python 3.8+
- See `requirements.txt` for detailed requirements

### License

MIT License


# IMDb Dizi Öneri Sistemi

## Türkçe

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
