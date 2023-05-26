<h3>Default Random Forest Sınıflandırıcı İle Sınıflandırma</h3>

![image](https://github.com/okancezik/RandomForestAlgorithm/assets/73329707/c9f3695c-da8e-4ecb-99ae-d3efccd74478)

<p>
  Default değerler ile oluşturulan sınıflandırıcı model kullanılarak yapılan sınıflandırma sonrası doğruluk skoru 0.9231 ölçüldüğü görüldü. 
  Karmaşıklık matrisini incelediğimizde ilk sınıfa ait örneklerin tamamı; ikinci sınıfa ait 7 örneğin 5 adeti ; 3. Sınıfa ait örneklerin yine 
  tamamı doğru olarak sınıflandırıldığı görülmektedir
</p>

<h3>20 Karar Ağaçlı Random Forest Sınıflandırıcı İle Sınıflandırma</h3>

![image](https://github.com/okancezik/RandomForestAlgorithm/assets/73329707/cb5a4c9b-cf1c-4b65-b475-2eb3cdcb077f)

<p>
  Karar ağacı sayısını 20 olarak belirlediğimizde sınıflandırma başarısında ciddi bir düşüş gözlemlendi.
  Bir önceki sınıflandırmada 100 karar ağacı bulunuyordu ve sınıflandırma başarısı 0.9231 iken şu an bu değer 0.8846.
  Ayrıca karmaşıklık matrisini incelediğimizde 1. Sınıftaki 10 örneğin 9’u doğru; ikinci sınıftaki 7 örneğin 6’sı doğru 3. Sınıftaki 9 örneğin 8’i doğru olarak
  sınıflandırıldığı gözlemlenmiştir.
</p>

<h3>Feature Importance Değerler Dikkate Alınarak Sınıflandırma</h3>

<p>
En düşük feature importance değerine sahip garden özelliği veri setinden çıkartarak sınıflandırma yapacağız ve sınıflandırma başarısını inceleyeceğiz.
</p>

![image](https://github.com/okancezik/RandomForestAlgorithm/assets/73329707/67b5b6bf-8c6c-4739-a346-f953171f4ac5)

<p>
  Sınıflandırma başarı metriklerini incelediğimizde bazı değerlerde değişiklik olduğunu ve accuracy_score değerinin arttığı gözlemlendi.
  Bu deney sonucu karmaşıklık matrisini incelediğimizde sınıflandırma başarısının arttığı gözlemlenmiştir. 1. Sınıfa ait 10 örneğin tamamı; 
  2. Sınıfa ait  7 örneğin 6’sı; 3. sınıfa ait 9 örneğin tamamının doğru sınıflandırıldığı görülüyor. 

  Buradan çıkarılması en önemli yorum, veri setinden çıkarılan özellik sınıflandırma başarısını arttırabilir. Çünkü modelin eğitilmesinde modele 
  gereksiz ve ayırt ediciliği düşük özellik vermek sınıflandırma eğitimini olumsuz etkileyebilir. Bu nedenle veri setlerinde ayırt edicilik 
  özelliği yüksek olan veriler kullanmak gerekir.
</p>  
-------------------------
<p>
En düşük 4 feature importance değerine sahip garden özelliği veri setinden çıkartarak sınıflandırma yapacağız ve sınıflandırma başarısını inceleyeceğiz.
</p>

![image](https://github.com/okancezik/RandomForestAlgorithm/assets/73329707/29c0a93c-7063-4d76-acb8-799cb250a12a)

<p>
  En düşük feature importance değere sahip 4 özelliği veri setinden çıkardığımızda sınıflandırma başarısında düşüş gözlemlenmiştir. 
  
  Karmaşıklık matrisini incelediğimizde 1. Sınıfa ait 10 örnekten 8’i doğru; ikinci sınıfa ait 7 örneğin 5 tanesi doğru; 3. Sınıfa ait 9 örneğin 
  8 tanesi doğru sınıflandırıldığı görülüyor.
</p>

<h3>Sınıflandırma Raporu</h3>

![image](https://github.com/okancezik/RandomForestAlgorithm/assets/73329707/f13d2c03-1cd6-40ca-9191-b5f0fbc97676)


