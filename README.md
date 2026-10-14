# streamlit-apps

Public [Streamlit](https://streamlit.io) apps, showcased in the [Notebook Gallery](https://radek-dev.github.io/notebook-gallery/).

| App | Description | Live |
| :-- | :-- | :-- |
| `app.py` | Customer segmentation with K-means on synthetic data | [customer-segments-demo.streamlit.app](https://customer-segments-demo.streamlit.app/) |

Related: [notebook-gallery](https://github.com/radek-dev/notebook-gallery) · [marimo-notebooks](https://github.com/radek-dev/marimo-notebooks) · [quarto-notebooks](https://github.com/radek-dev/quarto-notebooks)

## Run locally

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/). The environment is locked in `uv.lock`.

```sh
uv sync                        # create .venv from uv.lock
uv run streamlit run app.py
```

Add packages with `uv add <package>`.

## Deploy

Deploy from this repo on [Streamlit Community Cloud](https://share.streamlit.io) with `app.py` as the entry point. Community Cloud installs dependencies from `uv.lock`, so don't add a `requirements.txt` alongside it. Keep any credentials in the platform's secrets settings, never in the repo.
