# YOLO-TransT ![](https://img.shields.io/badge/contributor-ZhengWang-brightgreen.svg)  
YOLO-TransT: Recognition and tracking of estrus cow based on improved YOLOv8n and TransT models  
[Effect display](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/Effect%20display.mp4)  
[![Video Title](https://www.bilibili.com/video/BV1wu4y1K7iM/?spm_id_from=333.337.search-card.all.click&vd_source=d68da64987fce61a59890c929d25cd3d)

 
### 1.Abstract  
Real-time monitoring of estrus cows is labor-intensive and time-consuming for dairy farming. To achieve accurate recognition and real-time positioning of estrus cows in natural scenes, a model named YOLO-TransT, integrating the improved You Only Look Once v8 Nano (YOLOv8n) and Transformer Tracking (TransT) models, was proposed for estrus cow recognition and tracking. Firstly, the estrus cows were directly labelled, enabling accurate recognition and providing an initial bounding box for subsequent tracking. Secondly, the Context Augmentation Module (CAM) was incorporated into YOLOv8n to improve the model’s focus on estrus cow by associating with mounting behavior scenes. Thirdly, the Squeeze-and-Excitation (SE) module was introduced to boost the network’s learning ability and suppress redundant features. Finally, the improved YOLOv8n was integrated with the TransT to achieve recognition and tracking of the estrus cow. The experimental results showed that in the detection part of the YOLO-TransT model, the improved YOLOv8n had an Average Precision of estrus (APestrus) of 92.60%, an F1-score of 92.00%, 3.14 M parameters, 9.70 G Floating-point Operations (FLOPs), and a detection speed of 7.0 ms/frame. Compared to the original YOLOv8n, the improved YOLOv8n had increased APestrus by 4.10% and F1-score by 3.25%, while keeping the parameters, FLOPs, and detection speed essentially unchanged; In the tracking part, the TransT model had a tracking success rate of 70.3% and an accuracy rate of 85.5%. In conclusion, the YOLO-TransT can accurately recognize and track estrus cows in natural scenes, laying the foundation for intelligent livestock breeding.  
  
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
(1) An estrus cow recognition and tracking algorithm that integrated improved YOLOv8n and TransT models was proposed.  
(2) 通过引入CAM和SE注意力机制，改进YOLOv8n模型，增强了对发情奶牛的场景关联以及重要特征的学习能力，实现了更高的检测精度。  
(3) 将改进的YOLOv8n和TransT融合算法成功部署，设计了一套发情奶牛监测预警系统，实现了发情行为的实时监测与告警功能，具备实际应用价值。  
(4) 所提出的系统兼具高精度、实时性与轻量化特点，可有效满足大规模养殖场发情奶牛监测的需求，并提升精细化管理水平。

### 5.Results  
  
### 6. Data
To find the dataset used in this study, please make sure all files are downloaded from:  
XXXXXXXXX
**Extraction code**：please email at wang_zheng@nwafu.edu.cn  
  
  

