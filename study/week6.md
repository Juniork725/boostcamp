Week 6 (12/11 ~ 12/15)
===
>  ##### 주간 요약
>  Book recommendation 프로젝트 대회가 시작되었다.  
>  Github를 통해 협업하는 법을 배우고, 프로젝트에 적용하였다.  
>  Level 2부터 프로젝트를 함께 할 팀을 결성했다.  
>  컨디션 관리를 제대로 못 했다.  

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

Day 28 (12/13)
---
어제의 여파가 남아서인지 조금 힘든 하루였다.  
강의 내용은 이미지, 텍스트 등의 데이터를 활용하는 Multimodal과 여러 대회들의 winner solution이었다.  
이미지는 pre-trained resnet을 가져와 마지막 classification 직전의 AvgPool 레이어에 hook을 등록해 이미지 latent vector를 활용하는 실습 코드를 통해 다뤘다.  
텍스트는 DeepCoNN이라는 모델을 변형해 user와 item의 text 정보를 각각 latent vector로 변환 후 FM으로 처리했다.  
이번 프로젝트에도 표지 이미지와 요약 설명 텍스트가 있는데, 활용을 고려해볼 필요가 있겠다.  
다만 이미지 데이터의 해상도가 너무 낮아서 유의미한 학습이 될지 좀 의심스럽긴 하다.  

프로젝트 주간의 강의는 다 들었기에 이제 다음주까지 프로젝트에만 집중하면 되는 상황이다.  
오늘부터 서버와 리더보드가 열렸는데, 피어세션 때 다같이 서버에 접속해보자는 의견이 있었다.  
그래서 사전에 안내받은대로 서버 접속을 시도했는데, 관리자 권한이나 파일 경로 인식 문제 등등으로 1시간 반 넘게 헤맸다.  
그나마 조원분들도 도와주시고, 슬랙에서 여러 이슈들에 대한 대응법을 공유해주신 분이 계셔서 일찍 해결한 편이다.  
ssh나 vpn 같은 것들을 다뤄 본 적이 없다보니 아무래도 이런 부분에서 경험치 차이가 좀 나는 것 같다.  
차라리 이론 공부를 할 때는 마음이 편했는데 낯선 분야에서 이슈 대응을 하려니 꽤나 힘들었다.  

어찌저찌 서버 문제를 해결한 후에는 마스터클래스가 있었다.  
현직자시다보니 추천 시스템의 취업 시장에 대해 직접적으로 많이 말씀해주셨다.  
아무래도 비전공자는 전공자에 비해 취업 과정에서 넘어야 할 선입견의 벽이 있는 편이고, 다양한 경험이나 포트폴리오를 통해 극복해야한다고 하셨다.  
그리고 추천 시스템 자체가 등용문이 좁은 편이라 제2의 선택지에 대해서도 시야를 열어둬야한다고 하셨다.  
현업 실무자와 컨택해서 커피챗 등을 하며 관심 있는 산업 분야의 업무 분위기 등에 대해서 알아두는 것도 취준할 때 방향성을 잡는 데 도움이 된다고 하셨다.  

서버 이슈로 피어세션 시간을 혼자 다 잡아먹고, 마스터클래스 때 추천 시스템 분야에서 취업이 어렵다는 얘기까지 듣다보니 자신감이 좀 깎여나간 듯한 하루였다.  
몸 컨디션도 조금 안 좋아서 식사도 대충 해 먹게 되고, 악순환에 빠지고 있는 느낌이 든다.  
좀 더 일상생활에 신경 쓰면서 멘탈 관리를 해야겠다. 어떻게 보면 스트레스 대응법을 익히는 과정일 수도 있다고 생각한다.  
이것저것 시도해보면서 나한테 맞는 방법을 찾아야겠다.  

>  오늘의 질문 횟수: 0
>  오늘의 답변 횟수: 0

+ ##### 키워드: Multimodal, 취업, 멘탈 관리

