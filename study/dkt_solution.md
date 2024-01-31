공유해드리고 싶은 재밌는 시도들이 있어 글을 남깁니다.

발표를 했다면 더 좋았겠지만 좋은 성적을 내신 분들의 솔루션이 궁금해서 자원하지 않았고, 이렇게 글을 적게 됐습니다.

1. 대분류 앙상블  
모든 문제들은 9가지 중 하나의 대분류를 갖고 있습니다.
저희는 이에 맞춰 학습 데이터를 9개로 쪼갠 후 모델 9개로 각각 학습시켜보았습니다.
예를 들어 (모델1)은 대분류가 1번인 문제들만 모은 학습 데이터를 학습하는 식입니다.
그 후 추론을 할 문제의 대분류가 1번이면 (모델1)의 추론값을, 대분류가 3번이면 (모델3)의 추론값을 사용하는 식으로 앙상블했습니다.
적용 결과, LGBM에서는 성능이 많이 향상되는 걸 확인했습니다. 다만, lightGCN 등의 모델에서는 효과가 좋지 않았습니다.

2. Data Augmentation  
강의에서도 소개되었기에, 대부분의 조에서 sliding window를 시도해봤을 듯합니다.  
하지만 저희 조에서는 대체로 좋은 성과가 나지 않아서 중간에 폐기를 했었는데, 막판에 augmentation 방식을 바꾸니 효과가 있었습니다.  
저희가 맞혀야 할 문제는 각 유저가 마지막으로 푼 문제이기에, 각 시험지에서 마지막 문제일 가능성이 높습니다.  
때문에 sliding window를 그대로 적용하는 것보다, 시험지를 기준으로 적용하는 것이 효과적일 거라 생각했습니다.  
예를 들면, 유저 A가 시험지 1, 2, 3를 순서대로 풀었을 때, (A-1), (A-1,2), (A-1,2,3)와 같은 방식으로 데이터를 증강했습니다.  
대회 막판에 적용한 것이라 충분히 실험해보지는 못했지만, 적어도 확인된 범위 내에서는 성능 향상이 있었습니다.

3. Loss Function  
이번 대회의 평가 metric은 AUC이고, 그렇기에 추론값을 0과 1에 맞추는 것보다도 값들이 올바른 순서를 유지하도록 하는 것이 중요합니다.
이런 관점에서 볼 때 베이스라인에서 사용하는 BCE는 직접적으로 AUC를 향상시켜주는 loss가 아닙니다.
때문에 AUC와 직접 연관된 loss function을 구현하여 대체해 봤습니다.
상세한 설명은 아래 github 링크와, 해당 글에 소개된 논문을 참고하시면 좋을 것 같습니다.  
https://github.com/iridiumblue/roc-star  
간단히 설명하자면, negative sample의 prediction 값이 positive sample의 것보다 높으면, 두 값의 차이를 loss에 더해주는 방식입니다.  
단, negative의 값이 positive보다 낮다면 loss는 0이 됩니다.  
실험 결과, 같은 조건에서 loss function만 변경했을 때 성능이 향상되는 것을 확인했습니다.

4. Ranking Ensemble  
리더보드에서 저희 7조의 기록을 보시면 ACC가 굉장히 낮은데, 그 이유가 이 앙상블 방식 때문입니다.
위에서 언급했듯 이번 대회의 평가 metric은 AUC이기에, 데이터들의 순서를 맞히는 것이 중요합니다.  

그렇기에 저희는 단순히 예측 값을 앙상블 하지 않고, 해당 예측 값이 모델의 전체 예측 값에서 갖는 순위를 앙상블 하였습니다.  
예를 들어, 모델 A의 전체 744개 예측 중 첫번째 행의 예측 값이 14번째로 작다면, 이 14라는 숫자를 앙상블에 활용합니다.  
마찬가지로 모델 B에서 첫번째 행의 예측 값이 23번째로 작다면, 두 모델의 평균 앙상블 결과는 (14+23)/2가 됩니다.  
이렇게 앙상블을 진행한 이유는, 모델마다 예측 값의 분포가 다르기 때문입니다.

한 모델은 0~1까지 넓은 범위로 예측하는데, 다른 모델은 0.6 근처에서 미세하게 데이터를 구분하는 경우가 있었습니다.  
위에서 언급한 ranking ensemble은 이러한 영향을 없애줄 수 있기에 AUC에 더 유리한 방식이라 생각했습니다.  
실제로 같은 모델들을 예측 값으로 앙상블한 것과 ranking으로 앙상블한 것을 제출했는데, 후자의 AUC가 더 높았습니다.  
ACC가 낮게 나온 것은 제출 파일의 모든 값이 0.5를 넘어가기 때문입니다.


이상으로 소개를 마칩니다.  
설명만 보면 굉장한 성능 향상을 이룬 것 같지만, 실제로는 상승 폭이 그렇게 크지는 않았습니다 ㅎ  
이런 보조적인 것들보다는 적절한 모델 구조와 충분한 feature engineering이 성능에 더 큰 영향을 주는 게 아닐까 싶습니다.  

개인적으로는 굉장히 재밌는 시도들이었는데, 이 글을 읽어주시는 분들께도 흥미로웠길 바랍니다.  
긴 글 읽어주셔서 감사합니다! 