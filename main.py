import streamlit as st
import preprocessor
import hellper
import matplotlib.pyplot as plt


st.sidebar.title("Whatsapp chat analyzer")

uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)

    st.dataframe(df)

    # fetch unique users
    user_list=df["user"].unique().tolist()
    user_list.remove("group notification")
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user=st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show analysis"):

        col1,col2,col3,col4=st.columns(4)

        num_messages,num_words,num_of_media_messages, num_links=hellper.fetch_stats(selected_user,df)

        with col1:
            st.header("Total messages")
            st.title(num_messages)
        with col2:
            st.header("Number of total words")
            st.title(num_words)

        with col3:
            st.header("Number of media shared")
            st.title(num_of_media_messages)

        with col4:
            st.header("Number of total links")
            st.title(num_links)

        if selected_user=="Overall":
            st.title("Most busy users")
            x,new_df=hellper.most_busy_users(df)
            fig,ax=plt.subplots()

            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color="red")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        df_wc=hellper.create_word_cloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)





