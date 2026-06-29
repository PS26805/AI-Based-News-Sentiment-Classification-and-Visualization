import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="News Sentiment Analysis Dashboard",
    page_icon="📰",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
import pandas as pd

file_id = "16vUX3V7p80oa5MbJiQRNup2OGIDZln6r"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

df = pd.read_csv(url)

# ---------------- HEADER ----------------
st.title("📰 News Sentiment Analysis Dashboard")
st.markdown("### AI-Based News Sentiment Classification and Visualization")

# ---------------- DATASET INFO ----------------
with st.expander("📋 Dataset Information", expanded=True):
    st.write(f"*Total Records:* {len(df)}")
    st.write("*Features:*")
    st.write("- Headline")
    st.write("- Category")
    st.write("- Sentiment")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 Dashboard Menu")

category_filter = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["category"].dropna().unique().tolist())
)

# ---------------- FILTER DATA ----------------
filtered_df = df.copy()

if category_filter != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == category_filter
    ]

# ---------------- PROJECT STATISTICS ----------------
st.header("📊 Project Statistics")

col1, col2, col3 = st.columns(3)

positive = len(
    filtered_df[
        filtered_df["Sentiment"] == "Positive"
    ]
)

negative = len(
    filtered_df[
        filtered_df["Sentiment"] == "Negative"
    ]
)

neutral = len(
    filtered_df[
        filtered_df["Sentiment"] == "Neutral"
    ]
)

col1.metric("Total Headlines", len(filtered_df))
col2.metric("Positive News", positive)
col3.metric("Negative News", negative)
co14.metric("Neutral News",neutral)

# ---------------- DATASET PREVIEW ----------------
st.header("📋 Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# ---------------- SENTIMENT DISTRIBUTION ----------------
st.header("📈 Sentiment Distribution")

sentiment_counts = filtered_df["Sentiment"].value_counts()

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(
    sentiment_counts.index,
    sentiment_counts.values
)
ax1.set_xlabel("Sentiment")
ax1.set_ylabel("Count")
ax1.set_title("Sentiment Distribution")
st.pyplot(fig1)

# ---------------- PIE CHART ----------------
st.header("🥧 Sentiment Breakdown")

fig2, ax2 = plt.subplots(figsize=(6, 6))

ax2.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%"
)

ax2.set_title("Sentiment Percentage")

st.pyplot(fig2)

# ---------------- CATEGORY DISTRIBUTION ----------------
st.header("📂 Category Distribution")

category_counts = (
    filtered_df["category"]
    .value_counts()
    .head(10)
)

fig3, ax3 = plt.subplots(figsize=(10, 5))

ax3.bar(
    category_counts.index,
    category_counts.values
)

ax3.set_xlabel("Category")
ax3.set_ylabel("Count")
ax3.set_title("Top 10 Categories")

plt.xticks(rotation=45)

st.pyplot(fig3)

# ---------------- END ----------------
st.success("Dashboard Analysis Completed Successfully")