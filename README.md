# 인공지능

- 사람처럼 판단, 예측, 추천, 생성하는 기술 전체
- 챗봇, 음성인식, 자율주행, 이미지 생성, 추천 시스템

`전체 구조`

```
인공지능(Artificial Intelligence)                  사람처럼 판단/예측.추천하려는 전체 분야
 └── 머신러닝(Machine Learning)                    데이터를 통해 규칙(패턴)을 학습하는 방법
      ├── 지도학습(Supervised Learning)            정답(Label)이 있는 데이터를 학습하는 방식
      │     ├── 분류(Classification)               정답이 카테고리인 문제
      │     └── 회귀(Regression)                   정답이 숫자인 문제
      │
      ├── 비지도학습(Unsupervised Learning)        정답(label) 없이 데이터 패턴만 찾는 방식
      │
      └── 딥러닝(Deep Learning)                    머신러닝 중에서 신경망을 깊게 쌓은 방식
            ├── CNN(Convolutional Neural Network)  이미지 처리에 특화된 딥러닝 모델
            ├── RNN(Recurrent Neural Network)      순서(sequence) 데이터 처리 모델. 자연어/시계열
            └── Transformer                        현재 AI의 핵심 구조. 문장 안에서 중요한 단어끼리 관계를 학습
```

## AI 분야

### 데이터 분석가 트랙

```
수집
→ SQL
→ Pandas
→ 시각화
→ 머신러닝
```

### AI 엔지니어 트랙

```
데이터
→ 딥러닝
→ 모델 학습
→ API 서버
→ 배포
```

### 생성형 AI 엔지니어 트랙

```
문서 수집
→ 임베딩
→ 벡터DB
→ LLM
→ RAG
→ AI Agent
```

### 배포 / MLOps

```
모델 학습
→ API 서버화
→ Docker
→ Kubernetes
→ 모니터링
```

## AI 엔지니어 로드맵

현재 AI 업계에서는 특히 Hugging Face와 Transformer 생태계의 중요성이 매우 커지고 있습니다.
Hugging Face가 중요한 이유는 최근 AI 산업은 Transformer, 생성형 AI, LLM 중심으로 움직입니다.

### 1단계 — 프로그래밍 기초(Python)

- 변수, 조건문, 반복문
- 함수
- 배열(List), 딕셔너리(Dictionary)
- 파일 읽기/쓰기
- 예외처리
- 객체지향 기초

### 2단계 — 웹/DB 기초

- backend: REST API servier(FastAPI, Node.js)
- frontend: Vue.js,react.js

### 3단계 — 데이터 분석 기초

- NumPy
- Pandas
- Matplotlib
- AI API

`Kaggle `

- 데이터 연습
- 타이타닉/회귀 실습

### 4단계 — 머신러닝

- scikit-learn

### 5단계 — 딥러닝

- 모델 개발
- TensorFlow → 딥러닝 프레임워크
- Keras → TensorFlow 프레임워크위에서 딥러닝 모델 만드는 라이브러리

### 6단계

- Hugging Face → 생성형 AI 모델 플랫폼. 생성형 AI의 GitHub

### 7단계

RAG + AI 서비스 개발

### 8단계

AI 서비스 배포 FastAPI + Docker

## AI 도구

### 1. 데이터 수집/크롤링

| 도구                | 역할            |
| :------------------ | :-------------- |
| Beautiful Soup HTML | 파싱            |
| Scrapy              | 대규모 크롤링   |
| Selenium            | 브라우저 자동화 |

### 2. SQL / 데이터베이스

AI에서도 SQL은 매우 중요합니다.

| 도구       | 역할             |
| :--------- | :--------------- |
| MySQL      | 관계형 DB        |
| PostgreSQL | 데이터 분석 강점 |
| MongoDB    | 문서형 DB        |
| Redis      | 캐시/세션        |

### 3. 데이터 분석/전처리

가장 먼저 배우는 영역입니다.

| 도구       | 역할              |
| :--------- | :---------------- |
| NumPy      | 수학/행렬 계산    |
| Pandas     | 데이터프레임 처리 |
| Seaborn    | 통계 시각화       |
| Matplotlib | 기본 그래프       |
| Plotly     | 인터랙티브 그래프 |

여기서 배우는 것:

