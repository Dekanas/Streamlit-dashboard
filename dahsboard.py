import streamlit as st
import pandas as pd
import plotly.express as px

# Create a function to read the excel file and store the data in a DataFrame
def read_excel(file):
    return pd.read_excel(file)

# Create the app's main function
def app():
    st.set_page_config(page_title='Chart builder', page_icon=':chart_with_upwards_trend:', layout='wide')
    # Allow the user to upload an excel file
    file = st.file_uploader("Upload an excel file", type=["xlsx", "xls"])

    if file is not None:
        # Read the excel file and store the data in a DataFrame
        df = read_excel(file)
        
        # Create a container for the charts
        chart_container = st.empty()

        # Create a function to create the chart
        def create_chart():
            # Allow the user to choose a chart type
            chart_type = st.selectbox("Choose a chart type", ["Scatter", "Bar", "Line"])

            if chart_type == "Scatter":
                # Allow the user to choose the X and Y variables
                x_variable = st.selectbox("Choose the X variable", df.columns)
                y_variable = st.selectbox("Choose the Y variable", df.columns)

                # Create a scatter chart
                fig = px.scatter(data_frame=df, x=x_variable, y=y_variable)
                chart_container.write(fig)

            elif chart_type == "Bar":
                # Allow the user to choose the X and Y variables
                x_variable = st.selectbox("Choose the X variable", df.columns)
                y_variable = st.selectbox("Choose the Y variable", df.columns)

                # Create a bar chart
                fig = px.bar(data_frame=df, x=x_variable, y=y_variable)
                chart_container.write(fig)
                
            elif chart_type == "Line":
                # Allow the user to choose the X and Y variables
                x_variable = st.selectbox("Choose the X variable", df.columns)
                y_variable = st.selectbox("Choose the Y variable", df.columns)

                # Create a line chart
                fig = px.line(data_frame=df, x=x_variable, y=y_variable)
                chart_container.write(fig)


        # Allow the user to add multiple charts
        add_chart = st.button("Add chart")
        if add_chart:
            create_chart()

        # Allow the user to remove last chart
        remove_chart = st.button("Remove last chart")
        if remove_chart:
            chart_container.empty()


if __name__=='__main__':
    app()