echo "Cloning Repository"
git clone https://github.com/Hintpirox/allfine.git /allfine
cd /allfine
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
