import os, sys
import json
import requests

import dotenv
dotenv.load_dotenv(verbose=True)
remote = os.getenv('REMOTE')

def upload(storage):
    try:
        full_path = os.path.join(os.path.dirname(__file__),storage)
        with open(full_path, 'r') as f:
            d = json.load(f)
        
        assert d
        req = requests.post(remote, json=d)
        print req
        if (req.status_code == 200): #aka data was successfully recieved and interpreted without a problem
            #os.remove(full_path)
            #make the lights green or something
            return;
        # Else - raise some red light saying that the file was not properly uploaded
    except requests.exceptions.RequestException as e:
        print e
    except AssertionError:
        print "JSON term is null - could not be loaded from data"
    except IOError:
        print "Could not open file."
    except ValueError:
        print "Error with JSON interpretation."
    except Exception as e:
        print "EXCEPTION:"
        print e.message, e.args
        
if __name__ == "__main__":
    storage = 'data/storage/2019-12-24T05:27:02Z.json'
    upload(storage)