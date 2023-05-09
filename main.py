import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.header(":green[Aplikasi Pengolahan Data dalam Statistika]")
    
    # Memasukkan data manual
    st.header("Masukkan Data!:point_right::point_left:")
    rows = st.number_input("Jumlah Baris Data:", min_value=1, value=1)
    cols = st.number_input("Jumlah Kolom Data:", min_value=1, value=1)
    
    data = []
    for i in range (rows):
        row = []
        for j in range(cols):
            value = st.number_input(f"Data Baris {i+1}, Kolom {j+1}", value=0.00)
            row.append(value)
        data.append(row)
        
    df = pd.DataFrame(data)
    st.write("Data yang Dimasukkan:")
    st.write(df)
    
 # Menghitung nilai rata-rata, median, range, simpangan rata-rata, ragam, dan simpangan baku
    st.header("Hasil Pengolahan Data:memo:")
    st.write("Rata-rata: ", np.mean(data))
    st.write("Median: ", np.median(data))
    st.write("Range/Jangkauan: ", np.round(np.var(data), 2))
    st.write("Simpangan Rata-rata: ", np.round(np.mean(np.abs(data - np.mean(data))), 2))
    st.write("Ragam/Variasi: ", np.round(np.max(data)-np.min(data), 2))
    st.write("Simpangan Baku/Standar Deviasi: ", np.round(np.std(data), 2))
    
if __name__ == '__main__':
    main()