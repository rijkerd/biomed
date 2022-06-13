FROM python:3.9.6-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app


# Install base dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev


# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements /usr/src/app/requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project
COPY . .

EXPOSE 8000

ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]