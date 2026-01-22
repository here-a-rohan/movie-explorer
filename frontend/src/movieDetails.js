import { getMovieById } from "./api";

document.addEventListener("DOMContentLoaded", async () => {
  const el = document.getElementById("movieDetails");

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id");

  if (!id) {
    el.innerHTML = "<p>No movie selected</p>";
    return;
  }

  try {
    const movie = await getMovieById(id);

    el.innerHTML = `
      <h1>${movie.title}</h1>

      <div class="meta">📅 Year: ${movie.year}</div>
      <div class="meta">⭐ Rating: ${movie.rating}</div>
      <div class="meta">🎬 Director: ${movie.director?.name || "-"}</div>

      <div class="section">
        <strong>Genres</strong>
        <div class="badges">
          ${movie.genres.map(g => `<span class="badge">${g.name}</span>`).join("")}
        </div>
      </div>

      <div class="section">
        <strong>Cast</strong>
        <div class="cast">
          ${movie.actors.map(a => `<span>${a.name}</span>`).join("")}
        </div>
      </div>
    `;
  } catch (err) {
    el.innerHTML = "<p>Failed to load movie</p>";
    console.error(err);
  }
});
