import datetime
from lab2.models.model import Model


class AnimeType:
    SERIES = 1
    MOVIE = 2
    OVA = 3
    OAD = 4
    ONA = 5
    OAV = 6
    SPECIAL = 7


class Anime:
    def __init__(self,
                 id: int = -1,
                 name: str = '',
                 type: int = AnimeType.SERIES,
                 episodes: int = 1,
                 rating: float = 10,
                 end_date=None,
                 start_date=None,
                 studio_id: int = -1):

        self.id = id
        self.name = name
        self.type = type
        self.episodes = episodes
        self.rating = rating
        self.end_date = end_date
        self.start_date = start_date
        self.studio_id = studio_id

    @staticmethod
    def from_record(anime):
        id, name, type, episodes, rating, end_date, start_date, studio_id = anime
        return Anime(id, name, type, episodes, rating, end_date, start_date, studio_id)

    def to_record(self):
        return self.id, self.name, self.type, self.episodes, self.rating, self.end_date, self.start_date, self.studio_id

    def __repr__(self):
        return f"<Anime {self.id} '{self.name}'>"


class AnimeModel(Model):
    def __init__(self):
        super().__init__()

    def get(self, id: int = 0):
        query = """SELECT * FROM animes WHERE id = %s;"""
        data = (id, )

        try:
            self.db.cur.execute(query, data)

            record = self.db.cur.fetchall()[0]
        except Exception as e:
            print(e)
            return Anime(name='Not Found')

        return Anime.from_record(record)

    def list(self, search_name: str ='', limit: int = 30, offset: int =0):
        query = """
            SELECT 
                * 
            FROM animes 
            WHERE 
                name LIKE %s 
            LIMIT %s OFFSET %s;
        """

        data = (f"%{search_name}%", limit, offset)

        rows = []
        try:
            self.db.cur.execute(query, data)

            rows = self.db.cur.fetchall()
        except Exception as e:
            print(e)

        return list(map(lambda x: Anime.from_record(x), rows))

    def list_related_to(self, id: int = 0):
        query = """SELECT * FROM animes WHERE ..."""
        data = (id, )

        rows = []
        try:
            self.db.cur.execute(query, data)

            rows = self.db.cur.fetchall()
        except Exception as e:
            print(e)

        return list(map(lambda x: Anime.from_record(x), rows))

    def create(self, anime: Anime):
        query = """
            INSERT INTO animes 
                (name, type, episodes, rating, end_date, start_date, studio_id) 
            VALUES 
                (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
        """
        data = anime.to_record()[1:]

        inserted_id = -1

        try:
            self.db.cur.execute(query, data)
            self.db.conn.commit()

            inserted_id = self.db.cur.fetchone()[0]
        except Exception as e:
            print(e)

        record = self.get(inserted_id)

        return record

    def delete(self, id: int):
        query = """
            DELETE FROM animes
            WHERE id = %s 
            RETURNING id;
        """
        data = (id, )

        deleted = False

        try:
            self.db.cur.execute(query, data)
            self.db.conn.commit()

            if self.db.cur.fetchone()[0] == id:
                deleted = True
        except Exception as e:
            print(e)

        return deleted

    def update(self, anime: Anime):
        query = """
            UPDATE animes
            SET 
                name = %s, 
                type = %s,
                episodes = %s,
                rating = %s,
                end_date = %s,
                start_date = %s,
                studio_id = %s 
            WHERE id = %s
            RETURNING id;
        """
        data = (
            anime.name,
            anime.type,
            anime.episodes,
            anime.rating,
            anime.end_date,
            anime.start_date,
            anime.studio_id,
            anime.id
        )

        updated = False

        try:
            self.db.cur.execute(query, data)
            self.db.conn.commit()

            if self.db.cur.fetchone()[0] == anime.id:
                updated = True
        except Exception as e:
            print(e)

        return updated