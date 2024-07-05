if ! command -v pip &> /dev/null
then
    echo "pip not found, installing..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user
    export PATH=$PATH:~/.local/bin
fi

# Install Python 3.11 if not already installed
if ! command -v python3.11 &> /dev/null
then
    echo "python3.11 not found, installing..."
    sudo apt-get update
    sudo apt-get install -y python3.11
fi

pip install -r requirements.txt
python3.11 manage.py collectstatic