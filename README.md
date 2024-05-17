# Camera Management Services

## Code patterns
1. Please see [HERE](https://docs.google.com/document/d/1PcPYR32B2S5YPrsAKrCcrEkeksQUY799q_cD4rKN3Xs/edit?usp=sharing)
## Getting Started
1. Run the project using `python manage.py runserver` and you should see the success page URL provided in terminal.


### Creating an App
1. Create a folder with the app name in `apps`. For example: `poll_api`
1. Run `python manage.py startapp poll_api apps/poll_api` from the root directory of the project
1. Modifing `apps/poll_api` to have the same structure like `apps/example_api`.

## Scope
- Goal: Develop a structure for both `django-rest-framework` and `django` projects.

## Project Tree
```bash
Camera-Management-Microservice
├── apps
│   ├── cameraManagementMicroservice
│   │   ├── districtServices
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations
│   │   │   ├── models.py
│   │   │   └── v1
│   │   │       ├── admin.py
│   │   │       ├── serializers.py
│   │   │       ├── services.py
│   │   │       ├── tests.py
│   │   │       ├── urls.py
│   │   │       └── views.py
│   │   └── nationServices
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── __init__.py
│   │       ├── migrations
│   │       │   ├── __init__.py
│   │       ├── models.py
│   │       └── v1
│   │           ├── admin.py
│   │           ├── __init__.py
│   │           ├── migrations
│   │           │   └── __init__.py
│   │           ├── serializers.py
│   │           ├── services.py
│   │           ├── tests.py
│   │           ├── urls.py
│   │           └── views.py
│   ├── __init__.py
│   ├── logManagementMicroservice
│   │   └── __init__.py
│   ├── userManagementMicroservice
│   │   └── __init__.py
│   └── warningManagementMicroservice
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
├── deployments
│   ├── django-project
│   │   └── Dockerfile
│   ├── docker-compose.yml
│   └── nginx
│       ├── default.conf
│       └── Dockerfile
├── docs
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── deployment.md
│   ├── local-development.md
│   └── swagger.yaml
├── entrypoint.sh
├── logs
├── manage.py
├── media
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements
│   ├── common.txt
│   ├── development.txt
│   ├── local.txt
│   └── production.txt
├── scripts
└── static
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
