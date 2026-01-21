# Movie Explorer (FastAPI + Vite + Bootstrap)

A full-stack Movie Explorer platform to browse and filter movies, and view details (cast, director, genres).
No authentication required.

## Tech Stack
- Backend: FastAPI, SQLAlchemy, SQLite
- Frontend: Vite + Vanilla JS + Bootstrap
- Docker: Docker Compose

## Features
- Movies list with search + filters (server-side filtering)
- Movie details page (separate URL using `?id=`)
- Swagger/OpenAPI docs at `/docs`
- Dockerized frontend + backend

## URLs
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- Swagger: http://localhost:8000/docs

---

## Run with Docker

From the repo root:

```bash
docker compose up -d --build
