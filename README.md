# personalweb

personalweb serves as persoanl website boilerplate, made in Django. This includes a homepage, a blog, a projects section and a contact section. If it seems good for your use, go grab it. 

## Getting Started

Although using SQLite is fine. A [recent bug][sqlite bug] in SQLite made working with Django unusable after first database migration. Therefore, we'll be using MySQL.

Make sure MySQL or MariaDB is installed on local computer. Installation instruction for MySQL can be found on [MySQL Docs][mysql docs] website. Same goes for [MariaDB][mariadb docs]. Choose whatever you want. They both act same at this point of time. If you are on Fedora, MariaDB is already installed there.

Now, make a virtual environment if you haven't already so that you're not messing up your system level packages. Install packages with `pip install -r requirements.txt`.

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Then you run as with any other Django application.

    python manage.py runserver

If you are interested in deploying to cloud, see Deployment section in GitHub wiki.

## Development

Necessary dependencies.

 * `Pillow` - For handling images in blog post
 * `mysqlclient` - to talk to MySQL/MariaDB server

Development dependencies.

 * `pylint` - spot the error until it's too late
 * `autopep8` - so that you don't have to remember every moves

Found a bug? Have an idea? Create an [issue](https://github.com/santosh/personalweb/issues). Seel also [CONTRUBUTING](./.github/CONTRIBUTING.md).

## License

This project is licensed under BSD-3. See [LICENSE][license] for full license.

 [sqlite bug]: https://code.djangoproject.com/ticket/29182
 [mysql docs]: https://dev.mysql.com/doc/refman/5.7/en/installing.html
 [mariadb docs]: https://mariadb.com/kb/en/library/where-to-download-mariadb/
 [license]: https://github.com/santosh/personalweb/blob/master/LICENSE
 [personalweb deployment wiki]: https://github.com/santosh/personalweb/wiki/Deployment