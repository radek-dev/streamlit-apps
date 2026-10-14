# streamlit-apps

Public [Streamlit](https://streamlit.io) apps, showcased in the [Notebook Gallery](https://radek-dev.github.io/notebook-gallery/).

| App | Description |
| :-- | :-- |
| `app.py` | Customer segmentation with K-means on synthetic data |

## Run locally

```sh
uv run --with-requirements requirements.txt streamlit run app.py
```

## Deploy

Deploy from this repo on [Streamlit Community Cloud](https://share.streamlit.io) with `app.py` as the entry point. Keep any credentials in the platform's secrets settings, never in the repo.
