# MeLearningDjangoRest
Me learning Django REST framework

## Planned folder structure
src/
├── manage.py
│
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── pools/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py


## REST API

## Specification - breakdown into REST API
 `Logs user into the system`
 >POST auth/login

`Logs user out from the system`
>POST auth/logoff

`Gets the list of the files of the organization` - org is a paramer, because it's a filter of the collection. 
                                                 - Nesting would make this complex, because potential m2m relationsship
GET files?organizationId={org_id}

`Gets the list of the files of the user`
GET files?userId={user_id}

`Downloads the file`
GET files/{file_id}

`Uploads a file`
POST files/upload

## Specification - breakdown into db/model
  model:
    - user:
      -- org_id
      -- username etc
      -- auth_mechanism

    - org
      -- name

    - file
      - org_id
      - user_uploader_id
      - blob
      - download_count
      - uploaded_at
      - downloaded_at

    - log
      - model: [file/org/user] (string)
      - event: [upload/download/login/logoff] (string)
      - timestamp: (date)

## Specification - breakdown1
### breakdown 1.1.
  - Django & Django REST
    - Database, by your own choice
  - login/logout
  - session auth/token
  - users and files belong to an organization
  - files belongs to the uploader's organization
  - upload/download
    - download: incl. timestamp
  - track:
    - download_count by file
    - download_count by org

### breakdown 1.2.
[-] Please write a web application that provides a REST API for logged-in users to upload and download any kind of files.
[-] The users must be able to login and logout. 
[-] Use either token or session authentication (hint: use the user model and authentication mechanism provided by django). 
[-] Each user and file must belong to an organization. 
[] Once uploaded, the file must belong to the same organization as the user who uploaded it.
[] There is no need to implement CRUD endpoints for users or organizations, those can be created by running a script.
[-] Users should see and be able to download any of the uploaded files from any organization. 
[] Write an endpoint for listing all the files that belong to one organization, and an endpoint for listing all the file downloads done by one user. 
[] Include timestamps when the file was uploaded and when the user downloaded a file.
[] Keep track of how many times each file has been downloaded, and how many total file downloads each organization has (number of all file downloads from that organization).
[] Include the number of downloads when listing files and organizations.
[] Use Django and Django REST Framework (https://www.django-rest-framework.org/). You can use a database of your choice.
[] Implementing a simple UI is a bonus.


## Specification
Please write a web application that provides a REST API for logged-in users to upload and download any kind of files.
The users must be able to login and logout. Use either token or session authentication (hint: use the user model and authentication mechanism provided by django). 
Each user and file must belong to an organization. Once uploaded, the file must belong to the same organization as the user who uploaded it.
There is no need to implement CRUD endpoints for users or organizations, those can be created by running a script.
Users should see and be able to download any of the uploaded files from any organization. Write an endpoint for listing all the files that belong to one organization, and an endpoint for listing all the file downloads done by one user. Include timestamps when the file was uploaded and when the user downloaded a file.
Keep track of how many times each file has been downloaded, and how many total file downloads each organization has (number of all file downloads from that organization). Include the number of downloads when listing files and organizations.
Use Django and Django REST Framework (https://www.django-rest-framework.org/). You can use a database of your choice.
Implementing a simple UI is a bonus.


### Some notes
1.	There should be no need to run makemigrations. The auto-generated files should be committed.
2.	Python dependencies (requirements.txt) should be committed as well, so that they stay the same.
3.	You are right that using the built-in Group as the organization model might get difficult. Consider implementing a model for the organization?
4.	Try to keep the coding style coherent and avoid uninformative comments in the code. For example, class names are now using different naming styles.
5.	User input must always be validated. You can use django-restframework's serializers to achieve this.
6.	Maybe re-think how useful the helper classes under common utils are and how they are used.
7.	As mentioned above, use django-restframework.
