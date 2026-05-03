# 🧪 Selenium WebDriver Otomasyon Projesi

**Ders:** Yazılım Kalite Yönetimi (SQM)  
**Öğrenci:** Fadime Yaren Durmuş — 200201003  
**Test Edilen Site:** [automationexercise.com](https://automationexercise.com)

---

## 📌 Proje Hakkında

Bu proje, **Selenium WebDriver** ve **pytest** kullanılarak gerçek bir e-ticaret sitesinin temel kullanıcı akışlarını otomatik olarak test etmektedir. Testler **Page Object Model (POM)** mimarisiyle yazılmış olup **Chrome** ve **Firefox** tarayıcılarında çapraz-tarayıcı (cross-browser) olarak çalıştırılabilir.

---

## 🗂️ Proje Yapısı

```
selenium_project/
│
├── pages/                        # Page Object Model sınıfları
│   ├── base_page.py              # Tüm sayfalar için ortak fonksiyonlar
│   ├── home_page.py              # Ana sayfa aksiyonları
│   ├── products_page.py          # Ürünler & arama sayfası
│   ├── login_page.py             # Giriş & kayıt sayfası
│   ├── cart_page.py              # Sepet sayfası
│   └── contact_page.py           # İletişim formu sayfası
│
├── tests/                        # Test senaryoları
│   ├── test_search_product.py    # Ürün arama testleri
│   ├── test_login.py             # Giriş / negatif testler
│   ├── test_cart.py              # Sepet işlemleri testleri
│   └── test_contact.py           # İletişim formu testi
│
├── reports/                      # Otomatik oluşturulan HTML raporlar
├── conftest.py                   # Merkezi driver fixture (setup/teardown)
├── pytest.ini                    # pytest yapılandırması & rapor ayarları
├── requirements.txt              # Python bağımlılıkları
└── README.md
```

---

## ⚙️ Kurulum

### 1. Gereksinimler

- Python 3.8+
- Google Chrome ve/veya Mozilla Firefox
- pip

### 2. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

Bu komut aşağıdaki kütüphaneleri yükler:

| Kütüphane | Amaç |
|-----------|------|
| `selenium` | Tarayıcı otomasyonu |
| `pytest` | Test çalıştırma çerçevesi |
| `pytest-html` | HTML test raporu üretimi |
| `webdriver-manager` | ChromeDriver / GeckoDriver otomatik yönetimi |

---

## ▶️ Testleri Çalıştırma

### Tüm testler (Chrome + Firefox):
```bash
pytest
```

### Sadece belirli bir test dosyası:
```bash
pytest tests/test_search_product.py -v
```

### Sadece Chrome'da çalıştır:
```bash
pytest -k "chrome"
```

### Sadece Firefox'ta çalıştır:
```bash
pytest -k "firefox"
```

### Belirli bir test fonksiyonu:
```bash
pytest tests/test_search_product.py::TestSearchProduct::test_search_result_matches_keyword -v
```

---

## 📊 HTML Test Raporu

Testler çalıştırıldıktan sonra rapor otomatik olarak oluşturulur:

```
reports/test_report.html
```

Raporu tarayıcıda açmak için:
```bash
# Windows
start reports/test_report.html

# macOS
open reports/test_report.html

# Linux
xdg-open reports/test_report.html
```

---

## 🧩 Test Senaryoları

### 1. Ürün Arama (`test_search_product.py`)

| Test | Açıklama | Tür |
|------|----------|-----|
| `test_homepage_title` | Ana sayfa başlığını doğrula | Pozitif |
| `test_all_products_page_visible` | Ürünler sayfası görünürlük kontrolü | Pozitif |
| `test_search_returns_results` | Arama sonuçları bölümü görünüyor mu | Pozitif |
| `test_search_result_matches_keyword` | İlk sonuç aranan kelimeyi içeriyor mu | Pozitif |
| `test_search_no_results_for_invalid_query` | Geçersiz aramada sayfa çökmüyor mu | Negatif |

### 2. Kullanıcı Girişi (`test_login.py`)

| Test | Açıklama | Tür |
|------|----------|-----|
| `test_login_page_opens` | Giriş sayfası açılıyor mu | Pozitif |
| `test_login_invalid_email` | Yanlış email hata mesajı veriyor mu | **Negatif** |
| `test_login_empty_fields` | Boş form gönderimde sayfa kalıyor mu | **Negatif** |
| `test_signup_with_existing_email` | Mevcut email ile kayıtta hata mesajı | **Negatif** |

### 3. Sepet İşlemleri (`test_cart.py`)

| Test | Açıklama | Tür |
|------|----------|-----|
| `test_cart_page_opens` | Sepet sayfası açılıyor mu | Pozitif |
| `test_add_product_to_cart` | Ürün sepete eklenebiliyor mu | Pozitif |
| `test_cart_shows_correct_product` | Doğru ürün sepette görünüyor mu | Pozitif |

### 4. İletişim Formu (`test_contact.py`)

| Test | Açıklama | Tür |
|------|----------|-----|
| `test_contact_page_opens` | İletişim sayfası açılıyor mu | Pozitif |
| `test_contact_form_submission` | Form gönderimi başarı mesajı veriyor mu | Pozitif |

**Toplam:** 14 test senaryosu × 2 tarayıcı = **28 test çalışması**

---

## 🏗️ Mimari: Page Object Model (POM)

Bu projede **Page Object Model** tasarım deseni kullanılmıştır.

```
Test Dosyası
    │
    ▼
Page Object (örn. ProductsPage)
    │  → Elementlerin lokasyonları (locators) burada tutulur
    │  → Kullanıcı aksiyonları burada tanımlanır (search, click, vb.)
    ▼
BasePage
    │  → Ortak yardımcı fonksiyonlar (popup kapatma, js_click, wait)
    ▼
Selenium WebDriver
```

**POM'un Avantajları:**
- Element lokasyonları tek bir yerde — site değişirse sadece 1 dosya güncellenir
- Test kodları okunabilir ve bakımı kolay
- Kod tekrarı (DRY prensibi) ortadan kalkar

---

## 🔄 Cross-Browser Testing

`conftest.py` içindeki `@pytest.fixture(params=["chrome", "firefox"])` sayesinde her test otomatik olarak **iki farklı tarayıcıda** çalıştırılır.

```python
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    drv = create_driver(request.param)
    yield drv       # testi çalıştır
    drv.quit()      # tarayıcıyı kapat (teardown)
```

---

## 🛡️ Karşılaşılan Zorluklar & Çözümler

| Zorluk | Çözüm |
|--------|-------|
| Reklam popup'ları tıklamaları engelliyor | Generic `close_popups_if_any()` fonksiyonu |
| Element henüz yüklenmemiş | `WebDriverWait` + `expected_conditions` (explicit wait) |
| Normal `.click()` çalışmıyor | `JavaScript execute_script` ile tıklama |
| Her testte driver açıp kapama | `conftest.py` fixture + `yield` ile otomatik teardown |
| Testlerin sonucunu görsel takip | `pytest-html` ile HTML rapor üretimi |

---

## 📚 Kullanılan Teknolojiler

| Teknoloji | Versiyon | Amaç |
|-----------|----------|------|
| Python | 3.8+ | Programlama dili |
| Selenium WebDriver | 4.x | Tarayıcı otomasyonu |
| pytest | 7.x | Test framework |
| pytest-html | 4.x | Raporlama |
| webdriver-manager | 4.x | Driver yönetimi |
| Google Chrome | Güncel | Test tarayıcısı |
| Mozilla Firefox | Güncel | Test tarayıcısı |