- 결측치 처리
- 이상치 탐지
- 데이터 시각화
- 상관관계 분석
- EDA(탐색적 데이터 분석)

### 4. 머신러닝

전통적인 AI 모델 단계입니다.

| 도구         | 역할                     |
| :----------- | :----------------------- |
| scikit-learn | 머신러닝 표준 라이브러리 |
| XGBoost      | 강력한 부스팅 모델       |
| LightGBM     | 빠른 대용량 학습         |
| CatBoost     | 범주형 데이터 강점       |

여기서 배우는 것

- 회귀분석
- 분류
- 군집화
- 모델 평가
- Feature Engineering

### 5. 딥러닝

- 신경망 기반 AI입니다.
- 딥러닝 모델을 만드는 도구

| 도구               | 역할                   |
| :----------------- | :--------------------- |
| Keras              | 쉬운 딥러닝.           |
| TensorFlow         | 구글 딥러닝 프레임워크 |
| **PyTorch** :star: | 연구·실무 인기         |
| TorchVision        | 이미지 처리            |

### 6. 생성형 AI / LLM

최근 가장 중요한 분야입니다.

| 도구         | 역할          |
| :----------- | :------------ |
| Hugging Face | 모델 허브     |
| Transformers | LLM 사용      |
| LangChain AI | 앱 개발       |
| LlamaIndex   | 문서 기반 AI  |
| OpenAI API   | GPT 사용      |
| Ollama       | 로컬 LLM 실행 |

여기서 배우는 것

- 프롬프트 엔지니어링
- RAG
- 벡터DB
- AI 챗봇
- AI Agent

### 7. 벡터 DB / AI 검색

RAG에서 중요합니다.

| 도구     | 역할             |
| :------- | :--------------- |
| Chroma   | 간단한 벡터DB    |
| FAISS    | 고속 유사도 검색 |
| Milvus   | 대규모 벡터DB    |
| Pinecone | 클라우드 벡터DB  |

### 8. 개발 환경

| 도구               | 역할                         |
| :----------------- | :--------------------------- |
| Jupyter Notebook   | 데이터 분석 실습             |
| Google Colab       | 무료 GPU                     |
| Visual Studio Code | 개발 IDE                     |
| Kaggle             | 데이터 분석/AI 학습용 플랫폼 |

### 9. 배포 / 백엔드

AI 모델을 서비스화할 때 사용합니다.

| 도구       | 역할        |
| :--------- | :---------- |
| FastAPI AI | API 서버    |
| Flask      | 간단한 서버 |
| Docker     | 컨테이너    |
| Kubernetes | 대규모 운영 |

### 10. 클라우드 / MLOps

실무에서 매우 중요합니다.

| 도구                | 역할              |
| :------------------ | :---------------- |
| Amazon Web Services | AWS 클라우드      |
| Google Cloud        | GCP               |
| Microsoft Azure     | Azure             |
| MLflow              | 실험 관리         |
| Airflow             | 데이터 파이프라인 |

`배워야할 것`

```
지도학습
  - 회귀
  - 분류

알고리즘
  - 선형회귀
  - 로지스틱 회귀
  - 의사결정트리
  - 랜덤포레스트
  - XGBoost

라이브러리
  - scikit-learn

실습프로젝트
  - 고객 이탈 예측
  - 스팸메일 분류
  - 영화 추천 시스템
  - 중고차 가격 예측
  - 신용카드 이상거래 탐지
```

`서비스 예시`

- 유투브 추천 : 머신러닝 + 딥러닝
- ChatGPT : Transformer 기반 LLM
- 자율주행 : CNN + Transformer
- 주가예측 : RNN/LSTM + Transformer

`방식`

```
학습(Training)   -> 모델 생성  -> 추론(Inference)  -> 실제 예측 서비스
```

### 실무에서 어떻게 이어지는가

예: 쇼핑몰 추천 시스템

```
데이터 수집 -> 머신러닝/딥러닝 모델 학습 -> 사용자 행동 패턴 학습 -> 추론 단계에서 추천 수행
```

예: 집값 예측

```
회귀 모델 학습 -> 새 집 정보 입력 -> 가격 추론
```

예: 스팸 메일

```
분류 모델 학습 -> 메일 입력 -> 스팸 여부 추론
```

### 기타

- 자바문법과 비교
- 정보처리 기출문제
