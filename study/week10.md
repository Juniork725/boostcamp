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

Day 44 (01/09)
---
오늘은 Graph 기반 모델에 대한 강의를 끝으로 이번 대회에 관련된 강의를 모두 수강했다.  
Graph 구조 학습의 목표는 크게 3가지인데, Node classification, Graph classification, Link prediction으로 나뉜다.  
이번 DKT 대회에 적용하자면 사용자와 문제들을 node로 간주하고, 문제를 맞혔다면 link가 있는 것으로 하여 link prediction 문제로 볼 수 있다.  
이 때 활용할 수 있는 모델로는 이전에 배웠던 GCN이나 이를 발전시킨 GAT 등이 있다.  
GCN이 주변 node들의 embedding을 message로 만들어 합하는 방식이라면, GAT는 두 node의 embedding을 하나의 가중치로 변환 후, 주변 node들의 embedding에 대해 가중합을 하는 방식이다.  
두 embedding으로 가중치를 만드는 것이 attention 방식과 유사하다.  
GCN이나 GAT와 같은 모델들은 layer를 쌓을수록 receptive field가 넓어지는 효과가 생기는데, 이게 지나치면 over-smoothing 현상이 발생한다.  
이는 각 node들이 너무 넓은 영역의 정보들을 모아 서로 비슷해지는 현상을 말한다.  
Over-smoothing을 방지하기 위해서는 node dropout, edge dropout, layer-wise edge dropout 등의 방법을 활용할 수 있다.  

그러나 graph 기반 모델은 이번 DKT 대회처럼 시계열 데이터의 특성을 반영하지 못한다.  
때문에 다른 시계열 모델에 비해 성능이 떨어지는데, 이를 만회하는 아이디어가 있다.  
Graph 기반 모델로 각 사용자와 문제들에 대한 embedding을 학습한 후, 이를 transformer 등의 시계열 모델에 사용하는 것이다.  
원래는 사용자와 문제에 대한 embedding이 랜덤한 값에서 시작해 학습되는데, 이를 graph 모델로 학습해서 사용하기 때문에 pre-trained model을 사용하는 것과 비슷한 효과가 생긴다.  
굳이 graph 기반 모델이 아니더라도, MF로 학습하거나 FM으로 다른 feature들에 대한 embedding까지 학습하는 식으로 변형하는 것도 가능할 것 같다.  

피어세션 때는 git branch가 잘 관리되고 있는지 점검하고 잘못된 부분을 수정했다.  
잘못 생성된 branch를 내가 [git push origin -d "BRANCH_NAME"] 명령어로 삭제했는데, 다른 팀원들의 git graph에는 여전히 예전 branch가 남아있는 문제가 생겼다.  
분명 github에서 확인해도 branch가 없는데, 다른 분들이 pull을 해도 여전히 예전 branch가 남아있었다.  
이것저것 시도해보다가 [git fetch -p]와 같은 명령어로 해결했다. 찾아보니 --prune 이라는 옵션을 통해 원격 저장소에 없는 branch를 지워주는 명령어였다.  
그 외에 가상환경에서 gpu가 인식이 되지 않는 문제를 발견하고, 이것이 torch 버전과 cuda 버전이 호환되지 않아 생기는 문제임을 알게 되어 torch 버전을 낮춰 해결하기도 했다.  

아직 프로젝트 초반이라 작업 환경이나 협업 과정에서 여러 문제가 생기고 있는데, 그래도 하나씩 잘 해결하며 전진 중이다.  

+ ##### 키워드: GAT, Over-smoothing

Day 45 (01/10)
---
본격적인 modeling에 앞서 몇 가지 EDA를 진행하고, validation 방법을 변경하는 코드를 짰다.  
데이터의 sparsity가 97% 정도로 나와, MF와 같은 collaborative filtering을 적용해볼만 하다고 생각했다.  
그리고 한 유저당 푼 문제 수는 어느 정도인지, 한 문제당 푼 유저 수는 어느 정도인지 등도 확인했다.  
유저 기준으로는 cold start 문제가 크게 없을 듯한데, test_data.csv에서 푼 유저 수가 1명인 문제들이 있었다.  
때문에 MF를 적용한다면, train_data.csv와 test_data.csv를 모두 합친 후 train과 valid dataset을 나누는 게 좋을 듯하다.  

