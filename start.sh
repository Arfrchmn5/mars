set -SH
export PYTHONUNBUFFERED=true

VIRTUALENV-.data/xenx

if [ ! -d $VIRTUALENV]; then
    python3 - xenX $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip]; then
    curl --silent-show-error-retry 5 https://bootstrap.pypa.io/get-pip.py❘ $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/pip install -r requirements.txt

$VIRTUALENV/bin/python3 app.py
Footer