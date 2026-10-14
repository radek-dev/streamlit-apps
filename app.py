import numpy as np
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Customer Segments", page_icon="📊", layout="wide")

st.title("Customer Segments")
st.markdown(
    "Cluster **synthetic** customers with K-means and inspect the segments. "
    "No real or personal data is used. "
    "[← Back to the Notebook Gallery](https://radek-dev.github.io/notebook-gallery/)"
)

with st.sidebar:
    st.header("Settings")
    n_customers = st.slider("Number of customers", 100, 2000, 500, step=100)
    k = st.slider("Number of segments (k)", 2, 8, 3)
    seed = st.number_input("Random seed", value=42, step=1)


@st.cache_data
def make_data(n: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    centres = [(20, 8), (60, 3), (35, 15)]
    parts = []
    for spend, visits in centres:
        size = n // len(centres)
        parts.append(
            pd.DataFrame(
                {
                    "annual_spend": rng.normal(spend * 20, 80, size).clip(0),
                    "visits_per_month": rng.normal(visits, 2, size).clip(0),
                    "basket_size": rng.normal(spend / 4, 3, size).clip(1),
                }
            )
        )
    return pd.concat(parts, ignore_index=True)


df = make_data(n_customers, int(seed))
features = ["annual_spend", "visits_per_month", "basket_size"]
scaled = StandardScaler().fit_transform(df[features])
labels = KMeans(n_clusters=k, n_init=10, random_state=int(seed)).fit_predict(scaled)
df["segment"] = "Segment " + pd.Series(labels + 1).astype(str)

left, right = st.columns([2, 1])
with left:
    st.subheader("Spend vs. visits")
    st.scatter_chart(df, x="visits_per_month", y="annual_spend", color="segment")
with right:
    st.subheader("Segment sizes")
    st.bar_chart(df["segment"].value_counts().sort_index())

st.subheader("Segment profiles (average)")
st.dataframe(df.groupby("segment")[features].mean().round(1), width="stretch")

st.caption("Limitations: synthetic data with well-separated groups; real data is messier.")
