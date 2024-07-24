import streamlit as st

st.title("Profiling Risk Clusters")
st.header("Purchasing Habits across Risk Levels", divider = 'red')

st.subheader('Average Inactivity')
st.image('purchasing1.png')
st.markdown("The average number of days of inactivity of a high churn risk customer is 255 days, compared to low risk and medium risk customers at 0.63 days and 0.83 days respectively. High-risk customers also only have an average of 10 total transactions whereas low-to-medium risk customers have an average of 300+.")
st.markdown("---")

st.subheader('Average Spending (PHP) per Transaction')
st.image('purchasing2.png')
st.markdown("The average spending of high churn risk customers is P29k, much higher than their low-to-medium risk counterparts, but remember that high risk customers have much lower transaction volume, thus on aggregate from 2020-2021, medium-low risk customers (PHP63.9M+ and PHP305M+ respectively) outspend their high risk counterparts (PHP 7M+).") 
st.markdown("---")

st.subheader('One-time Purchaser')
st.image('purchasing3.png')
st.caption("To put the previous graph into context, a whopping 92% of high churn risk customers are one-time purchasers, using their credit card just a single day and becoming inactive later.")
st.markdown("---")

st.subheader('Trend of Transaction Volume')
st.image('transaction_volume.png')
st.caption("Based on this line graph, we see that the behavior of low risk and medium risk customers is very similar, with a single small 3-4% spike in transaction volume during holiday season as expected. High risk customers however fluctuate in transaction volume much more, with a large 17% spike around July to October 2021.")
