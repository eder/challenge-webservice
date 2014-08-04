# Challenger Webservice

Challenger Webservice is an example Flask application illustrating some of my common practices

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [MySQL](http://www.mysql.com/)


It is strongly recommended to also install and use the following tools:

1. [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)
2. [Vagrant](http://vagrantup.com)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone git@github.com:eder/challenge-webservice.git
    $ cd challenger-webservice

#### 2. Create and initialize virtualenv for the project:
	$ sudo pip install virtualenv
    $ virtualenv challenge
    $ pip install -r requirements.txt

#### 3. Edit database connection
		config/migration.py
		$ engine = sqlalchemy.create_engine('mysql://root:12345@localhost/') # line 6
	 	$ app.config['SQLALCHEMY_DATABASE_URI']'mysql://root:12345@localhost/challengeWebservice_development line 10

#### 4. Upgrade the database:

    $ cd config/

#### 5. Database Migrations
	$ python migration.py db init
	$ python migration.py db migrate
	$ python migration.py db upgrade
	

#### 6. Run the development server:

    $ python run.py

#### 7. How to use Webservice
	Create user:
	$ curl -X POST -F facebookId=30 http://localhost:5000/person/
	
	Delete user:
	$ curl -X DELETE http://localhost:5000/person/30/
	
	List users with limit:
	$ curl http://localhost:5000/?limit=xxx
#### Tests

To run the tests use the following command:

    $ nosetests