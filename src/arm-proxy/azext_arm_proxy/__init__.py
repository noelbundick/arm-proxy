from azure.cli.core import AzCommandsLoader

from azext_arm_proxy._help import helps  # pylint: disable=unused-import


class ArmProxyCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType

        arm_proxy_custom = CliCommandType(operations_tmpl="azext_arm_proxy.custom#{}")
        super(ArmProxyCommandsLoader, self).__init__(
            cli_ctx=cli_ctx, custom_command_type=arm_proxy_custom
        )

    def load_command_table(self, args):
        from azext_arm_proxy.commands import load_command_table

        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_arm_proxy._params import load_arguments

        load_arguments(self, command)


COMMAND_LOADER_CLS = ArmProxyCommandsLoader
