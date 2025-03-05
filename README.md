# YOLO Containerized Model

This is a containerized model of YOLO built to run and train with CUDA. It has functionality to convert coco datasets to yolo datasets and output an evaluation as well. 

# Installation

# Usage
To use each of the commands, an example is provided below for ease of use. The arguments are (mode, model size (n,s,m,l,x), epochs/model directory)

## Dataset Conversion

docker run --rm --gpus all -v /mnt/c/Users/david.chaparro/Documents/data/fits_with_sp3_ra_dec_v3_COCO_dataset_mini:/app/data yolo_cuda convert n 0

## Training

docker run --gpus all --rm -v /mnt/c/Users/david.chaparro/Documents/data/fits_with_sp3_ra_dec_v3_COCO_dataset_mini:/app/data yolo_cuda train m 20

## Evaluation

docker run --rm --gpus all -v /mnt/c/Users/david.chaparro/Documents/data/fits_with_sp3_ra_dec_v3_COCO_dataset_mini:/app/data yolo_cuda eval n /app/data/yolo_annotations/models_and_results/model.pt