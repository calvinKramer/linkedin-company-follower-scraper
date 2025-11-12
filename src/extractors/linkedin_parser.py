thonimport requests

def parse_post(post_url):
    response = requests.get(post_url)
    data = response.json()
    
    post_data = {
        "postId": data['id'],
        "postContent": data['content'],
        "author": data['author'],
        "publicationDate": data['created_time'],
        "likes": data['engagement']['likes'],
        "shares": data['engagement']['shares'],
        "comments": data['engagement']['comments'],
        "followers": extract_followers(data['followers'])
    }
    return post_data

def extract_followers(followers_data):
    followers = []
    for follower in followers_data:
        followers.append({
            "followerName": follower['name'],
            "followerProfile": follower['profile_url'],
            "engagement": follower['engagement_type']
        })
    return followers