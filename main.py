def delete_book():
    books = load_books()
    if not books:
        print("\nНет книг для удаления.\n")
        return
    
    print("\n--- Удаление книги ---")
    print("1. Удалить по номеру")
    print("2. Удалить по автору и названию")
    choice = input("Выберите способ (1/2): ").strip()
    
    if choice == "1":
        show_all_books()
        try:
            index = int(input("Введите номер книги для удаления: ")) - 1
            if 0 <= index < len(books):
                removed = books.pop(index)
                save_books(books)
                print(f"Книга '{removed['title']}' удалена!")
            else:
                print("Неверный номер книги")
        except ValueError:
            print("Ошибка: введите число")
    elif choice == "2":
        author = input("Автор: ").strip()
        title = input("Название: ").strip()
        for i, book in enumerate(books):
            if book['author'].lower() == author.lower() and \
               book['title'].lower() == title.lower():
                removed = books.pop(i)
                save_books(books)
                print(f"Книга '{removed['title']}' удалена!")
                return
        print("Книга не найдена")
    else:
        print("Неверный выбор")
