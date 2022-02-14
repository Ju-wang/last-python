from economy_scrapping import get_article
from save import save_file

articles = get_article()

save_file(articles)
