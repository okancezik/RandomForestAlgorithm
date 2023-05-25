# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:41:34 2023

@author: okan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# Bu fonksiyon özelliklerin feature importance skorlarını hesaplar ve grafik ile görselleştirir
def plot_feature_importance(rfc,X_train):
    
    # veri setindeki özelliklerin önem puanları hesaplandı
    feature_scores = pd.Series(rfc.feature_importances_, index=X_train.columns).sort_values(ascending=False)

    print(feature_scores)

    # Seaborn grafiği oluşturuldu
    sns.barplot(x=feature_scores, y=feature_scores.index)

    # Etiket isimleri eklendi
    plt.xlabel('Özellik önem skorları')
    plt.ylabel('Özellikler')

    # Grafiğe başlık eklendi
    plt.title("Özellik Önem Skor Grafiği")
    plt.show()

# Bu fonksiyon sınıflandırma sonrası karmaşıklık matrisini geri döndürür.
def calculate_confussion_matrix(y_test, y_pred):
    
    # Karmaşıklık matrisi oluşturuldu
    confussionMatrix = confusion_matrix(y_test, y_pred)
    return confussionMatrix
    
# Bu fonksiyon sınıflandırma raporunu geri döndürür. Örneğin accuracy score, recall vs başarı metriklerini.
def calculate_classification_report(y_test, y_pred):
    # classfication report
    return classification_report(y_test, y_pred)


# -------------DEFAULT PARAMETRELER İLE SINIFLANDIRMA--------------------

# Veri setini kullanmak üzere dataset adlı değişkene aktardım.
dataset = pd.read_csv("Dataset_Soru_2.csv")

# Dataset içindeki özellikleri X ve sınıf değişkeni y olarak ayırdım
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Veri setini eğitim ve test veri seti olarak ayırdım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

