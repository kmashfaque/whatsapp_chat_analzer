def fetch_stats(selected_user,df):

    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    num_messages=df.shape[0]
    words = []
    for messages in df["message"]:
        words.extend(messages.split(" "))

    num_of_media_messeges=df[df["message"]=="<Media omitted>"].shape[0]
    return num_messages, len(words),num_of_media_messeges

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

