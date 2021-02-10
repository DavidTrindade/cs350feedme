from blog.models import Feed, Article
from django.contrib.auth.models import User
import pandas as pd
import csv
from pathlib import Path

DATA_DIR = Path("../../")


def get_csv(filepath, num_rows="", col=0):
    """Creates list with csv data"""
    with open(filepath, 'r') as f:
        df = pd.read_csv(filepath, index_col=col, nrows=num_rows) if num_rows != "" else pd.read_csv(filepath, index_col=col)
        return df.values.tolist()

def clear_data():
    """Clears data from all sql tables"""
    print("Delete data from all tables? (y/n)")
    if input("> ").lower() != "y":
        print("No data was altered")
        return False
    Feed.objects.all().delete()
    Article.objects.all().delete()
    print("Cleared data from all tables.")
    return True

def load_feeds(num_feeds):
    df = pd.read_csv(DATA_DIR/"dropna_feeds.csv")
    feeds = df.values.tolist() if num_feeds == "" else df[:num_feeds].values.tolist()
    Feed.objects.bulk_create([
        Feed(id=id, feed_link=feed, title=title, desc=desc, link=link)
        for id, feed, title, desc, link in feeds
    ])

    load_articles(num_feeds)


def load_articles(num_articles):
    df = pd.read_csv(DATA_DIR/"articles2.csv", index_col=0)
    articles = df.values.tolist() if num_articles == "" else df[df['feed_id'].isin(range(num_articles))].values.tolist()
    Article.objects.bulk_create([
        Article(feed=Feed.objects.get(id=id), link=link, title=title, desc=desc)
        for id, link, title, desc in articles
    ])

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
                print("Not a valid number")
                continue
        break
    
    load_feeds(num_feeds)

if __name__ == '__main__':
    main()