그리고 EDA를 ipynb 파일로 진행하고, 해당 코드를 github로 공유하면 좋지 않을까 싶어서 피어세션 때 제안해봤다.  
하지만 EDA를 할 때마다 branch를 파고, PR을 하는 것이 너무 번거롭다는 의견이 나와서 구글 공용 드라이브를 활용하기로 했다.  
깃허브에 기록이 안 남는 게 조금 아쉽긴 한데, 번거롭다는 의견도 충분히 이해가 가서 의견을 따르기로 했다.  

오늘로 프로젝트가 시작된지 1주일이 지났는데, 현재로서는 모델링보다 github 활용법이나 EDA 공유 방법 등 작업 환경을 가다듬는 것에 집중 중이다.  

+ ##### 키워드: EDA, Validation, 협업 컨벤션

Day 46 (01/11)
---
몸 컨디션이 많이 나빠져서 낮에 병결 신청을 하고 병원에 다녀왔다.  
병원 다녀온 후에도 프로젝트 작업은 거의 못 해서 오늘은 피어세션과 멘토링 정도만 소화했다.  

피어세션 때 어제 만들었던 새로운 validation에 대한 의견을 나눴는데, validation score와 LB score가 오히려 더 벌어져서 이를 개선하기 위해 수정 방안을 모색했다.  
멘토링 때도 의견을 받았는데, 아마 validation dataset의 크기가 작아져서 데이터의 다양성이 줄어든 게 LB와 차이가 나는 원인일 것 같다.  

그리고 멘토링 때 LASSO와 RIDGE에 대해 질문했는데, 둘 다 regularization을 위해 weights의 크기를 줄여주는 역할이지만, LASSO의 경우 미분 불가능한 지점이 생기는 문제가 있어 RIDGE를 주로 쓴다고 한다.  
또 feature selection을 할 때 sklearn의 RFE라는 기능을 쓸 수 있는데, 각 feature들의 importance를 측정하고 값이 낮은 것들을 재귀적으로 제거하는 기능인 듯하다.  
대신 이 기능을 쓸 때 다중공선성 문제에 대한 고려는 빠져있기에 주의할 필요가 있다고 하셨다.  
다중공선성 문제란 회귀분석에서 두 독립변수가 강한 상관관계를 갖는 문제를 뜻한다. 이 경우 각 변수들이 독립이라는 가정을 위배하고, 모델의 성능에도 악영향을 끼친다고 한다.  
이 문제를 해결하기 위해서는 statsmodels라는 library를 활용할 수 있다.  
해당 library를 통해 변수들의 VIF(Variance Inflation Factor)를 계산할 수 있고, 공분산 행렬의 조건 수(conditional number)라는 것을 확인할 수 있다.  
VIF가 크다는 것은 다른 변수들에 의존적이라는 것을 의미하고, 조건 수가 크다는 것은 다중공선성이 존재함을 의미한다.  
처음 보는 내용이라 아직 다 이해하지는 못했는데, 잘 정리된 글이 있어 나중에 이걸 참고하면 좋을 것 같다. [(링크)](https://datascienceschool.net/03%20machine%20learning/06.04%20%EB%8B%A4%EC%A4%91%EA%B3%B5%EC%84%A0%EC%84%B1%EA%B3%BC%20%EB%B3%80%EC%88%98%20%EC%84%A0%ED%83%9D.html)  
그 외에 feature engineering이나 modeling에 대한 코멘트, github 활용에 대한 코멘트를 받았다.  
github는 충분히 잘 활용하고 있다고 평가해주셨고, 추가적으로 branch를 나눌 때 issue 단위가 아니라 주제 단위로 나누면 더 좋을 것 같다고 하셨다.  
이번 프로젝트에서 제일 신경 쓴 부분이 github 활용이었는데, 좋은 평가를 받아서 뿌듯했다.  

+ ##### 키워드: 병결, RFE, 다중공선성, statsmodel, VIF, 조건 수
