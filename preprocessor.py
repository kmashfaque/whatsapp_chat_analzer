import re
import pandas as pd

def preprocess(data):
    pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s+\d{1,2}:\d{2}\s?[ap]m\s-\s"
    messages = re.split(pattern, data)[1:]
    date_time_list = re.findall(pattern, data)
    pattern = r"(\d{2}/\d{2}/\d{4}),\s+(\d{1,2}:\d{2}\s?[ap]m)"
    matches = [re.findall(pattern, dt)[0] for dt in date_time_list]

    # Creating the DataFrame
    df = pd.DataFrame(matches, columns=["message_date", "time"])

    # Combining "message_date" and "time" columns into a single column
    df["message_date"] = pd.to_datetime(df["message_date"] + " " + df["time"], format="%d/%m/%Y %I:%M %p")

    # Dropping the unnecessary columns
    df.drop(["time"], axis=1, inplace=True)

    # Renaming the "message_date" column to "date"

    df = pd.DataFrame({"user_message": messages, "message_date": df["message_date"]})

    df.rename(columns={"message_date": "date"}, inplace=True)

    users = []
    messages = []

    for message in df["user_message"]:
        entry = re.split(":", message)
        if entry[1:]:
            users.append(entry[0])
            messages.append(entry[1])
        else:
            users.append("group notification")
            messages.append(entry[0])

    df["user"] = users
    df["message"] = messages
    df.drop(columns=["user_message"], inplace=True)

    df["message"] = df["message"].str.replace(r"\n", "")

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute

    return df

