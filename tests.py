
import pytest

from main import BooksCollector

class TestBooksCollector:

    # Добавление новой книги
    @pytest.mark.parametrize('name', ["Клерки", "Новые парни турбо", "Кунг Фьюри"])
    def test_add_new_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # Установка жанра книги
    @pytest.mark.parametrize('name', ['Легенды Невского проспекта'])
    def test_set_book_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        assert collector.get_book_genre(name) == 'Комедии'

    # Получение жанра
    @pytest.mark.parametrize('name, genre', [('Легенды Невского проспекта', 'Комедии')])
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # Получение списка книг по определённому жанру
    @pytest.mark.parametrize('name, genre', [
        ("Клерки", 'Комедии'),
        ("Новые парни турбо", 'Комедии'),
        ("Кунг Фьюри", 'Комедии')])
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

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

    #Добавление книги в избранное
    @pytest.mark.parametrize('name', ["Клерки", "Новые парни турбо", "Кунг Фьюри"])
    def test_add_book_in_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    #Удаление книги из избранного
    @pytest.mark.parametrize('name', ["Клерки", "Новые парни турбо", "Кунг Фьюри"])
    def test_delete_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    #Попытка добавления новой книги с названием длиннее 41 знака
    @pytest.mark.parametrize('name', [('Мифы и реальность: загадки древних народов')])
    def test_add_new_book_negative(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    #Попытка добавления книги с отсутствующим в списке жанром и получение отсутствующего (пустого) жанра для книги
    @pytest.mark.parametrize('name, genre', [
        ("Хоббит или туда и обратно", 'Фэнтези'),
        ("Властелин Колец", 'Фэнтези'),
        ("Сильмариллион", 'Фэнтези')])
    def test_set_book_genre_and_get_book_genre_negative(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_genre = collector.get_books_genre()
        assert books_genre.get(name) == ''

    #Получение пустого списка детских книг
    @pytest.mark.parametrize('name, genre', [
        ("Кошмар на улице вязов", 'Ужасы'),
        ("Зловещие мертвецы", 'Ужасы'),
        ("Кунг Фьюри", 'Комедии')])
    def test_get_books_for_children_negative(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_list = collector.get_books_for_children()
        assert name is not books_list

    # Попытка добавить одну и ту же книгу в избранное дважды
    @pytest.mark.parametrize('name', ["Клерки", "Новые парни турбо", "Кунг Фьюри"])
    def test_add_book_to_favorites_twice(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        favorites_books = collector.get_list_of_favorites_books()
        assert favorites_books.count(name) == 1
