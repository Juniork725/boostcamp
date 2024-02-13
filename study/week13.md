Week 13 (01/29 ~ 02/02)
===
>  ##### 주간 요약
>  Movie Recommendation 대회가 시작되었다.  
>  Word2Vec을 기반으로 한 추천과 임베딩 시각화를 시도했다.  
>  파이프라인을 구축하고 MF를 구현해보기로 했다.  

Day 58 (01/29)
---
새로운 프로젝트인 Movie Recommendation 대회가 시작되었다.  
이번 대회는 결과에 상관없이 솔루션 발표를 해 보기로 해서 프로젝트가 시작되자마자 발표 자원을 했다.  
좋은 결과를 내면 더 좋겠지만, 그렇지 않아도 다양한 시도들을 소개할 수 있도록 많은 걸 도전해 볼 생각이다.  

이번에도 본격적인 프로젝트 시작에 앞서 수강해야 할 강의들이 있었다.  
오늘 들은 내용은 MF, Wide & Deep, BPR 등 전에 배웠던 모델들의 복습과 FPMC, PRME 등 새로운 모델을 배웠다.  
FPMC는 MF에 markov chain rule을 더한 방식이다.  
단순히 유저 u의 아이템 i에 대한 선호도를 구하는 것이 아니라, 아이템 j를 선택한 후 i를 선호할 확률을 구하는 것이다.  
따라서 f(u,i)를 예측하는 MF와 달리 f(i|u,j)를 구하는 것이 목표이다.  
positive item에 대한 값과 negative item에 대한 값의 차이를 구하고, 이 차이가 커지도록 학습한다.  

PRME는 유저 u의 아이템 i에 대한 선호도를 내적 대신 유클리드 거리로 나타내는 방식이다.  
기존 MF 계열 방식에서는 r_u와 r_i를 내적해서 선호도를 예측하는데, PRME는 두 벡터의 L2-norm에 음수를 취한 값을 선호도로 예측한다.  
이 값이 0에 가까울수록 유저가 선호하는 아이템이라 판단하고 추천하는 것이다.  
기존 방식과의 차이는 어떤 대상이 추천되느냐에 있다.  
내적을 통한 방식은 특정 유저가 선호하는 아이템 벡터와 비슷한 각도의 벡터를 갖는 아이템들이 추천된다.  
즉, 공포 영화를 좋아하는 유저라면 다른 장르를 추천하기보다는 공포 영화의 성격이 짙은 영화들만 추천하는 것이다.  
반면 거리를 이용한 PRME는 유저가 선호하는 수준의 공포도를 갖는 범위 내에서 비슷한 장르들의 영화를 추천한다고 할 수 있겠다.  

그리고 user-free 모델에 대해서도 배웠는데, 이러한 모델은 cold start user에 대해 대응이 가능하다는 장점이 있다.  
기본 아이디어는 유저가 사용한 아이템들을 원핫 인코딩으로 나타내고, 이에 대한 가중치 벡터 W를 곱해 특정 아이템에 대한 선호도를 예측한다.  
기본적으로 memory based 방식과 유사한 점이 있지만, 가중치 행렬의 파라미터를 학습할 수 있다는 점에서 차별된다.  

강의를 들은 후에는 피어세션을 하며 이번 프로젝트를 어떻게 진행할지에 대한 전반적인 논의를 했다.  
깃허브 컨벤션, 노션을 통한 일정 관리, 회의록 관리 등 세세한 부분들에 대해 모두 얘기를 나눴다.  
확실히 한 번 프로젝트를 같이 진행하고 나니 어떤 걸 정리해야 할지 감이 잡혀서 지난 프로젝트에 비해 훨씬 작업 방침이 깔끔하게 정해진 기분이다.  

+ ##### 키워드: Movie Recommendation 대회 시작, FPMC, PRME, user-free 모델, 프로젝트 방침 설정

