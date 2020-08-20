
from vsg import parser

from vsg.token import for_generate_statement as token

from vsg.vhdlFile.classify import parameter_specification
from vsg.vhdlFile.classify import generate_statement_body


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    for_generate_statement ::=
        generate_label :
            for generate_parameter_specification generate
                generate_statement_body
            end generate [ generate_label ] ;
    '''

    if not dVars['for_generate_statement']['for']:

        if classify_for_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['for_generate_statement']['generate']:

            if classify_generate_keyword(oObject, iObject, lObjects, dVars):
                return True

            if parameter_specification.tokenize(oObject, iObject, lObjects, dVars):
                return True

        else:

            if not dVars['for_generate_statement']['end']:

                if generate_statement_body.tokenize(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_keyword(oObject, iObject, lObjects, dVars):
                    return True

            else:

                if classify_semicolon(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_generate_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_label(oObject, iObject, lObjects, dVars):
                    return True

    return False


def classify_for_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'for':
        lObjects[iObject] = token.for_keyword(sValue)
        dVars['for_generate_statement']['for'] = True
        return True
    return False


def classify_generate_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'generate':
        lObjects[iObject] = token.generate_keyword(sValue)
        dVars['for_generate_statement']['generate'] = True
        dVars['history'].append('for_generate')
        return True
    return False


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['for_generate_statement']['end'] = True
        return True
    return False


def classify_end_generate_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'generate':
        lObjects[iObject] = token.end_generate_keyword(sValue)
        return True
    return False


def classify_end_label(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.end_generate_label(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        dVars['history'].pop()
        return True
    return False


def clear_flags(dVars):
    dVars['for_generate_statement']['for'] = False
    dVars['for_generate_statement']['generate'] = False
    dVars['for_generate_statement']['end'] = False
    
