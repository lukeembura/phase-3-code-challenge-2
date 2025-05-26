from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    DELETE FROM articles;
    DELETE FROM authors;
    DELETE FROM magazines;

    INSERT INTO authors (name) VALUES ('Alice'), ('Bob'), ('Carol');
    INSERT INTO magazines (name, category) VALUES ('Tech Today', 'Technology'), ('Health Weekly', 'Health');
    INSERT INTO articles (title, author_id, magazine_id) VALUES 
      ('AI Revolution', 1, 1),
      ('Healthy Living', 2, 2),
      ('Quantum Computing', 1, 1),
      ('Nutrition Facts', 3, 2),
      ('Tech Trends', 2, 1);
    """)

    conn.commit()
    conn.close()
