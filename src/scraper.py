thonimport requests
from linkedin_parser import parse_post
from data_exporter import export_data
from utils import get_company_posts

def scrape_linkedin(company_url):
    posts = get_company_posts(company_url)
    extracted_data = []
    
    for post in posts:
        post_data = parse_post(post)
        extracted_data.append(post_data)
    
    export_data(extracted_data)

if __name__ == "__main__":
    company_url = input("Enter the LinkedIn company URL: ")
    scrape_linkedin(company_url)