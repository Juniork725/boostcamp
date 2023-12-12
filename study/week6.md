Week 6 (12/11 ~ 12/15)
===
>  ##### 주간 요약
>  

Day 26 (12/11)
---
본격적으로 팀 프로젝트가 시작되는 주간이다.  
이번 프로젝트 주제는 book recommendation으로, 유저/책/평가 데이터를 이용해 test data의 평가를 예측하는 대회다.  

아침에는 부스트캠프에서 프로젝트가 어떤 식으로 진행되는지, 대회 플랫폼은 어떻게 활용하는지 등을 안내받았다.  
대회에서의 등수보다는 여러가지 실험을 해 보며 결과에 대해 분석하는 등 그 과정을 더 중요시하라는 말씀을 하셨다.  

안내 후에 바로 조원들과 모여 스크럼을 진행했다.  
우선 프로젝트의 목표부터 설정했는데, 나는 결과보단 과정을 중요시해야 한다는 입장이라 여러 방식으로 결과를 내고 이를 분석하는 걸 위주로 진행하자고 제안했다.  
대부분 동의하는 흐름이었고, 그래도 결과에 좀 욕심이 난다는 의견도 있어서 전체 2등 이내를 목표로 잡았다.  
조장도 정하자고 제안했고, 팀 프로젝트 경험이 있으신 조원분께서 조장을 맡아주시기로 했다.  

프로젝트를 시작하기 전에 수강을 권장하는 강의들이 있어서 우선 강의를 먼저 듣기로 했다.  
지난 RecSys 이론 때 배웠던 주요 모델들을 다시 복습하고, 이미지나 텍스트 데이터의 활용, 다른 대회들의 답안 사례 등을 다루는 듯하다.  
오늘은 Metrics, UBCF, IBCF, MF, ALS, GBDT 등에 대해 다뤘다.  
분명히 아이디어는 다 이해하고 있는 모델들인데, 구현된 코드를 읽으려니 모델에 맞게 data frame을 가공하는 과정이 익숙치 않아 좀 오래 걸렸다.  

강의를 듣고 피어세션 때 얘기를 나눠보니 다들 진도 나가는 속도가 비슷한 수준이었고, 수요일 정도면 얼추 다 들을 수 있겠다 싶었다.  
그래서 수요일까지는 우선 강의에 집중하고, 목요일부터는 프로젝트를 위주로 다루기로 했다.  
아마 목요일에는 데이터와 베이스 코드 분석을 하고, 금요일부터 각자 모델을 구현해 본 후 성능이 좋은 쪽으로 집중해 발전시켜나갈 듯하다.  

피어세션 후에 이번 대회 데이터에 대한 EDA 예시 코드를 읽어보면서 대략적으로 데이터 구성을 이해했다.  
코드를 따라 분석해나가다 보니 몇 가지 전처리 아이디어가 떠올랐는데, 나중에 모델 구현 때 테스트해봐야겠다.  

>  오늘의 질문 횟수: 1  
>  오늘의 답변 횟수: 0  

+ ##### 키워드: Book Recommendation Project

Day 27 (12/12)
---
캠프 시작한 후로 가장 시간이 모자랐던 날이다.  
어제에 이어서 FM, FFM, NCF, WDN 등의 모델을 복습하고, DCN이라는 모델도 추가로 다뤘다.  
이런 여러 모델들에 대한 성능을 측정해서 비교하고, 여러 hybrid approach를 통해 성능을 개선하는 과정을 배웠다.  
이때 각 모델들을 밑바닥부터 구현하는 것은 비효율적이기 때문에, 라이브러리를 활용해 모델을 테스트한 후 최적화하는 게 적절하다.  

위 내용들을 구현한 실습 코드를 읽으면서 공부했는데, 각 모델들의 코드를 한줄한줄 읽으며 이해하는 게 시간이 오래 걸리고 진이 빠졌다.  
그래도 코드들을 읽으면서 프로젝트에 활용할만한 아이디어들이 또 몇 개 떠올라서 피어세션 때 조원들과 공유했다.  

피어세션 후에는 캠퍼들이 관심 주제별로 모여서 의견을 교환하는 온라인 행사가 있었다.  
관심 주제로는 Data analysis, MLOps 등의 개발 분야와 게임, 음악 등의 도메인 주제가 있었다.  
나는 MLOps와 게임을 관심 주제로 선택했는데, MLOps에 관심이 있다기보다는 이번 부스트캠프에서 주로 다루게 될 부분이 MLOps일 것 같아서 선택했다.  
MLOps라는 용어 자체가 생소해서 찾아보니 데이터 수집, 분석부터 모델의 학습, 배포까지 모든 단계를 관리하는 방법론인 듯하다.  
그런데 막상 MLOps를 주제로 하는 팀에 들어가 이야기를 나눌 때, MLOps에 대한 얘기는 거의 하지 못하고 각자 자기소개만 하다보니 시간이 다 갔다.  
게임을 주제로 모인 팀에서도 생각보다 주제에 대해서는 크게 얘기를 나누지 않았던 것 같다.  
모두 합쳐서 2시간 정도 진행된 행사였는데, 마치고 나니 시간이 좀 아깝다는 느낌이 들어서 아쉬웠다.  

행사 후에는 깃허브를 활용한 협업을 주제로 특강이 있었다.  
이번 특강은 branch 관리 전략, issue와 pull request, 코드 리뷰를 활용한 개발 과정 등에 대해 다뤘다.  
깃허브로 협업을 해 본 적이 없어서 issue나 pull request 등의 기능은 별로 써 본 적이 없었는데, 활용 예시를 보니 꼭 익혀둬야겠다는 생각이 들었다.  
이번 프로젝트 repo에서도 pre-commit config를 설정하고, 이슈 템플릿과 PR 템플릿을 만드는 것부터 시작해야겠다.  
템플릿을 만들면서 branch 이름이나 commit head 등에 대한 컨벤션도 정해야겠다.  
그 후의 진행 흐름은 issue를 제시하고, 이에 맞춰 branch를 분기해 작업한 후, commit tail에 issue 번호를 달고, pull request를 작성하는 식으로 진행되는 듯하다.  
pull request에 close 등의 tag를 달아 issue를 자동으로 닫는 등 자잘한 팁 같은 것들도 많이 알려주셨는데, 조원들과 작업하면서 차차 익숙해져야겠다.  

특강 후에 오늘 목표로 했던 강의 진도가 조금 남아서 강의를 마저 들었다.  
Kakao ARENA 대회 사례를 통해 대회에 대한 접근 방식을 배웠다.  
기본적으로 추천 시스템은 도메인에 대한 경험과 지식이 중요하고, 데이터가 기업 보안 등으로 인해 구하기 어렵기에 대회 경험이 중요하다고 한다.  
대회에서 중요한 포인트는 주로 3가지가 있는데, Task와 Data에 대한 이해 / Domain에 대한 이해 / Metrics에 대한 이해 로 나뉜다.  
각각의 이해를 바탕으로 어떻게 데이터를 가공하고 모델들을 만들어야 하는지 고려하는 것이다.  
그리고 단일 모델로는 충분한 성능을 내기 어렵기 때문에 여러 모델들을 만들어 적절하게 hybrid 하는 것이 필요하다고 한다.  

>  오늘의 질문 횟수: 0  
>  오늘의 답변 횟수: 0  

+ ##### 키워드: DCN, GitHub 협업 전략, 대회 전략, Hybrid approach