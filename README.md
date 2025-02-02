# Kaplumbağa Yakalama Oyunu

Bu proje, Python'un standart **turtle** kütüphanesi kullanılarak oluşturulmuş basit bir oyun örneğidir. Oyuncu, ekranda rastgele beliren kaplumbağalara tıklayarak puan kazanmaya çalışır. Kaplumbağalar, belirlenen hedefe ulaşmadan önce tıklanmazsa puan kaybına neden olur. Oyun 1 dakika sürer ve süre sonunda toplam skor ekrana yazdırılır.

## Özellikler

- **Oyun Başlangıcı:**  
  - Oyun başladığında bir pencere açılır.
  - Ekranda skor ve kalan zaman bilgisi görüntülenir.

- **Kaplumbağaların Hareketi:**  
  - Kaplumbağalar rastgele konumlarda ortaya çıkar.
  - Her kaplumbağa, rastgele belirlenmiş hedef noktasına doğru hareket eder.
  - Hedefe ulaşan kaplumbağa “kaçmış” sayılır ve skor -1 olarak güncellenir.

- **Oyuncu Etkileşimi:**  
  - Oyuncu kaplumbağalara tıklayarak onları “yakalar”.
  - Yakalanan kaplumbağa için skor +1 artar.
  - Yakalanan veya kaçan kaplumbağa, ekrandan kaybolur ve yerine yeni bir kaplumbağa oluşturulur.

- **Oyun Süresi ve Sonuç:**  
  - Oyun 60 saniye sürer.
  - Süre dolduğunda oyun sonlanır ve final skor ekranda gösterilir.

    
- **Nasıl Oynanır?**
  - Oyun başladığında ekranda rastgele beliren kaplumbağaları göreceksiniz.
  - Kaplumbağalara tıklayarak yakalamaya çalışın. Her başarılı tıklamada skorunuz +1 artar.
  - Eğer kaplumbağa hedef noktasına ulaşırsa, puanınız -1 azalır.
  - Oyun süresi 60 saniyedir. Süre dolduğunda oyununuz sonlanır ve final skorunuz ekranda gösterilir.
