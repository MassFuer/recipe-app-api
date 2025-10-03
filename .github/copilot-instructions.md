# Copilot Instructions for AI Coding Agents

## Project Overview
- This is a Django-based REST API for managing recipes, organized as a multi-app project.
- Main Django project: `app/`
- Core Django app: `core/` (models, admin, management commands, migrations, and tests)

## Key Structure
- `app/manage.py`: Django entry point for all management commands.
- `app/app/`: Django project settings, URLs, and WSGI/ASGI config.
- `core/`: Contains business logic, models, admin, and custom management commands.
- `core/management/commands/`: Custom Django management commands (e.g., `wait_for_db.py`).
- `core/tests/`: All tests for models, admin, and commands.

## Developer Workflows
- **Run server:**
  ```sh
  python app/manage.py runserver
  ```
- **Run tests:**
  ```sh
  python app/manage.py test core
  ```
- **Run custom management command:**
  ```sh
  python app/manage.py wait_for_db
  ```
- **Dockerized workflows:**
  - Use `docker-compose.yml` and `Dockerfile` for containerized development and deployment.

## Project Conventions
- All business logic and models live in `core/`.
- Tests are colocated in `core/tests/` and follow the `test_*.py` naming convention.
- Custom management commands are in `core/management/commands/`.
- Use `requirements.txt` for runtime dependencies and `requirements.dev.txt` for development dependencies.
- No frontend code is present; this is a backend-only API project.

## Integration & Patterns
- Django ORM is used for all data access.
- Management commands are used for operational tasks (e.g., DB readiness).
- All cross-component logic is handled via Django's app structure and settings.

## Examples
- To add a new model: create it in `core/models.py`, add tests in `core/tests/test_models.py`, and run migrations.
- To add a new management command: create a file in `core/management/commands/`, subclass `BaseCommand`, and add tests in `core/tests/test_commands.py`.

## References
- See `README.md` for a high-level project summary.
- See `core/` for all business logic and tests.
- See `app/app/settings.py` for Django settings and configuration.
