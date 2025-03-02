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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1 тестируем добавление книги с некорректным названием (слишком длинным)
    def test_add_new_book_invalid_name(self):
        collector = BooksCollector()

        # добавляем книгу с названием длиной больше 40 символов
        collector.add_new_book('А' * 41)

        # проверяем, что книга не добавлена
        assert len(collector.get_books_genre()) == 0

    # 2 тестируем установку неверного жанра
    def test_set_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Невозможный жанр')

        # проверяем, что жанр не установлен
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # 3 тестируем установку жанра для книги
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # проверяем, что жанр книги установлен корректно
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # 4 тестируем, что книги с возрастным рейтингом не попадают в список книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Стивен Кинг: Оно')
        collector.set_book_genre('Стивен Кинг: Оно', 'Ужасы')

        # проверяем, что 'Стивен Кинг: Оно' не попадет в список книг для детей
        books_for_children = collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in books_for_children
        assert 'Стивен Кинг: Оно' not in books_for_children

    # 5 тестируем получение списка книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        # получаем список книг с жанром 'Фантастика'
        books = collector.get_books_with_specific_genre('Фантастика')

        # проверяем, что только одна книга в списке с нужным жанром
        assert len(books) == 1
        assert 'Гордость и предубеждение и зомби' in books

    # 6 тестируем добавление несуществующей книги в избранное
    def test_add_non_existent_book_to_favorites(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Не существующая книга')

        # проверяем, что список избранных остается пустым
        assert len(collector.get_list_of_favorites_books()) == 0

    # 7 тестируем удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга удалена из избранного
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    # 8 тестируем работу с пустым списком избранных книг
    def test_empty_favorites(self):
        collector = BooksCollector()

        # проверяем, что список избранных книг пуст
        assert collector.get_list_of_favorites_books() == []

    # 9 тестируем параметризацию установки жанра для нескольких книг
    @pytest.mark.parametrize("name, genre, expected_genre", [
        ("Гордость и предубеждение и зомби", "Фантастика", "Фантастика"),
        ("Что делать, если ваш кот хочет вас убить", "Ужасы", "Ужасы"),
        ("1984", "Детективы", "Детективы"),
        ("Три товарища", "Комедии", "Комедии"),
    ])
    def test_set_book_genre_parametrized(self, name, genre, expected_genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        # проверяем, что жанр установлен правильно
        assert collector.get_book_genre(name) == expected_genre