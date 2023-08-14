import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import smtplib, ssl
from email.mime.text import MIMEText
import my_naver_account as naver 
import datetime

st.set_page_config(page_title="뚜기뚜기마케터스", layout="wide")
st.title("RFM Analysis for Target Marketing Strategies")

# line1_spacer1, line1_1, line1_spacer2 = st.columns((0.1, 3.2, 0.1))
# line1_1.header("Customer Segmentation")

row3_1, row3_space2, row3_2, row3_space3 = st.columns((1.5, 0.3, 1.5, 0.1))
df = pd.read_csv('./stats_treemap.csv')

rfm = pd.read_csv('./rfm.csv')
# st.dataframe(rfm)

with row3_1:
    st.header("Customer Segnemtation")
    fig = px.treemap(df, values='Count', path=['label'])
    # fig.update_layout(title_text="Customer Segnemtation", title_x=0.4)
    st.plotly_chart(fig)

df2 = pd.read_csv('./Distribution_df.csv')
rfm_stats = pd.read_csv('./RFM_stats_df.csv')
rfm_stats.drop(['Unnamed: 0'], axis=1, inplace=True)
rfm_stats.index = ['Recency', 'Frequency', 'Monetary']
with row3_2:
    st.header("Distribution of RFM")
    tab1, tab2 = st.tabs(["Chart", "Data"])
    with tab1:
        fig = make_subplots(rows=3, cols=1, subplot_titles=("Recency", "Frequency", "Monetary"))
        # fig.update_layout(title_text="Distribution of RFM", title_x=0.4)            
        Recency = go.Histogram(x=df2['Recency'])
        Frequency = go.Histogram(x=df2['Frequency'])
        Monetary = go.Histogram(x=df2['Monetary'])
        fig.append_trace(Recency, 1, 1)
        fig.append_trace(Frequency, 2, 1)
        fig.append_trace(Monetary, 3, 1)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        tab2 = st.dataframe(rfm_stats) # 고객군별 RFM 통계로 바꾸기 

row1_1, row1_space2, row1_2, row1_space3 = st.columns((1, 1.3, 1, 0.1))
with row1_1:
    st.header("Customer List")
    option = st.multiselect(' ', options=('신규 고객', '충성 고객', '잠재적 충성고객', '관심 고객', '이탈 위험 고객', '이탈 고객'))

with row1_2:
    st.header("Ternary Plot")
    option2 = st.multiselect('  ', options=('신규 고객', '충성 고객', '잠재적 충성고객', '관심 고객', '이탈 위험 고객', '이탈 고객'))

category_df = pd.read_csv('./category.csv')
row2_1, row2_space2, row2_2, row2_space3 = st.columns((2, 0.1, 1, 0.1))
with row2_1:
    if option != []:
        if len(option) == 1:
            temp = category_df[category_df['Segment'] == option[0]]
            st.dataframe(temp)
        elif len(option) == 2:
            temp = category_df[(category_df['Segment'] == option[0])|(category_df['Segment'] == option[1])]
            st.dataframe(temp)
        elif len(option) == 3:
            temp = category_df[(category_df['Segment'] == option[0])|(category_df['Segment'] == option[1])|(category_df['Segment'] == option[2])]
            st.dataframe(temp)
        elif len(option) == 4:
            temp = category_df[(category_df['Segment'] == option[0])|(category_df['Segment'] == option[1])|(category_df['Segment'] == option[2])|(category_df['Segment'] == option[3])]
            st.dataframe(temp)
        elif len(option) == 5:
            temp = category_df[(category_df['Segment'] == option[0])|(category_df['Segment'] == option[1])|(category_df['Segment'] == option[2])|(category_df['Segment'] == option[3])|(category_df['Segment'] == option[4])]
            st.dataframe(temp)
        elif len(option) == 6:
            st.dataframe(category_df)
    else:
        st.dataframe(category_df)

