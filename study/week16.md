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

Day 72 (02/21)
---
어제 모델 튜닝을 하다보니 AUC는 잘 나오는데도 recall이 낮은 모델들이 많이 나타났다.  
아무래도 기존에 쓰던 loss가 AUC에 최적화 된 loss다보니 이런 결과가 나타나는 것 같았다.  
그래서 recall을 높일 수 있을만한 다른 loss가 없을까 찾아보다가, focal loss라는 것을 발견했다.  
기본적으로 CNN 계열에서 imbalanced data에 대한 classification을 할 때 사용하는 BCE의 변형인 듯하다.  
데이터의 label이 0과 1인 점, label이 1인 데이터가 상대적으로 매우 적은 점 등을 고려했을 때 focal loss의 목적과 비슷하다는 생각이 들어서 CFM에 적용해보았다.  
그랬더니 실제로 이전 loss를 쓸 때에 비해 recall 성능이 많이 좋아졌다.  
오늘까지는 모델을 최종적으로 개선하고, 내일부터는 앙상블을 시도할 예정이라 hyperparameter 튜닝을 대략적으로 마친 후 최종 모델 학습을 시작했다.  

+ ##### Focal loss 적용

Day 73 (02/22)
---
대회 마지막 날이라 앙상블에 집중한 하루였다.  
여러 아이디어들을 모아서 앙상블을 시도했는데, 결과적으로 EASE 모델 단일 성능을 능가하는 앙상블 결과가 나오지 않았다.  
내가 생각하기에는 user에 따른 recall의 차이가 커 보여서 이를 활용한 앙상블을 시도해보고 싶었는데, 구현 과정의 실수와 팀원들과의 의견 차이 등으로 인해 제대로 시도해보지 못해서 아쉬웠다.  
프로젝트 최종 결과는 6등으로 마무리했다.  
첫 대회에서 8등, 그 다음 대회에서 7등, 이번 대회에서 6등이니 나름 한 등수씩 발전했다고 볼 수도 있겠다.  
그래도 여러가지 시도를 많이 했는데 결과적으로 그에 걸맞는 성과를 내지 못한 건 참 아쉬운 부분이다.  

+ ##### 앙상블, Movie Rec 프로젝트 종료
