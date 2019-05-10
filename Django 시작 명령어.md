## Django commands

1. 파이썬 설치

   ```
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   exec "$SHELL"
   
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   exec "$SHELL"
   
   pyenv install 3.6.7
   pyenv global 3.6.7
   python -V #확인
   ```

   

2. 폴더생성

   ```
   mmkdir [프로젝트 이름]
   cd [프로젝트 이름]
   ```

3. 가상환경 생성

   * 가상환경 생성 (1)

     ```
     pyenv virtualenv 3.6.7 [가상환경 이름]-venv
     ```

   * 가상환경 삭제

     ```bash
     pyenv uninstall [가상환경 이름]
     ```

   * 가상환경 목록

     ```
     pyenv versions
     ```

   * 현재 폴더에 가상환경 활성화 (2)

     ```
     pyenv local [가상환경 이름]-venv
     ```

   * 현재 폴더에 활성화된 가상 환경 비활성화

     * ```.python-version``` 파일을 찾아 삭제한다.

4. djngo 프로젝트

   * django 설치 (3)

     ```
     pip install django
     pip install django==2.1.8
     ```

   * startproject (4)

     ```
     django-admin startproject [프로젝트 이름] .
     ```

   * start app (5)

     ```
     python manage.py startapp [pages(앱 이름)]
     ```


   * pages 안에 templates 폴더만들기

4. settings

   * 28번째줄 '[playground]-hyeonjin23.c9users.io' 입력 후 실행하여 로켓 확인 (프로젝트만들자마자 바로)

     ```bash
     python manage.py runserver $IP:$PORT
     ```

     

   * startapp 이후  settings 40번째줄 (앱 만든 후)

     ```python
     'pages(앱 이름).apps.[Pages]Config',
     ```


5.  migration

   * make migration

     ``` bash
     python manage.py makemigrations
     ```

   * db 적용

     ```bash
     python manage.py migrate
     ```

6. admin

   * 계정설정

     ```bash
     python manage.py createsuperusers
     ```

   * admin.py에 적용

     ```python
     from.model import Pages
     ```

   * models.py에 오버라이드(자신의 이름을 직접 쓴다)

     ```pytho
     def __str__(self):
     	return self.name 
     ```

     

7. windows에 setting

   cmd 이용

   ```bash
   1. api-venv\Scripts\activate.bat 가상환경 활성화
   	deactivate 가상환경 종료
   
   2. pip install django
   
   3. django-admin startproject 프로젝트이름 .
   
   4. python manage.py runserver 실행
   
   5. localhost:8000
   ```

   