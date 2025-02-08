import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd


def bar_columns(df):

    selected_columns = st.multiselect('Columns', options=df.columns)

    if selected_columns not in [None, '']:
        new_df =  df[selected_columns]
    
    return new_df

def bar_customization():

    with st.expander('TITLE AND LABELS'):
        selected_title = st.text_input('Chart Title')
        x_selected_label = st.text_input('X Axis Label')
        y_selected_label = st.text_input('Y Axis Label')
    
    with st.expander('GRID'):
        col_grid1, col_grid2, col_grid3 = st.columns(3, border=True)
        with col_grid1:
            grid_visible = st.checkbox('Visible', value=True)
            if grid_visible:
                _visible = True
                grid_color = st.color_picker('Color')

                grid_major = st.selectbox('Lines', options=['Major', 'Minor', 'Both'])
                if grid_major=='Major':
                    _major = 'major'
                if grid_major=='Minor':
                    _major = 'minor'
                if grid_major=='Both':
                    _major = 'both'

                grid_axis = st.selectbox('Axis', options=['Horizontal', 'Vertical', 'Both'])
                if grid_axis=='Horizontal':
                    _axis = 'y'
                if grid_axis=='Vertical':
                    _axis = 'x'
                if grid_axis=='Both':
                    _axis = 'both'
            else:
                _visible = False
                grid_color = '#000000'
                _axis = 'both'
                _major = 'both'

        

    return selected_title, x_selected_label, y_selected_label, grid_color, _visible, _axis, _major


def bar_grouped(df):

    # df.plot(kind='bar')

    # st.pyplot(plt)

    return


def bar_stacked(df):

    new_df = bar_columns(df)
    
    if new_df.shape[1] > 1:
        new_df.plot(kind='bar', stacked=True)

        # customize chart
        selected_title, x_selected_label, y_selected_label, grid_color, _visible, _axis, _major = bar_customization()
        plt.title(selected_title)
        plt.xlabel(x_selected_label)
        plt.ylabel(y_selected_label)
        if _visible == True:
            plt.grid(visible=_visible, which=_major, axis=_axis, color=grid_color)
        if _visible == False:
            plt.grid(visible=_visible)
        
        

        # show chart
        st.pyplot(plt)

    return




def bar_chart(csv_file):

    df = pd.read_csv(csv_file)
    with st.expander('DATA FRAME'):
        st.dataframe(df, height=200, use_container_width=True)

    with st.sidebar:
        bar_select = option_menu(
            menu_title='Chart Bar Type',
            options=['Grouped', 'Stacked']
        )
    
    if bar_select == 'Grouped':
        "ff"

    if bar_select == 'Stacked':
        bar_stacked(df)
    

    return