#These are my extra functions that will run in shared_gui_delegate
import rosebot

class m2_handler(object):
    def __init__(self, robot):
        self.robot = rosebot.RoseBot()

    def m2_fetch_ball(self, speed, speak):
        """

        :param speed:
        :param speak:
        :return:
        """
        print('Got: ', speed, speak)

    def m2_deliver_ball(self, speed):
        """

        :param speed:
        :return:
        """
        print('Got: ', speed)
