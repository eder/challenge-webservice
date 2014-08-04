# Challenger Webservice

Challenger Webservice is an example Flask application illustrating some of my common practices

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [MySQL](http://www.mysql.com/)


It is strongly recommended to also install and use the following tools:

1. [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)
2. [virtualenvwrapper](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenvwrapper)
3. [Vagrant](http://vagrantup.com)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone git@github.com:eder/challenger-webservice.git
    $ cd challenger-webservice

#### 2. Create and initialize virtualenv for the project:

    $ mkvirtualenv challenger-webservice
    $ pip install -r requirements.txt

#### 3. Edit database connection
		config/migration.py
		$ 6 engine = sqlalchemy.create_engine('mysql://root:12345@localhost/')
	 $ 10 app.config['SQLALCHEMY_DATABASE_URI']'mysql://root:12345@localhost/challengeWebservice_development'

#### 4. Upgrade the database:

    $ cd config/

#### Database Migrations
	$ python migration.py db init
	$ python config/migration.py db migrate
	$ python config/migration.py db upgrade
	

#### 5. Run the development server:

    $ python run.py

#### 6. Open [http://localhost:5000](http://localhost:5000)

#### Tests

To run the tests use the following command:

    $ nosetests