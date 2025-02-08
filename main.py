import streamlit as st
from streamlit_option_menu import option_menu
from bar_chart import bar_chart
from setting import page_layout


if __name__ == '__main__':

    page_layout('wide')
    
    selected = ''
    with st.sidebar:
        csv_file = st.file_uploader('Upload CSV File')

        if csv_file not in [None, '']:

            selected = option_menu(
                menu_title='Select a Chart',
                options=['Bar', 'Pie', 'Line'],
                icons=['bar-chart','pie-chart', 'graph-up']
            )
        
    if selected == 'Bar':
        bar_chart(csv_file)
