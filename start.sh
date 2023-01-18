if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hintpirox/allfine.git /allfine
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /allfine
fi
cd /allfine
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m main
