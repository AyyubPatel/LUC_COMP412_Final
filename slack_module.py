from slacker import Slacker
from Stephanie.Modules.base_module import BaseModule


class SlackModule(BaseModule):
    def __init__(self, *args):
        super(SlackModule, self).__init__(*args)


    def post_on_slack(self):
        self.assistant.say("Sure, What would you like to say?")
        msg = self.assistant.listen().decipher()
        slack = Slacker('<your test token>')
        slack.chat.post_message('#<channel name>', msg)