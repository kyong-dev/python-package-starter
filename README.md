## Python Package Starter

### How to use

- 'package' 폴더의 이름을 변경하세요.
- 'module.py' 파일명을 알맞게 변경하세요.
- 아래 패키지들을 설치해주세요.
```bash
pip install wheel && pip install twine
```
- whl파일(패키지 빌드)을 생성 하기 위해 아래 명령어를 입력해주세요.
```python
python setup.py bdist_wheel
```
- build, dist, .egg-info 세 폴더가 생성되었을 겁니다.
- 그 중 dist 폴더 안에 생성된 패키지 빌드 파일을 업로드 하기 위해 명령어를 입력합니다.
```python
twine upload dist/package-0.1.0-py3-none-any.whl
```
- username / password에 PyPi 로그인정보를 입력하면 된다.

## How to Update Version

- setup.py의 버전정보를 수정한다.
- init.py의 버전정보를 수정한다.
- 변경된 사항을 적용해 패키지 빌드를 한다.
```python
python setup.py bdist_wheel
```
- 생성된 파일을 업로드 한다.
```python
twine upload dist/package-0.2.0-py3-none-any.whl
```

## Edition

## Test Deployment