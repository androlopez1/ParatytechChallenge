"""
Routes definition: Created 2 endpoints for load and query data, and base url for data serialization.
"""

from flask import Blueprint, jsonify, request, current_app, render_template, redirect
import csv
import requests
from google.cloud import datastore
from config import HOST, PORT

bp = Blueprint('system_module_2', __name__)

@bp.route('/', methods=['GET'])
def get_data():
    """
    Get data from csv file and call load endpoint
    """
    data = []
    with open('data/netflix_titles.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    url = f'http://{HOST}:{PORT}/load'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return jsonify({"message": "Data succesfully loaded to Datastore"}), 200
    else:
        return jsonify({"error": "Error loading data to datastore"}), 500


@bp.route('/load', methods=['GET', 'POST'])
def system_module_1():
    """
    Populate database with serialized data.
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            client = current_app.datastore_client
            query = client.query(kind='Show')
            results = list(query.fetch())
            if  len(results) == 0: #If database is already populated, skip the process.    
                for show_data in data:
                    entity = datastore.Entity(client.key('Show'))
                    entity.update({
                        'show_id':show_data.get('show_id'),
                        'type': show_data.get('show_id'),
                        'title': show_data.get('title'),
                        'director': show_data.get('director'),
                        'cast': show_data.get('cast'),
                        'country': show_data.get('country'),
                        'date_added': show_data.get('date_added'),
                        'rating': show_data.get('rating'),
                        'duration': show_data.get('duration'),
                        'listed_in': show_data.get('listed_in'),
                        'release_year': show_data.get('release_year'),
                        'description': show_data.get('description')
                    })

                    client.put(entity)

            return jsonify({"message": "Data succesfully loaded to Datastore"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return redirect(f"http://{HOST}:{PORT}/", code=200)

@bp.route('/query', methods=['GET'])
def query_data():
    """
    Endpoint for listing all instances or get a particular one by title.
    """
    try:
        client = current_app.datastore_client
        title = request.args.get('title')
        query = client.query(kind='Show')
        if title:
            query.add_filter('title', '=', title)
            results = list(query.fetch())
        else:
            results = list(query.fetch())

        movies = []

        for result in results:
            movie_data = {
                'show_id':result['show_id'],
                'type': result['type'],
                'title': result['title'],
                'director': result['director'],
                'cast': result['cast'],
                'country': result['country'],
                'date_added': result['date_added'],
                'rating': result['rating'],
                'duration': result['duration'],
                'listed_in': result['listed_in'],
                'release_year': result['release_year'],
                'description': result['description'],
            }
            movies.append(movie_data)
        
        if title:
            return jsonify({"data": movies}), 200
        return render_template("index.html", movies=movies)
    except Exception as e:
        return jsonify({"error": str(e)}), 500