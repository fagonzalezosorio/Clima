import streamlit as st
import pandas as pd
import numpy as np
import datetime
# from streamlit_autorefresh import st_autorefresh
import pyautogui
import time
codigo_secreto = 'ahahah33'

############## funciones ########################

def crear_evento():
    input_fecha = st.date_input("Seleccione una fecha:", None)   #st.text_input("Ingrese fecha del evento:")

    if input_fecha:
        if input_fecha.strftime('%Y-%m-%d') in df.Fecha.unique():
            st.write("Ya existe un registro con la fecha indicada. Por favor elige otra fecha!")

            st.write("registro existente:")
            st.dataframe(df[df.Fecha == input_fecha.strftime('%Y-%m-%d')][['Fecha','mm','observacion']])
            #deberia dar la opcion de editar o eliminar el registro.
            return "hola" #finaliza la funcion
        
        input_mm = st.text_input("Ingrese monto en mm del evento:")
        if input_mm:
            try:
                int(input_mm)
                
            except ValueError:
                st.write("La cantidad debe ser un numero")
                return("hola")
            

            input_comentario = st.text_input("ingrese algún comentario u observacion del evento")
            if input_comentario:
                st.write("¿Deseas continuar con las opciones?")
                col1, col2, col3,col4 = st.columns(4) #(1,1,1,1,1)

                if col2.button("No"):
                    st.write("haz seleccionado No. La pagina se reiniciara!")
                    time.sleep(1)
                    pyautogui.hotkey("ctrl","F5")

                if col1.button("Sí"):
                    año = input_fecha.year; mes =  input_fecha.month;  dia =  input_fecha.day
                    aux = pd.DataFrame({"Año" : [año], "Mes" : [mes], "Dia" : [dia], "mm" : [input_mm], "observacion": [input_comentario]})
                    df3 = pd.concat([df2,aux], ignore_index=True).reset_index(drop = True)

                    with pd.ExcelWriter("Datos/Lluvia (1).xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                        df3.to_excel(writer,sheet_name= "Lluvia", index=False)
                    st.write("El registro ha sido ingresado satisfactoriamente")
                    time.sleep(2)
                    pyautogui.hotkey("ctrl","F5")




def actualizar_evento():
    st.write("funcion no disponible")

def eliminar_evento():
    fecha_eliminar = st.selectbox("seleccionar fecha a eliminar",[""] + np.sort(df.Fecha.unique())[::-1].tolist())

    if fecha_eliminar:
        st.write("esta seguro que desea eliminar dicho registro")
        st.dataframe(df[df.Fecha == fecha_eliminar])
        df3 = df2[(df2.Año != int(fecha_eliminar[0:4])) |(df2.Mes != int(fecha_eliminar[5:7])) | (df2.Dia != int(fecha_eliminar[8:10]))]

        st.write("¿Deseas continuar con las opciones?")
        col1, col2, col3,col4 = st.columns(4) #(1,1,1,1,1)

        if col2.button("No"):
            st.write("haz seleccionado No. La pagina se reiniciara!")
            time.sleep(1)
            pyautogui.hotkey("ctrl","F5")

        if col1.button("Sí"):
            with pd.ExcelWriter("Datos/Lluvia (1).xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df3.to_excel(writer,sheet_name= "Lluvia", index=False)

            st.write("El registro ha sido eliminado satisfactoriamente")
            time.sleep(2)
            pyautogui.hotkey("ctrl","F5")



### despliegue



st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 40px; font-weight:bold; text-shadow: 2px 2px 4px #000000;"> Mantenedor de datos </p>', unsafe_allow_html=True)
st.markdown("         ")
st.markdown("         ")


crud = st.selectbox("¿Que deseas realizar?",['Ingresar un nuevo registro','Modificar un registro existente','Eliminar un registro existente'])

## cargamos los datos

df=pd.read_excel("Datos/Lluvia (1).xlsx")
df2 = df.copy()
df = df.dropna(how='all')

cols = df.columns.tolist()
df = df.rename(columns = dict(zip(cols,[str(col).strip() for col in cols])) )
df["Fecha"] = pd.to_datetime(dict(year=df["Año"], month=df["Mes"], day=df["Dia"]))
df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')
df['Año'] = df['Año'].astype(int)
# df = df[df.Mes.notna()]
df['Mes'] = df['Mes'].astype(int)


if crud == 'Ingresar un nuevo registro': 
    crear_evento()
elif crud == 'Modificar un registro existente': 
    actualizar_evento()

elif crud == 'Eliminar un registro existente': 
    eliminar_evento()


# st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 30px; font-weight:bold; text-shadow: 2px 2px 4px #000000;"> Modificar registro existente </p>', unsafe_allow_html=True)
# st.markdown("         ")
# st.markdown("         ")

# input_fecha = st.date_input("Seleccione una fecha:", datetime.date.today())   #st.text_input("Ingrese fecha del evento:")
# input_mm = st.text_input("Ingrese monto en mm del evento:")
# input_comentario = st.text_input("ingrese algún comentario u observacion del evento")

# st.markdown(f'<p style="font-family:Calibri Light; color:Black; font-size: 30px; font-weight:bold; text-shadow: 2px 2px 4px #000000;"> desea modificar el evento del {input_fecha} con el monto de {input_mm} </p>', unsafe_allow_html=True)

# st.write("¿Deseas continuar con las opciones?")
# col1, col2 = st.columns(2)

# if col1.button("Sí"):
#     st.write("haz seleccionado si")

# if col1.button("No"):
#     st.write("haz seleccionado no")



# df=pd.read_excel("Datos/Lluvia (1).xlsx")
# df = df.dropna(how='all')
# cols = df.columns.tolist()
# df = df.rename(columns = dict(zip(cols,[str(col).strip() for col in cols])) )




########################################## RESUMEN MENSUAL-ANUAL ##################################3

# df["Fecha"] = pd.to_datetime(dict(year=df["Año"], month=df["Mes"], day=df["Dia"]))
# df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')
# df['Año'] = df['Año'].astype(int)
# df = df[df.Mes.notna()]
# df['Mes'] = df['Mes'].astype(int)

# mes = range(1,12)
# nombre = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
# mes_nombre = dict(zip(mes,nombre))
# nombre_mes = dict(zip(nombre,mes))
# df['mes_nombre'] = df.Mes.apply(lambda x: mes_nombre[x])


# ## creamos columnas
# col1,col2,col3 = st.columns((3,1,3))
# col1.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 20px; font-weight:bold;"> Lluvias en el periodo seleccionado: </p>', unsafe_allow_html=True)

# filtro_año=col2.selectbox("Año",df["Año"].unique())
# df_filtered= df.query('Año == @filtro_año')

# filtro_meses = col3.multiselect('Meses',df_filtered['mes_nombre'].unique())



# col1, col2 = st.columns((5,2))


# ##### df filtrado
# #
# filtro_meses_str = ', '.join([f'"{mes}"' for mes in filtro_meses])

# # Filtrar el DataFrame usando query
# if filtro_meses_str:
#     query_str = f'mes_nombre in [{filtro_meses_str}]'
#     df_filtered = df_filtered.query(query_str)
# else:
#     df_filtered = df_filtered




# col2.dataframe(df_filtered[['Fecha','mm']],  height=360)

# ### grafico mensual

# # Crear el gráfico de barras
# fig, ax = plt.subplots(figsize=(6, 4))
# ax.bar(df_filtered['Fecha'], df_filtered['mm'])
# ax.set_ylabel('Lluvia acumulada [mm]')
# ax.grid(True)
# plt.xticks(rotation=45)

# # Mostrar el gráfico en Streamlit
# col1.pyplot(fig)



# ########################################## RESUMEN HISTORICO ##################################3
# col1.markdown("         ")
# col2.markdown("         ")
# st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 20px; font-weight:bold;">Resumen historico de  lluvias </p>', unsafe_allow_html=True)
# col1, col2 = st.columns((5,2))
# col1.markdown("         ")
# col2.markdown("         ")


# # df2 = pd.pivot_table(df,index = 'Año', columns='mes_nombre', values='mm', aggfunc='sum', fill_value=0)

# # order_cols = sorted([nombre_mes[col] for col in df2.columns])
# # df2 = df2[[mes_nombre[col] for col in order_cols]]

# # df2.loc['Total'] = df2.sum(numeric_only=True)
# # df2['Total'] = df2.sum(axis=1, numeric_only=True)

# # col1.dataframe(df2.replace(0,""))
# col1.write('Fuente: Casa')

# ## historico conaf


# conaf=pd.read_excel("Datos/Lluvia (1).xlsx", sheet_name= 'conaf')
# conaf['Año'] = conaf['Año'].astype(int).astype(str)
# conaf = conaf.dropna(how='all')


# col2.dataframe(conaf,height=250)
# col2.write('Fuente: Conaf')


