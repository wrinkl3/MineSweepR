import argparse
from site_stat import SiteStater
from analysis import upper_outlier_indices
from operator import itemgetter

def stat_and_print(url, stater):
    score = stater.stat_website(url)
    if score is None:
        print("{} failed to load".format(url))
    else:
        print("{}: {}".format(url, score))
    return score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="the file that contains the urls")
    args = parser.parse_args()

    with open(args.urls, "rb") as f:
        urls = [url.strip().decode() for url in f.readlines() if url.startswith(b'http')]
    stater = SiteStater()

    scores, valid_urls = [], []
    for url in urls:
        score = stat_and_print(url, stater)
        if score:
            scores.append(score)
            valid_urls.append(url)
    
    indices = upper_outlier_indices(scores, 0.5)
    if len(indices) > 0:
        print('These websites might have a miner:')
        print(itemgetter(*indices)(valid_urls))
    else:
        print('No outliers detected')


if __name__ == "__main__":
    main()
