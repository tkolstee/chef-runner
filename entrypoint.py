#!/usr/bin/env python

import os
import jinja2
import sys
import subprocess

sys.tracebacklimit = 0

url = os.getenv('url') or 'http://chef/organizations/_default'
pemfile = os.getenv('pemfile') or '/config/client.pem'
clientname = os.getenv('client_name') or 'chef-runner'

env = jinja2.Environment()
env.loader = jinja2.FileSystemLoader('/root')
template = env.get_template('client.rb.erb')
with open('/root/.chef/config.rb', 'w') as f:
    f.write(template.render({'url': url, 'client': clientname }) + "\n")

os.symlink(pemfile, '/root/.chef/client.pem')
subprocess.run(['knife', 'ssl', 'fetch'])

if len(sys.argv) <= 1:
    cmd = ['bash', '-li']
else:
    cmd = sys.argv[1:]

subprocess.run(cmd)