# A fully featured FastApi social media application
 A full-featured social media platform built using FastAPI. This project offers user authentication, profile management, real-time feeds, media uploads, comments, likes, and follower systems — all through a blazing fast, modern Python API.

## Features

- FastAPI for high-performance async APIs
- 🔐 JWT Authentication (register, login, password hashing)
- Follow/unfollow system
- Create, edit, delete posts with optional image/video uploads
- Like/unlike posts
- Comment on posts
- User profiles with bio, avatar, and stats
- Search users and posts
- Media support via S3/local storage
- Notifications system (basic)
- Pytest-based test suite
- mySQL with SQLAlchemy ORM
- Alembic for DB migrations


##  Installation
- clone `https://github.com/Adagedo/social-media-application-fastapi.git`
- cd to fastapi

## install dependencies

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## Run Migrations
- `alembic upgrade head`

## Run The App
- `uvicorn main:app --reload`
- Visit `http://localhost:8000/docs` for Swagger UI.

## Run test
- `pytest tests/`

## Docker setup
- `docker-compose up --build`

## Contributing
- Fork the repo
- Create your feature branch: git checkout -b your branch-name
- Commit your changes: git commit -m "your commit"
- Push to the branch: git push origin your branch name
- Create a new Pull Request

## Contact
Have questions? Reach out at [adagedosolomon52@email.com].


