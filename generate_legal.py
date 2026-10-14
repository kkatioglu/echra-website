from pathlib import Path
from html import escape

DATE="13 Ekim 2026"
NOTE=("Hukuki metinler uygulamanın mevcut teknik işleyişine göre hazırlanmıştır. "
      "Veri sorumlusunun resmi unvanı ve tebligat adresi teyit edilmeden "
      "KVKK aydınlatma yükümlülüğü tam olarak yerine getirilmiş sayılamaz.")
LEGAL={
 "privacy":("Gizlilik Politikası",[
 ("Kapsam","Bu politika ECHRA iOS uygulaması, varsa Android uygulaması ve echra.com.tr tanıtım sitesinin veri işleme uygulamalarını açıklar. ECHRA, duyguları renk ve seslerle paylaşmaya, karşılıklı BONDS oluşturmaya ve karşılıklı onaya dayalı kısa ECHRA HUB sohbetlerine yönelik bir hizmettir."),
 ("İşlenen veriler","Kimlik doğrulama için gereken hesap bilgileri ve kullanıcı kimliği; seçilen takma ad ve ülke; isteğe bağlı profil fotoğrafı; gönderilen ve alınan ECHRA sinyallerinin zaman, tür, duygu ve yanıt durumları; BONDS, CLOSE, engelleme, bildirme ve TRACES kayıtları; uygulama tercihleri; kullanıcı açarsa çevrimiçi durumunun son görülme zamanı; kullanıcı izin verirse bildirim cihaz belirteci. Hizmetin çalışması ve güvenliği için teknik istek kayıtları işlenebilir."),
 ("Verilerin kullanım amaçları","Hesap ve oturum güvenliğini sağlamak; karşılıklı ECHRA/BONDS eşleşmesini yönetmek; sinyal ve bildirim iletmek; gönüllü çevrimiçi durumu göstermek; rapor ve engelleme taleplerini işlemek; kötüye kullanımı önlemek; seçilen kullanıcı tercihlerini uygulamak."),
 ("İsteğe bağlı fotoğraflar","Fotoğraf yüklemek zorunlu değildir. Uygulama özel dosya saklama alanı ve süreli erişim bağlantıları kullanır. Rastgele keşifte fotoğrafın paylaşımı, BONDS izinleri ve uygulama erişim kurallarıyla sınırlandırılır. Başka kişilerin ekranda gördükleri içerikleri ekran görüntüsüyle kaydetmesini teknik olarak tamamen engellemek mümkün değildir."),
 ("ECHRA HUB ve kısa sohbet","ECHRA HUB’da serbest metin sohbeti karşılıklı kabul ve geçici süre sınırıyla çalışır; mevcut uygulamada oturum sınırı 15 dakikadır. Mesaj metninin sunucu veritabanında kalıcı sohbet arşivi olarak tutulmaması amaçlanır. Gerçek zamanlı iletim ve hizmet sağlayıcılarının güvenlik günlükleri, sunucu mesaj arşivinden farklıdır. Kullanıcı ekranı kapattığında tüm üçüncü taraf sistemlerden anında silinme taahhüt edilmez."),
 ("Yapay zekâ ve simüle edilmiş profiller","Bazı BONDS profilleri açıkça SIMULATED/AI şeklinde etiketlenir; gerçek bir kişiyi temsil etmez. Bir AI karakteriyle sohbet ettiğinizde gönderdiğiniz metin, yanıt üretmek için ECHRA sunucusu üzerinden OpenAI API hizmetine aktarılabilir. API isteğinde saklama seçeneği kapalı olsa bile sağlayıcının kendi güvenlik, kötüye kullanım denetimi ve saklama kuralları ayrı olarak geçerli olabilir. AI karakterleri gerçek kişi değildir; yanıtlardaki bilgiler hata içerebilir."),
 ("Bildirimler ve çevrimiçi durum","Bildirim izni verdiğinizde gerekli cihaz belirteci bildirim altyapısı (Expo ve ilgili mobil platform) aracılığıyla işlenir. Bildirim izni cihaz ayarlarından kapatılabilir. Gerçek kişilerin ONLINE durumu yalnızca ilgili tercihi açtıklarında ve güncel uygulama etkinliği olduğunda paylaşılır. AI botlarının ONLINE işareti gerçek insan mevcudiyeti anlamına gelmez."),
 ("Hizmet sağlayıcılar ve aktarım","Hesap/doğrulama, veritabanı ve depolama için Supabase; push bildirim altyapısı için Expo ile Apple/Google; AI yanıtları için OpenAI; web barındırma için Railway gibi teknik hizmet sağlayıcılar kullanılabilir. Bu sağlayıcıların altyapısı yurt dışında veri işlenmesine neden olabilir. Aktarımın hukuki dayanağı ve uygulanacak güvenceler ayrıca veri sorumlusu tarafından belgelendirilmelidir."),
 ("Saklama, silme ve seçimler","Hesap verileri hizmetin sağlanması için gerekli olduğu sürece işlenir; kanuni saklama yükümlülükleri ve sınırlı teknik güvenlik/backup kayıtları ayrı değerlendirilir. Uygulama ayarlarında hesap silme işlemi başlatılabilir. TRACES silme seçeneği kişisel ekrandan kaydı gizler; karşı tarafın kendi kaydını otomatik silmez. İsteğe bağlı fotoğraf, bildirim ve çevrimiçi durum seçenekleri kullanıcı tarafından yönetilir."),
 ("Başvuru ve değişiklikler","KVKK kapsamında erişim, düzeltme, silme ve diğer başvurularınız için kkdigitalprojects+echra@gmail.com adresine yazabilirsiniz. Veri sorumlusunun resmi kimlik ve tebligat bilgileri ayrıca doğrulanmalıdır. Metnin tarihi ve maddeleri işleme faaliyetleri değiştiğinde güncellenir.")
 ]),
 "terms":("Kullanım Şartları",[
 ("Hizmet","ECHRA, kullanıcılara renk/ses temelli sinyal iletme, karşılıklı BONDS oluşturma ve isteğe bağlı kısa sohbet sunan bir mobil iletişim hizmetidir. Test aşamasındaki işlevler değişebilir; herhangi bir ECHRA için yanıt verilmesi garanti edilmez."),
 ("Hesap ve kullanım","Kullanıcı hesabından yapılan işlemlerden kullanıcı sorumludur. Yanlış kimliğe bürünmek, bir başkasını taciz etmek veya tehdit etmek, spam üretmek, sistem erişim kontrollerini aşmak, izinsiz otomasyon yapmak ve üçüncü kişilerin haklarını ihlal eden içerik paylaşmak yasaktır. Kullanıcıların yürürlükteki mevzuata uygun davranması gerekir."),
 ("Etkileşim ve rıza","İlk ECHRA veya BONDS oluşturmak karşı tarafın sürekli iletişim kurmak zorunda olduğu anlamına gelmez. PRIVATE soruları ve süreli sohbet ayrı izin kurallarına tabidir. Her kullanıcı gelen ECHRA’yı yanıtsız bırakabilir, BONDS’u kaldırabilir veya engelleyebilir."),
 ("AI karakterler","SIMULATED olarak etiketli karakterler otomatik üretimli içerikler sunabilir; gerçek kişilerin görüşleri veya eylemleri değildir. Bu içeriklere sağlık, hukuk, güvenlik ya da mali kararlar için tek başına dayanılmamalıdır. AI yanıtları hatalı olabilir."),
 ("Fotoğraf ve içerik","Yüklenen profil fotoğrafı üzerinde kullanıcının kullanım hakkı bulunmalıdır. Hukuka aykırı, başkasının özel hayatını veya fikri haklarını ihlal eden fotoğraf ve içerikler yüklenmemelidir. Kullanıcı hakları ihlal edilen içerikleri bildirebilir."),
 ("Geçici sohbetler","ECHRA HUB sohbeti mevcut sürümde sınırlı sürelidir. Hizmetin çalışması için geçici iletim yapılabilir; uçtan uca şifreleme veya tüm üçüncü taraf günlüklerinden otomatik silinme sözü verilmez."),
 ("Hizmetin durumu ve sorumluluk","Hizmet testteyken kesintiler, bildirim gecikmeleri ve değişiklikler meydana gelebilir. Mevzuatın izin verdiği ölçüde teknik kullanılabilirlik ve kullanıcılar arası karşılık verme garantisi verilmez. Bu hüküm tüketici ve veri koruma mevzuatından doğan emredici hakları sınırlandırmaz."),
 ("Şikâyet, engelleme, hesap silme","Engelleme/bildirme işlevleri uygulamadan kullanılabilir. Hesap silme talebi uygulamanın ayarlar bölümünden başlatılabilir. Ek bilgi için Hesap Silme ve Gizlilik sayfalarına bakınız."),
 ("Güncellemeler ve iletişim","Kullanım koşulları ürün işlevleri ve yürürlükteki hukuk doğrultusunda güncellenebilir. Destek ve iletişim için kkdigitalprojects+echra@gmail.com adresini kullanabilirsiniz. Yasal işletmeci ve tebligat bilgileri ayrıca doğrulanmalıdır.")
 ]),
 "cookies":("Çerez Politikası",[
 ("Web sitesinde kullanılan teknolojiler","echra.com.tr bu sürümünde reklam, takip pikseli, sosyal medya izleme kodu ve üçüncü taraf analiz çerezi içermez. Web sitesindeki statik HTML/CSS görselleri ve hukuki bağlantılar için ziyaretçiden ayrıca tercih çerezi alınmaz."),
 ("Teknik sunucu kayıtları","Tarayıcı ile sunucu arasında yapılan isteklerde IP adresi, zaman, istenen sayfa, tarayıcı bilgileri ve güvenlik iletim kayıtları barındırma altyapısının teknik günlüklerinde yer alabilir. Bu günlükler çerez değildir."),
 ("Yeni çerez eklenmesi","Gelecekte zorunlu olmayan analitik/pazarlama çerezleri eklenirse, kategori, amaç, sağlayıcı, saklama süresi ve gerekli kullanıcı izin mekanizması bu sayfaya ve siteye eklenmeden etkinleştirilmemelidir."),
 ("Tarayıcı ayarları","Çerez kullanımı olursa tarayıcı ayarları üzerinden depolanan çerezler silinebilir veya engellenebilir. Uygulama içi bildirim cihaz belirteci, tarayıcı çerezi değildir.")
 ]),
 "kvkk":("KVKK Aydınlatma Metni",[
 ("Veri sorumlusu","ECHRA hizmetinin işletmecisinin resmi kimliği ve tebligat adresi ayrıca doğrulanmalıdır. ECHRA marka adı tek başına veri sorumlusu kimliğinin yerine geçmez."),
 ("İşlenen veri kategorileri","Hesap ve kimlik doğrulama bilgileri, kullanıcı kimliği, takma ad ve ülke, tercihe bağlı profil fotoğrafı, ECHRA/BONDS/TRACES işlem kayıtları, PRIVATE izinleri, kısa sohbet oturum bilgileri, çevrimiçi olma tercihi ve cihaz bildirim belirteçleri, güvenlik ve teknik işlem günlükleri."),
 ("Amaçlar ve hukuki sebepler","Hesap oluşturma ve iletişim hizmeti sunma, izinlere dayalı BONDS ve oturum yönetimi, kullanıcı güvenliği ve şikâyet/engelleme taleplerinin işlenmesi amaçlanır. Hizmet için zorunlu işlemlerde KVKK m.5/2(c) sözleşmenin kurulması veya ifası, uygun durumlarda m.5/2(ç) hukuki yükümlülük veya m.5/2(f) meşru menfaat hükümleri değerlendirilebilir. Açık rıza gerektiren ayrı bir faaliyet varsa ayrıca onay alınır; her faaliyet için somut hukuki sebep veri sorumlusunca kesinleştirilmelidir."),
 ("Toplama yöntemi","Bilgiler uygulama üyeliği ve kullanımında kullanıcı girişleri, cihaz tercihleri, ECHRA sinyal olayları, isteğe bağlı fotoğraf/bildirim izni ve sunucu teknik işlemleri üzerinden elektronik ortamda toplanabilir."),
 ("Aktarımlar","Gerektiği ölçüde Supabase (kimlik/doğrulama, veritabanı ve dosya depolama), Expo ile Apple/Google (bildirim), OpenAI (AI sohbet yanıtı), Railway (web barındırma) gibi teknik hizmet sağlayıcılara aktarım yapılabilir. Yurt dışına aktarım koşulları ve hukuki mekanizması KVKK m.9 kapsamında ayrıca doğrulanmalıdır."),
 ("Saklama ve imha","Veriler işleme amaçları, gerekli operasyonel süreler ve kanuni saklama yükümlülükleri doğrultusunda tutulur. Hesap silme ve kişisel TRACES kaldırma işlevleri aynı kapsamda değerlendirilmez. Saklama envanteri ve imha süreleri veri sorumlusunca ilan edilebilir."),
 ("KVKK madde 11 kapsamındaki haklar","Kişisel verilerinizin işlenip işlenmediğini öğrenme, işlenmişse bilgi isteme, amacı ve uygun kullanımı öğrenme, yurt içi/yurt dışındaki aktarılan üçüncü kişileri bilme, eksik veya yanlış verilerin düzeltilmesini ve şartları oluştuğunda silinmesini/yok edilmesini isteme, bu işlemlerin aktarılan üçüncü kişilere bildirilmesini talep etme, yalnızca otomatik sistemlerce analiz sonucuna itiraz etme ve kanuna aykırı işlem nedeniyle zarar doğmuşsa giderim talep etme hakları bulunur."),
 ("Başvuru","Bu haklarla ilgili başvurularınızı kkdigitalprojects+echra@gmail.com adresine iletebilirsiniz. Veri sorumlusu unvanı ve tebligat bilgileri ayrıca doğrulanmalıdır; kimlik doğrulaması gereken talepler yürürlükteki usule göre ele alınır.")
 ]),
 "delete-account":("Hesap Silme",[
 ("Uygulama içinden silme","ECHRA → Ayarlar → ECHRA hesabımı sil seçeneğiyle hesap silme işlemini başlatabilirsiniz. Silme işlemi geri alınamaz; kimlik/doğrulama, uygulama profili, BONDS ilişkileri, ECHRA kayıtları ve isteğe bağlı fotoğraf ilgili uygulama işlemlerinin kapsamına göre kaldırılır."),
 ("Başka kullanıcılar","Diğer kullanıcıların kendi hesapları, bağımsız TRACES kayıtları ve kanunen tutulması gereken işlem kayıtları hesap silmeyle otomatik olarak ortadan kalkmayabilir."),
 ("Teknik saklama","Yedekler, güvenlik günlükleri, sağlayıcı kayıtları ve kanuni yükümlülüklerden doğan kayıtlar uygulamanın aktif verisinden farklı saklama sürelerine tabi olabilir."),
 ("Uygulamaya erişimin yoksa","Uygulamaya erişemiyorsanız hesap silme talebinizi kkdigitalprojects+echra@gmail.com adresine iletebilirsiniz. Hesap sahibi doğrulaması gerekebilir.")
 ]),
 "support":("İletişim ve Destek",[
 ("ECHRA desteği","ECHRA uygulamasındaki teknik sorunlar, BONDS/PRIVATE izinleri, hesap silme ve olası güvenlik ihlalleri için kkdigitalprojects+echra@gmail.com adresine yazabilirsiniz."),
 ("Yasal iletişim","Kişisel veri ve KVKK talepleri için kkdigitalprojects+echra@gmail.com adresini kullanabilirsiniz. Veri sorumlusunun resmi unvanı ve tebligat adresi henüz doğrulanmadığından hukuki bilgilendirme tamamlanmış sayılmaz."),
 ("Uygulama içi yardım","Uygulamadaki ayar ve engelleme/rapor işlevleri kullanılabilir. Ek destek için kkdigitalprojects+echra@gmail.com adresine ulaşabilirsiniz.")
 ])
}

