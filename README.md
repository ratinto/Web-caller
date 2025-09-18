# Lightweight Flask App for Render

This is a minimal Flask web app with a self-pinging API to prevent sleeping on Render or similar platforms.

## Features
- `/ping` endpoint returns a simple JSON response.
- Background thread pings the `/ping` endpoint every 3 seconds to keep the app awake.

## Deployment (Render)
1. **Add Environment Variable:**
   - `SELF_URL` = `https://<your-render-url>/ping`
2. **Build Command:**
   - `pip install -r requirements.txt`
3. **Start Command:**
   - `python app.py`

## Local Development
```sh
pip install -r requirements.txt
python app.py
```

## Notes
- The app listens on port 5000 by default.
- The self-ping thread uses the `SELF_URL` environment variable if set, otherwise defaults to `http://localhost:5000/ping`.
