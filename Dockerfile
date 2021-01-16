FROM python:3

WORKDIR ./src


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PATH "$PATH:/new/path"
CMD [ "python", "./src/newsbot.py" ]
