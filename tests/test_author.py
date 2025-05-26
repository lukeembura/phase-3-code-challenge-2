import unittest
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

class TestAuthor(unittest.TestCase):
    def setUp(self):
        # Set up the database and test data
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()

        self.author = Author(name="Jane Smith")
        self.author.save()

        self.magazine = Magazine(name="Health Weekly", category="Health")
        self.magazine.save()

        self.article = self.author.add_article(self.magazine, "Healthy Living Tips")

    def test_author_creation(self):
        self.assertIsNotNone(self.author.id)
        self.assertEqual(self.author.name, "Jane Smith")

    def test_find_by_id(self):
        found_author = Author.find_by_id(self.author.id)
        self.assertIsNotNone(found_author)
        self.assertEqual(found_author.name, "Jane Smith")

    def test_articles(self):
        articles = self.author.articles()
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["title"], "Healthy Living Tips")

    def test_magazines(self):
        magazines = self.author.magazines()
        self.assertEqual(len(magazines), 1)
        self.assertEqual(magazines[0]["name"], "Health Weekly")

    def tearDown(self):
        # Clean up the database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()
        conn.close()

if __name__ == "__main__":
    unittest.main()
