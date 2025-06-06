FROM python:3.9.7-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
COPY . .
RUN pip3 install -r requirements.txt
RUN pip install lxml[html_clean]
CMD ["bash","run.sh"]
