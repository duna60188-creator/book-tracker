def show_all_books():
    books = load_books()
    if not books:
        print("\nСписок книг пуст.\n")
        return
    print("\n--- Список книг ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} - «{book['title']}»")
        print(f"   Оценка: {book['rating']}/5, Дата: {book['date']}")
    print()

def show_average_rating():
    books = load_books()
    if not books:
        print("\nНет книг для подсчёта средней оценки.\n")
        return
    total = sum(book['rating'] for book in books)
    average = total / len(books)
    print(f"\nСредняя оценка всех книг: {average:.2f}\n")

def show_author_stats():
    books = load_books()
    if not books:
        print("\nНет книг для статистики.\n")
        return
    stats = {}
    for book in books:
        author = book['author']
        stats[author] = stats.get(author, 0) + 1
    print("\n--- Статистика по авторам ---")
    for author, count in sorted(stats.items()):
        print(f"{author}: {count} книг(а/и)")
    print()
