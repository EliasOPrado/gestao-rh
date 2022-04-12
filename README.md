## Sistema de gestão de RH.


### Deploy

Restart nginx:
`sudo /etc/init.d/nginx restart`

Connect Django application with uwsgin and nginx:

`uwsgi --socket mysite.sock --module gestao_rh.wsgi --chmod-socket=666`

If there is an `uswgi.ini` file add the following command to linux bash:

`uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data`