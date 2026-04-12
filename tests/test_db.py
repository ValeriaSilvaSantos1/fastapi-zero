from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, _mock_db_time):  # noqa: PT019
    with _mock_db_time(model=User) as time:
        new_user = User(
            username='test', email='test@test.com', password='secret'
        )
        session.add(new_user)  # 1. Adiciona o usuário à sessão
        session.commit()  # 2. Faz o commit enquanto o tempo está mockado

    user = session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com',
        'password': 'secret',
        'created_at': time,
    }
