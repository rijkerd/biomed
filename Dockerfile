FROM python:3.9.6-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app


# Install base dependencies
RUN apk update \ 
    && apk add build-base mysql-dev bash


# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile .
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project
COPY . .

EXPOSE 80

ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]