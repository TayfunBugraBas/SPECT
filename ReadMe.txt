SPECT Kalp Hastalığı Teşhisi Proje Aşamaları

<----İlk yapılacaklar---->

1.Winrar içerisindeki herşeyi bir dosyaya yada rahat bulunabilecek bir uzantıya taşıyınız.

2.Aşamaları sırasıyla takip ediniz.

<----Gerekli Programlar---->

1.Bilgisayarınıza Python 3.8 veya üzeri bir paket Python yükleyiniz. https://www.python.org/downloads/

2.MySql Yükleyiniz  https://dev.mysql.com/downloads/installer/ (Her türlü eklenti gerekmektedir)

3.Visual Studio code yükleyiniz. https://code.visualstudio.com/

<----Mysql Database oluşturma---->

1.Bilgisayarınızın arama kısmına my sql workbench yazarak mysql workbenchini açınız.

2.Bir Mysql Connections oluşturunuz local varsa local olanı kullanmanız uygun olur.

3.açtıktan sonra üst çubuktan "Server->import Data yapınız.

4. DB klasörünü seçiniz.

5.Sol üst kısımda çıkan "import progress" tıklayınız.

6."Start import" tıklayınız.

7.flaskapp şemasının database'e yüklendiğinden emin olunuz.


<----Program içi yüklemeler Python---->

1.app.py dosyasının olduğu dosyayı Visual studio code ile açınız.

2. app.py yi Visual Studio code ile açınız, Python eklentisini yüklemeyi unutmayınız.

3.Terminal oluşturunuz 

4. Terminalde app.py dosyasının olduğu dosyaya gidiniz.

5. Terminalde "python -m venv env" yazarak sanal ortam oluşturunuz.

6. Terminalde "env\Scripts\activate" yazarak sanal ortamı aktif hale getiriniz.

7. Terminalde "pip install Flask" yazarak flaski yükleyiniz.

8. eğer pip yada python bulamazsa bilgisayar->gelişmiş sistem ayarları->ortam değişkenleri->path giderek  python pathini ve python içerisindeki scripts dosyasının pathini yerleştirmeniz gerekmektedir.
 
9. Her pip install aşamasından sonra visual studioyu yeniden başlatmanız gerekmektedir.

10. Terminalde "pip install flask-mysqldb" yazarak database erişim uzantısını yükleyiniz.

11. Terminalde "pip install flask-mysql-connector" yazarak database erişim uzantısını yükleyiniz.

12.Databaseinize erişmek için Gerekli bilgileri app.config yazan yerlerde doldurunuz.

13.Programı Terminalde "flask run" yazarak çalıştırınız.

<----Bunlar yapıldığında web aplikasyonu düzgün bir şekilde çalışması gerekir aksi taktirde Bana ulaşınız.---->

