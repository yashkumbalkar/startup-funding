import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned_my.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups', num_startups)

    st.header('Month on Month graph')

    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    selected_option = st.selectbox('Select Type', ['Total', 'Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig3)


def load_investor_detail(investor):
    st.title(investor)

    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest Investments')

        st.dataframe(big)
        fig, ax = plt.subplots()
        ax.bar(big.index, big.values)
        st.pyplot(fig)

    with col2:
        vertical = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum().head()

        st.subheader('Sectors invested in')

        st.dataframe(vertical)
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical, labels= vertical.index, autopct = "%0.01f%%")
        st.pyplot(fig1)

    df['year'] = df['date'].dt.year
    year_invest = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('Year on Year Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_invest.index, year_invest.values)

    st.pyplot(fig2)





# st.dataframe(df.head())

st.sidebar.title('Startup Funding Analysis')

# st.session_state.option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'], key='analysis')
# option = st.session_state.option

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    # btn0 = st.sidebar.button('Show Overall Analysis')
        load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('StartUp Analysis')

else:
    selected_investor = st.sidebar.selectbox('Select Startup',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_detail(selected_investor)


