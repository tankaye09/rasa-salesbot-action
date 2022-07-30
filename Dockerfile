# FROM rasa/rasa:latest
FROM rasa/rasa-sdk:3.2.0


COPY app /app
COPY server.sh /app/server.sh

USER root
RUN chmod -R 777 /app
USER 1001
EXPOSE 5055

# RUN rasa train nlu

# ENTRYPOINT ["/app/server.sh"]