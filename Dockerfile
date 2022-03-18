# Here is the build image
FROM python:3.8.0-slim as builder
COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install --user -r requirements.txt
COPY . /app
# Here is the production image

FROM python:3.8.0-slim as app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/ /home/adidas-django-auth
WORKDIR ../home/adidas-django-auth
ENV PATH=/root/.local/bin:$PATH
