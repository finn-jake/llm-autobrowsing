import os
from utils import *
from pages import *
from st_on_hover_tabs import on_hover_tabs

def main_app():
    #st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
    pg = st.navigation({
        "HOME": [st.Page("pages/page_01.py", title = "INTRO", icon = ":material/house:")],
        "ASSISTANT": [st.Page("pages/chat.py", title = "AVOCADO CHAT", icon = ":material/chat:")]
    }
    )

    pg.run()
if __name__ == "__main__":  
    main_app()