from operator import inv
import subprocess
import requests

github_url = 'https://github.com/jenkinsci/'

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
                addGitSubmodule(plugin_name)
        else:
            plugin_name += '-plugin'
            response = requests.get(github_url + plugin_name)
            if response.status_code == 200:
                addGitSubmodule(plugin_name)
            else:
                print(plugin_name)
