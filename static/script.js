const titleBox = document.getElementById("title");
const descBox = document.getElementById("description");
const button = document.getElementById("btn");
const releaseBox = document.getElementById("release-date");
const posterBox = document.getElementById("poster");
const trailerBox = document.getElementById("trailer");
const genreSelect = document.getElementById("genre");


function selectGenre() {
    fetch("/genre")
        .then(response => response.json())
        .then(genres => {
            genres.forEach(genre => {
                const option = document.createElement("option");
                option.value = genre.id;
                option.textContent = genre.name;
                genreSelect.appendChild(option);
            });
        })
        .catch(err => console.error("Error loading genres:", err));
}

selectGenre();

function fetchMovie() {
    const selectedGenre = genreSelect.value;

    fetch(`/movie?genre_id=${selectedGenre}`)
        .then(response => response.json())
        .then(data => {
            titleBox.textContent = data.title;
            descBox.textContent = data.overview;
            releaseBox.textContent = data.release_date;
            posterBox.src = data.poster;
            posterBox.alt = data.title;
            if (data.trailer) {
                trailerBox.innerHTML = `<iframe width="560" height="315"
                    src="${data.trailer.replace("watch?v=", "embed/")}"
                    title="Trailer"
                    frameborder="0"
                    allowfullscreen></iframe>`;
            } else {
                trailerBox.textContent = "No trailer available";
            }
        })
        .catch(error => console.error("Error:", error))
        .finally(() => {

        });
}

fetchMovie();
button.addEventListener("click", fetchMovie);
