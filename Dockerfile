FROM rasa/rasa:latest

COPY app /app
COPY server.sh /app/server.sh

USER root
RUN chmod -R 777 /app
USER 1001
EXPOSE 5055

# RUN rasa train nlu
CMD rasa run actions -p process.env.PORT