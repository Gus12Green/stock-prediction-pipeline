import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_pickle("predictions.pkl")

st.title("Predicción de Cotización de IBM 📈")
st.write("Visualización de las predicciones para los próximos 60 minutos.")

st.subheader("Predicciones")
df_display = df.rename(columns={"timestamp": "Fecha y Hora", "prediction": "Precio ($)"})
st.dataframe(df_display.set_index("Fecha y Hora"))

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["timestamp"], y=df["prediction"], mode="lines+markers", name="Predicción"))
fig.update_layout(title="Predicción de IBM", xaxis_title="Fecha y Hora", yaxis_title="Precio ($)")
st.plotly_chart(fig)
