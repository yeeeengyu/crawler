# HOW TO USE UV - UV 사용법

## 1. install uv - uv 설치
```pip install uv```
### installation check - 설치 확인
```uv --version```

## 2. synchronize dependencies - 의존성동기화
```uv sync```
- 오류시 pyproject.py 파일 유무 확인
- 없으면안댐
## 3. 가상환경 활성화
- Windows / Powershell

    ```source ./.venv/Scripts/activate```

    안되면 ```source ./.venv/Scripts/activate.ps1```
- Mac / Bash

    ```source ./.venv/bin/activate```