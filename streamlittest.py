import streamlit as st
import pandas as pd

#st.write("hello from stream")
#text_input = st.text_input("Enter Something")

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(columns=['Date', 'X', 'Y'])

#, 'Demand', 'From', 'To', 'Service', 'Vehicle', 'Capacity'])

col0, col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(10)
#idx= col0.text_input('Idx')
date = col1.date_input('Date of Analysis')
x = col2.text_input('Analysis Type' )
y = col3.text_input('Account' )
# demand = col4.text_input('Demand' )
# from_ = col5.text_input('From')
# to = col6.text_input('To' )
# service = col7.text_input('Service' )
# vehicle = col8.text_input('Vehicle' )
# capacity = col9.text_input('Capacity' )

run = st.button('Submit')

df_new = pd.DataFrame({'Date': date, 
                            'X': x, 
                            'Y': y
                            #'Demand': demand, 
                            #'From': from_, 
                            #'To': to,
                            #'Service': service, 
                            #'Vehicle': vehicle, 
                            #'Capacity': capacity
                            }
                            , index=[len(st.session_state.mdf)]
                            )    
        
if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.dataframe(st.session_state.mdf)
    

st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")


st.table(st.session_state.mdf)