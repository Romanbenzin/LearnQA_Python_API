FROM python
WORKDIR /test_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=DEV
CMD python -m pytest -s --alluredir=test_results/ /tests_project/Lesson_four/again/tests


#docker pull python -
#docker build -t pytest_runner . -