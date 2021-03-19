import os

from share_post import run_plugin

from pelican.generators import ArticlesGenerator
from pelican.tests.support import get_context, get_settings

from . import share_post


def test_share_post(tmp_folder):
    base_path = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(base_path, "test_data")

    share_post.register()

    settings = get_settings()
    context = get_context(settings)

    generator = ArticlesGenerator(
        context=context,
        settings=settings,
        path=test_data_path,
        theme=settings["THEME"],
        output_path=tmp_folder,
    )
    generator.generate_context()

    run_plugin([generator])

    share_links = generator.articles[0].share_post

    assert (
        share_links["diaspora"]
        == "https://sharetodiaspora.github.io/?title=Test%20post&url=/test-post.html"
    )

    assert share_links["twitter"] == (
        "https://twitter.com/intent/tweet?text=Test%20post"
        "&url=/test-post.html&hashtags=foo,bar,foobar"
    )

    assert (
        share_links["facebook"]
        == "https://www.facebook.com/sharer/sharer.php?u=/test-post.html"
    )
    assert share_links["linkedin"] == (
        "https://www.linkedin.com/shareArticle?"
        "mini=true&url=/test-post.html&title=Test%20post&"
        "summary=I%20have%20a%20lot%20to%20test&source=/test-post.html"
    )

    assert (
        share_links["hacker-news"]
        == "https://news.ycombinator.com/submitlink?t=Test%20post&u=/test-post.html"
    )

    assert (
        share_links["email"] == "mailto:?subject=Test%20post&amp;body=/test-post.html"
    )

    assert (
        share_links["reddit"]
        == "https://www.reddit.com/submit?url=/test-post.html&title=Test%20post"
    )
