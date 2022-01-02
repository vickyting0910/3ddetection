# 3D Object Detection

This project aims for Visualization, Fusion and Object Detection on LIDAR and Camera data. 


## Data

This project uses the data from the [Waymo Open dataset](https://waymo.com/open/). 


## Requirements

### Installation

- conda install numpy
- TensorFlow Object Detection API: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html
- WSL GPU Installation: https://docs.nvidia.com/cuda/wsl-user-guide/index.html
- CUDA Archive: https://developer.nvidia.com/cuda-toolkit-archive
- cuDNN Installation: https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html
- waymo_open_dataset: https://github.com/waymo-research/waymo-open-dataset/blob/master/docs/quick_start.md

### Clone from Github

- Simple Waymo Open Dataset Reader/ https://github.com/gdlg/simple-waymo-open-dataset-reader
- SFA3D/ https://github.com/maudzung/SFA3D
- Complex-YOLOv4-Pytorch/ https://github.com/maudzung/Complex-YOLOv4-Pytorch

### Download Pre-trained Models under ./tool/objdet_models/darknet or resnet/pretrained

python download_pretrain.py

- https://drive.google.com/file/d/1RcEfUIF1pzDZco8PJkZ10OL-wLL2usEj/view
- https://drive.google.com/file/d/1Pqx7sShlqKSGmvshTYbNDcUEYyZwfn3A/view

### Download Pre-Computed Results under ./results

- https://drive.google.com/drive/folders/1IkqFGYTF6Fh_d8J3UjQOSNJ2V42UDZpO
- https://drive.google.com/drive/folders/1-s46dKSrtx8rrNwnObGbly2nO3i4D7r7

## Pipeline

### Setup Google Cloud Credentials

1. Download the file and extract from https://cloud.google.com/sdk/docs/install

2. Run ./google-cloud-sdk/bin/gcloud init

3. Log in by gcloud auth login

4. Check in the bucket: https://console.cloud.google.com/storage/browser/waymo_open_dataset_v_1_2_0_individual_files/


### Set up the Example

1. Download a file from the bucket under ./training/

2. Read in the file

data_filename = './training/training_segment-10017090168044687777_6380_000_6400_000_with_camera_labels.tfrecord'
show_only_frames = [0, 1] 
datafile = WaymoDataFileReader(data_filename)
datafile_iter = iter(datafile)  # initialize dataset iterator


### Pre-processing: Compute Lidar Point-Cloud from Range Image

exec_list = ['show_range_image']: pre-process lidar and range images

1. extract lidar data and range image

2. map the range channel onto an 8-bit scale

3. focus on +/- 90° around the image center on the range channel

4. map the intensity channel onto an 8-bit scale

5. remove the outliers of the intensity channel

6. stack the range and intensity channels

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/range_image.png)


### Visualization using open3d
exec_list = ['show_pcl']: visualize point clouds

1. initialize open3d

2. create open3d instance

3. convert the point-cloud into 3d vectors

4. add geometry

5. visualize point clouds

6. close the windows after mouse right click

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds1.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds2.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds3.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds4.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds5.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds6.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/pointclouds7.png)

Visually, at least 3 cars can be identified  from the point clouds of different angles. The features are stable over point clouds, height and intensity maps. Also, the observations are stable via model-based object detections. 

### Bird's Eye View (BEV)
exec_list = ['pcl_from_rangeimage', 'bev_from_pcl']: create the tensor from intensity, height and density layers

1. pre-process too low reflectivity

2. bev-map discretization

3. transform all metrix x-, y-coordinates into bev-image coordinates

4. visualize point clouds

5. compute intensity layer of the BEV map

6. compute height layer of the BEV map

7. compute density layer of the BEV map

8. create the tensors

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/intensity.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/height.png)


### Model-based Object Detection

exec_list = ['pcl_from_rangeimage', 'load_image', 'bev_from_pcl', 'detect_objects', 'show_objects_in_bev_labels_in_camera']

The model is based on [Super Fast and Accurate 3D Object Detection](https://github.com/maudzung/SFA3D)

1. load model configs

2. load object detection configs

3. load the model

4. infer the results

5. decode the model outputs

6. detect objects

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/labels.png)

![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/detectedobjects.png)


### Evaluation

exec_list = ['pcl_from_rangeimage', 'bev_from_pcl', 'detect_objects', 'validate_object_labels', 'measure_detection_performance', 'show_detection_performance']

1. calculate intersection over union (IOU) between label and detection bounding-box on detected objects

2. calculate the recall and precision

3. plot the results

precision = 1.0, recall = 1.0
![alt_text](https://github.com/vickyting0910/3dfusion/blob/main/img/eval.png)


