from blog.models import Feed, Article
from django.contrib.auth.models import User
import pandas as pd

def clear_data():
    """Clears data from all tables"""
    print("Delete data from all tables? (y/n)")
    if input("> ").lower() != "y":
        print("No data was altered")
        return False
    Feed.objects.all().delete()
    Article.objects.all().delete()
    print("Cleared data from all tables.")
    return True

def load_feeds(num_feeds):
    with open("feeds.csv", 'r') as f:
        df = pd.read_table(f)
    

def main():
    if not clear_data():
        print("WARNING: Continuing without clearing data could cause issues.")
        print("Continue anyway? (y/n)")
        if input("> ").lower() != "y":
            print("EXITING")
            return
    print("Enter number of feeds to load. (Leave blank for all)")
    num_feeds = input("> ")
    load_feeds(num_feeds)

if __name__ == '__main__':
    main()