Day 29 (12/14)
---
오늘은 베이스라인 코드를 읽고 EDA를 진행했다.  
구조가 복잡하지 않아서 코드는 간단하게 파악했고, ratings 데이터를 보며 user의 평가 수 분포를 위주로 EDA를 했다.  
확인해보니 책 1권에 대한 평가만을 남긴 user가 압도적으로 많았고, 우리가 예측해야 하는 test 데이터에서도 5개 이하의 평가를 남긴 유저들에 대한 예측이 30% 정도를 차지했다.  
이런 정보들을 pyplot을 이용해 그래프로 남겨두고, 피어세션 때 보여주며 인사이트를 공유했다.  
다른 분들의 EDA 결과도 들었는데, 데이터의 결측치 분포가 어떠한지와 user별로 선호하는 장르가 명확한 편이라는 내용을 들었다.  

피어세션 후 멘토링 때는 대회 관련 여러 팁들을 들었다.  
EDA에 너무 집중하기보다는, 모델을 여러 방향으로 실험해보고 그 결과를 바탕으로 데이터를 분석하는 게 효율적이라고 하셨다.  
그리고 모델들을 실험할 때 seed를 고정하는 것이 중요하고, 소규모 데이터로 실험하면 빠르게 결과를 얻어 비교하기 좋다는 팁도 주셨다.  

내일부터는 각자 모델을 다루면서 커스텀 할 예정인데, 요즘 몸 컨디션이 조금 안 좋아서 걱정이다.  
내일만 지나면 주말이니 마저 힘내고, 주말에는 푹 쉬면서 회복에 집중해야겠다.  

그리고 오늘 level 2부터 프로젝트를 함께 할 팀을 완성했다.  
처음 계획처럼 level 1 팀을 유지하지는 못했지만, 같이 팀을 이뤄보고 싶었던 분들과 팀이 성사돼서 다행이다.  

>  오늘의 질문 횟수: 1  
>  오늘의 답변 횟수: 0  

+ ##### 키워드: EDA, 팀 결성

Day 30 (12/15)
---
깃허브 공용 repo를 다듬고, 베이스라인 코드를 수정해 공유했다.  
특강 때 github에 대해 배운 걸 바탕으로, issue 생성 - PR - merge의 흐름을 갖추도록 협업 방침을 정했다.  
프로젝트 협업은 처음이라 생소한 게 많은데, 그래도 무난히 적응해서 github 활용에 익숙해지고 있다.  

그리고 베이스라인 코드에서 users와 books 데이터에 대해 전처리가 부족한 부분이 있어 코드를 작성 후 pull 해서 공유했다.  
전처리 방식을 바꿔서 모델을 학습시켰더니 조금이지만 결과가 개선되길래 해당 결과를 리더보드에 업로드 하고 오늘 작업을 마무리했다.  

피어세션 때는 내가 추가한 코드에 대해 설명하고, merge 승인을 받으면서 조금이나마 '이런 게 협업 흐름이구나' 하는 느낌을 받았다.  
그리고 필요한 기능이나 실험해볼만한 조건 등을 issue로 등록해두고 하나씩 처리하면서 관리하기로 했다.  

컨디션 이슈로 오늘은 힘을 좀 빼고 작업했는데, 그래도 결과물은 나쁘지 않아서 1인분 역할은 충분히 한 것 같다.  
아직 구현할 코드가 좀 남아있긴 한데, 나머지 작업은 다음주에 마저 이어서 하면 될 것 같다.  

그리고 이제 이론 강의는 거의 끝나고 프로젝트 위주로 진행될 예정이라, 질문과 답변이 딱히 없는 상황이다.  
피어세션 때 프로젝트에 대해 의견 교환은 많이 하는데, 의견들을 다 질문이나 답변으로 간주하고 세는 건 괜히 회의에 집중하는데 방해만 될 것 같아서 안 하고 있다.  
원래 질문, 답변 횟수를 세던 게 내가 얼마나 적극적으로 소통하면서 공부하는지 객관적으로 보려던 목적이었는데, 지금은 의미가 퇴색됐으니 다음주부터는 회고 양식에서 빼야겠다.  

>  오늘의 질문 횟수: 0  
>  오늘의 답변 횟수: 0

+ ##### 키워드: Github 이슈 관리, 데이터 전처리
