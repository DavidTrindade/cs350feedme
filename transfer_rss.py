from blog.models import Feed
from django.contrib.auth.models import User
import pandas as pd
import csv
from pathlib import Path

DATA_DIR = Path("../../dataframes")

def clear_data():
    """Clears data from all sql tables"""
    print("Delete data from all tables? (y/n)")
    if input("> ").lower() != "y":
        print("No data was altered")
        return False
    Feed.objects.all().delete()
    print("Cleared data from all tables.")
    return True

def load_feeds(num_feeds):
    df = pd.read_csv(DATA_DIR/"df_import.csv")
    feeds = df.reset_index().values.tolist() if num_feeds == "" else df[:num_feeds].reset_index().values.tolist()
    Feed.objects.bulk_create([
        Feed(id=id1, feed_link=feed, title=title, desc=desc, link=link)
        for id1, id2, feed, title, desc, link in feeds
    ])

    # load_articles(num_feeds)


# def load_articles(num_articles):
#     df = pd.read_csv(DATA_DIR/"articles2.csv", index_col=0)
#     articles = df.values.tolist() if num_articles == "" else df[df['feed_id'].isin(range(num_articles))].values.tolist()
#     Article.objects.bulk_create([
#         Article(feed=Feed.objects.get(id=id), link=link, title=title, desc=desc)
#         for id, link, title, desc in articles
#     ])

def main():
    if not clear_data():
        print("WARNING: Continuing without clearing data could cause issues.")
        print("Continue anyway? (y/n)")
        if input("> ").lower() != "y":
            print("EXITING")
            return
    print("Enter number of feeds to load. (Leave blank for all)")

    while True:
        num_feeds = input("> ")
        if bool(num_feeds):
            try:
                num_feeds = int(num_feeds)
            except ValueError:
                print("Please enter a number or leave blank.")
                continue
        break
    
    load_feeds(num_feeds)

if __name__ == '__main__':
    main()
