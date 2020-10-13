# dcu-20-2-it
대구가톨릭대학교 - IT분석 및 서비스 기획 
[모질라 도서관 예제](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)
1. django install
2. Creating the catalog application 

## 1. django install
* [python install site](https://www.python.org/) 
  * PATH 설정 클릭
* [vscode install site](https://code.visualstudio.com/)
* pip install django
* html Snippets, Preview 추가

### 1.1 pip upgrade

```bash
$ python.exe -m pip install --upgrade pip
```
### 1.2 django install

```bash
$ pip install django
```

### 1.3 pip 목록 확인하기

```bash
$ pip list 
```

### 1.4 폴더생성하고 django-admin을 이용해서 프로젝트 생성

```bash
# 장고프로젝트를 생성할 폴더 생성
$ mkdir 내가사용하고자하는폴더이름
$ cd 내가사용하고자하는폴더이름

# 장고프로젝트 생성 
$ django-admin startproject 장고프로젝트이름
$ cd 장고프로젝트이름

# 장고프로젝트 실행하기
$ python manage.py runserver
```

<a>http://127.0.0.1:8000/</a> 에 들어가서 현재 자신의 local에 서버가 가동이 된 것을 확인한다.

### 1.5 장고프로젝트 생성한 폴더로 이동후에 vscode에서 작업

```bash
$ code . # code 즉 vscode를 현재 위치에서 작업을 하겠다. => 하고나면 vscode가 켜진다.
```

### 1.6 vscode에게 local pyhton의 위치를 알려줘야 실행이 가능하다.

### 1.6.1 cmd + shift + p 
* 위 명령어로 명령팔레트를 열고 python select interpreter 클릭해서 자신의 local python을 클릭한다.

## 2. Creating the catalog application
* The tool creates a new folder and populates it with files for the different parts of the application

```bash
$ python manage.py startapp catalog
```

### 2.1 Registering the catalog application
* 어플리케이션이 생성되었으니 프로젝트에 등록해야합니다. 
* 애플리케이션들은 프로젝트 설정 안에 INSTALLED_APPS 리스트에 추가함으로써 등록이 가능합니다.
* 여기서 catalog를 추가해줘야 한다.

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'catalog',
]
```

## 3. Specifying the database
* SQLite database 를 사용합니다.
* settings.py 에 설정해야 합니다.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## 4. Other project setting => TIME_ZONE
* TIME_ZONE , SECRET_KEY,  DEBUG 설정이 가능하다.

```bash
TIME_ZONE = 'Asia/Seoul'
```

## 5. Hooking up the URL mapper
* locallibrary/loccallibrary/urls.py 을 열어서 URL 맵퍼를 사용합니다.
* www.xxxx.com//catalog 로 시작되는 요청이 들어오면 catalog/urls.py를 참조해서 맵핑하겠다는 설정입니다.

```bash
# Use include() to add paths from the catalog application 
from django.conf.urls import include
from django.urls import path

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
```

### 5.1 catelog 사이트를 루트 URL(127.0.0.1:8000:/catalog/)로 리다이렉트 설정
* 마찬가지로 위와 같은 파일 하단에 입력해줍니다.

```bash
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url="/catalog", permanent=True)),
]
```

### 5.2 add config static files like CSS, JavaScript, Image

```bash
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 5.3 위의 urls.py 설정을 리스트 형태로 하나로 입력하기
* There are a number of ways to extend the urlpatterns list.

```bash
from django.contrib import admin
from django.urls import path
# Use include() to add paths from the catalog application 
from django.conf.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url="/catalog", permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 5.4 마지막으로 urls.py라는 파일을 catalog폴더 안에 생성

```bash
from django.urls import path
from catalog import views


urlpatterns = [
]
```

### 6. Testing the website framework
* 정상적으로 돌아가는지 테스트하기 전에 database migration을 해야한다.

### 6.1 Running database migrations
* 장고는 ORM(Object-Relational-Mapper : 객체-관계-매퍼)를 사용하여 장고 코드안에 있는 모델 정의(객체)를 기본 데이터베이스에서 사용하는 데이터 구조(관계형 DB)에 매핑합니다.
* makemigrations은 migrate전에 점검
* migrate는 migration을 실제로 DB에 적용

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Runnin the websites

```bash
python manage.py runserver
```

### 7.1 서버 실행 후 에러 => pages/urls를 정의하지 않아서 당연한 에러이다.





