export const API_URL = "http://localhost:8000";

export async function getMovies(filters = {}) {
  const params = new URLSearchParams(filters);
  const res = await fetch(`${API_URL}/movies?${params.toString()}`);
  if (!res.ok) throw new Error("API failed");
  return res.json();
}

export async function getMovieById(id) {
  const res = await fetch(`${API_URL}/movies/${id}`);
  if (!res.ok) throw new Error("Failed to load movie");
  return res.json();
}
