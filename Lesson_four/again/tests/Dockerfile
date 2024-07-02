FROM python
WORKDIR /test_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=prod
CMD python -m pytest -s --alluredir=test_results/ /tests_project/Lesson_four/again/tests

# изначальный вариант: COPY ../../../../requirements.txt .
#docker pull python - скачать контейнер
#docker build -t pytest_runner . - Запустить все команды из файла, для создания докер файла (чтобы контейнер создался)
#docker run --rm --mount type=bind,src=/Users/shchetnikov.ra/PycharmProjects/LearnQA_Python_API,target=/tests_project/ pytest_runner