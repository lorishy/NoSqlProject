import streamlit as st
import pandas as pd
from pymongo import MongoClient
from fonctions.fonction_4 import aggregation_function_4
from fonctions.fonction_6 import aggregation_function_6

st.set_page_config(
    page_title="Stats Joueurs",
    page_icon="⚽",
)

# Connexion à la base de données MongoDB
client = MongoClient()
db = client["IPSSI"]
collection = db["DbFootball"]

# Titre de l'application
st.title("Statistiques Football - Par joueurs")

# Fonction d'aggrégation 4
result_4 = aggregation_function_4(collection)
result_df_4 = pd.DataFrame(result_4)
result_df_4 = result_df_4.rename(columns={"_id": "Joueur", "avg_minutes_played": "Moyenne des minutes jouées"})
st.subheader("Top 20 des joueurs ayant le plus de minutes jouées")
st.table(result_df_4.style.format({
    'Moyenne des minutes jouées': '{:.2f}'
}))

# Fonction d'aggrégation 6
result_6 = aggregation_function_6(collection)
result_df_6 = pd.DataFrame(result_6)
result_df_6 = result_df_6.rename(columns={"_id": "Joueur", "goals_per_match": "Moyenne des buts par match"})
st.subheader("Top 20 des joueurs ayant la plus grosse moyenne de but par match")
st.table(result_df_6.style.format({
    'Moyenne des buts par match': '{:.2f}'
}))