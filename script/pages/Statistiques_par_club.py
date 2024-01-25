import streamlit as st
import pandas as pd
from pymongo import MongoClient
from fonctions.fonction_2 import aggregation_function_2

st.set_page_config(
    page_title="Stats Clubs",
    page_icon="⚽",
)

# Connexion à la base de données MongoDB
client = MongoClient()
db = client["IPSSI"]
collection = db["DbFootball"]


st.title("Statistiques Football - Par Club")


# Fonction d'aggrégation 2
result_2 = aggregation_function_2(collection)
result_df_2 = pd.DataFrame(result_2)
st.subheader("Top 20 du nombre total de buts marqués par club")
result_df_2['Club_with_Country'] = result_df_2['_id'].apply(lambda x: f"{x['Club']} ({x['Country']})")
result_df_2 = result_df_2.rename(columns={"Club_with_Country": "Club", "total_goals": "Nombre total de buts"})
st.table(result_df_2[['Club', 'Nombre total de buts']].style.format({'Nombre total de buts': '{:.2f}'}))