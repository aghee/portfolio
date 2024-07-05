if ! command -v pip &> /dev/null
then
    echo "pip not found, installing..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user
    export PATH=$PATH:~/.local/bin
fi

# Install Python if not already installed
if ! command -v python &> /dev/null
then
    echo "python not found, installing..."
    sudo apt-get update
    sudo apt-get install -y python
fi

pip install -r requirements.txt
python manage.py collectstatic