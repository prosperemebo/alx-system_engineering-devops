# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.172.59.160
    HostName 54.172.59.160
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
