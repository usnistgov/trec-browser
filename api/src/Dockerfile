FROM python:3

WORKDIR /usr/src/app 

COPY requirements.txt ./ 
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt  

COPY . . 

CMD [ "python", "main.py" ]