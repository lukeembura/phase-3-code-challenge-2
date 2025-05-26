from lib.db.connection import get_connection
try:
    from models.article import Article
except ImportError:
    from models.article import Article  # Adjusted import path as a fallback

class Author:
    def __init__(self, name, id=None):
        if not name or not name.strip():
            raise ValueError("Author name cannot be empty.")
        self.name = name.strip()
        self.id = id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE authors SET name=? WHERE id=?", (self.name, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row["name"], row["id"])
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row["name"], row["id"])
        return None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM articles
            WHERE author_id = ?
        """, (self.id,))
        return cursor.fetchall()

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
SELECT DISTINCT m.* FROM magazines m
JOIN articles a ON m.id = a.magazine_id
WHERE a.author_id = ?
""", (self.id,))
        return cursor.fetchall()

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row["category"] for row in rows]

    def add_article(self, magazine, title):
        if not isinstance(magazine, (int,)):
            magazine_id = magazine.id if hasattr(magazine, "id") else None
        else:
            magazine_id = magazine
        article = Article(title=title, author_id=self.id, magazine_id=magazine_id)
        article.save()
        return article

    @staticmethod
    def add_author_with_articles(author_name, articles_data):
        """
        Add an author and their articles in a single transaction
        articles_data: list of dicts with 'title' and 'magazine_id' keys
        """
        conn = get_connection()
        try:
            conn.execute("BEGIN TRANSACTION")
            cursor = conn.cursor()
            # Insert author
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?) RETURNING id",
                (author_name,)
            )
            author_id = cursor.fetchone()[0]
            # Insert articles
            for article in articles_data:
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                    (article['title'], author_id, article['magazine_id'])
                )
            conn.execute("COMMIT")
            return True
        except Exception as e:
            conn.execute("ROLLBACK")
            print(f"Transaction failed: {e}")
            return False
        finally:
            conn.close()
