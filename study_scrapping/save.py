import csv


def save_file(articles):
    file = open("articles.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "read", "url"])
    for article in articles:
        writer.writerow(list(article.values()))
    return
