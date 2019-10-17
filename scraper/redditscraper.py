import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='[REDACTED]',
                     client_secret='[REDACTED]',
                     user_agent='[REDACTED]',
                     redirect_uri='[REDACTED]',)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

topics_dict = {"title": [],
               "score": [],
               "id": [],
               "url": [],
               "comms": [],
               "created": [],
               "body": []}
subreddit = reddit.subreddit('fireteams')
top_science = subreddit.new()

for submission in top_science:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)

# topics_data.to_csv('top_SciencePosts.csv', index=False)
