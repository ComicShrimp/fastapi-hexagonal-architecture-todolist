from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    __self__ = providers.Self()

    # Allow the configuration to be provided later
    config = providers.Configuration()
