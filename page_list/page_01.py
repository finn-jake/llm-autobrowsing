import streamlit as st
import streamlit.components.v1 as components
#components.iframe("https://trade.mql5.com/trade?servers=SomeBroker1-Demo,SomeBroker1-Live,SomeBroker2-Demo,SomeBroker2-Live&amp;trade_server=SomeBroker-Demo&amp;startup_mode=open_demo&amp;lang=en&amp;save_password=off")

st.set_page_config(layout = "wide")
st.balloons()

st.markdown('#### The brief introduction page for the features implemented on this platform')
st.markdown("<br>", unsafe_allow_html=True)

st.markdown('I have implemented three main functions for auto-browsing  \n'
            '[Here are the guts of this platform](https://github.com/finn-jake/llm-autobrowsing)')

st.markdown("1. Recognizing whether the user's query requires browsing. \n"
            "2. Listing the search terms necessary for browsing. \n"
            "3. Aggregating the results using the main LLm and evaluating the significance of each result while summarizing the content with a worker LLM.")

st.image("source/concept.png", caption = "How chat engine works", width = 900)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("Especially, Mini GPT evaluates whether the parsed web text is significant and summarizes the content to offer is as bait to the main LLM model.  \n"
            "verifying that Mini GPT performs its role correctly and fetching URLs that contain high-quality content remain tasks still to be advanced.")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("One of the things I am considering is improving usability. Since Mini Gpt takes a lot of time to work,  \n"
            "I am trying to minimize the waiting time by exposing some compressed information.")

st.image("source/example.png", width = 900)