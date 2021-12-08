FROM python:3.10-alpine

ADD EnvDefault.py /
ADD first-fit.py /
CMD [ "python3", "/first-fit.py"]
