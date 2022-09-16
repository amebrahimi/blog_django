FROM python:3

WORKDIR /code

COPY requirements.txt .
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=db
ENV REDIS_URL=redis://redis:6379
ENV ENABLE_DEBUG=true

EXPOSE 8000

COPY . .


