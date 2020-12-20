import click

from lab2.controllers.anime import AnimeController
from lab2.models.anime import AnimeModel
from lab2.views.anime import AnimeView

anime_model = AnimeModel()
anime_view = AnimeView()
anime_controller = AnimeController(anime_model, anime_view)


@click.group()
def cli():
    pass


@cli.group()
def animes_group():
    click.echo('Animes group')


@animes_group.command('Render List of animes')
@click.option('--search-query', default='', prompt='Search', type=str)
@click.option('--limit', default=15, prompt='Limit', type=int)
@click.option('--offset', default=0, prompt='Offset', type=int)
def list_animes(search_query, limit, offset):
    anime_controller.render_list(search_query, limit, offset)


@click.command('Render anime entity')
@click.option('--id', prompt='Anime ID', required=True, type=int)
def get_anime(id):
    anime_controller.render_one(id)

