# FSND_Capstone_Fyyur
Fullstack Nanodegree Final Project - FyyurAPI

# Fyyur
The Fyyur models a company that is responsible for creating venues and managing and assigning actors to those venues.

only server side.

Application hosted on Heroku 

https://fierce-falls-57821.herokuapp.com/

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

* Base URL: The Backend is hosted on heroku [here](https://fierce-falls-57821.herokuapp.com/)
* Authentication: This application use Auth0 service

* Use this link to get new token [Get Token](https://fsnddd.us.auth0.com/authorize?audience=Capstone&response_type=token&client_id=kyyTrXCvJ2kUB22lgF53Mo2R76a996NO&redirect_uri=https://localhost:8080/login-results)

Users in this application are:

Assistant: Can Views Artists, Venues, Shows <br>
Email: testassistant@gmail.com<br>
Password: Test1234

Manager: Assistant Access + CURD on Artist, Venue, Show<br>
Email: testmanager@gmail.com<br>
Password: Test1234
<br><br>

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
* General: Return list of artists in Database
* Sample: `curl -X GET 'https://fierce-falls-57821.herokuapp.com/artists' \
-H 'Authorization: Bearer Assisant_Token'`<br>

        {
            "artists": [
                {
                    "city": "SA",
                    "genres": [],
                    "id": 1,
                    "name": "Mohammad",
                    "phone": "111-111-1111",
                    "seeking_description": "gfgfgfgf",
                    "seeking_venue": true,
                    "shows": [],
                    "state": "SA"
                }
            ],
            "success": true
        }

#### GET /venues
* General: Return list of venues in Database
* Sample: `curl -X GET 'https://fierce-falls-57821.herokuapp.com/venues' \
-H 'Authorization: Bearer Assisant_Token'`<br>

        {
            "success": true,
            "venues": [
                {
                    "address": "self.address",
                    "city": "self.city",
                    "genres": [],
                    "id": 1,
                    "name": "self.name",
                    "phone": "self.phone",
                    "seeking_description": "self.seeking_description",
                    "seeking_talent": false,
                    "shows": [
                        {
                            "id": 2
                        }
                    ],
                    "state": "self.state"
                }
            ]
        }

#### GET /shows
* General: Return list of shows in Database
* Sample: `curl -X GET 'https://fierce-falls-57821.herokuapp.com/shows' \
-H 'Authorization: Bearer Assisant_Token'`<br>

        {
            "shows": [
                {
                    "artist_name": "Mohammad",
                    "id": 2,
                    "venue_name": "self.name"
                }
            ],
            "success": true
        }

#### POST /artists
* General: Add artist in DB
* Sample: `curl -X POST 'https://fierce-falls-57821.herokuapp.com/artists' \
-H 'Authorization: Bearer Manager_Token' \
-H 'Content-Type: application/json' \
--data-raw '{
            "name": "Mohammad",
            "city": "SA",
            "state": "SA",
            "phone": "111-111-1111",
            "genres": [],
            "seeking_venue": true,
            "seeking_description": "gfgfgfgf"
        }'`<br>

        {
            "created_id": 1,
            "success": true
        }

#### POST /venues
* General: Add venue in DB
* Sample: `curl -X POST 'https://fierce-falls-57821.herokuapp.com/venues' \
-H 'Authorization: Bearer Manager_Token' \
-H 'Content-Type: application/json' \
--data-raw '{
    "name": "self.name",
    "city": "self.city",
    "state": "self.state",
    "address": "self.address",
    "phone": "self.phone",
    "genres": [],
    "seeking_talent": false,
    "seeking_description": "self.seeking_description"
}'`<br>

        {
            "created_id": 1,
            "success": true
        }


#### POST /shows
* General: Add Show in DB if artist and venue exist
* Sample: `curl -X POST 'https://fierce-falls-57821.herokuapp.com/shows' \
-H 'Authorization: Bearer Manager_Token' \
-H 'Content-Type: application/json' \
--data-raw '{
    "venue_id" : 1,
    "artist_id" : 1,
    "start_time" : "12/12/2012"
}'`<br>

        {
            "created_id": 1,
            "success": true
        }

#### PATCH /artists/<artist_id>
* General: Update Artist in DB
* Sample: `curl -X PATCH 'https://fierce-falls-57821.herokuapp.com/artists/1' \
-H 'Authorization: Bearer Manager_Token' \
-H 'Content-Type: application/json' \
--data-raw '{
    "name": "Majwed"
}'`<br>

        {
            "artist": {
                "city": "SA",
                "genres": [],
                "id": 1,
                "name": "Majwed",
                "phone": "111-111-1111",
                "seeking_description": "gfgfgfgf",
                "seeking_venue": true,
                "shows": [
                    {
                        "id": 2
                    }
                ],
                "state": "SA"
            },
            "success": true
        }

#### PATCH /venues/<venue_id>
* General: Update Venue in DB
* Sample: `curl -X PATCH 'https://fierce-falls-57821.herokuapp.com/venues/1' \
-H 'Authorization: Bearer Manager_Token' \
-H 'Content-Type: application/json' \
--data-raw '{
    "name": "Majwed"
}'`<br>

        {
            "success": true,
            "venue": {
                "address": "self.address",
                "city": "self.city",
                "genres": [],
                "id": 1,
                "name": "Majwed",
                "phone": "self.phone",
                "seeking_description": "self.seeking_description",
                "seeking_talent": false,
                "shows": [
                    {
                        "id": 2
                    }
                ],
                "state": "self.state"
            }
        }

#### DELETE /artists/<artist_id>
* General: Delete Artist
* Sample: `curl -X DELETE 'https://fierce-falls-57821.herokuapp.com/artists/2' \
-H 'Authorization: Bearer Manager_Token'`<br>

        {
            "delete_id": 2,
            "success": true
        }

#### DELETE /venues/<venue_id>
* General: Delete Venue
* Sample: `curl -X DELETE 'https://fierce-falls-57821.herokuapp.com/venues/2' \
-H 'Authorization: Bearer Manager_Token'`<br>

        {
            "delete_id": 2,
            "success": true
        }


# Postman user
in this repo there is collection file exported with latest postman version

you can use it to test all API Provided in here

PS: Update Tokens For Folders in the collection
