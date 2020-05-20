def load_command_table(self, _):

    with self.command_group("arm-proxy") as g:
        g.custom_command("start", "start_arm_proxy")

    with self.command_group("arm-proxy", is_experimental=True):
        pass
