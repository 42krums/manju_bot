FROM python:3.6.5
WORKDIR /app
RUN pip install discord.py
CMD ["/bin/sh"]