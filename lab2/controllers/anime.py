import click
from lab2.controllers.basic_controller import BasicController
from lab2.models.anime import AnimeModel
from lab2.views.anime import AnimeView


class AnimeController(BasicController):
    def __init__(self, model: AnimeModel, view: AnimeView):
        # TODO: move to BasicController
        self.model = model
        self.view = view

    def render_one(self, id):
        try:
            anime = self.model.get(id)
            self.view.render_one(anime)
        except Exception as e:
            click.echo(e)

    def render_list(self, search_query='', limit=15, offset=0):
        try:
            animes = self.model.list(search_query, limit=limit, offset=offset)
            self.view.render_list(animes)
        except Exception as e:
            click.echo(e)
