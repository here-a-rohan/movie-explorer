import "bootstrap/dist/css/bootstrap.min.css";
import "./style.css";
import { getMovies } from "./api";

document.addEventListener("DOMContentLoaded", () => {
  const el = document.getElementById("movies");
  const btn = document.getElementById("btnSearch");

  if (!el || !btn) {
    console.error("❌ Required DOM elements not found");
    return;
  }

  // Function to fetch and render movies
  async function load() {
    el.innerHTML = `<div class="loading">Loading...</div>`;

    try {
      const filters = {
        title: document.getElementById("search").value,
        year: document.getElementById("year").value,
        rating: document.getElementById("rating").value,
      };

      // Remove empty filters so we don't send unnecessary query params
      Object.keys(filters).forEach(k => !filters[k] && delete filters[k]);

      const movies = await getMovies(filters);

      if (!movies.length) {
        el.innerHTML = `<p class="text-center">No movies found</p>`;
        return;
      }

      // Render movie cards
      el.innerHTML = movies.map(m => `
        <div class="col-md-4">
          <div class="card h-100 shadow-sm">
            <div class="card-body">
              <h5>${m.title}</h5>
              <p>🎞 ${m.genre}</p>
              <p>📅 ${m.year}</p>
              <p>⭐ ${m.rating}</p>
            </div>
          </div>
        </div>
      `).join("");

    } catch (err) {
      console.error(err);
      el.innerHTML = `<p class="text-danger text-center">Failed to load movies</p>`;
    }
  }

  // Search button click
  btn.addEventListener("click", load);

  // Press Enter in search box triggers search
  document.getElementById("search").addEventListener("keypress", (e) => {
    if (e.key === "Enter") load();
  });

  // Initial load
  load();
});
