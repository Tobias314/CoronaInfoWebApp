import sqlite3
import config

'''class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)
'''

#@Singleton
class DatabaseConnection:

    def __init__(self):
        self.connection = sqlite3.connect(config.DATABASE_PATH)

    def close(self):
        self.connection.close()

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()
