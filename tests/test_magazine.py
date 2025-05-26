import unittest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article
from lib.db.connection import get_connection

class TestMagazine(unittest.TestCase):
    def setUp(self):
        # Set up the database and test data
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()

        self.magazine = Magazine(name="Science Today", category="Science")
        self.magazine.save()

        self.author = Author(name="Alice Johnson")
        self.author.save()

        self.article = self.author.add_article(self.magazine, "Quantum Physics Explained")

    def test_magazine_creation(self):
        self.assertIsNotNone(self.magazine.id)
        self.assertEqual(self.magazine.name, "Science Today")
        self.assertEqual(self.magazine.category, "Science")

    def test_find_by_id(self):
        found_magazine = Magazine.find_by_id(self.magazine.id)
        self.assertIsNotNone(found_magazine)
        self.assertEqual(found_magazine.name, "Science Today")

    def test_articles(self):
        articles = self.magazine.articles()
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Quantum Physics Explained")

    def test_contributors(self):
        contributors = self.magazine.contributors()
        self.assertEqual(len(contributors), 1)
        self.assertEqual(contributors[0].name, "Alice Johnson")

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
