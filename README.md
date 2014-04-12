# This repo is a work in progress, and is not yet functional.

django-wiki-migrate
===================

Migrate content from your old wiki to your shiny new
[django-wiki](https://github.com/benjaoming/django-wiki) site.

**Note: This script migrates content ONLY. It will not retain user accounts or page history.**

## Installation

    git clone git://github.com/george2/django-wiki-migrate.git
    cd django-wiki-migrate
    sudo setup.py install

## Usage

Migrating is easy!

    django-wiki-migrate [OPTIONS] FROM_URL TO_URL

For example,

    $ django-wiki-migrate --type=MediaWiki -u djangouser \
        http://myoldwiki.example.com/ http://example.com/djangowiki
    django-wiki password:
    Collecting information from your old wiki...
    Migrating page 1 of XXX: Aaa
    Migrating page 2 of XXX: Bbb
    ...
    Migrating page XXX of XXX: Zzz
    All done!

Since there is currently only one type implemented, MediaWiki, the
`--type` flag is optional.

## Extending

To add support for migrating from other types of wikis, extend the
`ToDjangoWiki` class, and implement the `findPages` and `migratePage`
methods. Then just plop your `MyWikiTypeToDjangoWiki.py` in the
`django_wiki_migrate` folder, add `MyWikiTypeToDjangoWiki` to the
`__all__` list in `__init__.py`, and send a pull request.
