# Better Movie Generator

A simple full-stack web application that generates a random high-rated movie using the TMDB API, with genre filtering and trailer previews.

![photo_5332321659312083280_w](https://github.com/user-attachments/assets/0003c081-3bb3-4de8-b2f3-bdf8251479cb)

---

## Features

* Random movie generation
* Genre filtering using dynamic TMDB genre IDs
* Movie poster, description, release date, and rating
* Embedded YouTube trailer (when available)
* Avoids immediate duplicate movies
* Clean, minimal user interface

---

## Tech Stack

**Backend**

* Python
* FastAPI
* TMDB API

**Frontend**

* HTML
* CSS 
* JavaScript (Fetch API)

**Testing**

* Pytest
* FastAPI TestClient

---

## Description

This project was built to practice working with real-world APIs and full-stack application flow.

The backend fetches movie data from TMDB, handles pagination and filtering by genre, and returns a random movie.
The frontend consumes the API, dynamically updates the DOM, and embeds trailers using YouTube when available.

---

## What I Learned

* How to read and work with large API documentation
* Structuring a FastAPI backend
* Frontend and backend communication
* Dynamic DOM manipulation with JavaScript
* Handling API edge cases such as empty results and pagination
* Basic state management without a database
* Writing automated tests for API endpoints

---

## Testing

This project includes automated tests for the API endpoints using **pytest** and **FastAPI TestClient**.

### How to Run Tests

1. Make sure all dependencies are installed:

```bash
pip install -r requirements.txt
````

2. Run all tests from the project root:

```bash
pytest -v tests/
```

### What the Tests Cover

* `/movie` endpoint:

  * Status code is 200
  * Response is not empty
  * Response is a dictionary
  * Keys include `title` and `overview`

* `/genre` endpoint:

  * Status code is 200
  * Response is not empty
  * Response is a list of dictionaries
  * Each genre has an `id` field of type integer
  * List is not empty

* Consistency between movie `genre_ids` and available `/genre` IDs

---

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/better-movie-generator.git
```

2. Navigate to the project folder:

```bash
cd better-movie-generator
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

5. Open `index.html` in your browser or use the frontend live server.



