Week 16 (02/19 ~ 02/23)
===
>  ##### 주간 요약
>  

Day 70 (02/19)
---
이번 프로젝트의 마지막 주간이다.  
CFM의 성능을 최대한 끌어올려보려고 feature를 건드려보다가, Catboost에서 User의 feature importance가 높은 것을 확인했었다.  
그래서 예전에 사용했던 LMF의 user embedding을 K-means clustering 한 후 t-SNE로 시각화했는데 생각보다 clustering이 잘 된 것처럼 보였다.  
실제로 Catboost에 넣었을 때 user cluster의 importance가 높게 나오기도 했다.  
반면, item도 clustering을 해 봤는데 feature importance도 작게 나오고, CFM에 넣었을 때 성능도 많이 떨어졌다.  

때문에 user cluster는 feature로 활용하되, item cluster는 배제 할 예정이다.  
모델이 무겁다보니 GPU 메모리를 많이 차지해서 최대한 feature selection을 하고 최소한의 feature를 활용하는 것이 중요한 것 같다.  

+ ##### Embedding Clustering

Day 71 (02/20)
---
어제의 결과를 바탕으로 feature selection과 함께 hyperparameter tuning을 하는 중이다.  
모델을 만져보면서 느낀 건데, resnet 등에서는 이미지의 크기를 줄이면서 channel 수를 늘리고, layer를 깊게 쌓아 나가는 듯한데 CFM에서는 오히려 그 반대로 하는 게 성능이 잘 나오는 것 같다.  
이미지의 크기는 줄여나가되, channel 수도 줄여가면서 최대한 feature interaction 정보를 압축해서 뽑아내고, layer를 깊게 쌓는 것보다는 embedding dimension을 키워 원본의 해상도를 높이는 것이 더 효과적이다.  

다만 여러 가지 방법들을 실험해보기에는 모델이 한 번 돌아가는 데 걸리는 시간이 너무 길다는 것이 문제다.  
그래서 실험은 한 두번 정도만 더 해 보고, 내일까지 최종 모델을 학습시켜서 제출해야 할 것 같다.  

+ ##### CFM 모델 튜닝
