# detectron2_mask_rcnn

Dataset hazırlarken kullanılan uygulama:

https://github.com/wkentaro/labelme

Etiketleme yapılırken poligon etiketleme yapılmalı.

Dataset→ train ve val klasörü açılır.

Train ve val içine ayrı ayrı resimler ve train.json ve val.json label dosyası eklenir.


Model eğitimi için github linki:

https://github.com/yasarniyazoglu/Detectron2-MaskRcnn-Custom-Dataset

Eğitim sonunda çıkan .pth uzantılı dosya yeterli


Anaconda tarafında yapılması gereken adımlar:

1. conda create -n apra python=3.8.10

2. conda activate apra

3. pip install pyyaml==5.1

4. pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
 
5. pip install cython pyyaml==5.1

6. pip install -U torch torchvision

7. git clone https://github.com/facebookresearch/detectron2 detectron2_repo

8. cd detectron2_repo

9. pip install -e .

Detectron2_repo içerisine detect.py kodu ve ağırlık dosyası eklenir.

Test fotoğrafı:

![ngbfv](https://user-images.githubusercontent.com/62421679/221659824-90beaef5-6523-4284-94a3-8b8a44eb5ae9.PNG)

Çıktısı:

![vffdvf](https://user-images.githubusercontent.com/62421679/221659428-fe8427d2-e2b1-4cc7-9d33-6ab992a64e92.PNG)


