===============================
XIXI (flask R0.12)
===============================

Personal flask practice website, in name of my girl


Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.zshrc`` or ``.profile``.

.. code-block:: zsh

    export APP_SECRET='something-really-secret'

Before running shell commands, set the ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables ::

    export FLASK_APP=/path/to/autoapp.py
    export FLASK_DEBUG=1

Then run the following commands to bootstrap your environment ::

    git clone https://github.com/defbobo/xixi
    cd xixi
    pip install -r requirements/dev.txt
    bower install
    flask run

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    flask run


Deployment
----------

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.


Gunicorn
--------

To deploy with gunicorn, run ::

    cd /path/to/autoapp.py
    gunicorn -w 4 -b 127.0.0.1:8000 autoapp:app &


Nginx
-----

To run server behind nginx HTTP proxy, run ::

    cd /etc/nginx/sites-available
    vi default

A simple nginx configuration ::

    server {
        listen 80;

        server_name ruihang.site;
        client_max_body_size  4M;

        access_log  /var/log/nginx/access.cms.ruihang.log;
        error_log  /var/log/nginx/error.cms.ruihang.log;

        location / {
            proxy_pass         http://127.0.0.1:8000/;
            proxy_redirect     off;

            proxy_set_header   Host                 $host;
            proxy_set_header   X-Real-IP            $remote_addr;
            proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto    $scheme;
        }

        location /static {
            alias /var/www/xixi/xixi/static;
        }

        location /robots.txt {
            alias /var/www/xixi/xixi/static/robots.txt
        }
    }



Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
