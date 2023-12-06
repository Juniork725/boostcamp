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

Day 22 (12/5)
---
오늘은 깃허브 특강 후반부가 진행되었다.  
지난주에 다뤘던 내용들을 복습하고, rebase, cherrypick, pull, push 등을 배웠다.  
예전에는 git으로 원격 저장소를 다룰 때 SourceTree를 썼는데, VS Code로 다루는 게 훨씬 편해서 갈아타기로 했다.  
특강 내용을 실습하며 따라갈 때 내 개인 repository와는 호환이 잘 되었는데, 강사님의 공유 repository에 접근하려니 자꾸 에러가 났다.  
아마 인증 관련해서 문제가 생긴 것 같은데, 특강이 끝나고 공유 repo가 사라져서 확인은 못 해 봤다.  
나중에 프로젝트가 시작되면 본격적으로 작업을 시작하기 전에 제대로 접근이 되는지 먼저 테스트해봐야겠다.  

특강을 마친 후에는 심화 과제를 살펴봤다. 가능하면 풀어보려고 했는데 슬랙 공지로 구인구팀 관련 공지가 날아와서 과제는 내일 마저 보기로 했다.  
슬랙 공지를 살펴보니 이제 Level 2부터 활동할 팀을 결성한다고 한다. 노션 페이지에 자기소개를 적어두고 슬랙이나 줌을 통해 팀을 만들어나가는 듯하다.  
나는 일단 현재 조원들과 같이 진행하기로 어느 정도 얘기가 되어 있어서 금요일에 조원들이 오프라인 행사를 다녀오면 마저 논의하고 결정해야겠다.  

>  오늘의 질문 횟수: 2  
>  오늘의 답변 횟수: 0  

+ ##### 키워드: Github, 구인구팀

Day 23 (12/6)
---
오늘은 CTR 예측을 위한 딥러닝 모델들과 Multi-Armed Bandit에 대해 배웠다.  
첫 모델은 Wide & Deep으로, memorization을 담당하는 Wide component와 generalization을 담당하는 Deep component를 결합하여 구성된다.  
이 때 wide와 deep component의 입력값이 다르고, wide component에서 feature engineering이 필요하다.  
이를 개선한 모델이 DeepFM 모델로, wide component를 FM으로 대체한 모델이다.  
FM component는 low-order interaction에 효과적이고, Deep component는 high-order interaction에 효과적이다.  

Deep Interest Network(DIN)는 user behavior feature를 처음 사용한 모델이다.  
기존 딥러닝 기반 모델들은 사용자의 다양한 관심사를 반영하기 어려웠다.  
반면 DIN은 유저가 기존에 소비한 아이템 리스트를 user behavior feature로 만들어 반영할 수 있다.  
Transformer의 attention과 유사한 Local Activation이라는 layer를 통해 소비한 아이템들과 후보 아이템간의 연관성을 계산하고, 이를 이용해 아이템 임베딩을 가중합한다.  

Behavior Sequence Transformer(BST)는 여기서 더 나아가 아이템 소비 이력을 sequential data로 간주해 순서까지 고려한다.  
DIN이 attention과 유사한 부분을 갖고 있다면, BST는 Transformer와 동일하게 multi-head self attention, add & norm, FFN 레이어를 모두 갖는다.  

Multi-Armed Bandit(MAB)은 각 아이템들을 하나의 슬롯 머신처럼 생각하고, 각 슬롯 머신마다 보상이 나올 확률이 정해져있다는 가정을 활용한다.  
이 때 어떤 슬롯 머신을 얼마나 많이 당겨야 보상을 최대화할 수 있는지에 대한 방법론이 MAB이다.  
가장 단순한 Greedy Algorithm, 랜덤성을 추가한 Epsilon-Greedy Algorithm, 기댓값에 신뢰도를 추가한 Upper Confidence Bound 등이 있다.  
좀 더 발전된 방법론으로는 베타 분포를 실시간으로 갱신해 활용하는 Thompson Sampling, 아이템을 선택할 때의 context vector를 활용하는 LinUCB 등이 있다.  

강의를 듣고 피어세션 때는 과제에 대해 질문 교환을 하고, 내일 스터디를 어떻게 할지 논의했다.  
한 주제로 스터디를 고정하기보다는 각자 공부하고 싶은 내용을 자유롭게 공부하고, 피어세션 때 간단히 공부한 내용을 설명하는 식으로 진행하게 됐다.  

피어세션 후에 멘토링 시간에는 CS 공부나 코테 준비는 어느 정도나 해야 할지, Front-end와 Back-end 능력은 얼마나 중요할지 등에 대해 들었다.  
CS는 네트워크 같은 분야보다는 자료구조 등 AI 개발과 관련된 분야를 위주로 공부하는 게 좋을 듯하고, FE나 BE 역시 상대적으로 AI 개발 능력에 비해 우선도가 낮은 듯하다.  
프로젝트 주제 선정에 대해서도 말씀하셨는데, 프로젝트 기획 의도가 무엇인지, 프로젝트를 진행할 때 데이터 처리나 모델 선정 등은 어떻게 할지 등을 고려해야 한다고 하셨다.  
특히 모델을 구현할 때 복잡하고 세련된 모델보다는 간단한 모델이라도 어떻게 서비스에 맞게 개량하는지가 더 중요하다.  
그리고 내가 생각했던 당뇨 환자 메뉴 추천 프로젝트도 코멘트를 간단히 받았는데, 데이터를 구하기가 어렵고 ML로 잘 해결할 수 있는 문제가 아닐 것 같다고 부정적인 의견을 주셨다.  
주제에 대해서는 좀 더 고민을 해 봐야 할 듯하다.  

>  오늘의 질문 횟수: 3  
>  오늘의 답변 횟수: 3  

+ ##### 키워드: Wide & Deep, DeepFM, DIN, BST, MAB
