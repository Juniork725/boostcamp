Week 19 (03/11 ~ 03/15)
===
>  ##### 주간 요약
>  Prototype을 완성하고 멘토님께 피드백을 받았다.  
>  서비스 품질 향상을 위해 모델 개량 및 데이터 정제를 진행 중이다.

Day 84 (03/11)
---
EASE 모델에서 두 유저에 대한 추천 방식을 바꿔가며 테스트 해 보고, Prototype 최종 버전에 맞춰 코드를 수정했다.  
코드 수정은 사용하는 데이터 크기가 커짐에 따라 프로그램 실행 속도가 느려져서 train과 inference를 분리하고, 새로운 return format 요구에 대응하는 것으로 완료했다.  
내일 멘토링 시간에 prototype 피드백을 받을 때까진 모델과 관련한 수정은 없을 예정이다.  

유저에 대한 추천 방식을 바꾸고, hyper parameter를 조정하는 등 몇 가지 변화를 줘 봤는데, 1~5위의 추천 결과는 크게 달라지지 않았다.  
그래서 추천 결과 자체보다는 사용자에게 추천 결과를 좀 더 합리적으로 설명할 수 있는 방식을 고려해 변경했다.  

내일 prototype 피드백이 끝나면 본격적으로 최종 서비스 개발에 돌입할 계획이라, 슬슬 전반전에서 후반전으로 넘어가고 있다는 느낌이 든다.  

+ ##### 키워드: EASE 모델 코드 수정, 추천 방식 변경

Day 85 (03/12)
---
Prototype을 완성하고, 멘토님께 피드백을 받았다.  
모델은 어제와 크게 바뀌지 않았고, streamlit 구현을 담당하신 분이 로고 제작, 그래프 표시 등 마무리 작업을 열심히 해 주셔서 최종 제출본이라고 봐도 손색이 없을 정도로 깔끔하게 완성됐다.  
멘토님께서도 깔끔하게 만들어졌다고 긍정적으로 피드백을 주셨고, 멘토님 steam id를 넣어서 확인해보니 실제로 플레이했던 게임들이 많이 추천된다고 하셨다.  
그리고 모델의 추천 결과가 적절한지 분석하기 위해 임의로 몇몇 유저들을 골라 결과를 확인한 뒤 각 유저의 플레이 이력과 비교해 정성적인 평가를 진행해보라고 하셨다.  

모델 개선을 위해 hyper parameter인 lambda 수정, playtime의 절대값 대신 평균 playtime과의 상대값 사용 등의 방법을 고려 중이다.  
우선 방법들을 적용한 후 내 정보를 넣어 테스트 해 보고, 제일 괜찮다고 판단되는 모델을 기준으로 추후에 정성적인 평가를 진행해보려 한다.  

+ ##### 키워드: Prototype 완성, 피드백

Day 86 (03/13)
---
모델 수정 및 실험을 시작했다.  
우선 게임별로 평균 playtime이라는 feature를 만들어 데이터를 분석해봤는데, 그 값이 0인 게임들이 1/6 정도 존재했다.  
즉, 게임을 사서 library에 저장한 사람은 있지만, 실제로 플레이 한 유저는 한 명도 없는 게임들이다.  
어떤 게임들인지 궁금해서 확인해봤는데, 아직 미출시 된 게임이지만 게임사 직원이 갖고 있는 경우이거나, 게임의 퀄리티가 떨어져서 유저들이 기피하는 게임들이 많았다.  
그리고 각 게임을 보유한 유저의 수가 1~2명 정도로 적어서 전체 interaction data에서 이 게임들이 차지하는 비율이 굉장히 적었다.  
그래서 EASE 모델의 학습에도 크게 도움이 되지 않고, pivot table을 불필요하게 키우는 요인이라 판단되어 data에서 배제했다.  
지금은 모델 학습 전에 EDA를 하고 직접 데이터를 배제하는 중이지만, 추후에 데이터를 담당하는 조원분께서 학습에 사용할 데이터를 따로 선별해내는 DB 정제 작업을 진행해주실 예정이다.  

lambda 값도 수정해서 실험을 해 봤는데, lambda 값이 줄어드니 이전보다 개인화 된 추천이 이루어지는 느낌을 받았다.  
lambda 값이 곧 regularization term을 의미하기에, 이전보다 데이터 패턴을 더 유연하게 학습해서 개인화가 된 것이라고 해석할 수 있겠다.  
다만, 아직 DB 정제가 덜 된 데이터를 기준으로 학습한 결과이기에 실험 결과는 대략적인 양상을 파악하는 정도로만 활용하고, 이후에 DB 정제가 완료되면 본격적으로 실험을 진행할 계획이다.  

+ ##### 키워드: 모델 수정 계획 수립 및 실험

Day 87 (03/14)
---
오늘은 작업 내용은 딱히 없었고, 데이터 정제 작업을 기다리면서 시간을 보냈다.  
회의 때 데이터를 어떻게 필터링 할 것인가, 추천 결과 화면을 어떻게 제시할 것인가, cold start 유저에 어떻게 대응할 것인가 등에 대해 논의한 것 정도가 주요 일과였다.  

회의를 모두 마친 후에 다른 조들의 프로젝트 발표를 들었는데, 3개 조의 발표만 듣긴 했지만 다들 아직 서비스 구현 과정에 머물러 있는 느낌이었다.  
우리 조는 일단 prototype이 완성되었고, 여기에 기능을 추가하거나 보완하면서 발전시켜 나가는 단계라 비교적 빨리 구현이 된 것 같다.  
조원분들의 작업 속도가 빠른 덕분도 있지만, 모델링을 굉장히 간소화 했고, 기획 단계에서부터 서비스를 상세히 구상하고 최대한 프로젝트 규모를 줄인 영향도 있다.  
프로젝트 초반에 같은 주제로 서비스를 구상했음에도 각자가 생각하는 서비스 형태가 다 달랐는데, 이걸 빠르게 취합하고 단일화 한 것이 도움이 많이 되었다.  

+ ##### 키워드: 서비스 기획, 프로젝트 경량화

Day 88 (03/15)
---
DB 정제가 어느 정도 되어서 본격적으로 실험을 시작했다.  
하이퍼 파라미터 튜닝, z score를 이용해 playtime에 상대성 부여, 데이터 전처리 방식 변경 등 여러 방식을 적용해보고 추천 결과를 비교했다.  
하지만 아무래도 정성적 평가에 그치다보니 내가 개인적으로 더 선호하는 추천 결과는 있어도 모델 성능의 우위를 객관적으로 판단하기는 어려웠다.  
그리고 두 모델의 추천 결과가 서로 다른 부분에서 마음에 드는 경우도 있었다.  
그래서 여러 조건의 모델 결과를 앙상블로 합쳐보는 것도 시도해 볼만 할 것 같다.  
inference time이 늘어나는 문제가 있을 것 같지만, 일단 다음주에 테스트 해 보고 판단해야겠다.  

+ ##### 키워드: 모델 튜닝, 앙상블 계획