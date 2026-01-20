const BASE_URL = "http://localhost:8000";

export async function getMovies(filters = {}) {
  const params = new URLSearchParams(filters);
  const res = await fetch(`http://localhost:8000/movies?${params.toString()}`);
  if (!res.ok) throw new Error("API failed");
  return res.json();
}

