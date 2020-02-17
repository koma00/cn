install_django:
	cd backend; \
	python3 -m venv venv; \
	. venv/bin/activate; \
	python3 -m pip install --upgrade pip; \
	pip install -r ../requirements.txt

install_vue:
	npm install -g @vue/cli; \
	npm install -g @vue/cli-init; \
	npm install axios vue-axios --save

run_django:
	cd backend;\
	. venv/bin/activate; \
	python manage.py runserver

run_vue:
	cd frontend; \
	npm run dev