# Личный кабинет репетитора
 
Электронный органайзер репетитора для обработки информации об учениках, расписании и материалов к урокам.

### Использованные технологии:




![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/FlyingJackson/TutorOffice
```

```
cd  TutorOffice
```

Для управления зависимостями и сборкой пакетов установить Poetry

```
Установка на OSX и Linux
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Установка на Windows
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

Установка через менеджер пакетов pip
pip install --user poetry
```
Установить зависимости
```
poetry install 
```
Выполнить миграции
```
python manage.py makemigrations
```

```
python manage.py migrate
```


Запустить проект:

```
python manage.py runserver
```

### Описание моделей:

Модель Subject

```
class Subject:
    """
    Модель для предметов, преподаваемых учителями.
    """
    Поля:
    title - название предмета
    (текстовое поле с максимальной длиной 30, уникальным значением,
     индексируемое)
```



Модель Пользователей (User, Teacher, Student):

```
class User(AbstractUser):
    """
    Базовая модель для описания ученика и учителя.
    """
    Поля:
    
    id - первичный ключ
    (UUIDField поле, уникальное, неизменяемое)
       
    first_name - имя пользователя
    (обязательное текстовое поле с длиной от 2 до 50 символов)
    
    last_name - фамилия пользователя
    (обязательное текстовое поле с длиной от 2 до 50 символов)
        
    email - электронная почта
    (обязательное уникальное EmailField поле с длиной от 7 до 50 символов)
   
    phone - телефон
    (обязательное уникальное текстовое поле с длиной от 10 до 20 символов)
    
    email_verify - подтверждение электронного адреса
    (Булево поле со значением по умолчанию 'False')
     
    photo - фотография пользователя
    (необязательное поле ImageField)
    
    Сортировка по фамилии и имени.
    
    
    class Student:
    """
    Расширение модели User для модели Студента
    """
    
    profile - профайл
    (связь OneToOneField)
    
    
    class Student:
    """
    Расширение модели User для модели Студента
    """
    
    profile - профайл
    (OneToOneField связь с таблицей User)
    
    class Teacher:
    """
    Расширение модели User для модели Учитель
    """
    profile-профайл
    (OneToOneField связь с таблицей User)
                                   
    students-связь с таблицей Students
    (ManyToManyField связь через таблицу TeacherStudent)
    
    subjects - связь с таблицей Subjects
    (ManyToManyField)
    
    class TeacherStudent:
    """
    Модель-связь преподавателя со студентом.
    Предоставляет возможность самостоятельной регистрации ученика учителем.
    """
    teacher - связь с таблицей Teacher 
    (ForeignKey)
    student - связь с таблицей Student
    (ForeignKey)
        
    first_name - имя пользователя
    (обязательное текстовое поле с длиной от 2 до 50 символов)
    
    last_name - фамилия пользователя
    (обязательное текстовое поле с длиной от 2 до 50 символов)
    
    email - электронная почта
    (обязательное уникальное EmailField поле с длиной от 7 до 50 символов)
    
    email_verify - подтверждение электронного адреса
    (Булево поле со значением по умолчанию 'False')
     
    comment - комментарий учителя
    (обязательное текстовое поле)

```
Materials
```
p 
```
Homeworks
```
p
```

```
p
```


Lessons

```
p
```



### Заголовок:


```      

```



### Эндпойнты:

AUTH


```
/api/v1/auth/signup/
Регистрация нового пользователя
Получение кода подтверждения на переданный email.

{
  "email": "string",
  "username": "string"
}

/api/v1/auth/token/
Получение JWT-токена в обмен на username и confirmation code.
{
  "username": "string",
  "confirmation_code": "string"
}

```
LESSONS
```
/api/v1/

```
MATERIALS
```

```
HOMEWORKS
``````


``````

``````

USERS
```
/api/v1/users/
Получение списка всех пользователей
Права доступа: Администратор

Добавление пользователя
Права доступа: Администратор
Поле email  должны быть уникальными.
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
} 
/api/v1/users/{username}/
Получение пользователя по username
Изменение данных пользователя по username
Удаление пользователя по username
Права доступа: Администратор

/api/v1/users/me/
Получить данные своей учетной записи
Изменить данные своей учетной записи
Права доступа: Любой авторизованный пользователь
``````
```
```

### Алгоритм регистрации пользователей:
```
1. Пользователь отправляет POST-запрос на добавление нового пользователя 
с параметрами email и username на эндпоинт /api/v1/auth/signup/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и
confirmation_code на эндпоинт /api/v1/auth/token/,
 в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и
 заполняет поля в своём профайле (описание полей — в документации).
 Размещение, получение, редактирование постов
```


### Пусть работа репетитора станет удобней!