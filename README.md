# Chef-Runner

Contains chef-workstation and python
Knife is configured to work as part of the entrypoint script.

## Usage
```
docker run -it               \
  ${CONFIGDIR}:/config       \
  ${SCRIPTSDIR}:/scripts     \
  ${COOKBOOKSDIR}:/cookbooks \
  -e url="${SERVER_URL}"     \
  -e client_name="${CLIENT}" \
  -e pemfile="${PEM_LOC}"    \
  knife node list
```
pemfile specifies the location from within the container
where the client PEM file can be found. The default is
`/config/client.pem`.

This should match the node_name specificed in client_name.

A `/root/.chef` directory is created and a `client.rb` file
populated inside with the correct values. The PEM file
is symlinked from `/root/chef/client.pem`.

Specifying a command will run it after the entrypoint completes, otherwise
you will be dropped into a root shell.

