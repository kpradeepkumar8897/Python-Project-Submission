import requests
import pandas as pd
import random

def fetch_books_from_openlibrary(query="fiction", max_results=100):
    """
    Fetch book data from Open Library Search API based on a search query.
    Returns a list of book dicts containing title, authors, subjects, first_publish_year, and edition_count.
    """
    print("Fetching books from Open Library API...")
    books = []
    base_url = "https://openlibrary.org/search.json"
    params = {
        "q": query,
        "limit": max_results
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        for item in data.get("docs", []):
            book = {
                "title": item.get("title", "Unknown Title"),
                "authors": ", ".join(item.get("author_name", ["Unknown Author"])),
                "genres": ", ".join(item.get("subject", ["Unknown Genre"])) if "subject" in item else "Unknown Genre",
                "published_year": item.get("first_publish_year", None),
                "edition_count": item.get("edition_count", 0),
            }
            books.append(book)
        print(f"Fetched {len(books)} books.")
        return books

    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
        return []

def save_books_to_csv(books, filename="books_data.csv"):
    """
    Save list of book dicts to CSV file using pandas.
    """
    df = pd.DataFrame(books)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def load_books_from_csv(filename="books_data.csv"):
    """
    Load book data from CSV file into pandas DataFrame.
    """
    try:
        df = pd.read_csv(filename)
        print(f"Loaded {len(df)} books from {filename}")
        return df
    except FileNotFoundError:
        print(f"File {filename} not found. Please fetch data first.")
        return pd.DataFrame()

def filter_books(df, genre=None, min_edition_count=None, min_year=None, max_year=None):
    """
    Filter books DataFrame based on criteria.
    """
    filtered = df.copy()

    if genre:
        filtered = filtered[filtered['genres'].str.contains(genre, case=False, na=False)]

    if min_edition_count is not None:
        filtered = filtered[filtered['edition_count'] >= min_edition_count]

    if min_year is not None:
        filtered = filtered[filtered['published_year'] >= min_year]

    if max_year is not None:
        filtered = filtered[filtered['published_year'] <= max_year]

    return filtered

def random_book_suggestion(df):
    """
    Return a random book suggestion from DataFrame.
    """
    if df.empty:
        return None
    return df.sample(1).iloc[0]

def main():
    """
    Main function for user interaction and running the app.
    """
    print("Welcome to the Book Suggestion Bot!")

    # Step 1: Fetch or load data
    while True:
        choice = input("Do you want to (1) Fetch fresh data or (2) Load existing data from CSV? Enter 1 or 2: ").strip()
        if choice == '1':
            query = input("Enter a search term for books (e.g., fiction, science): ").strip()
            books = fetch_books_from_openlibrary(query=query, max_results=100)
            if books:
                save_books_to_csv(books)
                df = pd.DataFrame(books)
            else:
                print("No books fetched, try again or load existing data.")
                continue
            break
        elif choice == '2':
            df = load_books_from_csv()
            if df.empty:
                continue
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    # Step 2: User filters
    while True:
        print("\nAvailable genres in data:")
        genres = set()
        for g_list in df['genres'].dropna():
            for g in g_list.split(','):
                genres.add(g.strip())
        print(", ".join(sorted(genres)))

        genre = input("Enter genre to filter by (or press Enter to skip): ").strip()
        min_edition_count = input("Enter minimum edition count to filter by (or press Enter to skip): ").strip()
        min_year = input("Enter minimum publication year to filter by (or press Enter to skip): ").strip()
        max_year = input("Enter maximum publication year to filter by (or press Enter to skip): ").strip()

        try:
            min_edition_count_val = int(min_edition_count) if min_edition_count else None
            min_year_val = int(min_year) if min_year else None
            max_year_val = int(max_year) if max_year else None
        except ValueError:
            print("Invalid numeric input. Please try again.")
            continue

        filtered_df = filter_books(df, genre=genre if genre else None,
                                   min_edition_count=min_edition_count_val,
                                   min_year=min_year_val,
                                   max_year=max_year_val)

        if filtered_df.empty:
            print("No books found matching the filters. Suggesting a random book from the entire dataset.")
            book = random_book_suggestion(df)
        else:
            print(f"\nFound {len(filtered_df)} books matching your criteria.")
            print(filtered_df[['title', 'authors', 'genres', 'published_year', 'edition_count']].head())
            book = random_book_suggestion(filtered_df)

        if book is not None:
            print("\nRandom Book Suggestion:")
            print(f"Title: {book['title']}")
            print(f"Author(s): {book['authors']}")
            print(f"Genre(s): {book['genres']}")
            print(f"Published Year: {book['published_year']}")
            print(f"Edition Count: {book['edition_count']}")
        else:
            print("No book found for the suggestion.")

        again = input("\nDo you want to filter again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the Book Suggestion Bot. Goodbye!")
            break

if __name__ == "__main__":
    main()
