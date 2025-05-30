# 📚 Book Suggestion Bot

This is a simple Python-based command-line application that fetches book data using the Google Books API and provides personalized book recommendations based on filters like genre, popularity, and publication year.

---

## 🚀 Features

- Fetch real-time book data from **Google Books API**
- Save and load data using **CSV files**
- Filter books by:
  - Genre
  - Minimum popularity (rating)
  - Publication year range
- Get **random book suggestions**
- CLI-based interactive experience

---

## 🛠️ Technologies Used

- Python 3.x
- `requests` for API interaction
- `pandas` for data manipulation
- `random` and `time` for utility functions

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/book-suggestion-bot.git
   cd book-suggestion-bot
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   > You may need to manually create a `requirements.txt` file with:
   > ```
   > requests
   > pandas
   > ```

---

## ▶️ Usage

Run the main script:

```bash
python book_bot.py
```

### Options in the app:
- Choose to fetch fresh data from the API or load from an existing CSV
- Apply filters like genre, popularity, and publication year
- View a few book recommendations
- Get a **random book suggestion** from the filtered results

---

## 📁 File Overview

| File              | Description                                      |
|-------------------|--------------------------------------------------|
| `book_bot.py`     | Main script containing all the logic             |
| `books_data.csv`  | (Generated) CSV file storing book data           |
| `README.md`       | Project overview and instructions                |

---

## 🔧 Sample Functionality

- **Fetch Books**  
  Query Google Books API and retrieve book details like title, authors, genres, publication year, and ratings.

- **Filter Books**  
  Filter books using flexible options:
  ```python
  filter_books(df, genre="Fiction", min_popularity=3.5, min_year=2015)
  ```

- **Suggest a Random Book**
  ```python
  random_book_suggestion(filtered_df)
  ```

---

## ❗ Notes

- Google Books API limits `maxResults` to 40 items per request.
- The `ranking` field is a placeholder and not used since the API doesn't provide rank data.
- Make sure you are connected to the internet when fetching new data.

---

## ✅ To Do

- Add support for pagination and more results
- Add support for more detailed user preferences
- Create a simple GUI version

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Your Name**  
Feel free to reach out via GitHub or contribute to improve the project!
# Python-Project-Submission
