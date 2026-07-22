import streamlit as st


def display_overview():
    with open("content/overview.md", "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("\n\n")

    for part in parts:
        if part == "[FIGURE_1]":
            _, col_mid, _ = st.columns([0.5, 2, 0.5])
            with col_mid:
                st.image(
                    "figures/quadratic_loss_function.png",
                    use_container_width=True,
                    caption="Figure 1. The Taguchi concept of economic loss due to poor quality is governed by a quadratic loss function within some region close to the target."
                )

        elif part == "[FIGURE_2]":
            _, col_mid, _ = st.columns([0.5, 2, 0.5])
            with col_mid:
                st.image(
                    "figures/square_loss_function.png",
                    use_container_width=True,
                    caption="Figure 2. The conformance to specification concept of economic loss due to poor quality is governed by a square loss function."
                )
        
        elif part == "[BUTTON_1]":
            st.markdown(
                """
                <div class="store-button-wrapper">
                    <a href="https://www.brokenquality.com/bookshelf/p/definition-of-qualit-epub" target="_blank">
                        <button class="store-button">Click here to learn more!</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.markdown(part)
    
    st.divider()