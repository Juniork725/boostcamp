Week 11 (01/15 ~ 01/19)
===
>  ##### 주간 요약
>  

Day 48 (01/15)
---
오늘은 data augmentation을 위주로 작업했다.  
이전에 sliding window를 이용한 아이디어를 제안했었는데, 주말 사이에 다른 조원분이 구현을 해 두신 상태였다.  
그래서 해당 코드를 약간 수정하고, sliding window 대신 random sampling도 적용해보면서 성능 차이를 확인했다.  
실험 결과, 예상과는 다르게 augmentation이 성능 향상에 크게 영향을 주지 않았다.  

피어세션 때 실험 결과를 공유했는데, 모델의 구조가 data augmentation의 영향을 받기에 불리한 것 아닐까? 라는 의견이 제시되었다.  
확실히 모델이 학습하는 parameter의 수 자체가 적으면 데이터가 늘어나도 별 영향을 받지 않을 듯하다.  

+ ##### 키워드: Data Augmentation
