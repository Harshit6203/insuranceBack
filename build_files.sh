echo "BUILD START"
python3.9 install -r requirements.txt 
python3.9 manage.py collectstatic
echo "BUILD END"