
from vsg.token import condition_clause as token

from vsg.vhdlFile.classify_new import condition

from vsg.vhdlFile import utils

'''
    condition_clause ::=
        until condition
'''

def detect(iToken, lObjects):
    if utils.is_next_token('until', iToken, lObjects):
        return True
    return False


def classify_until(lUntils, iToken, lObjects):

    iCurrent = utils.assign_next_token_required('until', token.until_keyword, iToken, lObjects)

    iCurrent = condition.classify_until(lUntils, iCurrent, lObjects)

    return iCurrent
