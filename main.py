import feedparser
import listparser
import argparse
import time
import datetime

def get_date_word(entry):
    possibilities = ['date_parsed', 'updated_parsed', 'published_parsed']
    for p in possibilities:
        if p in entry:
            return p
    return None

def get_dead_feeds(filename, interval):
    fin = open(filename, 'r')
    opml = listparser.parse(fin)

    now = datetime.datetime.now()

    for f in opml.feeds:
        d = feedparser.parse(f.url)
        if 'title' in d.feed:
            if d.entries:
                entry = d.entries[0]
                date = get_date_word(entry)
                if date:
                    time_updated = datetime.datetime.fromtimestamp(time.mktime(entry[date]))
                    if now - time_updated > datetime.timedelta(days=interval):
                        print('MAYBE: The feed "{}" has not been modified in at least {} days. Url tried is {}'.format(f.title, interval, f.url))
                else:
                    print('MAYBE: The feed "{}"\'s most recent item has no information on when it was published. Url tried is {}'.format(f.title, f.url))
            else:
                print('DEAD: The feed "{}" appears to have zero posts. Url tried is {}'.format(f.title, f.url))
            
        else:
            print('DEAD: The feed "{}" is likely either dead or moved. Url tried is {}'.format(f.title, f.url))

def main():
    parser = argparse.ArgumentParser(description='Determine dead rss/atom feeds')
    parser.add_argument('filename', action='store', type=str, help='the name of the opml file containing a list of your feeds')
    parser.add_argument('--interval', nargs='?', default=365, type=int, help='the length of time (in days) without an update that qualifies a feed as "dead"')

    args = parser.parse_args()
    get_dead_feeds(args.filename, args.interval)
    print('DONE')

if __name__ == "__main__":
    main()
