# Flask & Heroku Mnist Dataset Model Deployment

![Test Image 1](DigitRecognizer.PNG)

## Proje Linki (*Heroku* ile Deploy edildi):

https://mnistdeployment.herokuapp.com/

### Amaç

Bu projede amacımız, Deploy ortamında sağlanan tuval alanına çizilen rakamları doğru bir şekilde tanımlamaktır.

### Veri Seti Hakkında

MNIST ("Modified National Institute of Standards and Technology") verisi, derin öğrenmenin fiilen "merhaba dünya" veri kümesidir. 1999'da piyasaya sürüldüğünden bu yana, el yazısı görüntülerden oluşan bu klasik veri kümesi, sınıflandırma algoritmalarını karşılaştırmak için oluşturulmuştur.

Mnist datası el yazısıyla yazılmış rakamların görüntülerinden oluşan bir veri setidir. Bu veri setinde yer alan görüntüler 0-9 arasında yer alan rakamlardan ve 28*28 pixel boyutlarında tek kanallı (gri) görüntülerden oluşmaktadır. Veri seti 60000 eğitim, 10000 test olmak üzere toplam 70000 adet görüntüden oluşmaktadır.

Veri seti hakkında daha fazla bilgi için: http://yann.lecun.com/exdb/mnist/index.html ziyaret edebilirsiniz.

### Gereklilikler

Repoyu olduğu gibi kopyalamanız veya forklamanız gerekmektedir.

### Projeyi Heroku'dan Çalıştırmak için:

1. Bu repo olduğu gibi kopyalanarak yeni bir repo oluşturulur. Örneğin Mnist-Prediction isimli bir repo veya forklayarak direk devam edebilirsiniz.
2. [Heroku](https://www.heroku.com/) 'dan hesap açılır.
3. Create New App bölümünden yeni bir uygulama açılır ve isimlendirilir.
4. Deploy bölümünde yer alan "Deployment Method" bölümünden Github seçilir.
5. Mnist-Prediction isminde Github'ta yer alan repo ile eşleştirme yapılır.
6. Manual Deploy diyerek model deploy edilir.

### Model Deployment Çalıştırma

İlk tahmin işlemi için için tahmin süresi 20 saniye kadar sürebilir (Bunun sebebi model yüklendiği içindir). Ancak daha sonra tahmin süresi büyük ölçüde azalmaktadır. 





