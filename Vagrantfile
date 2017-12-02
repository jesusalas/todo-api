# -*- mode: ruby -*-
# vi: set ft=ruby :

# equal to the name of the root folder
PROJECT_NAME = "todo-api"

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"

  config.vm.provision "shell", path: "./deploy/setup.sh", :args => "#{PROJECT_NAME}"
  config.vm.synced_folder ".", "/var/www/#{PROJECT_NAME}"

  # guest = vm, host = local
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 5000, host: 5000
end
