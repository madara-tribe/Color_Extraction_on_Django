FROM gcr.io/$PROJECT_ID/quickstart-image

RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH


ADD run.sh /usr/local/bin/run.sh


ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app

CMD ["/bin/bash", "/usr/local/bin/run.sh"]
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"