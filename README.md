# Voiceos Server
Repository for Voiceos websocket server

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
Activate this environment:
```
> source ~/Python_envs/voiceos/bin/activate
```

You will know if you have the environment activated or not from your
command line prompt:
```
(voiceos) >
```

All the required python packages are defined in the
requirements.txt file. Use the `pip` command to install or
upgrade. Remember you need to do this each time someone adds a required
package to the project.
```
(voiceos) > pip3 install -r requirements.txt
```

To add a required package to the project, use the `pip freeze` command:
```
(voiceos) > pip3 freeze > requirements.txt
```

Run instructions
install mysql
make database voiceos
to export env variables. Copy and paste voiceos.env from wiki into repo and change python path
export environment variables:
```
(voiceos) > source voiceos.env

```
then install mysql, create a database called voiceos 

```
brew install mysql
mysql -u root -p
mysql -u username -p
CREATE DATABASE voiceos;
```
Once voiceos database has been created, you can now go to the your virtual environment
```
(voiceos) > python3 src/manage.py db upgrade
(voiceos) > python3 src/manage.py seed
(voiceos) > python3 src/run.py
```

install voiceos via localtunnel.me
launch in terminal
> lt -s voiceos -p 5000

This launches api as https://voiceos.localtunnel.me
