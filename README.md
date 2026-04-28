## python  설치

## [vscode에 파이썬 설치](https://code.visualstudio.com/docs/python/python-tutorial)

1. Python 3
2. VS Code
3. VS Code Python extension (For additional details on installing extensions, see Extension Marketplace)



## [uv](https://docs.astral.sh)
- Python 생태계에서 등장한 빠른 패키지/가상환경 관리 도구로서 Rust로 구현됨
- 기존의 pip, pip-tools, pipx, poetry, pyenv, virtualenv 등을 하나로 통합하여 대체할 수 있는 강력한 도구

[설치가이드](https://docs.astral.sh/uv/getting-started/installation/)  


```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

[project 시작하기](https://docs.astral.sh/uv/guides/projects/)

```bash
uv init hello-world
cd hello-world
uv run main.py
```

의존성관리  
```bash
uv add requests
```
##


## 실기 대비

정보처리기사 실기 Python은 주로 코드의 출력 결과를 묻는 단답형/예상 문제(2~3문제, 약 10~15점)로 출제됩니다. 백준의 브론즈~실버 수준인 데이터 입출력(print, input), 배열(list), 딕셔너리, 슬라이싱, 기본 반복문/조건문, 간단한 알고리즘(합계, 최대값) 위주로 연습하며 대소문자, 공백 등 정답 형식을 철저히 맞춰야 합니다. 


1. 파이썬 주요 학습 내용 및 백준 연습 문제 (실기 대비)
기본 입출력 & 슬라이싱: 파이썬의 print()와 split(), 리스트 슬라이싱(a[start:end])은 필수입니다.  
추천 백준: 2557번(Hello World), 10818번(최소, 최대)  
반복문과 조건문: for i in range()와 if-elif-else를 통한 논리 구조 파악.  
추천 백준: 2739번(구구단), 10871번(X보다 작은 수)  
데이터 구조 (리스트/딕셔너리): 리스트 요소 접근 및 딕셔너리 활용.  
추천 백준: 10817번(세 수), 2562번(최댓값)  
간단한 알고리즘: 1차원 배열 활용, 기본 탐색.  
추천 백준: 1463번(1로 만들기 - 기초 DP)   


2. 정보처리실기 파이썬 시험 특징
출제 형식: 코드를 보여주고 실행 결과를 적는 형식이 대부분입니다.  
주의사항: 대·소문자를 구분하며, 띄어쓰기(공백)와 줄바꿈이 정확해야 부분 점수 없이 정답 처리됩니다.  
난이도: 프로그래밍 언어 활용(Python, C, Java) 파트에서 약 27% 내외로 출제되며, 기초 문법을 알고 있으면 풀 수 있는 수준입니다.   


3. 학습 팁
YouTube - 이기적 정보처리기사 실기 Python 등 영상 강의를 통해 빈출 유형을 파악합니다.  
백준 브론즈(Bronze) 등급의 문제를 파이썬으로 꾸준히 풀며 기본 문법에 익숙해지는 것이 중요합니다.  
https://youtu.be/DkgiPJczxJk  
