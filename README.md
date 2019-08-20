# NOMAD TRAVEL SITE
![alt text](https://lh3.googleusercontent.com/DXS4kn3fgbwpq7C6crOJou2xqhudc_pD730UrHCAZRP3c68zbiaU8va8BJ5ujhf0xPjVgWUz6KbGuTKiWy3NYt0oVMrKkvrDuQAgqGspgO1g-utGMVHQN18kx2n7qoqnPREeXcRgPA=s150-p-k
 "created by Dan Collins")
 
 ### STEPS

* Clone the repo https://github.com/dacogemini/nomad.git 

* Run Postgres

* Navigate to root directory and in the bash terminal run <code>python manage.py runserver</code>


### TECHNOLOGIES USED

What Technologies Are We Using?
The backend application is written in <b>Python</b>, using the <b>Django</b> framework and Djangoadmin. The frontend application is written in <b>Javascript/HTML5</b>, <b>Jinja</b> templating and <b>SASS</b> & <b>Bootstrap</b> for styling. 


<img src="https://lh3.googleusercontent.com/KW52L5UnrHTD81gLX1P94EIyGCYMfv2GjzYFAaRCCphZT-28h5MuA4NmMKLqbLN9nKprWlDG6xNUgcO8YRq4XH4LVZkcKozH4n0572h94_YI9DKsQVpTcOSIepK1Y5uelGIF1UmQrw=w110" align="left"/>  

<img src="https://lh3.googleusercontent.com/ul6Mw0hdKF6n4zlydwxMe5QzvgIDuz1U25SOKhZdOviVeayTFv7DVsTT05zk2clHYOPtwQkTrmYX95wbHBaWBtPvLJFBOBPNNOzB9EY1HWRBPcXE2JtRSu0PQnIU_4HkktD-O1PMSg=w80" align="left"/>

<img src="https://lh3.googleusercontent.com/hmFsU1gVh-71pDq6k3Wkc8fRkmAfd1rXTsPE_6Cuclx3-2mz-EIQw6YGT4FHlyArnjmUmOJGdRZsDeWp4cV4h2o_J9HSQbrKCbctSmx_lQGWd2RQqWAv887kc-Npelj1q11yQEdT-g=w80" align="left"/>

![sass icon](https://lh3.googleusercontent.com/KuEWejhj2GaiP7nNmkKGR3Zh9OCBnY5V4tZgAxCYiH4T3pCTugLTqyC-uzKHQf1VSSgKgb9a9Oa5w4WO1Dz94FTXlWKhcIQB-fh37ltQMb-_ysPEBnWLAl1kIME2FM67Q6OQrXmJow=w100
 "SASS")

<hr />

### PRODUCTION/DEPLOYMENT
<br />

![gunicorn icon](https://lh3.googleusercontent.com/9MmL-4BgOySjRwvHXJJ2L0ghS6RzAma1eoZdHldxiBsz40wUaxXgXcvKCKFFW9Ll1MBjo4xY7F4-fOgBkWplAb9TM-_JfAeNajCWESK5NmfqLr82y8S5FVtywqzBgoKR5I20-qNPpw=w200
 "Gunicorn")
 
 ![digital-ocean icon](https://lh3.googleusercontent.com/Ow1fBW7wqb4bdJVRVVeiY9YAqP5ZurB9qOLbMWKYZK58cfMiXpWV446sLp4vJOUBg2js5No6G7YZPEWdQxji618yOJkoYc97Bs_jv7LiE7wxvJteQa36WRrIciuuFQgnNqqHRj5vOg=s100-p-k
 "Digital-Ocean")

If you need to add new packages to the backend app, you can use Pipenv to do so:

```pipenv install <package_name>```
Here are the existing packages already in use:

Django: A full-featured web framework for Python
djangorestframework: A library that provides an extensive toolset for using Django as a backend API for an SPA.
django-filter: Easy Django Queryset filtering from URL params
django-storages: Adapter for various storage backends.
django-model-utils: A set of composable models, managers, and fields that extend Django's functionality.
django-dotenv: A package for managing Django's environment variables from a .env file.
gunicorn: A WSGI HTTP server used to serve the app.
psycopg2: A PostgreSQL adapter for Python.
pyyaml: A YAML parser and emitter.
pendulum: A package that extends and improves on Python's default date and time handling.
django-heroku: A package that configures Django apps to run on a Heroku dyno.
djoser: A package that provides RESTful hooks for Django's auth system.
djangorestframework-simplejwt: Allows us to use JWTs to authenticate users.
pillow: Image manipulation on the server.
django-cors-headers: Override CORS headers errors in local development.
django-role-permissions: Manage user authorization and roles.



