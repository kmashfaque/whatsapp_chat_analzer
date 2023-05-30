from urlextract import URLExtract
extractor=URLExtract()
from wordcloud import WordCloud

def fetch_stats(selected_user,df):
    # if selected_user=="Overall":
    #     # 1. fetching number of messages
    #     num_messages=df.shape[0]
    #     # 2. number of word
    #     words=[]
    #     for messages in df["message"]:
    #         words.extend(messages.split(" "))
    #     return num_messages,len(words)
    # else:
    #     new_df=df[df["user"]==selected_user]
    #     num_messages = new_df.shape[0]
    #     words = []
    #     for messages in new_df["message"]:
    #         words.extend(messages.split(" "))
    #
    #     return num_messages,len(words)
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    num_messages=df.shape[0]
    words = []
    for messages in df["message"]:
        words.extend(messages.split(" "))

    num_of_media_messeges=df[df["message"]=="<Media omitted>"].shape[0]

    num_links=[]

    for message in df["message"]:
        num_links.extend(extractor.find_urls(message))

    return num_messages, len(words),num_of_media_messeges, len(num_links)



def most_busy_users(df):
    busy_users=df["user"].value_counts().head()
    df=round((df["user"].value_counts()/df.shape[0])*100,2).reset_index().rename(
        columns={"index":"name","user":"percent"})

    return busy_users,df


def create_word_cloud(selected_user,df):
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color="white")
    df_wc=wc.generate(df["message"].str.cat(sep=" "))
    return df_wc