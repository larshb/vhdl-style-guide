
from vsg import parser


class on_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
