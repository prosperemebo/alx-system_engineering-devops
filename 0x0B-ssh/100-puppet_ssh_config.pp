# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 107.23.218.234
    HostName 107.23.218.234
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
