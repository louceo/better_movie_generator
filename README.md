# Movie Generator

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
