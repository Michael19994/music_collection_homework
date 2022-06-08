import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist("Disturbed", "Rock Band")
artist_repository.save(artist_1)

artist_2 = Artist("Michael", "Jackson")
artist_repository.save(artist_2)

Album_1 = Album("Indestructible","Rock-Metal", artist_1)
album_repository.save(Album_1)