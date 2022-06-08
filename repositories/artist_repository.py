from db.run_sql import run_sql
from models.artist import Artist

def select_all():
    artists = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["first_name"], row["last_name"], row["id"])
        artists.apend(artist)

    return artists

def select_one(id):
    artist = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["first_name"], result["last_name"], result["id"])
    return artist

def save(artist):
    sql = """INSERT INTO artists (first_name, last_name)
        VALUES (%s, %s) RETURNING id"""
    values = [artist.first_name, artist.last_name]
    result = run_sql(sql, values)[0]
    artist.id = result["id"]
    return artist

def update(artist):
    sql = """UPDATE artists
    SET (first_name, last_name) = (%s, %s)
    WHERE id = %s"""
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql)

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete_one(artist):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)    
