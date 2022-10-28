from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB
from app.db.repositories.users import UsersRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.comments import CommentsRepository
from app.models.domain.profiles import Profile
import asyncpg

import asyncio




DATABASE_URL="postgresql://postgres:@postgres-python:5432/anythink-market"
db = create_engine(DATABASE_URL)




p = Profile(username = "jake", bio = "I work at statefarm", image = "https://static.productionready.io/images/smiley-cyrus.jpg", following = True)




Session = sessionmaker(db)  
session = Session()

async def test():
    conn = await asyncpg.connect(DATABASE_URL)

    # Add 100 users
    for number in range(100):
    # user = await UsersRepository(conn).get_user_by_username(username="test199")
        user = await UsersRepository(conn).create_user(username=f"username-{number}", email=f"mail-{number}@gmail.com", password="test")
        # user = await UsersRepository(conn).get_user_by_username(username="test199")
        item = await ItemsRepository(conn).create_item(slug=f"slugg-{number}", title=f"titlee-{number}", description="auto-description", seller=user)
        comment = await CommentsRepository(conn).create_comment_for_item(item=item, body="auto-comment", user=user)
        # print(user)

asyncio.run(test())

print('Please fill the seeds file')
