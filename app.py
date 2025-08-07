import os, pandas as pd, streamlit as st, plotly.express as px
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RAW = os.path.join(DATA_DIR, "raw_batches_2025YTD.csv")
WEEKLY = os.path.join(DATA_DIR, "weekly_market_share.csv")
st.set_page_config(page_title="NIFDC Albumin", layout="wide")
st.title("NIFDC Human Serum Albumin — Weekly Market Share (2025 YTD)")
if not (os.path.exists(RAW) and os.path.exists(WEEKLY)):
    st.warning("No CSVs yet. Run the GitHub Action 'Scrape NIFDC (2025 YTD)' to populate data.")
else:
    raw = pd.read_csv(RAW, dtype=str)
    weekly = pd.read_csv(WEEKLY, dtype=str)
    for c in weekly.columns:
        if c.startswith(("share_","total_")) or c in ["batch_count","quantity_bottles","grams_total"]:
            weekly[c] = pd.to_numeric(weekly[c], errors="coerce")
    unit = st.sidebar.selectbox("Unit", ["batch_count","quantity_bottles","grams_total"])
    region = st.sidebar.selectbox("Region", sorted(weekly["region"].dropna().unique().tolist()))
    makers = sorted(weekly["manufacturer_norm"].dropna().unique().tolist())
    sel = st.sidebar.multiselect("Manufacturers", makers)
    df = weekly.copy()
    df = df[df["region"]==region]
    if sel: df = df[df["manufacturer_norm"].isin(sel)]
    share_col = {"batch_count":"share_batch_count","quantity_bottles":"share_quantity_bottles","grams_total":"share_grams_total"}[unit]
    st.plotly_chart(px.line(df, x="week_label", y=share_col, color="manufacturer_norm"), use_container_width=True)
    st.dataframe(df)
