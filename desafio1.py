#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt


# In[144]:


df=pd.read_csv(r'G:\Mi unidad\Work\Phydata\curso Eduardo\clase2\accident_2015.csv')
df.head()


# In[ ]:





# ### Identificar, usando consultas y con gráficas las siguientes características del dataset:

# In[37]:


# Contando el número de accidentes por estado
accident_counts = df.groupby('state_name').size()

# Encontrando el estado con el mayor número de accidentes
max_accidents_state = accident_counts.idxmax()
max_accidents_count = accident_counts.max()

print(f"El estado con el mayor número de accidentes es {max_accidents_state} con {max_accidents_count} accidentes.")
accident_counts.plot(kind='bar', color='orange', alpha=0.75)


# In[45]:


# Contando el número de accidentes por land use
accident_counts = df.groupby('land_use_name').size()

# Encontrando el estado con el mayor número de accidentes
max_accidents_land = accident_counts.idxmax()
max_accidents_count = accident_counts.max()

print(f"El terreno con el mayor número de accidentes es {max_accidents_land} con {max_accidents_count} accidentes.")
accident_counts.plot(kind='bar', color='orange', alpha=0.75)


# In[48]:


# Contando el número de accidentes por empresa
accident_counts = df.groupby('ownership_name').size()

# Encontrando el estado con el mayor número de accidentes
max_accidents_owner = accident_counts.idxmax()
max_accidents_count = accident_counts.max()

print(f"La empresa con el mayor número de accidentes es {max_accidents_owner} con {max_accidents_count} accidentes.")
accident_counts.plot(kind='bar', color='orange', alpha=0.75)


# In[84]:


# Contando el número de accidentes por trafficway
accident_counts = df.groupby('trafficway_identifier').size()

# Encontrando el estado con el mayor número de accidentes
max_accidents_carretera = accident_counts.idxmax()
max_accidents_count = accident_counts.max()

print(f"El terreno con el mayor número de accidentes es {max_accidents_carretera} con {max_accidents_count} accidentes.")

accident_counts.plot()
plt.show()

#elejimos solo los mayores a 100 ya que son muchos datos y ensucian nuestra grafica
more_100_accident_counts=accident_counts[accident_counts.values>100]
more_100_accident_counts.plot(kind='bar', color='orange', alpha=0.75)
plt.show()


# ### Realizar un análisis mensual de accidentes por estado. 
# 

# La informacion del mes del accidente esta en al columna month_of_crash (tambien hay una llamada month_of_crash_names), por lo que para cada estado, deberiamos contar la cantidad de veces que aparece ahi. Esto se puede hacer de manera relativamente sencilla con una crosstab (https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html). Las crosstab son una tabla que muestra la frecuencia con la que ciertas interacciones o combinaciones ocurren entre dos (o más) variables. Las crosstabs son útiles para comprender las relaciones entre datos.

# In[ ]:





# In[106]:


monthly_accidents = pd.crosstab(df['state_name'], df['month_of_crash_name'])
monthly_accidents.head()


# In[120]:


monthly_accidents.sum().plot(kind='bar', color='orange', alpha=0.75)
print(f"El Mes con menos accidentes es {monthly_accidents.sum().idxmin()} con {monthly_accidents.sum().min()} accidentes")
print(f"El Mes con mas accidentes es {monthly_accidents.sum().idxmax()} con {monthly_accidents.sum().max()} accidentes")


# In[ ]:





# ### Realizar un análisis según la hora del dia. 
#    - Ahondar para los estados con mayor cantidad de muertes
# 
#    Al igual que el caso anterior se puede hacer analizando la tabla de frecuencias con un crosstab

# In[132]:


hour_accidents = pd.crosstab(df['state_name'], df['hour_of_crash'])
hour_accidents.head()


# In[172]:


