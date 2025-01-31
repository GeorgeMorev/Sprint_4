import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Установление жанра книги и получение жанра по имени книги
    @pytest.mark.parametrize('name, genre', [('Легенды Невского проспекта', 'Комедии')])
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Легенды Невского проспекта')
        collector.set_book_genre('Легенды Невского проспекта', 'Комедии')
        assert 'Комедии' in collector.get_book_genre('Легенды Невского проспекта')

    # Получение списка книг по определённому жанру
    @pytest.mark.parametrize('name, genre', [
        ("Клерки", 'Комедии'),
        ("Новые парни турбо", 'Комедии'),
        ("Кунг Фьюри", 'Комедии')])
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre('Комедии')

    #Получение словаря books_genre
    @pytest.mark.parametrize('name, genre', [
        ("Клерки", 'Комедии'),
        ("Новые парни турбо", 'Комедии'),
        ("Кунг Фьюри", 'Комедии')])
    def test_get_books_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_genre = collector.get_books_genre()  # Получаем словарь {книга: жанр}
        assert name in books_genre  # Проверяем, что книга есть в словаре
        assert books_genre[name] == genre  # Проверяем, что у книги правильный жанр

    #Получение книг, подходящих детям
    @pytest.mark.parametrize('name, genre', [
        ("Клерки", 'Комедии'),
        ("Новые парни турбо", 'Комедии'),
        ("Кунг Фьюри", 'Комедии')])
    def test_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_list = collector.get_books_for_children()
        assert name in books_list

    #Добавляем книгу в избранное и получаем список избранных книг
    @pytest.mark.parametrize('name', ["Клерки", "Новые парни турбо", "Кунг Фьюри"])
    def test_add_book_in_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        books_in_favorites = collector.get_list_of_favorites_books()
        assert name in books_in_favorites

