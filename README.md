# Refactoring BlackJack

## 개요

- [기존 파이썬 프로젝트](https://github.com/GulSam00/Blackjack)의 코드를 수정하며 리팩터링에 대해 배워봅시다

## 리팩터링

- 함수를 이용해 동일 작업 실행을 단순화시키기
- for문을 이용해 반복 호출 자동화
- 딕셔너리와 리스트 차이 알고 활용하기
- in을 이용해 효과적인 if문 스위칭하기
- 클래스 상속으로 메소드 재사용하기
- 메소드 오버라이딩으로 메소드를 추가로 재사용하기
- 타입 선언으로 변수 속성 명확히 알기
- import문으로 코드 분산하기
- main()문 100줄 이하로 줄이기
- global 사용 없애기
- 출력문 개선
## 목표
- 함수 인자 최대 2개
- 게임 루프 내 재귀 호출 수정
- 캡슐화를 통해 게임 루프의 객체 내부 속성과의 유착 없애기