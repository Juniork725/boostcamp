Week 10 (01/08 ~ 01/12)
===
>  ##### 주간 요약
>  

Day 43 (01/08)
---
오늘은 transformer의 tuning과 ML pipeline의 전체적인 흐름에 대해 배웠다.  
Hyperparameter tuning은 이전 프로젝트에서도 했던 과정이라 대부분 복습 같은 느낌이었다.  
기억에 남는 부분은 batch size와 lr에 대한 내용인데, 둘은 보통 tuning 과정에서 양의 상관관계를 갖는다.  
예를 들어 batch size가 커지면 그만큼 weight update 횟수가 줄어들기 때문에 lr도 키워줘야 하고, 반대의 경우도 마찬가지다.  
지난 프로젝트 때 hyperparameter tuning을 하면서 공부했던 내용이라 금방 이해가 됐다.  
여기에 추가로, batch size가 크면 sharp minima에 빠지기 쉽다고 한다. 때문에 generalization이 잘 되지 않아 CV와 LB score의 차이가 쉽게 벌어진다.  
또한 Bert와 같은 pretrained model을 사용할 때는 lr에 주의를 기울여야한다.  
lr이 너무 크면 기존에 학습했던 가중치를 많이 까먹기 때문에 성능이 나빠진다고 한다.  

앙상블 기법의 하나로 OOF Stacking이라는 것도 배웠다.  
K-Fold 기법을 사용할 때, 각 fold별로 validation data에 대한 예측을 모으면 전체 train data에 대한 예측을 만들 수 있다. 이를 Out Of Fold(OOF)라 한다.  
"이미 정답을 알고 있는 train data에 대해 예측이 왜 필요하지?" 라는 의문이 생길 수 있는데, 이 예측을 바탕으로 실제 정답을 예측하는 meta model을 학습하기 위함이다.  
모델 A, B, C로 각각 OOF 예측을 하고, 이들을 concat.한 행렬을 입력으로 받아 train data의 정답을 예측하는 meta model을 학습시킨다. 이를 OOF Stacking이라 한다.  
meta model을 학습시킨 후, test data에 대한 A, B, C의 예측을 모아 meta model에 넣어주면 최종적으로 정답에 대한 예측을 반환해준다.  
강의에서 소개된 것은 OOF Stacking 이었지만, 여러 모델의 예측값을 stacking 하여 meta model로 학습시키는 아이디어는 OOF가 아니라도 활용할 수 있을 것 같다.  

강의를 듣고 피어세션까지 시간이 조금 남아서 github 활용 준비를 했다.  
branch 전략과 commit 컨벤션을 정하고, 이에 맞춰 이슈 템플릿과 PR 템플릿을 생성했다.  
피어세션 시간에 컨벤션 및 템플릿 양식 등을 공유해서 컨펌을 받고, 이슈 등록부터 PR까지 작업 흐름을 화면 공유를 하며 보여줬다.  
지난 프로젝트에선 다들 github 활용이 미숙하다보니 branch가 많이 꼬이고, 어느 순간부터 각자 로컬에서만 작업을 하게 됐다.  
이를 교훈 삼아 이번 프로젝트에서는 본격적으로 프로젝트 작업을 하기 전에 협업 흐름을 먼저 신경 쓰고자 한다.  

+ ##### 키워드: Batch size, Learning rate, OOF Stacking, Github 활용
