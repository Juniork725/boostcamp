Week 2 (11/13 ~ 11/17)
===
>  ##### 주간 요약
>   PyTorch 활용법에 대해 배우고, 피어세션을 통해 확률론 스터디를 시작했다.  
>   꾸준한 학습을 위해 적당한 템포를 유지하기로 다짐했다.  
>   과정 수료 후 '대회 출전'과 '완성된 서비스 출시'에 도전하겠다는 목표가 생겼다.  

Day 6 (11/13)
---
이번주는 PyTorch 활용법을 배울 예정이다.  
지난주는 강의 분량이 20시간 이상이었는데 이번주는 5시간 정도로 줄었다. 대신 그만큼 실습 분량이 상당히 늘었다.  

강의 내용은 크게 어려울 게 없다고 생각하면서 듣고 넘어갔는데, 피어세션 때 내가 놓친 부분들을 많이 발견했다.  

첫 번째는 contiguous라는 개념이었다.  
tensor[i][j][k]에서 k값이 1 증가할 때마다 메모리 주소가 1 단위씩 증가하면 contiguous하다.  
예를 들어,  
```
tensor[0][0][0] - tensor[0][0][1] - tensor[0][1][0] - tensor[0][1][1] - tensor[1][0][0] - .. 
```
과 같은 순서로 메모리 주소가 연속적이면 contiguous하다. [(참고 링크)](https://jimmy-ai.tistory.com/122)  

두 번째는 PyTorch의 autograd 원리에 대한 내용이었다.  
PyTorch에서는 backward라는 method를 통해 연결된 tensor들의 미분값을 구할 수 있다.  
이때 backward를 호출하는 tensor가 scalar이면 grad = tensor([1])에 의해 grad에 default 값이 들어간다.  
하지만 scalar가 아니라 vector라면 해당 tensor의 dimension과 맞는 tensor를 grad에 넣어줘야한다.  
이때, grad vector를 V, Jacobian matrix를 J라 하면 backward(grad = V)의 리턴값은 V@J이다.  

그 외에 과제를 풀면서 hook이라는 개념도 익혔다.  
hook은 패키지화된 코드에서 실행 로직을 분석하거나 추가적인 기능을 넣고 싶을 때 쓸 수 있는 interface라고 한다.  
처음에는 어떤 기능인지 잘 이해가 안 됐는데 다양하게 응용하며 연습해보니 금방 이해가 되었다.  

오늘의 정리는 개념에 대한 것들이 많은데, 나중에 찾아볼 수 있도록 잘 기록해둬야겠다.  

+ ##### 키워드: Contiguous, Backward Method, Hook

Day 7 (11/14)
---
오늘도 어제처럼 실습 과제에 대부분의 시간을 쏟았다.  

PyTorch로 Custom model을 만드는 방법을 익혔는데, 문제를 풀다가 직접 찾아보며 공부한 내용이 크게 2가지 있었다.  
첫 번째는 leaf variable이다. 다른 tensor와의 연산을 통하지 않고 독자적으로 생성된 tensor의 requires_grad 인자가 True이면, 이 tensor는 leaf variable이다.  
leaf variable은 X.fill_(1) 등의 in-place 연산을 지원하지 않기 때문에, torch.no_grad()로 requires_grad를 False로 바꾸고 연산해야한다.  

두 번째는 PyTorch의 Linear Model의 연산 방식이다.  
직관적으로는 (in_features, out_features) 형태의 weight를 생성한 후 input @ weight + bias 연산을 할 거라 생각했다.  
그런데 실제로는 (out_features, in_features) 형태의 weight를 생성하고 BLAS라는 라이브러리를 통해 연산을 한다고 한다.  
이에 대해 슬랙으로 질문을 하고 이유에 대해 논의했는데, 위처럼 transpose 형태로 만들어야 메모리 접근이 contiguous하게 이뤄져서 cache miss가 줄어들기 때문이라는 결론을 내렸다.  

과제 해결 후에 이어진 강의에서는 autograd, optimizer의 작동 과정과 Dataset, DataLoader 클래스에 대해 배웠다.  
Dataset은 입력 방식을 표준화하여 입력 형태를 정의한다고 한다.  
간단히 생각하면 외부로부터 데이터를 읽어들이고 이를 정형화된 형태로 가공하여 개별 data로 반환해주는 역할인 듯하다.  
Dataset 서브클래스를 만들 때는 \_\_len\_\_과 \_\_getitem\_\_ 메서드를 선언해줘야 한다.  
그래야 Dataset을 인자로 받는 DataLoader가 이를 바탕으로 batch를 생성할 수 있다.  

DataLoader는 Dataset의 \_\_getitem\_\_ 메서드를 이용해 데이터를 indexing하여 batch를 생성해준다.  
주로 GPU에 데이터를 넘겨주는 학습 단계 직전에 데이터를 tensor로 변환해 batch로 만들어주는 역할을 한다고 한다.  

그리고 오늘은 이런 개념들을 배운 것보다 과제를 하면서 document와 source code를 찾아 읽는 능력을 기른 게 가장 큰 소득인 거 같다.  
과제가 최대한 PyTorch document를 읽고 해석하여 문제를 풀도록 구성되어 있어서 연습하는 데 도움이 많이 됐다.  
앞으로 낯선 라이브러리를 사용할 때 document와 source code를 읽는 것에 대한 부담감이 많이 줄어들 것 같다.  

+ ##### 키워드: Dataset, DataLoader, Document, Source Code

Day 8 (11/15)
---
이번주의 실습 과제를 모두 끝냈고, 남은 강의들을 듣는 중이다.  
과제 내용은 Dataset과 DataLoader를 다루는 내용이었고, 문제에서 제시하는 조건이 좀 부족하다고 느껴서 헤맨 것 외에는 무난하게 풀었다.  
조건이 부족하다고 느낀 부분은 label 값이 0,1,2,3인데 이들을 'Business', 'World' 등으로 mapping 할 때 각 숫자가 어떤 label에 대응돼야 하는지 제시되지 않은 점이었다.  

과제를 끝내고는 PyTorch에서 model을 저장하고, pre-trained model을 불러와 customizing 하는 방법에 대해 공부했다.  
model의 일부 parameter들을 갱신되지 않도록 하는 freezing 기법에 대해서도 배웠다. 이런 창의적인 방법들을 새로 알게 되는 과정이 특히 재밌다.  

그 외에 강의를 보면서 질문이 2가지 생겼는데, 질문 게시판에서 다른 캠퍼분들이 친절히 답해주신 덕에 해결할 수 있었다.  
첫 번째는 transform을 할 때 Resize(244), CenterCrop(224)를 연속으로 취해주는 게 의미가 있나? 하는 점이었다.  
나는 Resize(244)가 (244,244) 크기로 잘라준다고 생각했는데, 실제로는 이미지의 크기 비율을 유지하면서 짧은 길이를 244로 바꿔준다고 한다.  
그래서 Resize 후에 CenterCrop까지 취해줘야 (244,244)의 정사각형 이미지가 되는 것이다.  

두 번째는 vgg16 모델을 불러온 후 vgg.fc = nn.Linear(1000,1) 같은 식으로 모듈을 추가해 줄 때, 왜 기존 모듈 뒤에 자동으로 Linear 모듈이 들어가는가? 였다.  
나는 vgg의 형태를 print로 출력했을 때 fc도 출력되길래 기존 모델에 자동으로 연결이 되는 것으로 생각했다.  
그런데 사실은 vgg 모델의 fc라는 attribute가 생기고, 거기에 Linear 모듈이 할당되는 것뿐이었다.  
그래서 forward 함수를 재정의하여 기존 모델 뒤에 fc 모델의 연산을 연결해주는 과정이 필요하다.  

두 질문 모두 내가 착각을 하고 있던 부분을 바로잡는 과정이었다.  
처음에는 사소한 질문이라서 그냥 넘어갈까 싶다가 물어본 것이었는데, 결과적으로 질문하길 잘했다는 생각이 들었다.  
피어세션 때도 다들 나랑 비슷한 착각을 하고 있었는지 질문에 대해 명확한 해답이 안 나왔는데, 내일 새로 알게 된 부분을 공유해야겠다.  

그리고 내가 질문을 통해 새로 배우게 된 만큼, 슬랙과 피어세션에서 다른 캠퍼분들의 질문에도 많이 답변해드렸다.  
backward hook이 어떤 원리로 작동하는지, DataLoader에서 collate function은 무엇을 하는지 등 나도 질문을 하며 확실하게 개념을 다졌다.  

강의를 듣고 나서 두런두런이라는 행사를 진행했다.  
변성윤 마스터님께서 자신의 커리어를 소개하시고 학습에 대한 고민 상담과 조언들을 해 주셨다.  
사실 피어세션이나 슬랙에서 다른 캠퍼들을 보면 다들 학업적 성취에 대해 많이 욕심을 낸다는 게 느껴진다.  
개인적인 성취감을 위해 노력하는 사람도 있겠지만, 왠지 주변 사람들에 비해 내가 부족한 부분이 많이 와닿고 불안해서 조바심을 내는 사람도 많을 것이다.  
나 역시도 이 정도는 알아야 하지 않을까? 라며 크게 중요하지 않은 부분들도 최대한 깊게 파고드는 경향이 있었다.  
물론 많은 걸 알면 당연히 좋겠지만, 한정된 시간과 집중력으로 모든 걸 배우는 것은 불가능하기에 선택과 집중이 필요하다.  
오늘 마스터님께서 말씀해주신 내용을 듣다 보니 위와 같은 생각이 들었다.  
그래도 1주차 때보다는 주변 분위기에 덜 휘둘리면서 나의 학습 템포를 되찾는 느낌이 들고 있지만, 앞으로도 이 느낌을 잃지 않도록 신경써야겠다.  

+ ##### 키워드: 학습 템포

Day 9 (11/16)
---
이번주 학습 내용을 모두 소화하고, 심화 과제까지 완료했다.  
지난주에는 분량이 너무 많아서 심화 과제는 도전을 못했는데 이번주에는 금요일을 남겨두고 모두 마쳤다.  

오늘 배운 내용은 모델을 학습시킬 때 multi GPU에 작업을 분산하기, 성능 개선을 위한 hyperparameter tuning, PyTorch를 활용할 때 주로 발생하는 문제들의 trouble shooting 등이었다.  
모두 실제로 AI 개발 프로젝트를 할 때 유용하게 와 닿을 듯한 내용들이었다.  
나는 아직 과제 수준으로 모델을 조금 다뤄본 게 전부라 이런 것들이 있구나 하는 느낌으로 가볍게 익혀뒀다.  

그리고 부스트캠프 슬랙에 어제의 학습 템포에 대한 다짐을 글로 적어서 공유했는데, 예상보다 많은 반응을 받아서 뿌듯했다.  
자신에 대한 채찍질로 힘들어하는 사람들에게 도움이 되고, 나 스스로도 공개적인 곳에 글을 씀으로써 다짐을 확실히 해 두려고 글을 작성했다.  

![image](https://github.com/Juniork725/boostcamp/assets/62535139/41044659-5dbe-48f4-ad4d-3dbfa9ea116b)

너무 무리하지 않으면서, 게으르지도 않도록. 적당한 수준을 유지하기 위해 꾸준히 나를 점검해야겠다.  

강의를 모두 듣고 나서는 피어세션, 마스터클래스, 멘토링이 연달아 있었다.  

피어세션 때는 생각지도 못한 칭찬을 많이 받았다.  
다른 사람의 질문이나 설명에 대한 이해력이 좋고, 슬랙에 유용하면서도 날카로운 질문을 많이 던져줘서 도움이 된다는 내용이었다.  
만난지 얼마 안 된 사람이 내 장점을 알아보고 칭찬해준다는 것에 기분이 좋았다.  
확실히 지난주에 비해 팀원들과 많이 가까워지고 소통의 어색함도 줄어들었다.  

피어세션 후 이어진 마스터클래스에서는 Chap GPT에 대한 내용이 많이 다뤄졌다.  
몇 가지 중요하다 생각한 부분을 적어보자면,
1. 현대의 AI는 pre-trained model을 활용하는 것이 대세다. 모델을 개발하는 것보다 데이터를 모으고 tagging 하는 것이 더 중요한 경우도 많다.  
2. 신입으로 지원할 때 특정 프로젝트에 대한 경험을 구체적으로 설명하자. 어떤 문제를 어떻게 풀었고, 그 과정에서 어떤 걸 느꼈는지가 중요하다.  
3. AI를 다루는 것에 그치지 않고, frontend와 backend를 모두 경험해보며 하나의 완성된 product를 publish 해 보는 것이 좋다.  

정도가 있다. 멘토링 때는 현업을 하시면서 유용하게 쓰시는 각종 툴이나 에디터 등을 소개받았는데, 내 기준에서 딱히 매력적으로 느껴지는 게 없어서 아쉬웠다.  
아무래도 멘토님이 부스트캠프를 거쳐 현업 AI 엔지니어가 되신 만큼 수료 이후 취업 과정에 대한 얘기를 들어보면 좋을 듯하다.  
지금까지 멘토링 때 미리 준비해 둔 질문이 없어서 멘토님이 이끌어가시는 분위기가 되었는데, 다음주 멘토링을 위해 미리 질문을 남겨둬야겠다.  

+ ##### 키워드: 나의 장점 - 통찰력, 취업 준비

Day 10 (11/17)
---
오늘은 부스트캠프 강의 내용이 아닌 확률론을 따로 공부했다.  
지난주에 AI 수학을 공부하며 팀원들 모두 확률, 통계에 대한 공부가 필요하다는 데에 공감했기에, 이번주부터 스터디를 하기로 했다.  
목요일까지 강의 분량을 끝내고 금요일에 따로 확률론을 공부하자는 것이 목표였는데, 다행히 계획을 달성했다.  

확률론 강의가 아직 초반부라 확률의 정의, combinations와 permutations의 계산 등 간단한 내용들 위주였다.  
그래도 강의를 하시는 교수님의 설명 스타일이나 표현 방식 등에 익숙해지는 걸 목표로 꼼꼼히 수강했다.  
확률과 통계가 수식으로 대하면 까다로울 때가 많은데, 최대한 직관에 따른 설명을 해 주셔서 나와 잘 맞았다.  

피어세션 때 직관을 활용하는 설명이 잘 이해가 되지 않는다는 조원도 있었는데, 차근차근 설명하니 금방 납득하셨다.  
이런 식으로 질문과 답변을 공유하는 횟수를 늘려가다보면 피어세션 시간이 점점 더 유익해질 것 같다.  

피어세션 이후 오피스 아워에서 이번주 과제 내용을 다뤄주셨는데, 과제를 어려워했다는 사람들이 생각보다 많아서 놀랐다.  
나는 양이 많긴 했지만 과제로 제공된 notebook에 설명들이 차근차근 되어 있어 접근하기 쉽다고 느꼈기 때문이다.  
이번주에는 지난주보다 질문 게시판에서 내가 답변을 해 준 것도 많았던 것 같다.  
앞으로 일일 회고를 할 때 그날의 질문과 답변 등을 알기 쉽게 기록해두고, 질문 횟수와 답변 횟수를 늘리는 걸 목표로 해도 좋을 것 같다.  

그리고 오피스 아워 마지막에 조교님께서 여러 대회들을 알려주셨는데, [Grand Challenge](https://grand-challenge.org/)라는 의료 영상 이미지 AI 대회가 있다고 한다.  
그 외에 캐글이나 데이콘, 클로바 AI 러쉬 등도 언급하셨는데, 첫 대회라면 데이콘도 추천한다고 하셨다.  
부스트캠프를 수료하면 대회에도 도전해보고, 어제 마스터클래스에서 들었던 것처럼 하나의 상품을 만들어보는 것도 도전해봐야겠다.  

+ ##### 키워드: 확률론 스터디, 수료 후 목표
