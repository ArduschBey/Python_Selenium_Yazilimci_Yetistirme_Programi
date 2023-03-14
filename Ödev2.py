from collections import Counter

students_list=[]

# Öğrenci Ekleme
def add_student():
    full_name = input("Lütfen sadece baş harfleri büyük olan ve aralarında tek boşluk olan bir isim ve soyad giriniz: ")
    students_list.append(full_name)
print(students_list)

# Öğrenci Çıkarma
def remove_student():
    full_name = input("Lütfen sadece baş harfleri büyük olan ve aralarında tek boşluk olan bir isim ve soyad giriniz: ")
    for student in students_list:
        if student==full_name:
            students_list.remove(full_name)
        else:
            print("Böyle bir kayıt görüntülenemiyor")
print(students_list)

# Çoklu Öğrenci Ekleme
def multiple_add_student():
    number_of_add = int(input("Lütfen eklemek istediğiniz öğrenci sayısını giriniz: "))
    i=0
    while i<=number_of_add:
        full_name = input("Lütfen sadece baş harfleri büyük olan ve aralarında tek boşluk olan bir isim ve soyad giriniz: ")
        students_list.append(full_name)
        i=i+1
        if i>=number_of_add:
            break

# Tüm öğrencileri Ekrana Yazdır
def show_all_students_list():
    for j in range(len(students_list)):
        print(students_list[j])

# Öğrenci Numarası Gösterme
def search_number_of_student():
    full_name = input("Lütfen sadece baş harfleri büyük olan ve aralarında tek boşluk olan bir isim ve soyad giriniz: ")
    for k in range(len(students_list)):
        if students_list[k]==full_name:
            print("{0} öğrenciye ait öğrenci numarası {1}'dir".format(full_name,k))

# Çoklu Öğrenci Silme
def multiple_delete_student():
    number_of_student = int(input("Silmek istediğiniz öğrenci sayısını giriniz: "))
    deleted_student=0
    while deleted_student<=number_of_student:
        student = input("Lütfen sadece baş harfleri büyük olan ve aralarında tek boşluk olan bir isim ve soyad giriniz: ")
        students_list.remove(student)
        deleted_student=deleted_student+1
        print(students_list)
        if deleted_student>=number_of_student:
            break


print("********* Öğrenci Kayıt Sistemine Hoşgeldiniz  *****")
       
while True:
    print("1.Buton Öğrenci Ekleme Butonudur.")
    print("2.Buton Öğrenci Çıkarma Butonudur.")
    print("3.Buton Çoklu Öğrenci Ekleme Butonudur.")
    print("4.Buton Tüm Öğrencileri Ekrana yazdırma Butonudur.")
    print("5.Buton Öğrenci Numarası Gösterme Butonudur.")
    print("6.Buton Çoklu Öğrenci Silme Butonudur.")
    print("7.Buton Sistemden Çıkış Butonudur.")

    choose_button=int(input("Hangi butona tıklamak istediğinizi seçiniz: "))

    if choose_button==1:
        add_student()
        print("Kayıt Yapıldı...")
        print(students_list) 
    elif choose_button==2:
        remove_student()
        print("Kayıt Silindi...")
        print(students_list) 
    elif choose_button==3:
        multiple_add_student()
        print("Çoklu Öğrenci Eklendi...")
        print(students_list) 
    elif choose_button==4:
        show_all_students_list()
        print("tüm Öğrenciler Görüntülendi...")
    elif choose_button==5:
        search_number_of_student()
        print("Öğrenci Numarası Görüntülendi...")
        print(students_list) 
    elif choose_button==6:
        multiple_delete_student()
        print("Çoklu Öğrenci Silindi...")
    else:
        print("Sistemden çıkış yapılıyor...")
        break