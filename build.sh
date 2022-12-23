pip install -r requirements.txt
python manage.py migrate --no-input
python -m pip install --upgrade pip --no-input
# python manage.py collectstatic --no-input
