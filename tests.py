import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self,collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1 тестируем добавление книги с некорректным названием (слишком длинным)
    def test_add_new_book_invalid_name(self,collector):

        # добавляем книгу с названием длиной больше 40 символов
        collector.add_new_book('А' * 41)

        # проверяем, что книга не добавлена
        assert len(collector.get_books_genre()) == 0

    # 2 тестируем установку неверного жанра
    def test_set_invalid_genre(self,collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Невозможный жанр')

        # проверяем, что жанр не установлен
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # 3 тестируем установку жанра для книги
    def test_set_book_genre(self,collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # проверяем, что жанр книги установлен корректно
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # 4 тестируем получение жанра для книги
    def test_get_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # проверяем, что возвращаемый жанр соответствует ожиданиям
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # 5 тестируем получение всех жанров книг
    def test_get_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        # проверяем, что метод get_books_genre возвращает правильный словарь
        books_genre = collector.get_books_genre()
        assert books_genre == {'Гордость и предубеждение и зомби': 'Фантастика'}

    # 6 тестируем, что книги с возрастным рейтингом не попадают в список книг для детей
    def test_get_books_for_children(self,collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Стивен Кинг: Оно')
        collector.set_book_genre('Стивен Кинг: Оно', 'Ужасы')

        # проверяем, что 'Стивен Кинг: Оно' не попадет в список книг для детей
        books_for_children = collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in books_for_children
        assert 'Стивен Кинг: Оно' not in books_for_children

    # 7 тестируем получение списка книг с определённым жанром
    def test_get_books_with_specific_genre(self,collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        # получаем список книг с жанром 'Фантастика'
        books = collector.get_books_with_specific_genre('Фантастика')

        # проверяем, что только одна книга в списке с нужным жанром
        assert len(books) == 1
        assert 'Гордость и предубеждение и зомби' in books

    # 8 тестируем добавление несуществующей книги в избранное
    def test_add_non_existent_book_to_favorites(self,collector):

        collector.add_book_in_favorites('Не существующая книга')

        # проверяем, что список избранных остается пустым
        assert len(collector.get_list_of_favorites_books()) == 0

    # 9 позитивный тест: добавление существующей книги в избранное
    def test_add_existing_book_to_favorites(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # добавляем книгу в избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга добавлена в избранное
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    # 10 еще один тест для добавления в избранное
    def test_add_book_in_favorites_multiple_times(self, collector):
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # добавляем книгу в избранное дважды
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга добавлена в избранное только один раз (не должно быть дубликатов)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    # 12 тестируем удаление книги из избранного
    def test_delete_book_from_favorites(self,collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        # проверяем, что книга удалена из избранного
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    # 13 тестируем работу с пустым списком избранных книг
    def test_empty_favorites(self,collector):

        # проверяем, что список избранных книг пуст
        assert collector.get_list_of_favorites_books() == []

    # 14 тестируем получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
         collector.add_new_book('Гордость и предубеждение и зомби')
         collector.add_book_in_favorites('Гордость и предубеждение и зомби')

         # проверяем, что список избранных книг содержит добавленную книгу
         assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    # 15 тестируем параметризацию установки жанра для нескольких книг
    @pytest.mark.parametrize("name, genre, expected_genre", [
        ("Гордость и предубеждение и зомби", "Фантастика", "Фантастика"),
        ("Что делать, если ваш кот хочет вас убить", "Ужасы", "Ужасы"),
        ("1984", "Детективы", "Детективы"),
        ("Три товарища", "Комедии", "Комедии"),
    ])
    def test_set_book_genre_parametrized(self,collector, name, genre, expected_genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        # проверяем, что жанр установлен правильно
        assert collector.get_book_genre(name) == expected_genre