Day 59 (01/30)
---
대회 강의를 추가로 듣고, 프로젝트 협업 컨벤션에 대한 논의, 최종 프로젝트 특강, 멘토링을 진행했다.  
특히 멘토링을 7시부터 진행하게 돼서 좀 늦게 마치기도 했고, 내일 병결 예정이라 오늘 미리 프로젝트 작업을 좀 해 두려다 보니 1시가 다 되어가는 지금 회고를 작성한다.  

강의 내용은 사실 많이 소화하지 못했다. 여러 복잡한 모델들을 소개해주셨는데, 설명을 짧게 다루고 넘어가시다보니 이해하기가 어려웠다.  
한 가지 기억에 남는 내용은 latent cross이다.  
hidden representation인 h와 context vector인 w가 있을 때, (1+w)와 h의 dot product로 h'을 계산하는 것이다.  
이때 w를 zero-mean gaussian으로 초기화하면 w가 mask나 attention의 역할을 하게 된다고 한다.  
context vector가 별로 영향이 없다면 0에 가까워져 h' = h가 된다.  

그 후에도 피어세션, 특강, 멘토링 등 여러 가지를 진행했는데 작성 시점 기준 이미 새벽 1시라 오늘은 짧게 생략하고자 한다.  
이번 프로젝트 목표로 컨디션 관리 잘 하기를 세웠는데 벌써 무너지지 않도록 주의를 기울여야겠다.  

+ ##### 키워드: Latent Cross, 컨디션 관리

Day 60 (01/31)
---
Word2Vec을 구현하여 영화들을 임베딩으로 만든 후 그 분포를 분석해봤다.  
clustering이 잘 된 느낌은 아니었지만, 장르는 영화의 특성과 크게 상관없다는 점과 개봉 연대가 생각보다 중요하다는 점을 발견했다.  
분석 결과를 조원들과 공유하고 사용한 코드를 PR했는데, 급하게 만든 코드라 그런지 조원들이 리뷰를 하기 어려워하는 반응들이었다.  
그래서 내일은 아마 코드를 다듬는 데 주로 시간을 보내지 않을까 싶다.  

Word2Vec으로 얻은 임베딩을 KMeans로 clustering하고, 유저가 어떤 cluster를 선호하는지에 따라 해당 cluster에서 가장 인기 있는 10가지 영화를 추천하는 방식을 적용해봤다.  
단순히 전체 영화 중 인기 있는 10가지를 추천하는 것과 비슷한 결과가 나왔는데, 내 생각엔 cluster에 대한 선호도 계산 방식에 오류가 있었던 것 같다.  
계산을 수정한 후 다시 같은 방식을 시도해 볼 예정이고, 그 외에 유저가 관람한 영화의 평균 임베딩과 가장 가까운 10개의 영화를 추천하는 방식도 시도해 볼 계획이다.  

그리고 오늘 피어세션 때 PM을 정했다.  
최종 프로젝트 때도 PM이 있어야 업무 효율성이 높아질 것 같다는 의견이 나왔고, 기왕 PM을 둘 거라면 이번 프로젝트부터 미리 맡아서 서로 익숙해지는 게 좋겠다는 판단을 했기 때문이다.  
PM을 맡아보고 싶어하시는 분이 한 분뿐이라 우선 그 분이 이번 프로젝트동안 PM을 맡기로 하셨다.  

+ ##### 키워드: Word2Vec, Kmeans Clustering, PM

Day 61 (02/01)
---
어제 계획했던대로 Word2Vec 관련 코드들의 refactoring을 진행했다.  
Type hint와 doc string을 추가하고, 코드를 여러 함수로 분할하여 다른 코드에서 사용이 가능하게끔 다듬었다.  

코드를 다듬으면서 Word2Vec 임베딩으로 여러 실험을 진행해봤는데, 성능이 그리 좋지 않았다.  
단순히 최고 인기 영화 10개를 추천해주는 것보다 조금 나은 정도에 그치는가 하면, 그보다도 못한 경우도 있었다.  
유저가 관람한 영화들의 평균 임베딩을 유저 임베딩으로 간주하고, 해당 임베딩과 거리가 가장 가까운 10개를 추천했더니 제일 성능이 나빴다.  
내 생각에는 유저가 공포 영화와 액션 영화를 좋아하더라도, 둘을 반쯤 합쳐놓은 영화에 대해서는 별로 선호하지 않는 경향이 있어서 이런 결과가 나온 것 같다.  

