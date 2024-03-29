import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_book_is_on_list(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_long_name_book_is_not_added(self):
        collector = BooksCollector()
        name = 'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_genre_for_book(self):
        collector = BooksCollector()
        name = '12 стульев'
        collector.add_new_book(name)
        collector.set_book_genre(name,'Комедии')
        assert collector.get_book_genre(name) == 'Комедии'

    def test_set_book_genre_adding_undefined_genre_is_not_added(self):
        collector = BooksCollector()
        name = 'Как относиться к себе и людям'
        collector.add_new_book(name)
        collector.set_book_genre(name,'Психология')
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Мастер и Маргарита', 'Фантастика'],
            ['Отцы и дети', 'Комедии'],
            ['Песнь Льда и Пламени', 'Ужасы']
        ]
    )
    def test_get_book_genre_book_genre_found(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_fantastic_genre(self):
        collector = BooksCollector()
        name_1 = 'Портрет Дориана Грея'
        name_2 = 'Грозовой перевал'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, 'Фантастика')
        collector.set_book_genre(name_2, 'Детективы')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 1

    def test_get_books_genre_books_displayed_in_dictionary(self):
        collector = BooksCollector()
        name_1 = 'Приключения Алисы в стране чудес'
        name_2 = 'Робинзон Крузо'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, 'Мультфильмы')
        collector.set_book_genre(name_2, 'Детективы')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'name_age_1,genre_age_1,name_age_2,genre_age_2',
        [
            ['Маленький принц', 'Мультфильмы', 'Заводной апельсин', 'Ужасы'],
            ['Звёздные войны', 'Фантастика', 'Агата Кристи', 'Детективы']
        ]
    )
    def test_get_books_for_children_books_with_age_genre_not_included_in_list(self, name_age_1, genre_age_1, name_age_2, genre_age_2):
        collector = BooksCollector()
        collector.add_new_book(name_age_1)
        collector.add_new_book(name_age_2)
        collector.set_book_genre(name_age_1, genre_age_1)
        collector.set_book_genre(name_age_2, genre_age_2)
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_book_added_in_favorites(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_deleted_from_favorites(self):
        collector = BooksCollector()
        name = 'Евгений Онегин'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_favorites_books_in_list(self):
        collector = BooksCollector()
        name = 'Облачный атлас'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1