hourly_accidents = df.groupby('hour_of_crash').size()
hourly_accidents.plot(kind='bar', color='orange', alpha=0.75)
plt.ylabel('Frequency')
plt.show()
#esto me cuenta el numero de accidentes, pero puede morir mas de una persona por accidente, asi que para saber en que hora mueren mas personas
#lo que haremo es agrupar por hora del choque y numero de muertes para poder contarlas con sum 

hourly_fatalities = df.groupby('hour_of_crash')['number_of_fatalities'].sum()
hourly_fatalities.plot(kind='bar', color='green', alpha=0.75)
plt.ylabel('number_of_fatalities')
plt.show()


# In[163]:


#los estados con mayor cantidad de muertes se obtienen de la misma manera
#agrupamos por estado y sumamos las muertes de la columna number_of_fatalities, el nlargest 5me muestra los 5 mas grandes
top_states = df.groupby('state_name')['number_of_fatalities'].sum().nlargest(5)
top_states_list = top_states.index.tolist()


# In[170]:


top_states.plot(kind='bar')
plt.ylabel('number of fataliies')


# In[174]:


#analizemos estos 5 en detalle por hora
df_top_states = df[df['state_name'].isin(top_states_list)] #selecciono solo los del top

#agreugamos por nombre  y hora, lo que crea un grupo de cada estado, y cada uno con sus horas,(multi index) 
# luego seleccionamos solo la columna de muertes y sumamos
# el unstack lo usamos para convertir las horas que eran indices en columnas
top_states_hourly_fatalities = df_top_states.groupby(['state_name', 'hour_of_crash_name'])['number_of_fatalities'].sum().unstack()
top_states_hourly_fatalities


# In[183]:


#para visualizar como va quedando
#df_top_states.groupby(['state_name', 'hour_of_crash_name'])['number_of_fatalities'].sum()


# In[184]:


#graficamos los 5 mas grandes por hora con mas muertes
plt.figure(figsize=(14,8))

for state in top_states_list:
    plt.plot(top_states_hourly_fatalities.columns, top_states_hourly_fatalities.loc[state], label=state)

plt.title("Fatalidades por Hora en los Estados con Mayor Cantidad de Muertes")
plt.xlabel("Hora del Día")
plt.ylabel("Número de Fatalidades")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, which="both", ls="--", c='0.65')
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# ### Finalmente realizar un análisis resaltando la razón entre números de accidentes y conductores ebrios. 
# 
# Las columna con esta informacion es  number_of_drunk_drivers

# In[199]:



#el total de accidentes es simplemente el total del df
total_accidents=len(df)

#contamos el numero la frecuencia con la que hay conductores ebrios
df['number_of_drunk_drivers'].value_counts()


# In[200]:


#esto me entrega el numero total de conductores ebrios
accidentes_con_ebrios = df[df['number_of_drunk_drivers'] > 0].shape[0]


# In[206]:


percentage_drunk=int(accidentes_con_ebrios/total_accidents*100)

print(f' Un {percentage_drunk}% de los accidentes involucran al menos 1 persona en estado de ebriedad')


# In[210]:


#queremos hacer un analisis temporal de la razon entre conductores ebrios y el total de accidentes
#para esto creamos una nueva columna "date"
df2=df[['year_of_crash', 'month_of_crash', 'day_of_crash']].rename(columns={'year_of_crash': 'year', 'month_of_crash': 'month', 'day_of_crash': 'day'})
df['date']=pd.to_datetime(df2[['year', 'month', 'day']])
df['date'].head()


# In[217]:


# Accidentes totales por mes
accidentes_totales_por_mes = df.groupby(df['date'].dt.month).size()

# Accidentes con conductores ebrios por mes
accidentes_ebrios_por_mes = df[df['number_of_drunk_drivers'] > 0].groupby(df['date'].dt.month).size()

# Cálculo de la proporción
proporcion_ebrios = accidentes_ebrios_por_mes / accidentes_totales_por_mes


# In[219]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
proporcion_ebrios.plot()
plt.title('Proporción de accidentes relacionados con el alcohol por Mes')
plt.ylabel('Proporción')
plt.xlabel('Mes')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




