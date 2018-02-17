# Voiceminder Server
Repository the Voiceminder database and REST API

### Environment Setup
Install python3:
```
> brew upgrade python3
```

Install and configure virtualenv:
```
> pip install virtualenv
> mkdir ~/Python_envs
> cd ~/Python_envs
> virtualenv -p /usr/local/Cellar/python3/3.6.2/bin/python3 voicenotes
```

# Using and Updating the Environment:
Anytime you want to activate this environment:
```
> source ~/Python_envs/voicenotes/bin/activate
```

You will know if you have the environment activated or not from your
command line prompt:
```
(voicenotes) >
```

All the required python packages are defined in the
requirements.txt file. Use the `pip` command to install or
upgrade. Remember you need to do this each time someone adds a required
package to the project.
```
(voicenotes) > pip3 install -r requirements.txt
```

To add a required package to the project, use the `pip freeze` command:
```
(voicenotes) > pip3 freeze > requirements.txt
```

Run instructions
install mysql
make database voicenotes
to export env variables, copy and paste voicenotes.env from wiki into repo and change python path
export environment variables:
```
(voicenotes) > source voicenotes.env

```
then install mysql, create a database called voicenotes 

```
brew install mysql
mysql -u root -p
mysql -u username -p
CREATE DATABASE voicenotes;
```
Once voicenotes database has been created, now you can go to the your virtual environment
```
(voicenotes) > python3 src/manage.py db upgrade
(voicenotes) > python3 src/manage.py seed
(voicenotes) > python3 src/run.py
```

install localtunnel via localtunnel.me
launch in terminal
> lt -s voicenotes -p 5000

This launches api as https://voicenotes.localtunnel.me
