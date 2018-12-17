# A simple Feedback Flask App

Welcome to **feedback** this is a simple **CRUD** Flask-app Rest-Plus API to complete a personal challenge, it's writted in python [Flask framework](http://flask.pocoo.org/ "Flask's official website") because it's cool for microservices, to data storage I am using [*postgreSQL*](https://www.postgresql.org/ "postgreSQL official website") a robust relational
DB.

¿now? 

## Time to install!

### Local SQLite Dev Version 

``` console
yugo@arkananetwork:~$ git clone https://github.com/ramses132/pedidosya-feedback.git <folder>

yugo@arkananetwork:~$ cd <folder>

yugo@arkananetwork:~$ export FLASK_APP=feedback.py

yugo@arkananetwork:~$ export FLASK_CONFIG=default

yugo@arkananetwork:~$ virtualenv -ppython3 venv && source ./venv/bin/activate

yugo@arkananetwork:~$ pip install requirements.txt

yugo@arkananetwork:~$ flask run

yugo@arkananetwork:~$ echo "Enjoy! : - )"
```

### Docker version

install [Docker CE](https://docs.docker.com/install/ "Docker official install guide") and [Docker Compose](https://docs.docker.com/compose/install/#install-compose "Docker Compose official install guide") (remember add ur user to docker group and restart session)

``` console
yugo@arkananetwork:~$ git clone https://github.com/ramses132/pedidosya-feedback.git <folder>

yugo@arkananetwork:~$ cd <folder>

yugo@arkananetwork:~$ docker-compose up --build

yugo@arkananetwork:~$ echo "[Contained Enjoy : - )]"

```

## Extras

I make a simple scrapper for swearwords because we will need a word black list 
to clean the reviews in the future it's make in [bonobo ETL](https://www.bonobo-project.org/ "Bonobo Project Official Site") and [Bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "BeautifulSoup Official Doc Site") 

Thanks for read! 
