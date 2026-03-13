FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git zsh curl \
    && sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token="]