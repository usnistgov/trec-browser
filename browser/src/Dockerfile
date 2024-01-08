FROM python:3.11-bookworm

WORKDIR /usr/src/app 

COPY requirements.txt ./ 
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt  

COPY . . 

CMD [ "mkdocs", "serve", "-a", "0.0.0.0:8000" ]