from django.apps import AppConfig


class EcommerceAppConfig(AppConfig):
    name = 'myshop'

    def ready(self):
        # import signal handlers
        import myshop.signals
