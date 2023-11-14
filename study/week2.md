Week 2 (11/13 ~ 11/17)
===
>  ##### 주간 요약
>   

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
