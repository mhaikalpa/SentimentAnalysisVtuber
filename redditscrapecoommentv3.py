import praw
import pandas as pd

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='f0-oUB1pvuBCeo0mNMeqEQ',
    client_secret='-6LHfqhyicJC1hSiB_Vb0bj2f4s7oA',
    user_agent='automatecommentpythonv2',
)

# Specify the Reddit post URL
post_url = 'https://www.reddit.com/r/VirtualYoutubers/comments/sptjo2/about_the_rushiamafumafu_situation/?utm_source=share&utm_medium=web2x&context=3'

# Create empty lists to store comments data
comments_data = {
    'Comment': [],
}

# Access the Reddit post and its comments
submission = reddit.submission(url=post_url)
submission.comments.replace_more(limit=None)

# Iterate through comments and collect data
for comment in submission.comments.list():
    comments_data['Comment'].append(comment.body)

# Create a Pandas DataFrame from the collected data
df = pd.DataFrame(comments_data)

# Save the DataFrame to a CSV file
df.to_csv('reddit_comments5.csv', index=False)

print("Reddit comments have been saved to 'reddit_comments.csv'")