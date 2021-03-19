# Share Post: A Plugin for Pelican

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/share-post/build)](https://github.com/pelican-plugins/share-post/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-share-post)](https://pypi.org/project/pelican-share-post/)
![License](https://img.shields.io/pypi/l/pelican-share-post?color=blue)

Share Post is a Pelican plugin that creates share links in articles that allow site visitors to share the current article with others in a privacy-friendly manner.

Many web sites have share widgets to let readers share posts on social networks. Most of these widgets are used by vendors for online tracking. These widgets can also be visually-distracting and negatively affect readers’ attention.

Share Post creates old-school URLs for some popular sites which your theme can use. These links do not have the ability to track site visitors. They can also be unobtrusive depending on how Pelican theme uses them.


Installation
------------

This plugin can be installed via:

    python -m pip install pelican-share-post

Usage
-----

This plugin adds to each Pelican article a dictionary of URLs that, when followed, allows the reader to easily share the article via specific channels. When activated, the plugin adds the attribute `share_post` to each article with the following format:

``` python
article.share_post = {
	"facebook": "<URL>",
	"email": "<URL>",
	"twitter": "<URL>",
	"diaspora": "<URL>",
	"linkedin": "<URL>",
	"hacker-news": "<URL>",
	"reddit": "<URL>",
}
```

You can then access those variables in your template. For example:

``` html+jinja
{% if article.share_post and article.status != 'draft' %}
<section>
  <p id="post-share-links">
    Share on:
    <a href="{{article.share_post['diaspora']}}" title="Share on Diaspora">Diaspora*</a>
    ❄
    <a href="{{article.share_post['twitter']}}" title="Share on Twitter">Twitter</a>
    ❄
    <a href="{{article.share_post['facebook']}}" title="Share on Facebook">Facebook</a>
    ❄
    <a href="{{article.share_post['linkedin']}}" title="Share on LinkedIn">LinkedIn</a>
    ❄
    <a href="{{article.share_post['hacker-news']}}" title="Share on HackerNews">HackerNews</a>
    ❄
    <a href="{{article.share_post['email']}}" title="Share via Email">Email</a>
    ❄
    <a href="{{article.share_post['reddit']}}" title="Share via Reddit">Reddit</a>
  </p>
</section>
{% endif %}
```

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/share-post/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html


Contributors
------------

* [Talha Mansoor](https://www.oncrashreboot.com) - talha131@gmail.com
* [Jonathan DEKHTIAR](https://github.com/DEKHTIARJonathan) - contact@jonathandekhtiar.eu
* [Justin Mayer](https://justinmayer.com)
* [Leonardo Giordani](https://www.thedigitalcatonline.com)


License
-------

This project is licensed under the MIT license.
