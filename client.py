"""
Module that creates a client as CLI application using CLICK.
Retrieve an item by title using the command: python client.py <<title>>
example: python client.py "Mine 9"
"""
import click
import requests
from config import HOST, PORT

API_BASE_URL = f"http://{HOST}:{PORT}"

@click.command()
@click.argument('title')
def query_movie(title):
    try:
        response = requests.get(f'{API_BASE_URL}/query', params={'title': title})

        if response.status_code == 200:
            data = response.json()
            for movie in data['data']:
                click.echo(f'show_id: {movie["show_id"]}')
                click.echo(f'title: {movie["title"]}')
                click.echo(f'director: {movie["director"]}')
                click.echo(f'cast: {movie["cast"]}')
                click.echo(f'country: {movie["country"]}')
                click.echo(f'date_added: {movie["date_added"]}')
                click.echo(f'rating: {movie["rating"]}')
                click.echo(f'duration {movie["duration"]}')
                click.echo(f'listed_in: {movie["listed_in"]}')
                click.echo(f'release_year: {movie["release_year"]}')
                click.echo(f'description: {movie["description"]}')
                click.echo('-' * 20)
        else:
            click.echo('Error querying the item')

    except Exception as e:
        click.echo(f'Error: {str(e)}')

if __name__ == '__main__':
    query_movie()
