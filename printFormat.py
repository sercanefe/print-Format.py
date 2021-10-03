#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:09:08 2021

@author: sercan
"""

#print ve formatlama

"""
\n 

eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa alt satırdan ekrana yazdırma işlemine devam eder.
"""

print("Ahmet\nSalih\nCem")

"""
\t

eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa bir tab boşluk bırakarak ekrana yazdırmaya devam eder.
"""

print("Ahmet\tSalih\tCem")

"""
type()

print() fonksiyonundan bahsetmişken type() fonksiyonunu öğrenmekte fayda var. 
type() fonksiyonu içine gönderilen değerin hangi veri tipinden olduğunu söyler.
"""

print(type(5))

"""
sep parametresi

print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız değerlerin arasına istediğimiz karakterlerin yerleştirilmesini sağlar.
eğer bu parametreyi kullanmazsak değerlerin arasına varsayılan olarak boşluk yerleştirildiğini biliyoruz.
"""

print("Mustafa","Murat","Halil",sep = "\n") 

"""
yıldızlı parametreler

eğer bir stringin başına * işareti koyup, print fonksiyonuna gönderirsek bu string karakterlerine ayrılacak 
ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacakttır.
"""

print(*"python")
print(*"python",sep = "!")

"""
formatlama

programlama yaparken bazı yerlerde bir stringin içinde daha önceden tanımlı string, float, int vs değerleri yerleştirmek isteyebiliriz.
böyle durumlar için pythonda "format()" fonksiyonu bulunmaktadır.
Örn: programımızda 3 tane tamsayı değerimiz var ve biz bunları bir string içinde ekrana basmak istiyoruz.
bunun için "format()" fonksiyonunun çok fazla özelliği olduğu için ben burada sadece en çok kullandığımız özelliğini göstereceğim.
"""

#burada 3 tane süslü parantezimiz {} var ve bunların yeirne sırasıyla format fonksiyonun içindeki değerler geçiyor.
print("{} {} {}".format(3.1423,5.324,7.324324))

a = 3
b = 4
print("{}  + {}'nin toplamı {}'dır.".format(a,b,a+b))

#süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.
print("{1} {0} {2}".format(20,"sercan",0o5))

#süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimizi söylüyor
print("{:.2f} {:.3f} {:.1f}".format(3.1463,5.2347,34.57984))

"""
format fonksiyonu ile ilgili kullanımları ihtiyacın olduğu zaman şu web sitesinden yararlanarak kullanabilirsin:
    https://pyformat.info/f
"""












