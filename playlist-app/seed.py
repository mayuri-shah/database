from models import Playlist,Song,PlaylistSong,connect_db,db
from app import app
connect_db(app)
db.drop_all()
db.create_all()

playlist1 = Playlist(name="playlist1",description="abcdefg")
playlist2 = Playlist(name = "playlist2",description="xyz")

db.session.add(playlist1)
db.session.add(playlist2)

db.session.commit()


song1 = Song(title = "song1",artist="maya")
song2 = Song(title = "song2",artist ="mehul")
song3 = Song(title = "song3",artist = "kajal")

db.session.add(song1)
db.session.add(song2)
db.session.add(song3)

db.session.commit()

addsong1_to_p1 = PlaylistSong(playlist_id = 1,song_id = 1)
addsong2_to_p1 = PlaylistSong(playlist_id = 1,song_id = 2)
addsong3_to_p1 = PlaylistSong(playlist_id = 1,song_id = 3)
addsong1_to_p2 = PlaylistSong(playlist_id = 2,song_id = 1)

db.session.add(addsong1_to_p1)
db.session.add(addsong2_to_p1)
db.session.add(addsong3_to_p1)
db.session.add(addsong1_to_p2)

db.session.commit()

