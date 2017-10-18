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


def run(urls, timeout, pause):
    with open(urls, "rb") as f:
        urls = [url.strip().decode() for url in f.readlines() if url.startswith(b'http')]
    stater = SiteStater(timeout=timeout, pause=pause)

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="the file that contains the urls")
    parser.add_argument("-t", "--timeout", type=int, default=60,
                    help="how much the browser should wait for the page before timing out")
    parser.add_argument("-p", "--pause", type=int, default=10,
                    help="how much the browser should stay on a page before measuring the cpu performance")

    args = parser.parse_args()
    run(args.urls, args.timeout, args.pause)


if __name__ == "__main__":
    main()
