### Python
Make sure you have Python 3+

### Clone
Clone this repository.
```
$ git clone https://github.com/ConsenSys/defi-score
```

### Set up Virtual Environment and Install Dependencies

##### With `virtualenv`
virtualenv env --python <PATH TO PYTHON EXECUTABLE>
source env/bin/activate
pip3 install -r implementation/requirements.txts

##### With `venv`
python -m venv <ENVIRONMENT_NAME>
source env/bin/activate
pip3 install -r implementation/requirements.txt

### Environment Variables
Create a new file `.env` based on `.env.example`

### Running Code
The code can then be run by using command
```
python -m implementation
```
