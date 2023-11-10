# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 100.25.16.172
    HostName 100.25.16.172
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
