from operator import inv
import subprocess
import requests

github_url = 'https://github.com/jenkinsci/'

valid = 0
invalid = 0

def addGitSubmodule(plugin_name):
    bashCommand = "git submodule add " + github_url + plugin_name
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if (str(error) == 'None'):
        print(error)

with open('plugins.txt') as file:

    for line in file:

        plugin_name = line.rstrip().split(":", 1)[0]

        if plugin_name.endswith('plugin'):
            response = requests.get(github_url + plugin_name)
            if response.status_code == 200:
                valid += 1
        else:
            plugin_name += '-plugin'
            response = requests.get(github_url + plugin_name)
            if response.status_code == 200:
                valid += 1
            else:
                print(plugin_name)
                invalid += 1


print("Valid " + str(valid))
print("Invalid " + str(invalid))
