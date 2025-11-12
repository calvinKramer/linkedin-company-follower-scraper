thonimport requests

def get_company_posts(company_url):
    posts_url = f"{company_url}/posts"
    response = requests.get(posts_url)
    return response.json()['data']