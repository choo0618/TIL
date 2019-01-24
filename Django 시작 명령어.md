## Django commands

1. 폴더생성

   ```
   mmkdir [프로젝트 이름]
   cd [프로젝트 이름]
   ```

2. 가상환경 생성

   * 가상환경 생성

     ```
     pyenv virtualenv 3.6.7 [가상환경 이름]
     ```

   * 가상환경 삭제

     ```bash
     pyenv uninstall [가상환경 이름]
     ```

   * 가상환경 목록

     ```
     pyenv versions
     ```

   * 현재 폴더에 가상환경 활성화

     ```
     pyenv local [가상환경 이름]
     ```

   * 현재 폴더에 활성화된 가상 환경 비활성화
     * ```.python-version``` 파일을 찾아 삭제한다.

3. djngo 프로젝트

   * django 설치

     ```
     pip install django
     ```

   * startproject

     ```
     django-admin statproject [프로젝트 이름] .
     ```

   * start app

     ```
     python manage.py startapp [앱 이름]
     ```

     