head='''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#020507"><meta name="robots" content="index,follow"><title>__TITLE__ — ECHRA</title><link rel="icon" href="/echra-logo.png" type="image/png"><link rel="stylesheet" href="/style.css"></head><body><main class="legal-page"><div class="legal-head"><a class="legal-brand" href="/">ECHRA</a><a href="/">← Ana sayfa</a></div><h1>__TITLE__</h1><p style="font-size:12px;color:#6f858b">Güncelleme: __DATE__</p>'''
footer='''<footer><nav aria-label="Yasal bilgiler"><a href="/terms.html">Kullanım Şartları</a> · <a href="/privacy.html">Gizlilik</a> · <a href="/cookies.html">Çerezler</a> · <a href="/kvkk.html">KVKK</a> · <a href="/delete-account.html">Hesap Silme</a> · <a href="/support.html">İletişim</a></nav></footer></main></body></html>'''
for slug,(title,sections) in LEGAL.items():
 page=head.replace("__TITLE__",escape(title)).replace("__DATE__",DATE)
 if slug in ("kvkk","support"):
  page+=f'<p class="legal-note">{escape(NOTE)}</p>'
 for h,body in sections:
  escaped_body=escape(body).replace("kkdigitalprojects+echra@gmail.com", '<a href="mailto:kkdigitalprojects+echra@gmail.com">kkdigitalprojects+echra@gmail.com</a>')
  page+=f'<section><h2>{escape(h)}</h2><p>{escaped_body}</p></section>\n'
 page+=footer
 Path(slug+".html").write_text(page,encoding="utf-8")
print("LEGAL FILES:",", ".join(sorted(str(x) for x in Path(".").glob("*.html"))))
