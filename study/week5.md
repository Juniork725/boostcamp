Week 5 (12/4 ~ 12/8)
===
>  ##### 주간 요약
>  

Day 21 (12/4)
---
지난주에 이어 RecSys 이론 강의를 듣는 주간이다.  
전체 10강 중 6강을 지난주에 들었기에 이번주는 비교적 강의가 널널할 것 같다.  

보통은 아침에 데일리스크럼을 할 때 당일 학습 목표량을 정하고 이를 공유하는데, 오늘은 프로젝트 주제에 대한 이야기를 추가로 나눴다.  
나는 주말동안 2가지 주제를 생각했는데, 하나는 당뇨병 환자를 위한 식단 추천이고 나머지는 개인 취향을 반영한 배경화면 이미지 생성기다.  
다른 조원들도 컴퓨터를 켜면 어떤 활동을 할지 추천해주는 프로그램과 취미 활동을 추천해주는 서비스 등을 제안했다.  
현재 조가 그대로 유지될지도 아직 미지수고, 파이널 프로젝트까지 기간도 많이 남아서 주제는 천천히 좀 더 고민해보기로 했다.  

강의 내용은 Graph Neural Network(GNN)에 대한 내용으로 시작했다.  
정형 데이터나 이미지와 달리 유저-아이템의 관계는 Graph를 통해 Non-Euclidean Space로 표현하는 것이 유리하다.  
Neural Graph Collaborative Filtering(NGCF)은 이런 graph 구조를 활용한 모델이다.  
각 유저와 아이템을 임베딩한 후, 이들로 Message를 만든다. 한 유저에 대한 어떤 아이템의 Message는 두 임베딩의 element-wise product와 아이템의 임베딩에 가중치를 곱해 만들어진다.  
그 후 각 유저 혹은 아이템별로 연결된 노드들과의 Message를 모두 합해 activation 함수를 적용함으로써 새로운 임베딩을 만든다.  
이렇게 만들어진 임베딩들은 다음 레이어에서 다시 Message를 만드는데 활용되어 재귀적인 구조를 형성한다.  
총 l개의 레이어에 대해 만들어진 e_0, ... , e_u를 모두 concatenate하여 최종 임베딩 e*를 만들고, 유저의 e와 아이템의 e를 곱해 유저와 아이템간의 선호도를 예측한다.  

LightGCN은 NGCF를 단순화한 모델로, 한 노드에 연결된 노드들의 임베딩을 단순히 합한 후 scale을 조정하여 다음 레이어의 임베딩으로 활용한다.  
대신 각 layer의 임베딩을 concat.하지 않고 가중합을 함으로써 가까운 노드들을 더 크게 반영한다.  

RNN을 활용한 GRU4Rec 모델은 유저의 선호가 계속 변한다는 가정을 바탕으로, 이전 선호들을 통해 현재의 선호를 추측한다.  
본래 RNN에서 사용되던 GRU를 활용한 것이 특징이다.  

그 후에는 Context-aware Recommendation(CAR)에 대해 배웠다.  
기존에 배웠던 모델들은 대부분 유저-아이템 상호작용만을 활용했는데, CAR은 이에 더해 맥락적 정보를 추가로 고려하는 것이다.  
대표적으로는 Factorization Machine(FM)과 Field-aware Factorization Model(FFM)이 있다.  
FM은 하나의 선택에 대한 n개의 feature를 바탕으로, linear regression에 feature간의 상호작용을 더해준다.  
이때 n개의 feature는 각각 v라는 vector를 갖고, feature간의 상호작용은 두 v의 dot product를 가중치로 하여 더해진다.  
FFM은 여기서 여러 feature들을 하나의 field로 묶고, 각 feature별로 field들에 대한 상호작용을 v로 갖는다.  
따라서 하나의 feature는 f개의 field에 대해 총 f개의 v를 갖는다.  
대체로 FM과 FFM이 단순한 linear regression이나 모든 상호작용을 개별적으로 생각하는 polynomial model에 비해 성능이 좋다고 한다.  
다만 FM과 FFM의 우위는 데이터셋이나 FFM에서 field를 어떻게 정의하느냐에 따라 달라진다고 한다.  

그 외에 weak learner들을 결합하여 decision tree를 만드는 Gradient Boosting Machine(GBM)에 대해서도 배웠다.  
Boosting 대신 Bagging을 쓰는 random forest보다는 성능이 좋지만, 학습 속도가 느리고 과적합이 심하다는 단점이 있다.  
때문에 XGBoost, LightGBM, CatBoost 등의 대안 모델들이 제시되었다.  

강의를 모두 듣고 과제도 해결한 후 피어세션을 진행했다.  
강의를 들으면서 FFM의 모든 field를 하나의 feature로만 구성하면 사실상 polynomial model이 될까? 라는 궁금증이 생겨서 이에 대해 조원들과 의견을 나눴다.  
내 의문을 제시하는 과정에서 FM과 FFM에 대해 내가 이해한 방식으로 설명했는데, 다른 조원들의 FM과 FFM에 대한 이해에 도움이 된 듯했다.  
설명을 마치고 내 궁금증을 얘기하니 다들 내 생각에 동의해주었다. 슬랙의 질문게시판에도 질문을 올려뒀는데, 내일 조교님이 답변을 달아주시면 확실히 해결될 것 같다.  

>  오늘의 질문 횟수: 4  
>  오늘의 답변 횟수: 1  

+ ##### 키워드: NGCF, LightGCN, FM, FFM
