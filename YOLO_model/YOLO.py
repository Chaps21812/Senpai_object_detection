from ultralytics import YOLO
from ultralytics.data.converter import convert_coco
import mlflow
from ML_Tools.Utils.mlflow import connect_MLflow_local
from YOLO_Preprocess import process_fits_and_save_png

class YOLO_Machina():
    def __init__(self):
        self.model = YOLO("yolo11m.pt")

    def convert_coco_to_yolo(self, path:str):
        old_annotations = path+"/annotations"
        old_images = path+"/images"
        new_data = path+"/yolo_annotations"
        convert_coco(labels_dir=old_annotations, save_dir=new_data)
        process_fits_and_save_png(old_images,new_data+"/images")

    def train(self, data_path:str, epochs=1000, imgsz=1200, batch=0.7):
        self.model.train(data=data_path, epochs=epochs,imgsz=imgsz,batch=batch)

    def evaluate(self, data_path):
        self.model= self.model.eval()
        results = self.model.predict(data_path)
        return results


if __name__ == "__main__":
    model = YOLO_Machina()
    model.convert_coco_to_yolo("/mnt/c/Users/david.chaparro/Documents/data/fits_with_sp3_ra_dec_v3_COCO_dataset_mini")
    results = model.evaluate("/mnt/c/Users/david.chaparro/Documents/data/fits_with_sp3_ra_dec_v3_COCO_dataset_mini/yolo_annotations/images")
    print("Done!")

    
