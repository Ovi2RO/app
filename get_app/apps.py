from django.apps import AppConfig

"""
GetAppConfig Module

This module defines the configuration for the `get_app` Django app.

The configuration specifies various settings, including the default auto field
for models and the app's name.

Classes:
    - GetAppConfig: Configuration class for the `get_app` Django app.

"""


class GetAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'get_app'

"""
    Configuration class for the `get_app` Django app.

    This class inherits from Django's `AppConfig` and allows customization
    of various settings related to the `get_app` app.

    Attributes:
        - default_auto_field (str): Specifies the default auto field for models.
        - name (str): The name of the app.

    Example:
        ```python
        # Inside your Django app's apps.py file
        from django.apps import AppConfig

        class GetAppConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'get_app'
        ```
    """
