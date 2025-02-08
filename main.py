import seaborn as sns
from matplotlib import pyplot
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(page_title='Custom  Charts')

_file = 'Sample CSV/Bar Data.csv'
df = pd.read_csv(_file)

st.dataframe(df, height=200)

col_title1, col_title2 = st.columns([0.4, 0.6], border=True)
with col_title1:
    selected_title = st.text_input('CHART TITLE')
    selected_title_font_size = st.slider('Title Size', min_value=8, max_value=50)
    
with col_title2:
    # select style
    selected_style=st.radio('STYLE', options=['white', 'dark', 'whitegrid', 'darkgrid', 'ticks'], horizontal=True)
    if selected_style=='white':
        sns.set_style('white')
    if selected_style=='dark':
        sns.set_style('dark')
    if selected_style=='whitegrid':
        sns.set_style('whitegrid')
    if selected_style=='darkgrid':
        sns.set_style('darkgrid')
    if selected_style=='ticks':
        sns.set_style('ticks')


col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.subheader('Chart Data')
    selected_set = st.multiselect('Select Columns', options=df.columns)
    new_df = df[selected_set]

with col2:
    "ddd"
with col3:
    st.subheader('Axis')
    # selected_rot = st.number_input('X Axis Label Rotation', min_value=45, max_value=90)
    selected_rot = st.select_slider('X Axis Label Rotation', options=[0, 45, 90])
    x_selected_label = st.text_input('X Axis Label')
    y_selected_label = st.text_input('Y Axis Label')






# Convert 'Date' column to datetime format for proper plotting
try:
    new_df["Date"] = pd.to_datetime(new_df["Date"])
except:
    st.error('No Data to plot')
else:

    # Melt the dataframe to long format for seaborn
    df_melted = new_df.melt(id_vars=["Date"], var_name="Brand", value_name="Count")

    # Set plot size and style
    plt.figure(figsize=(12, 7))

    # Create a bar plot
    my_plot=sns.barplot(data=df_melted, x="Date", y="Count", hue="Brand")

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=selected_rot)
    plt.xlabel(x_selected_label)
    plt.ylabel(y_selected_label)
    plt.title(selected_title, fontdict={'size':selected_title_font_size, 'name':'Arial'})
    
    # Show the plot
    try:
        st.pyplot(plt)
    except:
        st.warning('No data to plot')
    
    save_to_jpg = st.button('Save to JPG')
    result_file = Path(__file__).parent/'my_test.jpg'
    if save_to_jpg:
        plt.savefig(result_file)

    try:
        result_file = open(result_file, 'rb')
    except:
        st.warning('No File to Download')
    else:
        _dl = st.download_button('Save to Image File', data=result_file, file_name='my_image.jpg')
    
