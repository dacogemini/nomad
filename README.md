# NOMAD TRAVEL SITE 
![alt text](https://lh3.googleusercontent.com/7jjl6pispPrb4ggjm6y2kWL0zZVyqMC9nkYstLh4KPoZtBW-0MJj0m7FyYUt64H7O3ZmkUwNYRRyepkTZvFXMd7lFh5_AdZ3qzGFo7pVUJSKexLLr0MJavK4jLjnts0B8OorCVh6yQ=w100
 "created by Dan Collins")
 
 #### INSTALLATION INSTRUCTIONS:
* Clone the repo https://github.com/dacogemini/nomad.git 

* Run Postgres

* Navigate to root directory and in the bash terminal run <code>python manage.py runserver</code>


### TECHNOLOGIES USED

What Technologies Are We Using?
The backend application is written in <b>Python</b>, using the <b>Django</b> framework and <b>djangoadmin</b>. The frontend application is written in <b>Javascript/HTML5</b>, <b>Jinja</b> templating and <b>SASS</b> & <b>Bootstrap</b> for styling.<br /><br />


<img src="https://lh3.googleusercontent.com/KW52L5UnrHTD81gLX1P94EIyGCYMfv2GjzYFAaRCCphZT-28h5MuA4NmMKLqbLN9nKprWlDG6xNUgcO8YRq4XH4LVZkcKozH4n0572h94_YI9DKsQVpTcOSIepK1Y5uelGIF1UmQrw=w110" align="left"/>  

<img src="https://lh3.googleusercontent.com/ul6Mw0hdKF6n4zlydwxMe5QzvgIDuz1U25SOKhZdOviVeayTFv7DVsTT05zk2clHYOPtwQkTrmYX95wbHBaWBtPvLJFBOBPNNOzB9EY1HWRBPcXE2JtRSu0PQnIU_4HkktD-O1PMSg=w75" align="left"/>

<img src="https://lh3.googleusercontent.com/hmFsU1gVh-71pDq6k3Wkc8fRkmAfd1rXTsPE_6Cuclx3-2mz-EIQw6YGT4FHlyArnjmUmOJGdRZsDeWp4cV4h2o_J9HSQbrKCbctSmx_lQGWd2RQqWAv887kc-Npelj1q11yQEdT-g=w80" align="left"/>

![sass icon](https://lh3.googleusercontent.com/KuEWejhj2GaiP7nNmkKGR3Zh9OCBnY5V4tZgAxCYiH4T3pCTugLTqyC-uzKHQf1VSSgKgb9a9Oa5w4WO1Dz94FTXlWKhcIQB-fh37ltQMb-_ysPEBnWLAl1kIME2FM67Q6OQrXmJow=w100
 "SASS")
 
<br />

#### PRODUCTION/DEPLOYMENT

<br />

![digital-ocean icon](https://lh3.googleusercontent.com/Ow1fBW7wqb4bdJVRVVeiY9YAqP5ZurB9qOLbMWKYZK58cfMiXpWV446sLp4vJOUBg2js5No6G7YZPEWdQxji618yOJkoYc97Bs_jv7LiE7wxvJteQa36WRrIciuuFQgnNqqHRj5vOg=s80-p-k
 "Digital-Ocean") &nbsp;
![gunicorn icon](https://lh3.googleusercontent.com/9MmL-4BgOySjRwvHXJJ2L0ghS6RzAma1eoZdHldxiBsz40wUaxXgXcvKCKFFW9Ll1MBjo4xY7F4-fOgBkWplAb9TM-_JfAeNajCWESK5NmfqLr82y8S5FVtywqzBgoKR5I20-qNPpw=w200
 "Gunicorn") &nbsp;
 ![nginx icon](https://lh3.googleusercontent.com/NiSdIZ9C1oFvwal7MJtzM2MVy9TUvgXiHhkbaXQV-FsZMA0AWcx2CxldSKgJEE7eyUjOldQzYn85Ya1WWyGoJ7RS6GvXMAWeWrV-SKFW0gkNDDNgkmG2cCH05CVXSVuvhs16SHod9w=w170
 "Nginx") 

#### BACKEND PACKAGES

If you need to add new packages to the backend app, you can use Pipenv to do so:

```pipenv install <package_name>```

Here are the existing packages already in use:

- Django: A full-featured web framework for Python
- Gunicorn: A WSGI HTTP server used to serve the app.
- NGINX: A buffering reverse proxy server for gunicorn.
- Waitress: NOTE: if you are not using a buffering reverse proxy like Nginx, we recommend you use Waitress.
- psycopg2: A PostgreSQL adapter for Python.
- pillow: Image manipulation on the server.




