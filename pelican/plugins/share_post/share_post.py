"""
Share Post
==========

This plugin was originally created by
Talha Mansoor <talha131@gmail.com>

This plugin adds social share URLs to each article.
"""

# If you want to add a new link_processor please
# have a look at the create_link decorator and
# follow the example of the other functions

from urllib.parse import quote

from bs4 import BeautifulSoup

from pelican import contents, signals
from pelican.generators import ArticlesGenerator, PagesGenerator

_create_link_functions = []


# Use this decorator to mark a function as
# a link creator. The function's prototype shall be
# create_link_NAME(title, url, content)
# where
#   NAME is the name of the target, e.g. "dispora" or "facebook"
#   title is the HTML-safe title of the content
#   url is the content URL
#   content is the full object, should you need to extract more data.
def create_link(f):
    _create_link_functions.append(f)
    return f


@create_link
def create_link_email(title, url, content):
    return f"mailto:?subject={title}&amp;body={url}"


@create_link
def create_link_hacker_news(title, url, content):
    return f"https://news.ycombinator.com/submitlink?t={title}&u={url}"


@create_link
def create_link_diaspora(title, url, content):
    return f"https://sharetodiaspora.github.io/?title={title}&url={url}"


@create_link
def create_link_facebook(title, url, content):
    return f"https://www.facebook.com/sharer/sharer.php?u={url}"


@create_link
def create_link_twitter(title, url, content):
    twitter_username = content.settings.get("TWITTER_USERNAME", "")
    via = f"&via={twitter_username}" if twitter_username else ""

    tags = getattr(content, "tags", [])
    tags = ",".join([tag.slug for tag in tags])
    hashtags = f"&hashtags={tags}" if tags else ""

    return f"https://twitter.com/intent/tweet?text={title}&url={url}{via}{hashtags}"


@create_link
def create_link_reddit(title, url, content):
    return f"https://www.reddit.com/submit?url={url}&title={title}"


@create_link
def create_link_linkedin(title, url, content):
    summary = quote(
        BeautifulSoup(content.summary, "html.parser").get_text().strip().encode("utf-8")
    )

    return (
        f"https://www.linkedin.com/shareArticle?"
        f"mini=true&url={url}&title={title}&"
        f"summary={summary}&source={url}"
    )


def create_share_links(content):
    if isinstance(content, contents.Static):
        return

    main_title = BeautifulSoup(content.title, "html.parser").get_text().strip()

    try:
        sub_title = (
            " " + BeautifulSoup(content.subtitle, "html.parser").get_text().strip()
        )
    except AttributeError:
        sub_title = ""

    title = quote(f"{main_title}{sub_title}".encode("utf-8"))

    site_url = content.settings["SITEURL"]
    url = quote(f"{site_url}/{content.url}".encode("utf-8"))

    content.share_post = {}
    for func in _create_link_functions:
        key = func.__name__.replace("create_link_", "").replace("_", "-")
        content.share_post[key] = func(title, url, content)


def run_plugin(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                create_share_links(article)
                for translation in article.translations:
                    create_share_links(translation)
        elif isinstance(generator, PagesGenerator):
            for page in generator.pages:
                create_share_links(page)


def register():
    signals.all_generators_finalized.connect(run_plugin)
