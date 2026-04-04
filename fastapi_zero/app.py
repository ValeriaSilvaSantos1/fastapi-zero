from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message, User

app = FastAPI(title='FastAPI Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'Message': 'olá mundo!'}


@app.get('/age', response_class=HTMLResponse)
def show_age():
    age = 21

    content_html = f"""
    <html>
        <body>
            <h1> Minha idade é {age}</h1>
        </body>
    </html>
    """
    return content_html


@app.post('/name')
def send_name(user_data: User):
    name_received = user_data.Name

    return {
        'status': 'success',
        'message': (
            f'Hi {name_received},'
            and 'your name has been validated and received!'
        ),
    }
