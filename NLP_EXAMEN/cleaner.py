import re
import pandas as pd
import numpy as np

def remove_chat_metadata(chat_export_file):
    date_time = r"\d+\/\d+\/\d+,\s\d+:\d+"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    cleaned_corpus1 = re.sub(date_time, "", chat_export_file, flags=re.IGNORECASE)
    cleaned_corpus2 = re.sub(dash_whitespace, "", cleaned_corpus1, flags=re.IGNORECASE)
    cleaned_corpus = re.split(":", cleaned_corpus2)
    return cleaned_corpus


def construct(objet):
    if len(objet) == 2:
        return objet[1]
    else:
        None

def remove_non_message_text(df):
    indexNames = df[df['body_text_cons'] == ' <Media omitted>'].index
    df.drop(indexNames, inplace=True)
    return df


def clean(lien):
    data = pd.read_csv(lien, delimiter="\n", names=['body_text'], header=None)
    data.drop([0], axis=0, inplace=True)
    data["body_text_clean"] = data["body_text"].apply(lambda x: remove_chat_metadata(x))
    data["body_text_cons"] = data["body_text_clean"].apply(lambda x: construct(x))
    data['body_text_cons'] = data['body_text_cons'].replace(np.nan, "Good morning")
    data = remove_non_message_text(data)
    return data["body_text_cons"]


#if __name__ == "__main__":
 #   print(clean("chat.txt"))

