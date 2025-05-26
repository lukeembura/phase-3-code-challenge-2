import unittest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

class TestArticle(unittest.TestCase):
    def setUp(self):
        # Set up the database and test data
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()

        self.author = Author(name="John Doe")
        self.author.save()

        self.magazine = Magazine(name="Tech Monthly", category="Technology")
        self.magazine.save()

        self.article = Article(title="AI in 2023", author_id=self.author.id, magazine_id=self.magazine.id)
        self.article.save()

    def test_article_creation(self):
        self.assertIsNotNone(self.article.id)
        self.assertEqual(self.article.title, "AI in 2023")
        self.assertEqual(self.article.author_id, self.author.id)
        self.assertEqual(self.article.magazine_id, self.magazine.id)

    def test_find_by_id(self):
        found_article = Article.find_by_id(self.article.id)
        self.assertIsNotNone(found_article)
        self.assertEqual(found_article.title, "AI in 2023")

    def test_find_by_title(self):
        found_article = Article.find_by_title("AI in 2023")
        self.assertIsNotNone(found_article)
        self.assertEqual(found_article.id, self.article.id)

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
