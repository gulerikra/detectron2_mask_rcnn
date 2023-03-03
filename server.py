from flask import Flask
import torch
import torchvision
import numpy as np
import cv2
import random
from matplotlib import pyplot as plt
# Detectron2 imports
import detectron2
from detectron2.utils.logger import setup_logger
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import ColorMode, Visualizer
app = Flask(__name__)
@app.route('/aiCalistir')
def aiCalistir():
    image_path = "dogru.png"
    image = cv2.imread(image_path)


    # Make prediction
    outputs = predictor(image)


    # Visualize predictions
    v = Visualizer(image[:, :, ::-1], metadata=None, scale=0.8)
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    id= outputs["instances"].pred_classes
    for i in id:
        if id[i] ==0:
            sonuc ="dogru"
            print("doğru ürün")
        else:
       sonuc = "eksik"
       print("eksik ürün")
       break
    return sonuc


if __name__ == '__main__':
    setup_logger()


    # Load configuration
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.6  # set threshold for this model
    cfg.DATASETS.TRAIN = ("deytap/train",) # Train Verilerimiz Yapılandırma Dosyasına Kaydeder
    cfg.DATASETS.TEST = ()
    cfg.DATALOADER.NUM_WORKERS = 2 # Çalışan Sayısı
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x.yaml") # Ağırlıkları Çeker ve Yapılandırma Dosyasına Ekler
    cfg.SOLVER.IMS_PER_BATCH = 2 # Batch Size
    cfg.SOLVER.BASE_LR = 0.001 # Learning Rate (Öğrenme Oranı)
    cfg.SOLVER.GAMMA = 0.05 # Learning Rate Azaltma Çarpımı
    cfg.SOLVER.STEPS = [500] # Learning Rate Azaltma Adım Sayısı
    cfg.TEST.EVAL_PERIOD = 200 # Eğitim Sırasında Modeli Değerlendirmek İçin Adım Sayısı
    cfg.DATASETS.TEST = ("deytap/test", ) # Tets Verilerimiz Yapılandırma Dosyasına Kaydeder


    cfg.SOLVER.MAX_ITER = 2000 # İterasyon Sayısı
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2 # Sınıf Sayısı
    cfg.MODEL.WEIGHTS = 'model_final.pth'
    predictor = DefaultPredictor(cfg)
    app.run()
