import streamlit as st #criar dashboard
import pandas as pd #manipular dados
import plotly.express as px #construir gráficos

st.set_page_config(layout="wide")
df = pd.read_csv("supermarketSales.csv", sep=";", decimal=",")

#executar no terminal streamlit run dashboard.pY

#Perguntas:
#Combobox: com o mês/ano (visão mensal de vendas)
#Faturamento da unidade
#Tipo de produto vendido
#Contribuição por filial
#Desempenho da forma de pagamento
#Como foram as avaliações por flilais

df["Date"]=pd.to_datetime(df["Date"])
df=df.sort_values(["Date"])

#visão mensal e criar um controlador por combobox
df["Month"]=df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month=st.sidebar.selectbox("Mês",df["Month"].unique())

df_filter = df[df["Month"]==month]

#df_filter
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filter, x="Date", y="Total", color="City", barmode="group", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width= True)

fig_prod = px.bar(df_filter, x="Date", y="Product line", color="City", barmode="group", title="Faturamento por tipo de produto", orientation ="h")
col2.plotly_chart(fig_prod, use_container_width= True)

city_total = df_filter.groupby("City")[("Total")].sum().reset_index()

fig_city = px.bar(city_total, x="City", y="Total", barmode="group", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width= True)

df_filter = df[df["Month"]==month]
fig_kind = px.pie(df_filter, values="Quantity", names="Payment", title="Faturamento por tipo pagamento")
col4.plotly_chart(fig_kind, use_container_width= True)

avaliacao_total = df_filter.groupby("City")[("Rating")].mean().reset_index()
fig_avaliacao = px.bar(city_total, x="City", y="Rating", barmode="group", title="Avaliação")
col5.plotly_chart(fig_avaliacao, use_container_width= True)