# qa_python
В файле тестов описаны следующие тесты:

Для метода add_new_book:

1. test_add_new_book_add_book_and_this_book_is_on_list - позитивный тест, проверяющий, что книга добавляется в словарь и ключ этого словаря соответствует названию указанной пользователем книги;
2. test_add_new_book_long_name_book_is_not_added - негативный тест, который проверяет, что в названии книги содержится больше 40 символов и книга, соответственно не добавляется в словарь.

Для метода set_book_genre:

1. test_set_book_genre_add_genre_for_book - позитивный тест, который устанавливает жанр из списка для добавленной книги;
2. test_set_book_genre_adding_undefined_genre_is_not_added - негативный тест, который передаёт в параметр "жанр" не существующий в словаре жанр и удостоверяется, что тот не добавился в словарь

Для метода get_book_genre:

1. test_get_book_genre_book_genre_found - позитивный тест, в котором жанр находится по названию книги. 
В тесте использована параметризация для перебора нескольких наборов данных.

Для метода get_books_with_specific_genre:

1. test_get_books_with_specific_genre_get_fantastic_genre - позитивный тест, в котором для пользователя выводятся книги только с жанром "Фантастика"

Для метода get_books_genre:

1. test_get_books_genre_books_displayed_in_dictionary - позитивный кейс, проверяет, что в словарь попадают все значения добавленных книг вместе с жанром.

Для метода get_books_for_children:

1. test_get_books_for_children_books_with_age_genre_not_included_in_list - негативный кейс, в котором проверяется, что в словарь попали книги только для детей (возрастных жанров нет в списке).
Для данного теста использована параметризация для перебора данных из списка genre_age_rating.

Для метода add_book_in_favorites:

1. test_add_book_in_favorites_book_added_in_favorites - позитивный кейс, в котором проходит проверка на то, добавилась ли книга в список избранных.

Для метода delete_book_from_favorites:

1. test_delete_book_from_favorites_book_deleted_from_favorites - позитивный кейс, в котором проверяется удаление из списка избранных книг. Если книга добавлена (и она единственна) и в последствии удалена, то список не содержит книг.

Для метода get_list_of_favorites_books:

1. test_get_list_of_favorites_books_favorites_two_books_in_list - позитивный кейс, в котором получаем список избранных книг в количестве двух штук, так как в список было добавлено две книги.