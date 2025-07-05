def main() -> None:
    """Default main function for utilizing the {{ cookiecutter.project_name }}."""
    from {{cookiecutter.project_slug}}.logger import getLogger
    logger = getLogger(__name__)
    logger.info("Running project: '{{ cookiecutter.project_name }}'")


if __name__ == "__main__":
    main()
