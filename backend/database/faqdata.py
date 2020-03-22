import sqlite3
import dataclasses
from database.databaseconnection import DatabaseConnection

@dataclasses.dataclass()
class FaqItem:
    district: str
    state: str
    question: str
    answer: str
    tags: str



class FaqsData:

    def __init__(self, database_connection: DatabaseConnection):
        self.db_connection = database_connection
        self.cursor = database_connection.cursor()

    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.cursor = self.db_connection.cursor()

    def create_database_tables(self):
        self.cursor.execute('''CREATE VIRTUAL TABLE Faqs
                     USING FTS5(district_name, state_name, question, answer, tags);''')

    def create_or_update_question(self, faq_item:FaqItem):
        result = self.cursor.execute('''
            SELECT *
            FROM Faqs
            WHERE district_name=? AND state_name=? AND question=?
        ''', (faq_item.district, faq_item.state, faq_item.question))
        if result.fetchone() is None:
            self.cursor.execute("""
                                    REPLACE INTO Faqs
                                    VALUES (?,?,?,?,?)
                                    """, (faq_item.district, faq_item.state, faq_item.question, faq_item.answer, faq_item.tags))
        self.db_connection.commit()

    def full_text_search(self, search_phrase: str):
        result = self.cursor.execute("""
            SELECT * 
            FROM Faqs 
            WHERE question MATCH ? OR answer MATCH ?;
        """, (search_phrase, search_phrase))
        self.db_connection.commit()
        return result.fetchall()
