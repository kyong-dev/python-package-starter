# Python Package Starter

<br />

## How to use

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

<br />

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

<br />

## Test Deployment

정식 버전을 PyPi에 업로드 하기 전에 TestPyPi에 업로드해 테스트 해볼 수 있습니다. <br />
[Test PyPi](https://test.pypi.org/) 는 PyPi와 별개의 데이터 서버를 이용 중이기 때문에 따로 가입해줘야 한다.

정식 버전 업로드 하는 방식과 비슷하지만 마지막 업로드하는 명령어가 다르다.
```python
twine upload --repository-url https://test.pypi.org/legacy/ dist/package-0.1.0-py3-none-any.whl
```

업로드가 완료되면 업로드된 링크가 출력됩니다.

<br />

## Override

PyPi 서버에 이미 업로드 하여 fixed된 버전은 덮어 씌우거나 재업로드 할 수 없습니다. 하지만, 빌드 넘버를 추가 하여 같은 버전을 사용하되 다른 패키지 빌드를 업로드 할 수 있습니다.

```python
twine upload dist/package-0.1.0-1-py3-none-any.whl
twine upload dist/package-0.1.0-2-py3-none-any.whl
```


