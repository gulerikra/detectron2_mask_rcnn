# detectron2_mask_rcnn

Dataset hazırlarken kullanılan uygulama:

https://github.com/wkentaro/labelme

Etiketleme yapılırken poligon etiketleme yapılmalı.

Dataset klasörü içerisine train ve test klasörü açılır.

Train ve test içindeki fotoğraflar labelme uygulaması ile etiketlenir.


Model eğitimi için maskRcnn_detectron2.jpnyb kullanıldı.

Eğitim sonunda çıkan .pth uzantılı dosya yeterli


Modeli anaconda ile kullanabilmek için anaconda tarafında yapılması gereken adımlar:

1. conda create -n maskRcnn python=3.8.10

2. conda activate maskRcnn

3. pip install pyyaml==5.1

4. pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

 (Eğer bilgisayarda cuda yoksa 4. adım şu şekilde olmalı:)

 (pip install torch torchvision -f https://download.pytorch.org/whl/torch_stable.html)
 
5. pip install cython pyyaml==5.1

6. pip install -U torch torchvision

7. git clone https://github.com/facebookresearch/detectron2 detectron2_repo

8. cd detectron2_repo

9. pip install -e .

Detectron2_repo içerisine detect.py kodu ve .pth uzantılı ağırlık dosyası eklenir.

Test fotoğrafı:

![ngbfv](https://user-images.githubusercontent.com/62421679/221659824-90beaef5-6523-4284-94a3-8b8a44eb5ae9.PNG)

Çıktısı:

![bbb](https://user-images.githubusercontent.com/62421679/228287155-109988e1-0fa0-4bc6-a9bd-599ab681c41e.png)


Anaconda için lazım olabilecek ipuçları:

1. Anacondaya git kurmak için :  conda install -c anaconda git

2. Anaconda içinde kurulu olan enviroments listesi :  conda env list

3. Enviroment silmek için :  conda env remove --name <ortam-adı>

Not!!

Bilgisayarda Visual Studio yoksa pycocotools hatası alınır. Visual Studio kurulması gerekir.
