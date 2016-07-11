# dead-feed-checker
**dead-feed-checker** takes in an OPML file containing a list of RSS/Atom feeds and reports back which ones appear to be dead.

###Dependencies
* python3
* feedparser
* listparser

###Usage
In a *nix shell run:
```
  python3 main.py your_feed_list.opml
```
to get a list of all feeds that are suspected to be dead or have not updated in the past year.

The length of time to wait before flagging a feed as probably dead can be set using the `--interval` parameter.

###Use Cases:
* You want to make sure that sites you follow haven't accidentally moved/broken their rss feed without warning
* You want to clear out dead feeds due to limits due to limits from your feed reader on the number of feeds allowed.
* You're feeling nostolgic (in which case my other project [RSStory](https://github.com/malnoxon/rsstory) might be useful)

###Getting a list of your feeds from Feedly
1. Login to your feedly account
2. Go to "Organize sources" in the sidebar
3. At the bottom of the page click on "export OPML"
4. Download it


