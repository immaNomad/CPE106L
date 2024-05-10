import os
import sqlite3

def create_chinook_database():
    # Create the database connection
    conn = sqlite3.connect('chinook.db')
    cursor = conn.cursor()

    try:
        # Create the 'artists' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS artists (
                ArtistID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL
            )
        ''')

        # Create the 'albums' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS albums (
                AlbumId INTEGER PRIMARY KEY,
                Title TEXT,
                ArtistId INTEGER,
                FOREIGN KEY (ArtistId) REFERENCES artists(ArtistID)
            )
        ''')

        # Create the 'tracks' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tracks (
                TrackId INTEGER PRIMARY KEY,
                Name TEXT,
                AlbumId INTEGER,
                MediaTypeId INTEGER,
                GenreId INTEGER,
                Composer TEXT,
                Milliseconds INTEGER,
                Bytes INTEGER,
                UnitPrice NUMERIC,
                FOREIGN KEY (AlbumId) REFERENCES albums(AlbumId)
            )
        ''')

        conn.commit()
        print("Chinook database created successfully.")
    except sqlite3.Error as e:
        print(f'Error creating the Chinook database: {e}')
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_chinook_database()