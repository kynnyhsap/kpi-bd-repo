from lab2.models.anime import AnimeModel, Anime, AnimeType
import datetime

def main():
    AM = AnimeModel()

    print(AM.list(limit=10, offset=0))

    # jujutsu_kaisen = AM.create(Anime(
    #     name='Jujutsu Kaisen',
    #     type=AnimeType.SERIES,
    #     episodes=24,
    #     rating=8.9,
    #     start_date=datetime.date(2020, 10, 3),
    #     end_date=None,
    #     studio_id=1
    # ))
    #
    # print(jujutsu_kaisen)


    print(AM.list(limit=10, offset=0))


main()