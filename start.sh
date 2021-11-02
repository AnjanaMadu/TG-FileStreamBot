echo "Installing Requirements"
pip3 install -U pip > /dev/null
pip3 install --no-cache-dir -r requirements.txt > /dev/null
clear
python3 -m WebStreamer
