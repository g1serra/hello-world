# Main



```
py -m venv venv
```

```
venv\scripts\activate
```

```
python.exe -m pip install --upgrade pip
```

```
pip install flask
```

```
pip freeze > requirements.txt
```

```
pip install -r requirements.txt
```

```
echo >> .env
```

```
echo >> .gitignore
```

```
*.env
venv/
```

# Git
```
git clone https://github.com/g1serra/flask4dev1.git
```
```
git init
```

```
git branch -M main
```

```
git status
```

```
git add .
```

```
git commit -m "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
```
Here's the Bash version of the Git commit command with the current date and time as the commit message:
```
git commit -m "$(date +'%Y-%m-%d %H:%M:%S')"

```
```
git push -u origin main
```
# Python
## python-dotenv
```python
pip install python-dotenv -q
```
```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

print("API_KEY: ", api_key)
print("API_SECRET: ", api_secret)
```
