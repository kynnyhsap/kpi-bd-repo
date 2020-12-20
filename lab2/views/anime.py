import click

from lab2.views.basic_views import BasicView
from lab2.models.anime import Anime

from typing import List

class AnimeView(BasicView):
    def __init__(self):
        pass

    @staticmethod
    def render_one(anime: Anime):
        click.echo(f"[{anime.id}] {anime.name} | {anime.episodes} episodes | {anime.start_date} - {anime.end_date} | {anime.rating} ⭐️")

    @staticmethod
    def render_list(animes: List[Anime]):
        click.echo('Anime list:')
        for anime in animes:
            click.echo(f"\t[{anime.id}] {anime.name} | {anime.episodes} episodes | {anime.start_date} - {anime.end_date} | {anime.rating} ⭐️")
