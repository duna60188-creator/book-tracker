import json
import os
from datetime import datetime

BOOKS_FILE = "books.json"

def load_books():
 if not os.path.exists(BOOKS_FILE):
     return []
 try:
     with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
         return json.load(file)
 except:
     return []

def save_books(books):
 with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
     json.dump(books, file, ensure_ascii=False, indent=2)

def is_duplicate(books, author, title):
 for book in books:
     if book.get("author", "").lower() == author.lower() and \
        book.get("title", "").lower() == title.lower():
         return True
 return False

def get_valid_rating():
 while True:
     try:
         rating = int(input("Оценка (от 1 до 5): "))
         if 1 <= rating <= 5:
             return rating
         print("Ошибка: оценка должна быть от 1 до 5")
     except ValueError:
         print("Ошибка: введите целое число")

def get_date():
 date = input("Дата прочтения (ГГГГ-ММ-ДД, Enter для сегодняшней): ").strip()
 if not date:
     return datetime.now().strftime("%Y-%m-%d")
 return date

def add_book():
 books = load_books()
 print("\n--- Добавление книги ---")
 author = input("Автор: ").strip()
 title = input("Название: ").strip()
 
 if is_duplicate(books, author, title):
     print("Ошибка: такая книга уже есть в трекере!")
     return
 
 rating = get_valid_rating()
 date = get_date()
 
 book = {"author": author, "title": title, "rating": rating, "date": date}
 books.append(book)
 save_books(books)
 print(f"Книга '{title}' добавлена успешно!")

def show_all_books():
 print("Функция будет добавлена позже")

def show_average_rating():
 print("Функция будет добавлена позже")

def show_author_stats():
 print("Функция будет добавлена позже")

def delete_book():
 print("Функция будет добавлена позже")

def main():
 while True:
     print("\n" + "="*40)
     print("📚 ТРЕКЕР ПРОЧИТАННЫХ КНИГ 📚")
     print("="*40)
     print("1. Добавить книгу")
     print("2. Показать все книги")
     print("3. Показать среднюю оценку")
     print("4. Статистика по авторам")
     print("5. Удалить книгу")
     print("6. Выход")
     print("="*40)
     
     choice = input("Выберите пункт (1-6): ").strip()
     
     if choice == "1":
         add_book()
     elif choice == "2":
         show_all_books()
     elif choice == "3":
         show_average_rating()
     elif choice == "4":
         show_author_stats()
     elif choice == "5":
         delete_book()
     elif choice == "6":
         print("До свидания! 👋")
         break
     else:
         print("Неверный пункт")

if __name__ == "__main__":
 main()
