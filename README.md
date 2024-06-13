# How To Install

가상환경 필수입니다.

## 1. pip 업그레이드, setuptools 설치
```python
$ pip install --upgrade pip
$ pip install setuptools
```

## 2. editable 모드로 패키지 설치
```python
$ pip install -e .[dev]
```

zsh은 `".[dev]"`로 지정

## 3. pre-commit hook 지정하기
```python
$ pre-commit run --all-files  # 잘 동작하는지 확인
$ pre-commit install
```
