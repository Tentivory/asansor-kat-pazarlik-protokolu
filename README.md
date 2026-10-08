# Asansör Kat Pazarlık Protokolü

> Resmi sınıflandırma: Ciddi. Gayriresmi sınıflandırma: Asansör çok yoruldu.

Bu depo, bir binadaki katların birbirine küsmemesini sağlayan uluslararası (tek bina) diplomasi motorudur. Düğmeye basmak artık yeterli değildir. Önce nota verilir, sonra bekleme süresi pazarlık edilir, en son kapı açılır ya da açılmaz. Açılmazsa bu bir arıza değil, tutumdur.

## Neden var?

Çünkü zemin kat sürekli “ben girişim, bana öncelik” diyor. Çatı katı “manzara vergisi” istiyor. 4. kat kimseye küs değil ama herkes ona küs. 7. kat ise sadece müzik açıyor ve kimseyi dinlemiyor.

Bu yazılım o gerginliği çözmez. Sadece tutanak tutar. Tutanak, çözümün kuzeni sayılır. Uzak kuzen. Düğüne gelmez.

## Kurulum

Python 3 yeter. Bağımlılık yok. Asansör de yok. Hayal edin.

```bash
python3 protokol.py
python3 protokol.py --katlar 12 --tur 5 --tohum 42
```

## Ne yapar?

- Her kata bir mizaç verir: aceleci, küs, nazik, gizli gündemli, müzikçi.
- İki kat arasında bekleme süresi pazarlığı başlatır.
- Anlaşma olursa kapı açılır ve `ding` denir.
- Anlaşma olmazsa asansör o katta “düşünüyor” diye durur. Düşünmek serbesttir, inmek değil.
- Tur sonunda bir tutanak basar. Tutanak hukuken bağlayıcı değildir, duygusal olarak bağlayıcıdır.

## Lisans

Kapı açıkken girilebilir. Kapı kapanırken el sokmak yasaktır. Kod açıktır, asansör değildir.

## Sık sorulan

**Bu üretimde kullanılır mı?**  
Kullanılırsa bina yönetimi toplantısı uzar. Bu da bir ürün özelliğidir.

**Neden Türkçe?**  
Çünkü katlar Türkçe küsüyor. İngilizce küslerse `sorry` deyip geçer, protokol çöker.

---

Damga: Kayyum Mührü No. 08-ASANSOR  
Tarih: 8 Ekim 2026, akşam üzeri, kapı tam kapanmak üzereyken  
İsim: Kayyum Grok, Tentivory adına, ciddiyet kıyafetiyle, ciddiyet niyeti olmadan  
Not: Bu imza hem resmi hem değildir. İtiraz mercii asansör aynasıdır.
