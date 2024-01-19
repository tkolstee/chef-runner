FROM python:bookworm
WORKDIR /cookbooks

RUN wget -O /tmp/chef-ws.deb 'https://omnitruck.chef.io/stable/chef-workstation/download?p=debian&pv=12&m=x86_64' && dpkg -i /tmp/chef-ws.deb && rm -f /tmp/chef.deb
RUN pip install jinja2

RUN mkdir /root/.chef
VOLUME /config
VOLUME /cookbooks
VOLUME /scripts
COPY client.rb.erb /root/client.rb.erb
COPY ./entrypoint.py /entrypoint.py
RUN chmod ugo+x /entrypoint.py


ENTRYPOINT ["/entrypoint.py"]
