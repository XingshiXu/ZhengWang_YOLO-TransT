# YOLO-TransT ![](https://img.shields.io/badge/contributor-ZhengWang-brightgreen.svg)  
YOLO-TransT: Detection and tracking of estrus cow based on improved YOLOv8n and TransT models  

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

  
### 5.Results  
![结果](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/Results.jpg)  
![结果00](https://github.com/XingshiXu/ZhengWang_YOLO-TransT/blob/main/results01.png)  
 [**Performance display：**](https://www.youtube.com/watch?v=cj_6e8dhBjo) https://www.youtube.com/watch?v=cj_6e8dhBjo  


 

  
### 6. Data  
To find the dataset used in this study, please make sure all files are downloaded from [HERE](https://pan.baidu.com/s/1675c35QjB4OXbnwClF0zwQ):  
https://pan.baidu.com/s/1675c35QjB4OXbnwClF0zwQ  
**Extraction code**：please email at wang_zheng@nwafu.edu.cn   
(Since the manuscript of our research is still under review, the data related to this research will be open sourced here after the manuscript is published.)  

  
  

