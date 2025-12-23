

🤖 Türkçe Duygu Analizi Uygulaması (BERT & Docker)

Bu proje, girilen Türkçe metinlerin duygusal tonunu (Pozitif/Negatif) analiz etmek için geliştirilmiş uçtan uca bir yapay zeka servisidir. **BERT** mimarisi kullanılarak yüksek doğrulukta tahminleme yapar ve tamamen **Dockerize** edilmiş bir yapıya sahiptir.

 🛠️ Teknik Mimari

Proje, birbirine bağlı iki ana mikroservisten oluşmaktadır:

* **Frontend (Streamlit):** Kullanıcı etkileşimini yöneten, metin girişlerini alan ve sonuçları görselleştiren web arayüzü.
* **Backend (FastAPI):** `savasy/bert-base-turkish-sentiment-cased` modelini barındıran ve çıkarım (inference) yapan yüksek performanslı API katmanı.

 🚀 Kurulum ve Çalıştırma (Step-by-Step)

Uygulamayı çalıştırmak için bilgisayarınızda **Docker** ve **Docker Compose** kurulu olması yeterlidir. Başka hiçbir kütüphane veya model yüklemenize gerek yoktur.

 1. Projeyi İndirin

```bash
git clone https://github.com/HabipBolukbas/new_projectss.git
cd new_projectss

```

 2. Uygulamayı Ayağa Kaldırın

Terminalde şu komutu çalıştırarak her iki servisi (frontend ve backend) otomatik olarak kurun ve başlatın:

```bash
docker-compose up

```

*Bu komut ilk kez çalıştırıldığında gerekli Docker imajlarını oluşturacak ve BERT modelini güvenli bir şekilde indirecektir.*

 3. Uygulamaya Erişin

Servisler hazır olduğunda aşağıdaki linkleri kullanabilirsiniz:

* **Kullanıcı Arayüzü (Frontend):** [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)
* **API Dokümantasyonu (Backend):** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

 📂 Proje Yapısı

```text
.
├── app.py              # Streamlit Arayüz Kodu
├── main.py             # FastAPI & BERT Model Kodu
├── Dockerfile          # Backend için Docker yapılandırması
├── Dockerfile.frontend # Frontend için Docker yapılandırması
├── docker-compose.yml  # Servislerin orkestrasyon dosyası
├── deployment.yaml     # Kubernetes dağıtım dosyası
└── requirements.txt    # Gerekli Python kütüphaneleri

```

 📋 Nasıl Kullanılır?

1. Web arayüzünü açın.
2. Metin kutusuna analiz etmek istediğiniz Türkçe cümleyi yazın (Örn: *"Bu ürünün kalitesine bayıldım!"*).
3. **"Analiz Et"** butonuna basın.
4. Uygulama, cümlenin duygu durumunu ve bu tahmindeki güven skorunu (yüzde olarak) saniyeler içinde ekrana getirecektir.

---

