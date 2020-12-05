# Rakam Tanıma Projesi (Mnist) Flask & Heroku Model Deployment

![Test Image 1](DigitRecognizer.PNG)

## Proje Linki (*Heroku* ile Deploy edildi):

https://mnistdeployment.herokuapp.com/

### Amaç

Bu projede amacımız, Deploy ortamında sağlanan tuval alanına çizilen rakamları doğru bir şekilde tanımlamaktır.

### Gereklilikler

Repoyu olduğu gibi kopyalamanız veya forklamanız gerekmektedir.

### Projeyi Heroku'dan Çalıştırmak için:

1. Bu repo olduğu gibi kopyalanarak yeni bir repo oluşturulur. Örneğin Mnist-Prediction isimli bir repo veya forklayarak direk devam edebilirsiniz.
2. [Heroku](https://www.heroku.com/) 'dan hesap açılır.
3. Create New App bölümünden yeni bir uygulama açılır ve isimlendirilir.
4. Deploy bölümünde yer alan "Deployment Method" bölümünden Github seçilir.
5. Mnist-Prediction isminde Github'ta yer alan repo ile eşleştirme yapılır.
6. Manual Deploy diyerek model deploy edilir.

### Deployu Çalıştırma

İlk tahmin işlemi için için tahmin süresi 20 saniye kadar sürebilir (Bunun sebebi model yüklendiği içindir). Ancak daha sonra tahmin süresi büyük ölçüde azalmaktadır. 

### Veri Seti Hakkında

MNIST ("Modified National Institute of Standards and Technology") verisi, derin öğrenmenin fiilen "merhaba dünya" veri kümesidir. 1999'da piyasaya sürüldüğünden bu yana, el yazısı görüntülerden oluşan bu klasik veri kümesi, sınıflandırma algoritmalarını karşılaştırmak için oluşturulmuştur.

Mnist datası el yazısıyla yazılmış rakamların görüntülerinden oluşan bir veri setidir. Bu veri setinde yer alan görüntüler 0-9 arasında yer alan rakamlardan ve 28*28 pixel boyutlarında tek kanallı (gri) görüntülerden oluşmaktadır. Veri seti 60000 eğitim, 10000 test olmak üzere toplam 70000 adet görüntüden oluşmaktadır.

Veri seti hakkında daha fazla bilgi için: http://yann.lecun.com/exdb/mnist/index.html ziyaret edebilirsiniz.



#### Model Training


Training Process:

1. Train Test Split( test_size: 0.4 )
2. Normalized Training Data and reshape to (number of images,28,28,1)
3. Image Augumentation to generate augumented data 8 times the training data. Total training data becomes 9 times. 
4. Defining the model.
5. Model Plot

6. Applied Sparse Categorical Crossentropy loss function.
7. The submission part is for the generation of submission file for the kaggle Competition.(https://www.kaggle.com/c/digit-recognizer)

#### Accuracy:

Best that was achived in kaggle: 99.41%
Model currently running: 99.27% 



