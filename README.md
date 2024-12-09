# YOLO-TransT ![](https://img.shields.io/badge/Contributor-Zheng_Wang-brightgreen.svg)  ![](https://hits.sh/github.com/XingshiXu/ZhengWang_YOLO-TransT.svg?style=plastic&extraCount=20&color=fe7d37)
### YOLO-TransT: Detection and tracking of estrus cow based on improved YOLOv8n and TransT models  
  
**Click** the followed video, please:  
[![Video Title](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/1.jpg)](https://www.youtube.com/watch?v=cj_6e8dhBjo)  

 
### 1.Abstract  
Real-time monitoring of estrus cows is labor-intensive and time-consuming for dairy farming. To achieve accurate detection and real-time positioning of estrus cows in natural scenes, a model named YOLO-TransT, integrating the improved You Only Look Once v8 Nano (YOLOv8n) and Transformer Tracking (TransT) models, was proposed for estrus cow detection and tracking. Firstly, the Context Augmentation Module (CAM) was incorporated into YOLOv8n to improve the model’s focus on the estrus cow by associating with mounting behavior scenes; Secondly, the Squeeze-and-Excitation (SE) module was introduced to boost the network’s learning ability and suppress redundant features; Thirdly, the improved YOLOv8n and TransT were integrated to obtain the YOLO-TransT model, which realized the detection and tracking of estrus cow; Finally, based on the YOLO-TransT model, a set of estrus monitoring and warning system was designed. The experimental results showed that in the detection part of the YOLO-TransT model, the improved YOLOv8n had an Average Precision of estrus (APestrus) of 92.60%, an F1-score of 92.00%, 3.14 M parameters, 9.70 G Floating-point Operations (FLOPs), and a detection speed of 7.0 ms/frame. Compared to the original YOLOv8n, the improved YOLOv8n had increased APestrus by 4.10% and F1-score by 3.25%, while keeping the parameters, FLOPs, and detection speed essentially unchanged; In the tracking part, the TransT model had a tracking success rate of 70.3% and an accuracy rate of 85.5%. In conclusion, the YOLO-TransT can accurately detect and track estrus cows in natural scenes, laying the foundation for intelligent livestock breeding.    
  
### 2.What we do?  
We proposed an automatic detection and tracking algorithm for estrus cows in farming scenarios based on computer vision and designed a cow estrus monitoring and early warning system.  

### 3.Why we do?  
**（1）Farming aspect**  
① Cows in large-scale dairy farms are conceived through artificial insemination, however, the estrus period of cows is very short, about more than 20 days of estrus once, each time only lasts 4-26 hours, during which mounting behavior is the most significant external manifestation.  
② Traditional manual inspections are labor-intensive, highly subjective, and low accuracy, and can no longer meet the requirements of modern farming.  
**（2）Technical aspect**  
③ Computer vision-based methods can minimize the stress caused by contact devices on cows.  
④ Existing computer vision-based methods can only detect the mounting behavior of cows, but cannot locate individual estrus cows and lack an early warning mechanism.  

### 4. What we accomplished?  
(1) An estrus cow detection and tracking algorithm YOLO-TransT was proposed by integrating the improved YOLOv8n and TransT models.  
(2) By introducing Context Augmentation Module (CAM) and Squeeze-and-Excitation (SE) modules into the YOLOv8n model, integrating scene-related information of estrus cow and mounting behavior, discarding redundant features, to achieve high detection accuracy.   
(3) A dairy cow estrus monitoring and warning system was designed based on the YOLO-TransT model, which could effectively meet the dairy cow estrus monitoring needs of large-scale farms and improve the level of refined management.  

  

### 5. Enviornment   
 ```
# Create and activate Conda environment
conda create -n yolo_transt python=3.7
conda activate yolo_transt

# Install PyTorch and torchvision
conda install -c pytorch pytorch=1.10.1 torchvision=0.11.2

# Install ultralytics package
pip install ultralytics

# Install other dependencies
conda install matplotlib pandas tqdm
pip install opencv-python tb-nightly visdom scikit-image tikzplotlib gdown
conda install cython scipy
sudo apt-get install libturbojpeg
pip install pycocotools jpeg4py
pip install wget yacs
pip install shapely==1.6.4.post2
```  
### 6. Quick Start   
1. Place the downloaded dataset or your own dataset in the ```YOLO-TransT/Detection/Dataset folder```;  
2. Configure the relevant file paths required for running the YOLO model. Please refer to https://github.com/ultralytics/ultralytics;  
3. Train the detection model: ```run Detection/ultralytics/yolo/v8/detect/my_train.py```.  
4. Download the pre-trained weights of the tracking model (you can download it from the [**Google Drive**](https://drive.google.com/drive/folders/141ugLESIekckWuz_2YrEqxBS9Tpjxx-i?usp=drive_link ) or [**Baidu Netdisk**](https://pan.baidu.com/s/1OpxwcvfrQ8b0rWomOy7WIg) (**Extraction Code**: ed35) and put it in the Tracking/ltr/checkpoints folder;; 
5. Configure the detection model weights and tracking model weights address, run Demo: ```detection/ultralytics/yolo/v8/detect/my_predict.py```.  
    
### 7. Dataset  
In order to promote communication in the scientific community, the full code is uploaded in this study; since the project funded by this research grant has not yet been completed, part of the dataset is temporarily uploaded for researchers and enthusiasts to communicate, and the rest of the data will be uploaded in full after the project is completed.  
  
To find the dataset used in this study, please make sure all files are downloaded from [**Google_Drive**](https://drive.google.com/drive/folders/141ugLESIekckWuz_2YrEqxBS9Tpjxx-i?usp=drive_link) or [**Baidu_Netdisk**](https://pan.baidu.com/s/1OpxwcvfrQ8b0rWomOy7WIg)(**Extraction code**：ed35)
  
### 8.Results  
![结果](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/Results.jpg)  
![结果00](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/results01.png)  
 [**Performance display：**](https://www.youtube.com/watch?v=cj_6e8dhBjo) https://www.youtube.com/watch?v=cj_6e8dhBjo  