# Kategorik verileri sayısal değerlere dönüştürdük
encoder = ce.OrdinalEncoder(cols=['rooms', 'layer', 'location', 'price', 'garden', 'year','safety'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

''' Random Forest sınıflandırıcı model oluşturuldu.
(Random Forest Algoritmasında default karar ağacı 100 olarak gösterilmektedir.)'''
rfc = RandomForestClassifier(n_estimators=100,random_state=42)

# Sınıflandırıcı model eğitim veri seti ile eğitildi.
rfc.fit(X_train, y_train)

# Sınıflandırıcı model test veri seti ile sınandı.
y_pred = rfc.predict(X_test)

# Sonuç konsola yazdırıldı.
print('100 Karar ağaçlı model doğruluk skoru :  {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# veri setindeki özelliklerin önem puanları hesaplanır ve görselleştirildi.
plot_feature_importance(rfc, X_train)

# Karmaşıklık matrisi ekrana yazdırıldı
print('Confusion matrix\n\n', calculate_confussion_matrix(y_test, y_pred))

# sınıflandırma raporu konsola yazdırıldı
print(calculate_classification_report(y_test, y_pred))


# ------SINIFLANDIRICI MODELE FARKLI PARAMETRELER VEREREK SINIFLANDIRMA İŞLEMİ YAPMAK---------

'''Random Forest sınıflandırıcı model oluşturuldu.
Algoritmada kullanılacak ağaç sayısını 20 olarak belirttim.'''
rfc20tree = RandomForestClassifier(n_estimators=20,random_state=42)

# Sınıflandırıcı model eğitim veri seti ile eğitildi.
rfc20tree.fit(X_train, y_train)

# Sınıflandırıcı model test veri seti ile sınandı.
y_pred = rfc20tree.predict(X_test)

# Sonuç konsola yazdırıldı.
print('20 Karar ağaçlı model doğruluk skoru :  {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# Veri setindeki özelliklerin feature importance puanları hesaplanır ve görselleştirildi.
plot_feature_importance(rfc20tree, X_train)

# Karmaşıklık matrisi hesaplandı ve ekrana yazdırıldı.
print('Confusion matrix\n\n', calculate_confussion_matrix(y_test, y_pred))

# Sınıflandırma raporu hesaplandı ve ekrana yazdırıldı.
print(calculate_classification_report(y_test, y_pred))

# ---------EN DÜŞÜK FEATURE IMPORTANCE SKORA SAHİP ÖZELLİĞİ CIKARARAK SINIFLANDIRMA---------- 

# Dataset içindeki özellikleri X ve sınıf değişkeni y olarak ayırdım. (Garden özelliğini özelliklerden çıkardım)
X = dataset.drop(['class', 'garden'], axis=1)
y = dataset['class']

# Veri setini eğitim ve test veriseti olarak ayırdım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

# Kategorik verileri sayısal değerlere dönüştürdük
encoder = ce.OrdinalEncoder(cols=['rooms','layer','location', 'price','year','safety'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

# Sınıflandırıcı model eğitim veri seti ile eğitildi.
rfc.fit(X_train, y_train)

# Sınıflandırıcı model test veri seti ile sınandı.
y_pred = rfc.predict(X_test)

# Sonuç konsola yazdırıldı.
print('100 Karar ağaçlı(en düşük feature importance özellik çıkarıldı) model doğruluk skoru :  {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# Veri setindeki özelliklerin feature importance puanları hesaplanır ve görselleştirildi.
plot_feature_importance(rfc, X_train)

# Karmaşıklık matrisi hesaplandı ve ekrana yazdırıldı.
print('Confusion matrix\n\n', calculate_confussion_matrix(y_test, y_pred))

# Sınıflandırma raporu hesaplandı ve ekrana yazdırıldı.
print(calculate_classification_report(y_test, y_pred))

# ----------EN DÜŞÜK FEATURE IMPORTANCE SKORA SAHİP 2 ÖZELLİĞİ CIKARARAK SINIFLANDIRMA ----------

''' Dataset içindeki özellikleri X ve sınıf değişkeni y olarak ayırdım. 
(Garden ve Year özellikleri çıkarıldı)'''
X = dataset.drop(['class', 'garden','safety'], axis=1)
y = dataset['class']

# Veri setini eğitim ve test veriseti olarak ayırdım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

# Kategorik verileri sayısal değerlere dönüştürdük
encoder = ce.OrdinalEncoder(cols=['rooms','layer','location', 'price','year'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

# Sınıflandırıcı model eğitim veri seti ile eğitildi.
rfc.fit(X_train, y_train)

# Sınıflandırıcı model test veri seti ile sınandı.
y_pred = rfc.predict(X_test)

# Sonuç konsola yazdırıldı.
print('100 Karar ağaçlı(en düşük 2 feature importance özellik çıkarıldı) model doğruluk skoru :  {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# Veri setindeki özelliklerin feature importance puanları hesaplanır ve görselleştirildi.
plot_feature_importance(rfc, X_train)

# Karmaşıklık matrisi hesaplandı ve ekrana yazdırıldı.
print('Confusion matrix\n\n', calculate_confussion_matrix(y_test, y_pred))

# Sınıflandırma raporu hesaplandı ve ekrana yazdırıldı.
print(calculate_classification_report(y_test, y_pred))

# ---------EN DÜŞÜK FEATURE IMPORTANCE SKORA SAHİP 4 ÖZELLİĞİ CIKARARAK SINIFLANDIRMA----------- 

''' Dataset içindeki özellikleri X ve sınıf değişkeni y olarak ayırdım. 
(garden,year,safety,rooms özellikleri çıkarıldı)'''
X = dataset.drop(['class', 'garden','safety','year','rooms'], axis=1)
y = dataset['class']

# Veri setini eğitim ve test veriseti olarak ayırdım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

# Kategorik verileri sayısal değerlere dönüştürdük
encoder = ce.OrdinalEncoder(cols=['layer','location', 'price'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

# Sınıflandırıcı model eğitim veri seti ile eğitildi.
rfc.fit(X_train, y_train)

# Sınıflandırıcı model test veri seti ile sınandı.
y_pred = rfc.predict(X_test)

# Sonuç konsola yazdırıldı.
print('100 Karar ağaçlı(en düşük 4 feature importance özellik çıkarıldı) model doğruluk skoru :  {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# Veri setindeki özelliklerin feature importance puanları hesaplanır ve görselleştirildi.
plot_feature_importance(rfc,X_train)

# Karmaşıklık matrisi hesaplandı ve ekrana yazdırıldı.
print('Confusion matrix\n\n', calculate_confussion_matrix(y_test, y_pred))

# Sınıflandırma raporu hesaplandı ve ekrana yazdırıldı.
print(calculate_classification_report(y_test, y_pred))

