# Minigame Arcade (Streamlit)

A single-page Streamlit app with tabs for Sudoku, Word Search, and a mini Crossword.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL Streamlit prints (usually http://localhost:8501).

## Project structure

```
minigames/
├── app.py            # all game logic + tab layout
├── requirements.txt  # just streamlit
└── README.md
```

Everything lives in `app.py` for now, split into one `render_<game>()` function
per tab. As you add more games, it's worth splitting each into its own file
(e.g. `games/sudoku.py`) and importing them into `app.py` — the structure
already supports that with minimal changes.

## Adding a new game

1. Write a `render_mygame()` function that draws its UI with Streamlit widgets
   and reads/writes its state via `st.session_state` (so it survives reruns).
2. Add a new tab in `main()`:
   ```python
   tab1, tab2, tab3, tab4 = st.tabs([..., "🧩 My Game"])
   with tab4:
       render_mygame()
   ```

## Hosting it for free — Streamlit Community Cloud

1. Push this folder to a public (or private) GitHub repo.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "New app", pick the repo/branch, and set the main file path to
   `app.py`.
4. Deploy. You'll get a URL like `https://your-app-name.streamlit.app`.
5. Any push to the connected branch auto-redeploys the app.

Free tier notes: apps sleep after inactivity and wake on the next visit
(a few seconds of cold start), and there are limits on resources/private
repos on the free tier — check current details at
https://streamlit.io/cloud before relying on it for production traffic.

## Other hosting options

- **Docker + any cloud host** (Render, Fly.io, a VPS, AWS/GCP/Azure):
  wrap the app in a `Dockerfile` that runs
  `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`.
- **Hugging Face Spaces**: supports Streamlit natively as a Space type,
  free for small apps.
- **Self-hosted behind nginx**: run `streamlit run app.py` behind a
  reverse proxy with a process manager (systemd, pm2, supervisor) for
  a custom domain.

Streamlit Community Cloud is the easiest starting point if you just want
a shareable link without managing servers.
