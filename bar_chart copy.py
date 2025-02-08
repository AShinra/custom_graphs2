import seaborn as sns
from matplotlib import pyplot
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from pathlib import Path




def bar_chart(csv_file):

    # _file = 'Sample CSV/Bar Data.csv'
    df = pd.read_csv(csv_file)
  
    with st.expander('DATA FRAME'):
        st.dataframe(df, height=200)

    coltype1, coltype2 = st.columns([0.3, 0.7])
    with coltype1:
        bar_type = st.selectbox("Bar Type", options=['Stacked', 'Grouped'],)

    selected_set = st.multiselect('COLUMNS', options=df.columns)
    new_df = df[selected_set]
    
    with st.expander('TITLE AND LABELS'):
        selected_title = st.text_input('Chart Title')
        x_selected_label = st.text_input('X Axis Label')
        y_selected_label = st.text_input('Y Axis Label')

    with st.expander('CHART STYLING'):
        selected_style = st.select_slider('Themes', options=['white', 'dark', 'whitegrid', 'darkgrid', 'ticks'], value='whitegrid')

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

        col1, col2, col3 = st.columns([0.33, 0.33, 0.33], border=True)

        with col1:
            st.subheader('FONTS')
            selected_title_font_size = st.selectbox('Title Size', options=[x for x in range(8, 100)], help='Set Font Size')
            x_label_size = st.selectbox('X Axis', options=[x for x in range(8, 100)], help='Set Font Size')
            y_label_size = st.selectbox('Y Axis', options=[x for x in range(8, 100)], help='Set Font Size')
        with col2:
            st.subheader('DIMENSIONS')
            chart_length = st.slider('Chart Length', min_value=6, max_value=20, value=8)
            chart_width = st.slider('Chart Width', min_value=6, max_value=20, value=12)
        with col3:
            x_custom_angle = st.select_slider('X Axis Custom Angle', options=[0, 45, 90], value=45)
            y_custom_angle = st.select_slider('Y Axis Custom Angle', options=[0, 45, 90], value=0)
            legend_position = st.selectbox('Legend Position', options=['best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'])
            legend_style = st.selectbox('Legend Style', options=['Horizontal', 'Vertical'])

            if legend_style == 'Horizontal':
                if len(selected_set) == 1:
                    _style = 1
                else:
                    _style = len(selected_set)-1
            if legend_style == 'Vertical':
                _style = 1






    # Convert 'Date' column to datetime format for proper plotting
    # try:
    #     new_df["Date"] = pd.to_datetime(new_df["Date"])
    # except:
    #     st.error('No Data to plot')
    # else:

    if bar_type == 'Grouped':
        # Melt the dataframe to long format for seaborn
        df_melted = new_df.melt(id_vars=["Date"], var_name="Brand", value_name="Count")

        # Set plot size and style
        plt.figure(figsize=(chart_width, chart_length))
        fig, ax = plt.subplots()

        # remove specific borders
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # legends placement

        # Create a bar plot
        sns.barplot(data=df_melted, x="Date", y="Count", hue="Brand", width=1,)

        # Rotate x-axis labels for better visibility
        plt.xticks(rotation=x_custom_angle)
        plt.yticks(rotation=y_custom_angle)
        plt.xlabel(x_selected_label, fontdict={'size':x_label_size})
        plt.ylabel(y_selected_label, fontdict={'size':y_label_size})
        plt.title(selected_title, fontdict={'size':selected_title_font_size, 'name':'Arial'})
        plt.legend(loc=legend_position, ncol=_style )
    
    if bar_type=='Stacked':
        st.dataframe(new_df)
        new_df.plot(kind='bar', stacked=True)
    
    
    # Show the plot
    with st.expander('SHOW CHART'):
        st.pyplot(plt)
    
    save_to_jpg = st.button('Save to JPG')
    result_file = Path(__file__).parent/'my_test.jpg'
    if save_to_jpg:
        plt.savefig(result_file, bbox_inches='tight')

    try:
        result_file = open(result_file, 'rb')
    except:
        st.warning('No File to Download')
    else:
        st.download_button('Save to Image File', data=result_file, file_name='my_image.jpg')
    

def bar_grouped():



    return