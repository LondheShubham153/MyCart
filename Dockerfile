FROM python:3.7
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN chmod a+x run.sh
CMD [ "./run.sh" ]