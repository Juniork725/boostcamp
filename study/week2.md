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

그 외에 과제를 풀면서 hook이라는 개념도 배웠다.  
hook은 패키지화된 코드에서 실행 로직을 분석하거나 추가적인 기능을 넣고 싶을 때 쓸 수 있는 interface라고 한다.  

오늘의 정리는 개념에 대한 것들이 많은데, 나중에 찾아볼 수 있도록 잘 기록해둬야겠다.  

+ ##### 키워드: contiguous, backward method, hook
