# Detection and tracking of ooestrus dairy cows based on improved YOLOv8n and TransT models ![](https://img.shields.io/badge/Contributor-Zheng_Wang-brightgreen.svg)  ![](https://hits.sh/github.com/XingshiXu/ZhengWang_YOLO-TransT.svg?style=plastic&extraCount=20&color=fe7d37)
### Detection and tracking of ooestrus dairy cows based on improved YOLOv8n and TransT models    
  

 
### 1.Abstract  
Real-time monitoring of ooestrus cows in dairy farming is labour-intensive and time-consuming. To achieve accurate detection and real-time positioning of ooestrus cows in natural scenes, a model named YOLO-TransT, integrating the improved YOLOv8n and Transformer Tracking (TransT) models, was proposed for ooestrus cow detection and tracking. Firstly, the Context Augmentation Module (CAM) was incorporated into YOLOv8n to enhance the model’s focus on the ooestrus cow by associating with mounting behaviour; Secondly, the Squeeze-and-Excitation (SE) module was introduced to boost the network’s learning ability and suppress redundant features; Thirdly, the improved YOLOv8n and TransT were integrated to obtain the YOLO-TransT model, which realised the detection and tracking of ooestrus cow; Finally, based on YOLO-TransT, a cow ooestrus monitoring and warning system was designed. The experimental results showed that in the detection part of the YOLO-TransT, the improved YOLOv8n achieved a 92.60% Average Precision of ooestrus (APooestrus), 92.00% F1-score, with 3.14 M parameters, 9.70 G Floating-point Operations (FLOPs), and a 7.0 ms/frame detection speed. Compared to the original YOLOv8n, the improved YOLOv8n had increased APooestrus by 4.10% and F1-score by 3.25%, while keeping the parameters, FLOPs, and detection speed essentially unchanged; In the tracking part, the TransT model had a tracking success rate of 70.3%, a precision value of 85.5%, and an Area under Curve (AUC) value of 71.4%. In conclusion, the YOLO-TransT could accurately detect and track ooestrus cows in natural scenes, laying the foundation for intelligent livestock breeding.    
  
### 2.What we do?  
We proposed an automatic detection and tracking algorithm for ooestrus cows in farming scenarios based on computer vision and designed a cow ooestrus monitoring and early warning system.    

### 3.Why we do?  
**（1）Farming aspect**  
① Cows in large-scale dairy farms are conceived through artificial insemination, however, the ooestrus period of cows is very short, about more than 20 days of oestrus once, each time only lasts 4-26 hours, during which mounting behaviour is the most significant external manifestation..  
② Traditional manual inspections are labor-intensive, highly subjective, and low accuracy, and can no longer meet the requirements of modern farming.    
**（2）Technical aspect**  
③ Computer vision-based methods can minimize the stress caused by contact devices on cows.    
④ Existing computer vision-based methods can only detect the mounting behaviour of cows, but cannot locate individual oestrus cows and lack an early warning mechanism.    

### 4. What we accomplished?  
(1) An oestrus cow detection and tracking algorithm YOLO-TransT was proposed by integrating the improved YOLOv8n and TransT models.    
(2) By introducing Context Augmentation Module (CAM) and Squeeze-and-Excitation (SE) modules into the YOLOv8n model, integrating scene-related information of oestrus cow and mounting behaviour, discarding redundant features, to achieve high detection accuracy.     
(3) A dairy cow oestrus monitoring and warning system was designed based on the YOLO-TransT model, which could effectively meet the dairy cow oestrus monitoring needs of large-scale farms and improve the level of refined management.    

  

### 5. Enviornment   
 ```
Conda create -n yolo_transt python=3.7
Conda activate yolo_transt
conda install -c pytorch pytorch=1.10.1 torchvision=0.11.2 
pip install ultralytics
conda install matplotlib pandas tqdm
pip install opencv-python tb-nightly visdom scikit-image tikzplotlib gdown
conda install cython scipy
sudo apt-get install libturbojpeg
pip install pycocotools jpeg4py
pip install wget yacs
pip install shapely==1.6.4.post2
```  
### 6. Quick Start   
1. Place the downloaded cow mounting behavior dataset or your own dataset in the ```YOLO-TransT/Detection/Dataset folder```;  
2. Configure the relevant file paths required for running the YOLO model. Please refer to https://github.com/ultralytics/ultralytics;  
3. Train the detection model: ```run Detection/ultralytics/yolo/v8/detect/my_train.py```.  
4. Download the pre-trained weights of the tracking model (you can download it from the [Google Drive](https://drive.google.com/drive/folders/141ugLESIekckWuz_2YrEqxBS9Tpjxx-i?usp=drive_link ) or [Baidu Netdisk](https://pan.baidu.com/s/1OpxwcvfrQ8b0rWomOy7WIg) (Code: ed35) and put it in the Tracking/ltr/checkpoints folder;    
5. Configure the detection model weights and tracking model weights address, run Demo: ```Detection/ultralytics/yolo/v8/detect/my_predict.py```.  
    
### 7. Dataset  
To find the dataset used in this study, please make sure all files are downloaded from 
[Google Drive](https://drive.google.com/drive/folders/141ugLESIekckWuz_2YrEqxBS9Tpjxx-i?usp=drive_link ) or [Baidu Netdisk](https://pan.baidu.com/s/1OpxwcvfrQ8b0rWomOy7WIg) (Code: ed35)
  
### 8.Results  
![结果](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/Result.jpg)  

 [**Performance display：**](https://www.youtube.com/watch?v=IYBWnM-T8Yc) https://www.youtube.com/watch?v=IYBWnM-T8Yc  
