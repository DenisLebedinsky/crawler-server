FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV=development
ENV MONGODB_URI="mongodb://admin:admin123@ds159216.mlab.com:59216/videostats"
ENV MONGODB_URI_DEV="mongodb://admin:admin123@ds159216.mlab.com:59216/videostats"
ENV HOST=127.0.0.1
ENV PORT="5000"
COPY . .
EXPOSE 5000

CMD [ "python", "app.py" ]