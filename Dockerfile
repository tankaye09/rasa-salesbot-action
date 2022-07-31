# FROM rasa/rasa:latest
FROM rasa/rasa-sdk:3.2.0


COPY app /app
COPY server.sh /app/server.sh

USER root
RUN chmod -R 777 /app
USER 1001

# RUN rasa train nlu
# CMD [ "run","actions","-p",process.env.PORT, "--debug"]
# CMD [ "run","actions","--debug"]
# CMD ["start","--actions","actions","-p","$PORT"]

ENTRYPOINT ["/app/server.sh"]