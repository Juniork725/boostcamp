Week 8 (12/26 ~ 12/29)
===
>  ##### 주간 요약
>  AI 모델링 외에 서비스 개발에 필요한 여러 기초들을 배웠다.  
>  진로 고민을 하며 방향성을 점검하는 한 주였다.  
>  Level 1을 마무리하고, 새로운 팀원들을 맞이 할 준비를 했다.  

Day 36 (12/26)
---
이번 주는 AI 서비스 개발 기초에 대해 배우고, 현업자들의 특강을 듣는 주간이다.  
첫 강의 내용은 소프트웨어 엔지니어링이었다.  
소프트웨어 개발은 단순히 구현만 하는 것이 아니라, 계획-요구 조건 분석-설계-구현-테스트-유지 보수와 같은 일련의 과정으로 구성된다.  
이때 좋은 소프트웨어 설계는 모듈성, 높은 응집도, 낮은 결합성을 만족해야 한다.  

두번째 내용은 파이썬 버전 관리였다.  
버전이란 왜 필요한 것인지, 버저닝에는 어떤 종류가 있는지, pyenv를 통한 버전 관리와 venv를 통한 가상 환경 관리, poetry를 통한 패키지 관리 등을 배웠다.  

마지막 내용은 linux shell command였다.  
간단한 shell 명령어들과 redirection, pipe 등을 통해 한 명령어의 결과물을 추가로 활용하는 법을 배웠다.  
졸업논문을 쓸 때 linux 환경에서 작업을 했어서 나름 친숙한 느낌이 들었다.  

강의 후에는 피어세션을 하면서 연말에 조원들과 다 같이 모이기로 약속을 잡았고, 그 뒤의 멘토링 때는 고민 상담같은 시간을 가졌다.  
프로젝트 대회 결과가 잘 안 나온 건 아쉬운 일이지만, 그 과정에서 각자의 장단점을 잘 파악해서 강점은 다듬고, 약점은 보완하라는 말씀을 하셨다.  
그리고 최근에 진로에 대해 고민 중이라고 말씀드렸더니 내가 나중에 어떤 분야로 가든 AI를 활용한다면 지금 캠프에서 배우는 것들이 공통적으로 필요할 거라고 하셨다.  
요즘 진로 고민을 비롯해서 여러 고민들로 많은 사람들에게 조언을 받아보는 중인데, 이번주는 비교적 일정이 널널하니까 최대한 고민하면서 나의 방향성을 잡아나가는 시간으로 만들어야겠다.  

+ ##### 키워드: 소프트웨어 엔지니어링, 파이썬 버전 관리, linux shell command, 진로 고민

Day 37 (12/27)
---
오늘도 어제에 이어 AI 서비스를 개발할 때 필요한 기초 지식들에 대해 배웠다.  
Docker로 서버 환경을 가상화하여 사용하는 법, 개발 과정 중에 디버깅을 대하는 자세, MLOps란 무엇이며 주로 고려하는 요소에는 어떤 것들이 있는지, Online Serving과 Batch Serving의 차이 등을 주로 다뤘다.  

그간 있었던 강의들 중에 제일 이해가 잘 되는 것 같다. 강의 내용의 난이도 차이도 있지만 강의 흐름이 자연스러워서 받아들이기 쉬운 것 같다.  

이번 주는 마스터 클래스 대신 두런두런 2회차를 진행했다.  
데이터 관련 직무에는 어떤 것들이 있는지 등에 대해서도 소개해주셨지만, 대부분의 시간은 고민 상담으로 채워졌다.  
접수된 고민 사연이 워낙 많다 보니 어떤 고민은 공감되고, 어떤 고민은 잘 와닿지 않기도 하고 그랬다.  
그 중에서 몇 가지 남겨두고 싶은 조언들을 기록해둔다.  
첫째, 지금 나보다 잘하는 사람들을 보며 비교하기 쉬운데, 그 사람들이 나와 비슷한 연차였을 때를 기준으로 비교해보자.  
둘째, 너무 고민만 하면 이도저도 안 된다. 고민만 하는 것보다 지금 당장 할 수 있는 것에 최선을 다 하자.  
셋째, 포트폴리오와 면접은 자신을 포장하는 것이 아니라, 내가 해 온 것들을 잘 정리해서 보여주는 것이다.  
넷째, 막연하게 불안감이 느껴진다면 왜 불안한지 생각해보자.  

+ ##### 키워드: Docker, 디버깅, MLOps, Serving, 두런두런 2회차