with row2_2:
    if option2 != []:
        if len(option2) == 1:
            temp = rfm[rfm['Segment'] == option2[0]]
            fig = px.scatter_ternary(temp, a="recency_score", b="frequency_score", c="monetary_score")
            st.plotly_chart(fig, theme=None)
        elif len(option2) == 2:
            temp = rfm[(rfm['Segment'] == option2[0])|(rfm['Segment'] == option2[1])]
            fig = px.scatter_ternary(temp, a="recency_score", b="frequency_score", c="monetary_score")
            st.plotly_chart(fig, theme=None)
        elif len(option2) == 3:
            temp = rfm[(rfm['Segment'] == option2[0])|(rfm['Segment'] == option2[1])|(rfm['Segment'] == option2[2])]
            fig = px.scatter_ternary(temp, a="recency_score", b="frequency_score", c="monetary_score")
            st.plotly_chart(fig, theme=None)
        elif len(option2) == 4:
            temp = rfm[(rfm['Segment'] == option2[0])|(rfm['Segment'] == option2[1])|(rfm['Segment'] == option2[2])|(rfm['Segment'] == option2[3])]
            fig = px.scatter_ternary(temp, a="recency_score", b="frequency_score", c="monetary_score")
            st.plotly_chart(fig, theme=None)
        elif len(option2) == 5:
            temp = rfm[(rfm['Segment'] == option2[0])|(rfm['Segment'] == option2[1])|(rfm['Segment'] == option2[2])|(rfm['Segment'] == option2[3])|(rfm['Segment'] == option2[4])]
            fig = px.scatter_ternary(temp, a="recency_score", b="frequency_score", c="monetary_score")
            st.plotly_chart(fig, theme=None)
        elif len(option2) == 6:
            fig = px.scatter_ternary(rfm, a="recency_score", b="frequency_score", c="monetary_score")
            st.plotly_chart(fig, theme=None)
    else:
        fig = px.scatter_ternary(rfm, a="recency_score", b="frequency_score", c="monetary_score")
        st.plotly_chart(fig, theme=None)

        
    # option = st.selectbox('Choose Customer Segment', 
    #              options=('신규 고객', '충성 고객', '잠재적 충성고객', '관심 고객', '이탈 위험 고객', '이탈 고객'))
    # temp = rfm[rfm['Segment'] == option]
    # fig = px.scatter_ternary(temp, a="recency_score", b="frequency_score", c="monetary_score")
    # st.plotly_chart(fig)

row5_1, row5_space1 = st.columns((3, 0.1))
with row5_1:
    st.header("Email Target Marketing")

row4_1, row4_space1, row4_2, row1_space2, row4_3, row1_space3 = st.columns((1, 0.1, 2, 0.1, 0.5, 0.1))
with row4_1:
    # st.header("Email Target Marketing")
    option3 = st.multiselect('       ', options=('신규 고객', '충성 고객', '잠재적 충성고객', '관심 고객', '이탈 위험 고객', '이탈 고객'))

with row4_2:
    if option3 != []:
        if option3[0] == '신규 고객':
            email = st.text_area('                ', '신규고객 타켓 메시지')
        elif option3[0] == '충성 고객':
            email = st.text_area('                  ', '충성고객 타켓 메시지')
        elif option3[0] == '잠재적 충성고객':
            email = st.text_area('                     ', '잠재적 충성고객 타켓 메시지')
        elif option3[0] == '관심 고객':
            email = st.text_area('                            ', '관심 고객 타켓 메시지')
        elif option3[0] == '이탈 위험 고객':
            email = st.text_area('                           ', '이탈 위험 고객 타켓 메시지')
        elif option3[0] == '이탈 고객':
            email = st.text_area('                        ', '이탈 고객 타켓 메시지')
    else:
        st.text_area('         ', '마케팅 메시지')

def make_mime_text(mail_to, subjuct, body):
    msg = MIMEText(body, 'plane')
    msg['Subject'] = subjuct
    msg['To'] = mail_to 
    msg['From'] = naver.account 
    return msg

def send_naver_mail(msg):
    server = smtplib.SMTP('smtp.naver.com', 587)
    server.starttls()
    server.login(naver.account, naver.password)
    server.send_message(msg)

def send_test_email(email):
    msg = make_mime_text(mail_to=naver.account, subjuct='제목', body=email)
    send_naver_mail(msg)

with row4_3:
    st.write(' ')
    if st.button('Send Email'):
        # send_test_email(email) 
        st.write('Sending Time :', datetime.datetime.now())