실험을 하다 보니 제출 횟수를 많이 소모했는데, 그 과정에서 valid set의 필요성을 느꼈다.  
이번 대회는 베이스라인 코드를 사실상 무시하고 진행 중이라, validation에 대한 기능도 아직 구현이 되지 않은 상태이다.  
그래서 해당 내용을 이슈로 등록하고 valid data를 만드는 코드와 recall@10을 계산하는 코드를 구현해 해결했다.  
기존에 리더보드에 제출했던 방법론들을 기준으로 valid 값을 확인해보니 리더보드와 어느 정도 일치하는 것을 확인했다.  

그리고 오피스아워 때 베이스라인 코드에서 사용된 모델인 S3-Rec에 대한 설명을 들었다.  
간단히 요약하자면 아래 3단계를 통해 영화를 추천하는 모델이다.  
1. pretraining으로 각 영화 embedding에 side information을 담는다.  
2. 학습된 embedding을 seq_len만큼 입력으로 받고, 다음 영화의 embedding을 예측한다.  
3. 예측된 embedding과 가장 유사한 영화를 추천 대상으로 제시한다.

다만, 이 모델에 비해 현제 IBCF 방법이 성능이 더 좋게 나와서 아마 사용하지는 않을 것 같다.  
추천시스템은 특히나 SOTA 모델에 대한 의존성이 적다고 하는데, 가장 단순한 방법인 IBCF가 복잡한 SOTA 모델보다 좋은 성능을 내는 걸 보니 확실히 체감이 된다.  

+ ##### 키워드: Refactoring, Validation, S3-Rec

Day 62 (02/02)
---
오늘은 임베딩 시각화 분석과 파이프라인 구축 위주로 진행했다.  
성능이 잘 나왔던 IBCF의 임베딩을 시각화 해 봤는데 딱히 클러스터링이 잘 되거나 별다른 특징이 보이지 않았다.  
각 유저들이 관람한 영화 제목을 일렬로 이어붙인 후 토큰화 하여 Word2Vec도 진행해봤는데 마찬가지로 성능이나 임베딩 패턴에서 별 성과가 없었다.  
그래서 임베딩 분석은 일단 보류하고 MF 모델을 구현해보기로 했다.  

모델을 구현하는 김에 현재 베이스라인 코드 대신 우리 조의 파이프라인을 만들기로 했고, 내가 그 작업을 맡기로 했다.  
그래서 데이터셋, 데이터로더, 모델링, loss 계산 및 최적화, 로깅 등등 필요한 기능을 모두 구현하고 있다.  
다행히 지난 대회의 코드가 있어서 해당 코드를 많이 참고해서 작업 중이라 생각보다는 금방 끝날 것 같다.  

그리고 오늘 아침에 서버 접속이 안 되는 이슈가 있었는데, VSCode가 업데이트 되면서 Remote:SSH Extension의 버전도 업그레이드 되어 발생한 문제였다.  
조원들과 데일리 스크럼 때 같이 해결을 시도해서 생각보다 금방 원인을 찾았고, 인터넷을 보니 전세계적으로 문제를 겪고 있는 걸 알게 되었다.  
그래서 슬랙에 문제 상황과 해결책을 공유했더니 다들 덕분에 서버 접속에 성공했다며 감사 인사를 많이 남겨주었다.  

요즘 코어타임인 10시~19시 이외에도 계속 작업하는 날이 이어지고 있는데, 이번 대회는 왠지 자꾸 뭔가를 시도해보고 싶어져서 시간을 많이 투자하게 되는 것 같다.  
대회 종료 후에 솔루션 발표도 예정되어 있는 만큼 실험을 많이 해 보는 것은 좋은 일이지만, 너무 무리하지 않도록 주말에는 좀 쉬어야겠다.  

+ ##### 키워드: 파이프라인 구축, MF, 서버 접속 이슈 해결