Day 38 (12/28)
---
오늘은 머신러닝 프로젝트의 흐름과 streamlit을 활용해 프로토타입을 개발하는 법을 배웠다.  
몇 주 전에 최종 프로젝트 주제로 고민하다가 마땅한 주제를 못 찾고 보류했는데, 구체적으로 어떻게 프로젝트를 세워야 할지 배울 수 있었다.  
해결해야 할 문제가 어떤 것인지, 어떤 현상이 일어나고 있는지 파악한 후, 명확한 용어로 구체적인 문제를 정의하는 게 중요하다.  
실무적인 관점에서는 문제를 정의 후 간단한 방법을 먼저 제시한 후, 점진적으로 접근해나가는 게 좋다고 하셨다.  
이번 프로젝트 때 느꼈던 점과도 일맥상통하는 부분이 있었다. 새로운 방법을 도입할 때도 간단한 방법으로 먼저 결과를 얻은 후 그와 비교하며 발전시켜나가는 게 좋아보인다.  
문제를 해결할 때는 항상 ML이 정답인 것은 아니다. 이것도 예전에 멘토링 시간 때 멘토님이 말씀해주셨던 내용과 연결되었다.  
학습할 수 있는 패턴이 있고, 그 패턴이 복잡하고, 적절한 데이터를 수집해서 활용할 수 있는지 등 ML이 잘 해결할 수 있는 문제인지 판단하기 위해 여러 기준을 고려해야 한다.  
ML이 잘 해결할 수 있는 문제라고 판단이 되면, 비로소 ML로 해결할 주요 목표를 설정하고, 베이스라인과 프로토타입을 만든 후 모델을 본격적으로 개발해 배포하는 과정이 이어지는 것이다.  

위에서 언급했듯 ML 프로젝트 진행 과정에서 프로토타입이 필요한 순간이 있다.  
모델을 개발하여 실제 서비스에서 어떻게 활용할 것인지 다른 사람들에게 설명하고 프로젝트의 필요성을 설득할 때 등이 그런 순간이 될 것이다.  
하지만 프론트엔드를 꼼꼼히 개발하는 것은 불필요한 리소스를 많이 필요로 하기에, 간단한 프로토타입을 직접 만들 수 있는 능력이 필요하다.  
이때 주로 활용되는 프레임워크 중 하나가 streamlit이다.  
실습 과제로 streamlit을 활용해 이번 프로젝트에서 활용한 모델의 웹 프로토타입을 만들어보았다.  
예전에 카풀 앱을 만들면서 프론트엔드 작업을 했을 때보다 훨씬 간단하게 구현이 가능해서 금방 작업할 수 있었다.  
프로젝트 때 서버에서 작업하며 모델 성능을 확인할 때는 예측 결과가 단순한 숫자로만 보였는데, streamlit을 통해 웹에 결과를 띄우니 친숙하게 느껴지고 실제 서비스 같은 느낌이 들었다.  

+ ##### 키워드: ML 프로젝트 설계, streamlit

Day 39 (12/29)
---
Level 1을 마무리하는 날이었다.  
실무에서의 AI 개발에 대한 여러 이야기들을 듣고, 학습 데이터셋의 저작권 문제, 모델의 추론 결과의 편향 등 AI를 다룰 때 고려할 윤리적 문제 등에 대한 특강을 봤다.  

그 외에 처음으로 다른 도메인 분들과 피어세션 시간을 가지면서 강의 및 프로젝트 후기도 공유했다.  
그리고 오늘로 level 1을 마무리하며 8주간 함께 했던 멘토님, 조원들에게 인사를 하는 시간을 가졌다.  
딱히 거창하게 하진 않고 슬랙에 간단하게 인사글을 남기는 정도였는데, 막상 인사를 하려니 무슨 말을 할지 잘 떠오르지 않아서 마음을 다 담기가 어려웠다.  
그래도 조원들과는 일요일에 오프라인으로 만나기로 했고, 앞으로도 캠프 활동을 하면서 스페셜 피어세션 때 볼 수도 있어서 아쉬움을 어느 정도 달랬다.  

이제 본격적으로 level 2 조원들과 슬랙 채널도 만들고, github repo도 생성하면서 새로운 막에 접어들었다는 실감이 나기 시작한다.  
새로 만나는 조원분들과도 친근한 사이가 돼서 남은 캠프 생활을 재밌게 이어나가면 좋겠다.  

+ ##### 키워드: AI 윤리, Level 1 종료
