import streamlit as st
import pandas as pd
import plotly.express as px
from database import init_db, insert_reading, get_all_readings, delete_reading, seed_data
from datetime import date

# Init
init_db()
seed_data()

st.set_page_config(page_title="Energy Monitor", page_icon="⚡", layout="wide")
st.title("⚡ Energy Monitoring Dashboard")
st.caption("Strom- und Gasverbrauch nach Depot — PSI-Style")

# ── Sidebar: Neuen Eintrag hinzufügen ──────────────────────────────────────
st.sidebar.header("Neuen Verbrauch eintragen")

depot   = st.sidebar.selectbox("Depot", ["Berlin", "Hamburg", "Dortmund", "Frankfurt", "München"])
type_   = st.sidebar.radio("Typ", ["Strom", "Gas"])
value   = st.sidebar.number_input("Verbrauch (kWh)", min_value=0.1, max_value=9999.0, value=300.0)
date_in = st.sidebar.date_input("Datum", value=date.today())

if st.sidebar.button("➕ Eintrag speichern"):
    insert_reading(depot, type_, value, str(date_in))
    st.sidebar.success("Gespeichert!")
    st.rerun()

# ── Daten laden ────────────────────────────────────────────────────────────
rows = get_all_readings()
df = pd.DataFrame(rows, columns=["ID", "Depot", "Typ", "kWh", "Datum"])
df["Datum"] = pd.to_datetime(df["Datum"])

# ── KPI-Zeile ──────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Einträge gesamt",  len(df))
col2.metric("Ø Strom (kWh)",   round(df[df["Typ"]=="Strom"]["kWh"].mean(), 1))
col3.metric("Ø Gas (kWh)",     round(df[df["Typ"]=="Gas"]["kWh"].mean(), 1))

st.divider()

# ── Charts ─────────────────────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Verbrauch nach Depot")
    fig1 = px.bar(
        df.groupby(["Depot", "Typ"])["kWh"].sum().reset_index(),
        x="Depot", y="kWh", color="Typ",
        barmode="group",
        color_discrete_map={"Strom": "#00C4A7", "Gas": "#FF6B35"}
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("Verbrauch über Zeit")
    fig2 = px.line(
        df.sort_values("Datum"),
        x="Datum", y="kWh", color="Depot", line_dash="Typ",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── Tabelle mit Löschen ────────────────────────────────────────────────────
st.divider()
st.subheader("Alle Einträge")

for _, row in df.iterrows():
    c1, c2, c3, c4, c5 = st.columns([2, 1, 1, 2, 1])
    c1.write(row["Depot"])
    c2.write(row["Typ"])
    c3.write(f"{row['kWh']} kWh")
    c4.write(row["Datum"].strftime("%Y-%m-%d"))
    if c5.button("🗑️", key=f"del_{row['ID']}"):
        delete_reading(row["ID"])
        st.rerun()