# Niranjan Deal Finder

Niranjan Deal Finder is a full-stack application that compares products across multiple e-commerce platforms (Amazon, Flipkart, Meesho, Myntra, JioMart) to provide real-time pricing, ratings, and AI-driven recommendations.

## Project Structure
- `frontend/`: Next.js web application built with React, Tailwind CSS, and TypeScript.
- `backend/`: FastAPI Python server that aggregates data via web scraping and API providers.

## Deployment
This project is configured with a GitHub Actions CI pipeline (`.github/workflows/ci.yml`) to test the backend and lint/build the frontend.

For a full deployment guide (Local, Docker, Render, Vercel), see [`DEPLOYMENT.md`](./DEPLOYMENT.md).

## Getting Started

### Local Development
1. Clone the repository.
2. See the `backend/README.md` (or `DEPLOYMENT.md`) to set up the Python FastAPI backend.
3. See `frontend/README.md` to start the Next.js development server.
