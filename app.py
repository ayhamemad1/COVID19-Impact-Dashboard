import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")

st.title("🦠 COVID-19 Impact Analysis Dashboard (Top 15 Countries)")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("covid_19_clean_complete.csv")
    df.rename(columns={'Country/Region': 'Country', 'Province/State': 'Province', 'Date': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Province'] = df['Province'].fillna("N/A")
    df.fillna(0, inplace=True)
    df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']
    return df

df = load_data()
latest_date = df['Date'].max()

top_countries = df[df['Date'] == latest_date].groupby('Country')['Confirmed']     .sum().sort_values(ascending=False).head(15).index.tolist()

df_top = df[df['Country'].isin(top_countries)]
df_grouped = df_top.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered', 'Active']]     .sum().reset_index()

st.subheader("📊 KPI Summary (Latest Date)")
kpi_summary = df_grouped[df_grouped['Date'] == latest_date].groupby('Country')[
    ['Confirmed', 'Deaths', 'Recovered', 'Active']
].sum()
st.dataframe(kpi_summary)

st.subheader("📈 Confirmed Cases Over Time")
fig, ax = plt.subplots(figsize=(12, 6))
for country in top_countries:
    country_data = df_grouped[df_grouped['Country'] == country]
    ax.plot(country_data['Date'], country_data['Confirmed'], label=country)
ax.set_title("Confirmed Cases Over Time - Top 15 Countries")
ax.set_xlabel("Date")
ax.set_ylabel("Confirmed Cases")
ax.legend(loc='upper left', fontsize='small')
st.pyplot(fig)

st.subheader("🔥 Correlation Heatmap of KPIs")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.heatmap(kpi_summary.corr(), annot=True, cmap='coolwarm', ax=ax2)
ax2.set_title("Correlation Heatmap - COVID-19 KPIs")
st.pyplot(fig2)
