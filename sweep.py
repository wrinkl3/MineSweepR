import argparse
from site_stat import SiteStater
from analysis import upper_outlier_indices
from operator import itemgetter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="the file that contains the urls")
    args = parser.parse_args()

    with open(args.urls, "rb") as f:
        urls = [url.strip().decode() for url in f.readlines() if url.startswith(b'http')]
    stater = SiteStater()

    scores = [stater.stat_website(url) for url in urls]
    for w, s in zip(urls, scores):
        print("{}: {}".format(w, s))
    print("\n\n")
    indices = upper_outlier_indices(scores, 0.5)
    if len(indices) > 0:
        print('These websites might have a miner:')
        print(itemgetter(*indices)(urls))
    else:
        print('No outliers detected')


if __name__ == "__main__":
    main()
