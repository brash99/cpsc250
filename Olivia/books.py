from datetime import timedelta
from dateutil import parser


# Input from user book
def input_book():
    user_input = input("Please enter a book title: ")
    return user_input


# Input from user total pages
def input_pagenum():
    page_input = int(input("Please enter the total pages of that book: "))
    return page_input


# Input from user whether to add another book
def input_another_book():
    choice = input("Do you want to enter another book? (yes/no): ")
    return choice.lower() == "yes"


# Input from user pages to read per day
def input_pgsperday():
    day_input = int(input("Please enter how many pages to read in a day: "))
    return day_input


# Input from user today's date
def input_date():
    while True:
        date_input = input("Please enter today's date (format: January 1st, 2024): ")
        try:
            date = parser.parse(date_input)
            return date.strftime("%B %d, %Y")
        except ValueError:
            print("Invalid date format. Please enter the date in a valid format (e.g., 'May 27th, 2024').")


# Ask if user has started reading the book
def ask_started_reading(book_title):
    choice = input(f"Have you started reading {book_title}? (yes/no): ")
    return choice.lower() == "yes"


# Input the current page number
def input_current_page(book_title):
    page_number = int(input(f"What page are you on in {book_title}? "))
    return page_number


# Calculate finish date for a single book
def calculate_book_finish_date(total_pages, pgs_perday, start_date):
    days_needed = total_pages / pgs_perday
    finish_date = parser.parse(start_date) + timedelta(days=days_needed)
    return finish_date


# Main function to input and process books
if __name__ == "__main__":

    books = []  # List to store book information
    all_books_finish_dates = []  # List to store anticipated finish dates for all books

    # Input books
    while True:
        book_title = input_book()
        total_pages = input_pagenum()

        books.append({
            "title": book_title,
            "total_pages": total_pages,
        })

        if not input_another_book():
            break

    # Input additional information
    pgs_perday = input_pgsperday()
    date = input_date()

    # Calculate finish date for each book sequentially
    for i, book in enumerate(books):
        # Check if the user has started reading the book
        if i == 0:
            started_reading = ask_started_reading(book["title"])
            if started_reading:
                current_page = input_current_page(book["title"])
                book["total_pages"] -= current_page

        # Calculate finish date for the current book
        finish_date_book = calculate_book_finish_date(book["total_pages"], pgs_perday, date)
        all_books_finish_dates.append((book["title"], finish_date_book))
        date = finish_date_book.strftime("%B %d, %Y")

    # Print information
    print("\nAnticipated Finish Date for All Books:")
    for title, finish_date in all_books_finish_dates:
        print(f"{title}: {finish_date.strftime('%B %d, %Y')}")
