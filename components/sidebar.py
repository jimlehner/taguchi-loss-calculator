import streamlit as st

# # Css styling
# def load_css(file_name):
#     with open(file_name) as f:
#         st.markdown(
#             f"<style>{f.read()}</style>",
#             unsafe_allow_html=True
#         )

# load_css("styles.css")

def read_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def display_sidebar():

    with st.sidebar:
        
        st.image(
            "figures/Broken_quality_logo.png",
            use_container_width=True
        )
        
        st.markdown(read_markdown("content/sidebar_project.md"))
        st.markdown(read_markdown("content/sidebar_author.md"))
        st.markdown(read_markdown("content/sidebar_contact.md"))
        st.markdown(read_markdown("content/sidebar_socials.md"))
        st.markdown(read_markdown("content/sidebar_website.md"))