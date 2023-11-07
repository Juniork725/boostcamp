# Week 1 (11/6 ~ 11/10)

## Day 1 (11/6)

OT를 진행하고 8주간 함께 활동할 조원들과 첫 만남을 가졌다.  
다들 어색해서 정적이 많이 흘렀는데, 어찌저찌 자기소개도 하고 팀 활동 규칙도 만들었다.  

강의 내용은 개발 환경 세팅과 python 문법 위주였다.  
실습 중에 cmder로 conda 실행하기가 있었는데, 시스템 환경 변수로 conda 폴더 경로를 넣어줘도 인식이 안 됐다.  
구글링으로 해결책을 찾았는데, cmder 프로그램 설정에서 환경 변수를 따로 추가해주니 해결됐다.  

그리고 python에서의 * 활용에 대한 내용이 있었는데, arguments 외에도 일반 변수를 unpacking 할 수 있다는 게 신기했다.  

코딩 컨벤션에 대한 내용도 있었는데, 나중에 조별 프로젝트를 진행하기 전에 조원들과 한번 정리해두면 좋을 듯하다.  

## Day 2 (11/7)

어제는 행사가 많아서 좀 정신없이 지나갔지만, 오늘은 본격적으로 이론 공부를 시작한 느낌이 들었다.  

python의 OOP 특성과 기초적인 선형대수학에 대해 공부했는데, closure를 구현할 때 decorator를 활용하는 부분이 좀 어려웠다.  
그래도 직접 코드를 응용해보고 구글링을 하면서 더 자세히 이해했다.  
예를 들어 outer 함수가 아래와 같이 선언됐을 때,
```python3
def outer(func):
  def inner(*args, **kwargs):
    func(*args, **kwargs)
  return inner
```
아래 두 코드는 같은 기능을 수행한다.
```python3
@outer
def func1(param):
  action
```
```python3
def func1(param):
  action
func1 = outer(func1)
```
decorator는 배울 때마다 완전히 이해하기가 어려웠는데 이번 기회에 확실하게 배웠다.  

그 외에 python의 함수는 내부적으로 객체로 구현되고, 함수를 매개변수로 사용할 때는 types 모듈의 FunctionType으로 type hinting을 할 수 있다는 것도 배웠다.  

강의를 들은 후에는 조별 모임인 피어세션을 진행했다.  
피어세션에서는 내가 공부한 Decorator 개념을 비롯해, 재귀함수, list comprehension, generator 등에 대해 조원들이 공부해 온 내용을 공유했다.  
확실히 혼자 공부할 때에 비해 한 내용을 다각도로 보고 이해하게 되는 느낌이 들었다.  
