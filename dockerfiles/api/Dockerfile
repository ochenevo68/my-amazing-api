FROM python:3.11

WORKDIR /workspace

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

COPY ./pyproject.toml /workspace/

RUN poetry config virtualenvs.in-project true && poetry install --without dev

ENV PATH="/workspace/.venv/bin:${PATH}"
