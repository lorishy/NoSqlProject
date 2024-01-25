import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from fonctions.fonction_3 import aggregation_function_3

st.set_page_config(
    page_title="Stats Ligues",
    page_icon="⚽",
)

# Connexion à la base de données MongoDB
client = MongoClient()
db = client["IPSSI"]
collection = db["DbFootball"]

# Titre de l'application
st.title("Statistiques Football - Par ligue")

# Fonction d'aggrégation 3
result_3 = aggregation_function_3(collection)
result_df_3 = pd.DataFrame(result_3)
fig, ax = plt.subplots()
ax.bar(result_df_3["_id"], result_df_3["total_goals"])
ax.set_xlabel("Ligues")
ax.set_ylabel("Nombre total de buts")
ax.set_xticklabels(result_df_3["_id"], rotation=45, ha="right")
plt.tight_layout()
st.subheader("Nombre total de buts par ligue")
st.pyplot(fig)