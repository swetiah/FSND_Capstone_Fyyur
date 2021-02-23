# FSND_Capstone_Fyyur
Fullstack Nanodegree Final Project - FyyurAPI

# Fyyur
The Fyyur models a company that is responsible for creating venues and managing and assigning actors to those venues.

only server side.

Application hosted on Heroku 

<!-- https://vast-stream-21858.herokuapp.com/ -->

# Motivation

This project to show my learning journey during this nanodegree

1.  Database with  **postgres**  and  **sqlalchemy**  (`models.py`)
2.  API  with  **Flask**  (`app.py`)
3.  TDD  **Unittest**  (`test_app.py`)
4.  Authorization &  Authentification **Auth0**  (`auth.py`)
5.  Deployment on  **`Heroku`**

## Working with the application locally
Make sure you have [python 3](https://www.python.org/downloads/) or later installed

1. **Clone The Repo**
    ```bash
    git clone https://github.com/swetiah/Capstone.git
    ```
2. **Set up a virtual environment**:
    ```bash
    virtualenv env
    source env/Scripts/activate # for Windows
    source env/bin/activate # for MacOs/Linux
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt # for Windows/Linux
    pip3 install -r requirements.txt # for MacOs
    ```
4. **Export Environment Variables**

    Refer to the `setup.sh` file and export the environment variables for the project.

5. **Create Local Database**:

    Create a local database and export the database URI as an environment variable with the key `DATABASE_URL`.

6. **Run Database Migrations**:
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

7. **Run the Flask Application locally**:
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run

    # if using CMD in Windows

    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run
    ```

## Testing
To run the tests, run
```bash
dropdb capstone
createdb capstone
python test_app.py # if running locally
```

## API Reference

### Getting Started

* Base URL: Currently this application is only hosted locally. The backend is hosted at ``
* Authentication: This application use Auth0 service

* Use this link to get new token [Get Token](https://fsnd-udacity.eu.auth0.com/authorize?audience=CastingAgency&response_type=token&client_id=WMvUqnD1GAJg2OH06i4Musq0vllhysMh&redirect_uri=https://localhost:8080/login-results)

Users in this application are:


### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return three types of errors:

* 404 – resource not found
* 422 – unprocessable
* 401 - Unauthorized
* 400 - bad request
* 500 - internal server error
* 403 - Forbidden

### Endpoints

#### GET /artists

#### GET /venues

#### GET /shows

#### POST /artists

#### POST /venues

#### POST /shows

#### PATCH /artists/<artist_id>

#### PATCH /venues/<venue_id>

#### DELETE /artists/<artist_id>

#### DELETE /venues/<venue_id>

# Postman user
in this repo there is collection file exported with latest postman version

you can use it to test all API Provided in here

PS: Update Tokens For Folders in the collection
