import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from fonctions.fonction_1 import aggregation_function_1
from fonctions.fonction_5 import aggregation_function_5

st.set_page_config(
    page_title="Stats pays",
    page_icon="⚽",
)

# Connexion à la base de données MongoDB
client = MongoClient()
db = client["IPSSI"]
collection = db["DbFootball"]

st.title("Statistiques Football - Par pays")

# Fonction d'aggrégation 1
result_1 = aggregation_function_1(collection)
result_df_1 = pd.DataFrame(result_1)
result_df_1 = result_df_1.rename(columns={"_id": "Pays", "total_players": "Nombre de joueurs", "total_matches_played": "Nombre de matchs joués"})
st.subheader("Nombre de joueurs et de matchs joués par pays")
st.table(result_df_1.style.format({'Nombre de joueurs': '{:.0f}', 'Nombre de matchs joués': '{:.0f}'}))

# Fonction d'aggrégation 5
result_5 = aggregation_function_5(collection)
result_df_5 = pd.DataFrame(result_5)
fig, ax = plt.subplots()
ax.bar(result_df_5["_id"], result_df_5["goals_per_match"])
ax.set_xlabel("Pays")
ax.set_ylabel("Buts par match")
ax.set_xticklabels(result_df_5["_id"], rotation=45, ha="right")
plt.tight_layout()
st.subheader("Moyenne de but par match par pays")
st.pyplot(fig)