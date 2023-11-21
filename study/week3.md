Week 3 (11/20 ~ 11/24)
===
>  ##### 주간 요약
>    

Day 11 (11/20)
---
이번주는 CNN, RNN, Transformer, Generative Model 등 기본적인 딥러닝 모델들에 대해 배울 예정이다. 또한 다음주까지 2주에 걸쳐 Data Vizualization에 대해 배운다.  

오늘은 MLP를 만들어보고, 이에 대해 optimizer를 바꿔가며 수렴 속도를 비교했다.  
optimizer 중에서도 momentum과 adaptive 개념을 결합한 ADAM이 보편적으로 가장 좋은 성능을 낸다고 한다.  
ADAM을 PyTorch에서 실습할 때 학습률만 설정하고 beta1, beta2 값은 default 값을 썼는데, 이유에 대해 질문하니 조교님께서 보편적으로 해당 값에서 가장 성능이 좋다고 하셨다.  

그리고 오늘 피어세션이 지금까지 중 가장 생산성 있었던 것 같다.  
내가 퀴즈를 풀다 이해가 잘 안 된 부분을 질문하기도 했고, 다른 조원들의 질문들에도 많이 대답하면서 optimizer들에 대한 전체적인 설명도 했다.  
사실 나와 같은 강의 영상을 보는 사람들에게 내가 설명을 한다는 것이 우습기도 하고, 틀리면 어쩌나 하는 생각도 들었다.  
그래도 설명하는 과정에서 내가 이해한 걸 복습할 수 있는 좋은 기회라고 생각하고 최대한 차근차근 설명했다.  

지난주에 비해 과제 난이도도 많이 낮아지고 분량도 줄어든 것 같아서 학습 일정에 여유가 좀 생길 것 같다.  
그동안 코어 타임을 넘겨서도 추가로 공부를 하는 날이 많았는데, 이번주는 최대한 7시 전에 모두 끝내고 나머지 시간은 일상 생활에 할애해야겠다.  
>  오늘의 질문 횟수: 3  
>  오늘의 답변 횟수: 6
+ ##### 키워드: MLP, Optimizer

Day 12 (11/21)
---
오늘은 대표적인 CNN과 RNN 모델들에 대해 배웠다.  
오늘 배운 모델들 대부분이 이미 더 나은 모델들로 대체된 것으로 알고 있지만, 각 모델들의 발전 과정을 보며 핵심 아이디어들을 배웠다.  

CNN의 경우는 더 깊고, parameter 수가 적으며 성능이 뛰어난 모델의 방향으로 개선되었다.  
보통 딥러닝 모델은 layer가 너무 깊어지면 성능이 떨어지고, parameter도 마찬가지로 너무 많아지면 generalization gap이 커지기 때문에 성능이 떨어진다고 한다.  
때문에 주요 아이디어들이 모두 parameter 수를 줄이거나 layer를 깊게 쌓아도 성능이 떨어지지 않도록 하는 것에 집중되어있다.  
첫 아이디어는 하나의 큰 kernel을 쓰는 대신 작은 kernel을 연속으로 쓰는 것이다. 이렇게 하면 receptive field의 크기를 유지하면서 parameter의 수를 줄일 수 있다.  
둘째는 1,1 convolution이다. Channel의 수를 줄임으로써 parameter의 수를 줄이는 효과가 있다.  
셋째는 Identity map이다. 하나의 함수 f를 통과한 f(x) 값에 input 값인 x를 더한 후 activation을 하는 것이다. 여기서 H(x) = f(x) + x라고 하면, H(x)를 학습하는 것이 결과적으로 f가 H(x) - x를 학습하는 것과 같아진다.  
이러한 학습 방법을 residual learning 이라고 하는데, 이에 대해 자세히 다루진 않았지만 layer를 깊게 쌓아도 학습이 잘 되게 하는 효과가 있다고 하셨다.  

이후에 CNN의 활용에 대해 배웠는데, Fully Convolutional Network로 이미지를 heatmap으로 만들어 Semantic Segmentation을 하거나 bounding box를 설정하고 그 위치와 크기, label에 대해 학습함으로써 Detection을 할 수 있다고 한다.  

RNN에서는 basic RNN model과 LSTM, GRU의 구조에 대해 배웠다.  
앞서 CNN에서는 각 모델의 특징만 배우고 실습으로는 단순한 CNN만 구현했는데, RNN에서는 다룬 모델의 종류는 적지만 실습에서 LSTM을 구현하는 게 어려웠다.  
MLP나 CNN에서는 하나의 데이터를 하나의 input으로 봤다면, LSTM에서는 하나의 데이터를 여러 input의 연속으로 간주해야했다.  
그렇다보니 input의 batch size, sequence length, input dimension, LSTM의 feature dimension 등 고려해야 할 요소가 많았다.  
각 dimension들의 관계나 parameter의 수 등이 잘 이해가 안 돼서 PyTorch document도 읽어가며 공부했더니 어느 순간 한번에 이해가 확 되었다.  

그리고 오늘 슬랙에서 다른 캠퍼분이 Xavier Normal Initialization과 He Normal Initialization에 대해 정리한 글을 올려주셨다.  
sigmoid와 같은 activation에 대해 zero-centering과 0 부근의 선형성을 가정하고, 대부분의 값들을 0 부근에 위치시키는 방법인 듯하다.  
만약 initialization 과정에서 분산이 너무 작다면 activation을 통과한 값이 대부분 0에 가까운 작은 값으로 나타나 기울기 소실의 위험이 커진다.  
반대로 분산이 너무 크면 activation을 통과한 값이 -1이나 1로 몰려서 나타나 기울기 폭발의 위험이 커진다.  
이를 고려해 적절한 분산의 정규분포로 initialization을 해주는 것이 위의 두 방법인 것이다.  
이 중에서 Xavier 방법은 주로 sigmoid 계열 activation에, He 방법은 주로 ReLU activation에 활용한다고 정리하셨다.  
그런데 실습 과제에서는 tanh activation에 대해 He 방법을 활용했길래 이에 대한 의견을 해당 캠퍼분과 나눴다.  
의견을 나누며 initialization 방법과 activation 함수를 바꿔가며 실험해보니 과제에서 사용된 조합 외에는 학습이 잘 되지 않았다.  
그래서 이에 대한 이유를 추측하고, initialization 방법과 activation 함수가 중요한 hyper parameter 라는 인사이트를 공유하였다.  

다른 캠퍼분과 강의에서 다루지 않은 내용으로 이렇게 깊게 의견을 공유한 적이 없었기에 꽤나 신선한 경험이었다.  

>  오늘의 질문 횟수: 3
>  오늘의 답변 횟수: 1
+ ##### 키워드: CNN, RNN, Weight Initialization
