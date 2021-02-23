import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, Artist, Venue, Show


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def index():
        return "Use Postman or curl to test endpoints"

    @app.route('/artists')
    @requires_auth('get:artists')
    def get_artists(self):
        artists = Artist.query.order_by(Artist.id).all()
        return jsonify({
            'success': True,
            'artists': [artist.format() for artist in artists]
        })

    @app.route('/venues')
    @requires_auth('get:venues')
    def get_venues(self):
        venues = Venue.query.order_by(Venue.id).all()
        return jsonify({
            'success': True,
            'venues': [venue.format() for venue in venues]
        })

    @app.route('/shows')
    @requires_auth('get:shows')
    def get_shows(self):
        shows = Show.query.order_by(Show.id).all()
        shows_data = []
        for show in shows:
            artist = Artist.query.get(show.artist_id)
            venue = Venue.query.get(show.venue_id)
            shows_data.append({
                'id': show.id,
                'venue_name': venue.name,
                'artist_name': artist.name
            })
        return jsonify({
            'success': True,
            'shows': shows_data
        })

    @app.route('/artists', methods=['POST'])
    @requires_auth('post:artists')
    def add_artist(self):
        body = request.get_json()

        if body is None:
            abort(422)

        name = body.get('name')
        city = body.get('city')
        state = body.get('state')
        phone = body.get('phone')
        genres = body.get('genres')
        seeking_venue = body.get('seeking_venue')
        seeking_description = body.get('seeking_description')

        artist = Artist(
            name,
            city,
            state,
            phone,
            genres,
            seeking_venue,
            seeking_description)

        try:
            artist.insert()
            return jsonify({
                'success': True,
                'created_id': artist.id
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/venues', methods=['POST'])
    @requires_auth('post:venues')
    def add_venue(self):
        body = request.get_json()

        if body is None:
            abort(422)

        name = body.get('name')
        city = body.get('city')
        state = body.get('state')
        phone = body.get('phone')
        address = body.get('address')
        genres = body.get('genres')
        seeking_talent = body.get('seeking_talent')
        seeking_description = body.get('seeking_description')

        venue = Venue(
            name,
            city,
            state,
            address,
            phone,
            genres,
            seeking_talent,
            seeking_description)

        try:
            venue.insert()
            return jsonify({
                'success': True,
                'created_id': venue.id
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/shows', methods=['POST'])
    @requires_auth('post:shows')
    def add_show(self):
        body = request.get_json()

        if body is None:
            abort(422)

        venueID = body.get('venue_id')
        artistID = body.get('artist_id')
        startTime = body.get('start_time')

        show = Show(venueID, artistID, startTime)

        try:
            show.insert()
            return jsonify({
                'success': True,
                'created_id': show.id
            })
        except Exception as e:
            print(e)
            abort(400)
#####

    @app.route('/artists/<int:artist_id>', methods=['PATCH'])
    @requires_auth('patch:artists')
    def edit_artist(self,artist_id):
        body = request.get_json()

        if body is None:
            abort(422)

        name = body.get('name')
        city = body.get('city')
        state = body.get('state')
        phone = body.get('phone')
        genres = body.get('genres')
        seeking_venue = body.get('seeking_venue')
        seeking_description = body.get('seeking_description')

        artist = Artist.query.get(artist_id)

        artist.name = name or artist.name
        artist.city = city or artist.city
        artist.state = state or artist.state
        artist.phone = phone or artist.phone
        artist.genres = genres or artist.genres
        artist.seeking_venue = seeking_venue or artist.seeking_venue
        artist.seeking_description = seeking_description or artist.seeking_description

        try:
            artist.update()
            return jsonify({
                'success': True,
                'artist': artist.format()
            })
        except Exception as e:
            print(e)
            abort(400)


    @app.route('/venues/<int:venue_id>', methods=['PATCH'])
    @requires_auth('patch:venue')
    def edit_venue(self,venue_id):
        body = request.get_json()

        if body is None:
            abort(422)

        name = body.get('name')
        city = body.get('city')
        state = body.get('state')
        phone = body.get('phone')
        address = body.get('address')
        genres = body.get('genres')
        seeking_talent = body.get('seeking_talent')
        seeking_description = body.get('seeking_description')

        venue = Venue.query.get(venue_id)

        venue.name=name or venue.name
        venue.city=city or venue.city
        venue.state=state or venue.state
        venue.phone=phone or venue.phone
        venue.address=address or venue.address
        venue.genres=genres or venue.genres
        venue.seeking_talent=seeking_talent or venue.seeking_talent
        venue.seeking_description=seeking_description or venue.seeking_description


        try:
            venue.update()
            return jsonify({
                'success': True,
                'venue': venue.format()
            })
        except Exception as e:
            print(e)
            abort(400)

    @app.route('/artists/<int:artist_id>', methods=['DELETE'])
    @requires_auth('delete:artists')
    def delete_artist(self,artist_id):
        artist = Artist.query.get(artist_id)

        if artist is None:
            abort(404)
        
        artist.delete()

        return jsonify({
            "success":True,
            "delete_id":artist_id
        })
    
    @app.route('/venues/<int:venue_id>', methods=['DELETE'])
    @requires_auth('delete:venue')
    def delete_venue(self,venue_id):
        venue = Venue.query.get(venue_id)

        if venue is None:
            abort(404)
        
        venue.delete()

        return jsonify({
            "success":True,
            "delete_id":venue_id
        })


    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(404)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resources Not Found"
        }), 404

    @app.errorhandler(AuthError)
    def handle_auth_error(e):
        response = jsonify(e.error)
        response.status_code = e.status_code
        return response

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
