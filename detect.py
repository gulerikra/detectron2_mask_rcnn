import torch
import torchvision
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

# Detectron2 imports
import detectron2
from detectron2.utils.logger import setup_logger
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import ColorMode, Visualizer

# Setup logger
setup_logger()

# Load configuration
cfg = get_cfg()
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.8  # set threshold for this model
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2 # Sınıf Sayısı
cfg.MODEL.WEIGHTS = 'model_final_son.pth'
cfg.MODEL.DEVICE='cpu'   # cuda yoksa bu satır gerekli
predictor = DefaultPredictor(cfg)


# Load image
image_path = "dogru.png"
image = cv2.imread(image_path)

# Make prediction
outputs = predictor(image)
id= outputs["instances"].pred_classes
print(len(id))
for i in id:
    if id[i] ==0:
        sonuc ="dogru"
        print("doğru ürün")
    else:
        sonuc = "eksik"
        print("eksik ürün")
        break

# Visualize predictions
v = Visualizer(image[:, :, ::-1], scale=0.9)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

plt.figure(figsize = (20, 10))
plt.imshow(cv2.cvtColor(out.get_image()[:, :, ::-1], cv2.COLOR_BGR2RGB))
a =cv2.cvtColor(out.get_image()[:, :, ::-1], cv2.COLOR_BGR2RGB)
# print(a)
plt.show()
