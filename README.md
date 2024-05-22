# Camera Management Services

## Code patterns
1. Please see [HERE](https://docs.google.com/document/d/1PcPYR32B2S5YPrsAKrCcrEkeksQUY799q_cD4rKN3Xs/edit?usp=sharing)
## Getting Started
1. Clone the repository from github.com: `git clone https://github.com/optimuskonboi/Code-Base-Django-Rest-Framework.git`.
2. Navigate to the repository folder: - `cd Code-Base-Django-Rest-Framework`
3. Run requirements.txt - `pip3 install -r requirements.txt`
4. Run the Application - `python3 manage.py runserver`
5. Go to - http://localhost:8000/
6. Swagger - http://localhost:8000/testswagger/

### Restore Database with file: test.sql

### Change Database Credentials with your Database - `config/settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'your_database_name', # example - blog_data
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '80',
    }
}
```

### Creating an App
1. Create a folder with the app name in `apps`. For example: `testService`
1. Run `python manage.py startapp testService apps/testService` from the root directory of the project.

## Scope
- Goal: Develop a structure for both `django-rest-framework` and `django` projects.

## Project Tree
```bash
Camera-Management-Microservice
├── apps
├── authenticatorServices
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   └── v1
    │       ├── admin.py
    │       ├── serializers.py
    │       ├── services.py
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
    ├── testService
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   └── v1
    │       ├── admin.py
    │       ├── serializers.py
    │       ├── services.py
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
    ├── healthcheck
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   └── v1
    │       ├── admin.py
    │       ├── serializers.py
    │       ├── services.py
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
│   └── logManagementMicroservice
│       └── __init__.py
├── common
│   ├── generics.py
│   └── mixins.py
├── config
│   ├── asgi.py
│   ├── config.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py

├── README.md
├── requirements.txt
```

## Rationale
Each `app` should be designed in way to be plug-able, that is, dragged and dropped
into any other project and it’ll work independently.

### `apps`
* A mother-folder containing all apps for our project. Congruent to any JS-framework's `src` folder.
* An app can be a django template project, or an API.

### `api`
* We like to place all our API components into a package within an app called
`api`. For example, in this repository it's the `example_api/api` folder. That allows us to isolate our API components in a consistent location. If
we were to put it in the root of our app, then we would end up with a huge list
of API-specific modules in the general area of the app.

For projects with a lot of small, interconnecting apps, it can be hard to hunt
down where a particular API view lives. In contrast to placing all API code
within each relevant app, sometimes it makes more sense to build an app
specifically for the API. This is where all the serializers, renderers, and views
are placed. Therefore, the name of the app should reflect its API version

### `api-versioning`
It might often be necessary to support multiple versions of an API throughout the lifetime of a project. Therefore, we're adding in support right from the start.

**For different API versions, we're assuming the following will change**:
- Serializers
- Views
- URLs
- Services

`model`s can be thought of as shared between versions. Therefore, migrating changes should be versioned carefully without breaking different versions of the API.

### `config`
* Contains project configuration files, including the primary URL file
* As environment specific variables will be handled using environment variables, we've deemed it unnecessary to have separate settings files.

### `deployments`
* Contains Docker, Docker-Compose and nginx specific files for deploying in different
environments

### `documentation`
* We’ll have CHANGELOG.md
* We’ll have CONTRIBUTING.md
* We’ll have deployment instructions
* We’ll have local startup instructions

### `services`
* We’ll be writing business logic in services instead of anywhere else.

### `gitignore`
* https://github.com/github/gitignore/blob/main/Python.gitignore
