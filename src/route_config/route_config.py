import features.echo.echo as echo
import features.default_proccess.default_proccess as default_proccess
from type.type import (
    CommandRoutingConfig,
    UnstructuredMessageRoutingConfig,
    RouteConfig,
)


route_config: RouteConfig = RouteConfig(
    command_routing_configs=[
        CommandRoutingConfig(
            command="echo",
            description="reply with user input.",
            args=["user_input"],
            options=[],
            handler=echo.handler,
        ),
    ],
    no_command_routeing_config=UnstructuredMessageRoutingConfig(
        description="display sample message.",
        handler=default_proccess.handler,
    ),
)
