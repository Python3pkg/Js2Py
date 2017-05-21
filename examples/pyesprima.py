# The MIT License
#
# Copyright 2014, 2015 Piotr Dabkowski
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the 'Software'),
# to deal in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so, subject
# to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#  OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

"""
SUPPORTS WHOLE ECMA SCRIPT 6 !!!
Usage:

tree = esprima.parse('var a = 10')   # Of course supports also options just like normal esprima!

You can convert tree to python dict if you want:

tree.to_dict()
"""
from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(exports, this, arguments, var=var):
    var = Scope({'this':this, 'exports':exports, 'arguments':arguments}, var)
    var.registers(['isKeyword', 'isolateCoverGrammar', 'consumeSemicolon', 'parseLeftHandSideExpression', 'throwUnexpectedToken', 'parsePatternWithDefault', 'parseExpressionStatement', 'advanceSlash', 'lastLineStart', 'tolerateUnexpectedToken', 'WrappingSourceLocation', 'source', 'parseThrowStatement', 'addComment', 'parseSwitchStatement', 'match', 'parseEmptyStatement', 'validateParam', 'exports', 'parseConditionalExpression', 'parseStatementListItem', 'parseClassDeclaration', 'Messages', 'isAssignmentTarget', 'parseVariableDeclaration', 'Token', 'reinterpretExpressionAsPattern', 'getComplexIdentifier', 'Position', 'isWhiteSpace', 'parseWhileStatement', 'parseTemplateLiteral', 'parseTemplateElement', 'parseGroupExpression', 'scanHexLiteral', 'parseBreakStatement', 'scanBinaryLiteral', 'firstCoverInitializedNameError', 'expectCommaSeparator', 'parseParams', 'SourceLocation', 'parsePrimaryExpression', 'FnExprTokens', 'scanning', 'scanRegExpFlags', 'parseImportDeclaration', 'parseVariableDeclarationList', 'parseFunctionExpression', 'parseReturnStatement', 'recordError', 'parseExportAllDeclaration', 'collectRegex', 'expect', 'skipMultiLineComment', 'scanNumericLiteral', 'parseYieldExpression', 'index', 'isIdentifierStart', 'parsePropertyMethodFunction', 'parseProgram', 'isImplicitOctalLiteral', 'state', 'isOctalDigit', 'parseArrayInitializer', 'isDecimalDigit', 'parseClassExpression', 'parseObjectProperty', 'parseCatchClause', 'peek', 'parseArguments', 'testRegExp', 'octalToDecimal', 'parseExportDeclaration', 'parseStatement', 'lastLineNumber', 'isLineTerminator', 'parseStatementList', 'parseModuleSpecifier', 'lex', 'parseFunctionSourceElements', 'isIdentifierName', 'advance', 'inheritCoverGrammar', 'isBindingElement', 'TokenName', 'reinterpretAsCoverFormalsList', 'length', 'isFutureReservedWord', 'parseImportNamespaceSpecifier', 'parseUnaryExpression', 'parseAssignmentExpression', 'Regex', 'parseLexicalBinding', 'tolerateError', 'parseBinaryExpression', 'startLineNumber', 'extra', 'scanIdentifier', 'parseNamedImports', 'unexpectedTokenError', 'parseNonComputedProperty', 'startIndex', 'startLineStart', 'parseParam', 'parseNewExpression', 'scanRegExpBody', 'Node', 'collectToken', 'parseWithStatement', 'parseDebuggerStatement', 'parseObjectPattern', 'parseImportSpecifier', 'skipComment', 'parseVariableStatement', 'strict', 'lookaheadPropertyName', 'tokenize', 'parseVariableIdentifier', 'parseExpression', 'constructError', 'scanStringLiteral', 'parseObjectPropertyKey', 'parseArrayPattern', 'expectKeyword', 'assert', 'lineNumber', 'parseConciseBody', 'createError', 'parseLeftHandSideExpressionAllowCall', 'hasLineTerminator', 'fromCodePoint', 'parseExportNamedDeclaration', 'parseBlock', 'Syntax', 'parseExportSpecifier', 'skipSingleLineComment', 'parseDoWhileStatement', 'codePointAt', 'scanHexEscape', 'isHexDigit', 'matchContextualKeyword', 'isStrictModeReservedWord', 'binaryPrecedence', 'parse', 'matchAssign', 'WrappingNode', 'parseObjectInitializer', 'getIdentifier', 'isRestrictedWord', 'parseSwitchCase', 'parsePropertyPattern', 'parseIfStatement', 'parseFunctionDeclaration', 'parsePostfixExpression', 'parseNonComputedMember', 'parseExportDefaultDeclaration', 'lastIndex', 'parseRestElement', 'parseScriptBody', 'parseBindingList', 'scanTemplate', 'PlaceHolders', 'parseLexicalDeclaration', 'checkPatternParam', 'parsePropertyFunction', 'scanPunctuator', 'parseArrowFunctionExpression', 'throwError', 'scanUnicodeCodePointEscape', 'scanOctalLiteral', 'scanRegExp', 'parseImportDefaultSpecifier', 'parsePattern', 'lineStart', 'parseForStatement', 'isIdentifierPart', 'matchKeyword', 'lookahead', 'parseTryStatement', 'parseComputedMember', 'parseContinueStatement', 'tryParseMethodDefinition', 'parseClassBody', 'filterTokenLocation'])
    @Js
    def PyJsHoisted_consumeSemicolon_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if (PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('startIndex')),Js(59)) or var.get('match')(Js(';'))):
            var.get('lex')()
            return var.get('undefined')
        if var.get('hasLineTerminator'):
            return var.get('undefined')
        var.put('lastIndex', var.get('startIndex'))
        var.put('lastLineNumber', var.get('startLineNumber'))
        var.put('lastLineStart', var.get('startLineStart'))
        if (PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('EOF')) and var.get('match')(Js('}')).neg()):
            var.get('throwUnexpectedToken')(var.get('lookahead'))
    PyJsHoisted_consumeSemicolon_.__name__ = 'consumeSemicolon'
    var.put('consumeSemicolon', PyJsHoisted_consumeSemicolon_)
    @Js
    def PyJsHoisted_isolateCoverGrammar_(parser, this, arguments, var=var):
        var = Scope({'this':this, 'parser':parser, 'arguments':arguments}, var)
        var.registers(['oldFirstCoverInitializedNameError', 'parser', 'oldIsBindingElement', 'oldIsAssignmentTarget', 'result'])
        var.put('oldIsBindingElement', var.get('isBindingElement'))
        var.put('oldIsAssignmentTarget', var.get('isAssignmentTarget'))
        var.put('oldFirstCoverInitializedNameError', var.get('firstCoverInitializedNameError'))
        var.put('isBindingElement', var.get('true'))
        var.put('isAssignmentTarget', var.get('true'))
        var.put('firstCoverInitializedNameError', var.get("null"))
        var.put('result', var.get('parser')())
        if PyJsStrictNeq(var.get('firstCoverInitializedNameError'),var.get("null")):
            var.get('throwUnexpectedToken')(var.get('firstCoverInitializedNameError'))
        var.put('isBindingElement', var.get('oldIsBindingElement'))
        var.put('isAssignmentTarget', var.get('oldIsAssignmentTarget'))
        var.put('firstCoverInitializedNameError', var.get('oldFirstCoverInitializedNameError'))
        return var.get('result')
    PyJsHoisted_isolateCoverGrammar_.__name__ = 'isolateCoverGrammar'
    var.put('isolateCoverGrammar', PyJsHoisted_isolateCoverGrammar_)
    @Js
    def PyJsHoisted_parseLeftHandSideExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'quasi', 'property', 'startToken'])
        pass
        var.get('assert')(var.get('state').get('allowIn'), Js('callee of new expression always allow in keyword.'))
        var.put('startToken', var.get('lookahead'))
        if (var.get('matchKeyword')(Js('super')) and var.get('state').get('inFunctionBody')):
            var.put('expr', var.get('Node').create())
            var.get('lex')()
            var.put('expr', var.get('expr').callprop('finishSuper'))
            if (var.get('match')(Js('[')).neg() and var.get('match')(Js('.')).neg()):
                var.get('throwUnexpectedToken')(var.get('lookahead'))
        else:
            var.put('expr', var.get('inheritCoverGrammar')((var.get('parseNewExpression') if var.get('matchKeyword')(Js('new')) else var.get('parsePrimaryExpression'))))
        #for JS loop

        while 1:
            if var.get('match')(Js('[')):
                var.put('isBindingElement', Js(False))
                var.put('isAssignmentTarget', var.get('true'))
                var.put('property', var.get('parseComputedMember')())
                var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishMemberExpression', Js('['), var.get('expr'), var.get('property')))
            else:
                if var.get('match')(Js('.')):
                    var.put('isBindingElement', Js(False))
                    var.put('isAssignmentTarget', var.get('true'))
                    var.put('property', var.get('parseNonComputedMember')())
                    var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishMemberExpression', Js('.'), var.get('expr'), var.get('property')))
                else:
                    if (PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Template')) and var.get('lookahead').get('head')):
                        var.put('quasi', var.get('parseTemplateLiteral')())
                        var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishTaggedTemplateExpression', var.get('expr'), var.get('quasi')))
                    else:
                        break

        return var.get('expr')
    PyJsHoisted_parseLeftHandSideExpression_.__name__ = 'parseLeftHandSideExpression'
    var.put('parseLeftHandSideExpression', PyJsHoisted_parseLeftHandSideExpression_)
    @Js
    def PyJsHoisted_throwUnexpectedToken_(token, message, this, arguments, var=var):
        var = Scope({'this':this, 'token':token, 'message':message, 'arguments':arguments}, var)
        var.registers(['token', 'message'])
        PyJsTempException = JsToPyException(var.get('unexpectedTokenError')(var.get('token'), var.get('message')))
        raise PyJsTempException
    PyJsHoisted_throwUnexpectedToken_.__name__ = 'throwUnexpectedToken'
    var.put('throwUnexpectedToken', PyJsHoisted_throwUnexpectedToken_)
    @Js
    def PyJsHoisted_parsePatternWithDefault_(params, kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'params':params, 'arguments':arguments}, var)
        var.registers(['kind', 'right', 'startToken', 'params', 'previousAllowYield', 'pattern'])
        var.put('startToken', var.get('lookahead'))
        var.put('pattern', var.get('parsePattern')(var.get('params'), var.get('kind')))
        if var.get('match')(Js('=')):
            var.get('lex')()
            var.put('previousAllowYield', var.get('state').get('allowYield'))
            var.get('state').put('allowYield', var.get('true'))
            var.put('right', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
            var.get('state').put('allowYield', var.get('previousAllowYield'))
            var.put('pattern', var.get('WrappingNode').create(var.get('startToken')).callprop('finishAssignmentPattern', var.get('pattern'), var.get('right')))
        return var.get('pattern')
    PyJsHoisted_parsePatternWithDefault_.__name__ = 'parsePatternWithDefault'
    var.put('parsePatternWithDefault', PyJsHoisted_parsePatternWithDefault_)
    @Js
    def PyJsHoisted_parseExpressionStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'expr'])
        var.put('expr', var.get('parseExpression')())
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishExpressionStatement', var.get('expr'))
    PyJsHoisted_parseExpressionStatement_.__name__ = 'parseExpressionStatement'
    var.put('parseExpressionStatement', PyJsHoisted_parseExpressionStatement_)
    @Js
    def PyJsHoisted_advanceSlash_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['checkToken', 'prevToken'])
        pass
        var.put('prevToken', var.get('extra').get('tokens').get((var.get('extra').get('tokens').get('length')-Js(1.0))))
        if var.get('prevToken').neg():
            return var.get('collectRegex')()
        if PyJsStrictEq(var.get('prevToken').get('type'),Js('Punctuator')):
            if PyJsStrictEq(var.get('prevToken').get('value'),Js(']')):
                return var.get('scanPunctuator')()
            if PyJsStrictEq(var.get('prevToken').get('value'),Js(')')):
                var.put('checkToken', var.get('extra').get('tokens').get((var.get('extra').get('openParenToken')-Js(1.0))))
                if ((var.get('checkToken') and PyJsStrictEq(var.get('checkToken').get('type'),Js('Keyword'))) and (((PyJsStrictEq(var.get('checkToken').get('value'),Js('if')) or PyJsStrictEq(var.get('checkToken').get('value'),Js('while'))) or PyJsStrictEq(var.get('checkToken').get('value'),Js('for'))) or PyJsStrictEq(var.get('checkToken').get('value'),Js('with')))):
                    return var.get('collectRegex')()
                return var.get('scanPunctuator')()
            if PyJsStrictEq(var.get('prevToken').get('value'),Js('}')):
                if (var.get('extra').get('tokens').get((var.get('extra').get('openCurlyToken')-Js(3.0))) and PyJsStrictEq(var.get('extra').get('tokens').get((var.get('extra').get('openCurlyToken')-Js(3.0))).get('type'),Js('Keyword'))):
                    var.put('checkToken', var.get('extra').get('tokens').get((var.get('extra').get('openCurlyToken')-Js(4.0))))
                    if var.get('checkToken').neg():
                        return var.get('scanPunctuator')()
                else:
                    if (var.get('extra').get('tokens').get((var.get('extra').get('openCurlyToken')-Js(4.0))) and PyJsStrictEq(var.get('extra').get('tokens').get((var.get('extra').get('openCurlyToken')-Js(4.0))).get('type'),Js('Keyword'))):
                        var.put('checkToken', var.get('extra').get('tokens').get((var.get('extra').get('openCurlyToken')-Js(5.0))))
                        if var.get('checkToken').neg():
                            return var.get('collectRegex')()
                    else:
                        return var.get('scanPunctuator')()
                if (var.get('FnExprTokens').callprop('indexOf', var.get('checkToken').get('value'))>=Js(0.0)):
                    return var.get('scanPunctuator')()
                return var.get('collectRegex')()
            return var.get('collectRegex')()
        if (PyJsStrictEq(var.get('prevToken').get('type'),Js('Keyword')) and PyJsStrictNeq(var.get('prevToken').get('value'),Js('this'))):
            return var.get('collectRegex')()
        return var.get('scanPunctuator')()
    PyJsHoisted_advanceSlash_.__name__ = 'advanceSlash'
    var.put('advanceSlash', PyJsHoisted_advanceSlash_)
    @Js
    def PyJsHoisted_parseIfStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['test', 'node', 'alternate', 'consequent'])
        pass
        var.get('expectKeyword')(Js('if'))
        var.get('expect')(Js('('))
        var.put('test', var.get('parseExpression')())
        var.get('expect')(Js(')'))
        var.put('consequent', var.get('parseStatement')())
        if var.get('matchKeyword')(Js('else')):
            var.get('lex')()
            var.put('alternate', var.get('parseStatement')())
        else:
            var.put('alternate', var.get("null"))
        return var.get('node').callprop('finishIfStatement', var.get('test'), var.get('consequent'), var.get('alternate'))
    PyJsHoisted_parseIfStatement_.__name__ = 'parseIfStatement'
    var.put('parseIfStatement', PyJsHoisted_parseIfStatement_)
    @Js
    def PyJsHoisted_tolerateUnexpectedToken_(token, message, this, arguments, var=var):
        var = Scope({'this':this, 'token':token, 'message':message, 'arguments':arguments}, var)
        var.registers(['token', 'message', 'error'])
        var.put('error', var.get('unexpectedTokenError')(var.get('token'), var.get('message')))
        if var.get('extra').get('errors'):
            var.get('recordError')(var.get('error'))
        else:
            PyJsTempException = JsToPyException(var.get('error'))
            raise PyJsTempException
    PyJsHoisted_tolerateUnexpectedToken_.__name__ = 'tolerateUnexpectedToken'
    var.put('tolerateUnexpectedToken', PyJsHoisted_tolerateUnexpectedToken_)
    @Js
    def PyJsHoisted_WrappingSourceLocation_(startToken, this, arguments, var=var):
        var = Scope({'this':this, 'startToken':startToken, 'arguments':arguments}, var)
        var.registers(['startToken'])
        PyJs_Object_48_ = Js({'line':var.get('startToken').get('lineNumber'),'column':(var.get('startToken').get('start')-var.get('startToken').get('lineStart'))})
        var.get("this").put('start', PyJs_Object_48_)
        var.get("this").put('end', var.get("null"))
    PyJsHoisted_WrappingSourceLocation_.__name__ = 'WrappingSourceLocation'
    var.put('WrappingSourceLocation', PyJsHoisted_WrappingSourceLocation_)
    @Js
    def PyJsHoisted_scanStringLiteral_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['ch', 'octToDec', 'quote', 'start', 'str', 'unescaped', 'octal'])
        var.put('str', Js(''))
        var.put('octal', Js(False))
        var.put('quote', var.get('source').get(var.get('index')))
        var.get('assert')((PyJsStrictEq(var.get('quote'),Js("'")) or PyJsStrictEq(var.get('quote'),Js('"'))), Js('String literal must starts with a quote'))
        var.put('start', var.get('index'))
        var.put('index',Js(var.get('index').to_number())+Js(1))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if PyJsStrictEq(var.get('ch'),var.get('quote')):
                var.put('quote', Js(''))
                break
            else:
                if PyJsStrictEq(var.get('ch'),Js('\\')):
                    var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                    if (var.get('ch').neg() or var.get('isLineTerminator')(var.get('ch').callprop('charCodeAt', Js(0.0))).neg()):
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('ch'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('u')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('x')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('source').get(var.get('index')),Js('{')):
                                    var.put('index',Js(var.get('index').to_number())+Js(1))
                                    var.put('str', var.get('scanUnicodeCodePointEscape')(), '+')
                                else:
                                    var.put('unescaped', var.get('scanHexEscape')(var.get('ch')))
                                    if var.get('unescaped').neg():
                                        PyJsTempException = JsToPyException(var.get('throwUnexpectedToken')())
                                        raise PyJsTempException
                                    var.put('str', var.get('unescaped'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                                SWITCHED = True
                                var.put('str', Js('\n'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                                SWITCHED = True
                                var.put('str', Js('\r'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('t')):
                                SWITCHED = True
                                var.put('str', Js('\t'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                                SWITCHED = True
                                var.put('str', Js('\x08'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                                SWITCHED = True
                                var.put('str', Js('\x0c'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('v')):
                                SWITCHED = True
                                var.put('str', Js('\x0b'), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('8')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('9')):
                                SWITCHED = True
                                var.put('str', var.get('ch'), '+')
                                var.get('tolerateUnexpectedToken')()
                                break
                            if True:
                                SWITCHED = True
                                if var.get('isOctalDigit')(var.get('ch')):
                                    var.put('octToDec', var.get('octalToDecimal')(var.get('ch')))
                                    var.put('octal', (var.get('octToDec').get('octal') or var.get('octal')))
                                    var.put('str', var.get('String').callprop('fromCharCode', var.get('octToDec').get('code')), '+')
                                else:
                                    var.put('str', var.get('ch'), '+')
                                break
                            SWITCHED = True
                            break
                    else:
                        var.put('lineNumber',Js(var.get('lineNumber').to_number())+Js(1))
                        if (PyJsStrictEq(var.get('ch'),Js('\r')) and PyJsStrictEq(var.get('source').get(var.get('index')),Js('\n'))):
                            var.put('index',Js(var.get('index').to_number())+Js(1))
                        var.put('lineStart', var.get('index'))
                else:
                    if var.get('isLineTerminator')(var.get('ch').callprop('charCodeAt', Js(0.0))):
                        break
                    else:
                        var.put('str', var.get('ch'), '+')
        if PyJsStrictNeq(var.get('quote'),Js('')):
            var.get('throwUnexpectedToken')()
        PyJs_Object_28_ = Js({'type':var.get('Token').get('StringLiteral'),'value':var.get('str'),'octal':var.get('octal'),'lineNumber':var.get('startLineNumber'),'lineStart':var.get('startLineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_28_
    PyJsHoisted_scanStringLiteral_.__name__ = 'scanStringLiteral'
    var.put('scanStringLiteral', PyJsHoisted_scanStringLiteral_)
    @Js
    def PyJsHoisted_parseThrowStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'argument'])
        pass
        var.get('expectKeyword')(Js('throw'))
        if var.get('hasLineTerminator'):
            var.get('throwError')(var.get('Messages').get('NewlineAfterThrow'))
        var.put('argument', var.get('parseExpression')())
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishThrowStatement', var.get('argument'))
    PyJsHoisted_parseThrowStatement_.__name__ = 'parseThrowStatement'
    var.put('parseThrowStatement', PyJsHoisted_parseThrowStatement_)
    @Js
    def PyJsHoisted_addComment_(type, value, start, end, loc, this, arguments, var=var):
        var = Scope({'start':start, 'end':end, 'arguments':arguments, 'loc':loc, 'this':this, 'type':type, 'value':value}, var)
        var.registers(['comment', 'loc', 'end', 'value', 'start', 'type'])
        pass
        var.get('assert')(PyJsStrictEq(var.get('start',throw=False).typeof(),Js('number')), Js('Comment must have valid position'))
        var.get('state').put('lastCommentStart', var.get('start'))
        PyJs_Object_11_ = Js({'type':var.get('type'),'value':var.get('value')})
        var.put('comment', PyJs_Object_11_)
        if var.get('extra').get('range'):
            var.get('comment').put('range', Js([var.get('start'), var.get('end')]))
        if var.get('extra').get('loc'):
            var.get('comment').put('loc', var.get('loc'))
        var.get('extra').get('comments').callprop('push', var.get('comment'))
        if var.get('extra').get('attachComment'):
            var.get('extra').get('leadingComments').callprop('push', var.get('comment'))
            var.get('extra').get('trailingComments').callprop('push', var.get('comment'))
    PyJsHoisted_addComment_.__name__ = 'addComment'
    var.put('addComment', PyJsHoisted_addComment_)
    @Js
    def PyJsHoisted_parseSwitchStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'discriminant', 'clause', 'defaultFound', 'oldInSwitch', 'cases'])
        pass
        var.get('expectKeyword')(Js('switch'))
        var.get('expect')(Js('('))
        var.put('discriminant', var.get('parseExpression')())
        var.get('expect')(Js(')'))
        var.get('expect')(Js('{'))
        var.put('cases', Js([]))
        if var.get('match')(Js('}')):
            var.get('lex')()
            return var.get('node').callprop('finishSwitchStatement', var.get('discriminant'), var.get('cases'))
        var.put('oldInSwitch', var.get('state').get('inSwitch'))
        var.get('state').put('inSwitch', var.get('true'))
        var.put('defaultFound', Js(False))
        while (var.get('startIndex')<var.get('length')):
            if var.get('match')(Js('}')):
                break
            var.put('clause', var.get('parseSwitchCase')())
            if PyJsStrictEq(var.get('clause').get('test'),var.get("null")):
                if var.get('defaultFound'):
                    var.get('throwError')(var.get('Messages').get('MultipleDefaultsInSwitch'))
                var.put('defaultFound', var.get('true'))
            var.get('cases').callprop('push', var.get('clause'))
        var.get('state').put('inSwitch', var.get('oldInSwitch'))
        var.get('expect')(Js('}'))
        return var.get('node').callprop('finishSwitchStatement', var.get('discriminant'), var.get('cases'))
    PyJsHoisted_parseSwitchStatement_.__name__ = 'parseSwitchStatement'
    var.put('parseSwitchStatement', PyJsHoisted_parseSwitchStatement_)
    @Js
    def PyJsHoisted_match_(value, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'value':value}, var)
        var.registers(['value'])
        return (PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Punctuator')) and PyJsStrictEq(var.get('lookahead').get('value'),var.get('value')))
    PyJsHoisted_match_.__name__ = 'match'
    var.put('match', PyJsHoisted_match_)
    @Js
    def PyJsHoisted_parseEmptyStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node'])
        var.get('expect')(Js(';'))
        return var.get('node').callprop('finishEmptyStatement')
    PyJsHoisted_parseEmptyStatement_.__name__ = 'parseEmptyStatement'
    var.put('parseEmptyStatement', PyJsHoisted_parseEmptyStatement_)
    @Js
    def PyJsHoisted_validateParam_(options, param, name, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'options':options, 'param':param, 'name':name}, var)
        var.registers(['param', 'options', 'key', 'name'])
        var.put('key', (Js('$')+var.get('name')))
        if var.get('strict'):
            if var.get('isRestrictedWord')(var.get('name')):
                var.get('options').put('stricted', var.get('param'))
                var.get('options').put('message', var.get('Messages').get('StrictParamName'))
            if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('options').get('paramSet'), var.get('key')):
                var.get('options').put('stricted', var.get('param'))
                var.get('options').put('message', var.get('Messages').get('StrictParamDupe'))
        else:
            if var.get('options').get('firstRestricted').neg():
                if var.get('isRestrictedWord')(var.get('name')):
                    var.get('options').put('firstRestricted', var.get('param'))
                    var.get('options').put('message', var.get('Messages').get('StrictParamName'))
                else:
                    if var.get('isStrictModeReservedWord')(var.get('name')):
                        var.get('options').put('firstRestricted', var.get('param'))
                        var.get('options').put('message', var.get('Messages').get('StrictReservedWord'))
                    else:
                        if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('options').get('paramSet'), var.get('key')):
                            var.get('options').put('stricted', var.get('param'))
                            var.get('options').put('message', var.get('Messages').get('StrictParamDupe'))
        var.get('options').get('paramSet').put(var.get('key'), var.get('true'))
    PyJsHoisted_validateParam_.__name__ = 'validateParam'
    var.put('validateParam', PyJsHoisted_validateParam_)
    @Js
    def PyJsHoisted_parseConditionalExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['previousAllowIn', 'expr', 'alternate', 'startToken', 'consequent'])
        pass
        var.put('startToken', var.get('lookahead'))
        var.put('expr', var.get('inheritCoverGrammar')(var.get('parseBinaryExpression')))
        if var.get('match')(Js('?')):
            var.get('lex')()
            var.put('previousAllowIn', var.get('state').get('allowIn'))
            var.get('state').put('allowIn', var.get('true'))
            var.put('consequent', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
            var.get('state').put('allowIn', var.get('previousAllowIn'))
            var.get('expect')(Js(':'))
            var.put('alternate', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
            var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishConditionalExpression', var.get('expr'), var.get('consequent'), var.get('alternate')))
            var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
        return var.get('expr')
    PyJsHoisted_parseConditionalExpression_.__name__ = 'parseConditionalExpression'
    var.put('parseConditionalExpression', PyJsHoisted_parseConditionalExpression_)
    @Js
    def PyJsHoisted_parseStatementListItem_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Keyword')):
            while 1:
                SWITCHED = False
                CONDITION = (var.get('lookahead').get('value'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('export')):
                    SWITCHED = True
                    if PyJsStrictNeq(var.get('state').get('sourceType'),Js('module')):
                        var.get('tolerateUnexpectedToken')(var.get('lookahead'), var.get('Messages').get('IllegalExportDeclaration'))
                    return var.get('parseExportDeclaration')()
                if SWITCHED or PyJsStrictEq(CONDITION, Js('import')):
                    SWITCHED = True
                    if PyJsStrictNeq(var.get('state').get('sourceType'),Js('module')):
                        var.get('tolerateUnexpectedToken')(var.get('lookahead'), var.get('Messages').get('IllegalImportDeclaration'))
                    return var.get('parseImportDeclaration')()
                if SWITCHED or PyJsStrictEq(CONDITION, Js('const')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('let')):
                    SWITCHED = True
                    PyJs_Object_138_ = Js({'inFor':Js(False)})
                    return var.get('parseLexicalDeclaration')(PyJs_Object_138_)
                if SWITCHED or PyJsStrictEq(CONDITION, Js('function')):
                    SWITCHED = True
                    return var.get('parseFunctionDeclaration')(var.get('Node').create())
                if SWITCHED or PyJsStrictEq(CONDITION, Js('class')):
                    SWITCHED = True
                    return var.get('parseClassDeclaration')()
                SWITCHED = True
                break
        return var.get('parseStatement')()
    PyJsHoisted_parseStatementListItem_.__name__ = 'parseStatementListItem'
    var.put('parseStatementListItem', PyJsHoisted_parseStatementListItem_)
    @Js
    def PyJsHoisted_parseClassDeclaration_(identifierIsOptional, this, arguments, var=var):
        var = Scope({'this':this, 'identifierIsOptional':identifierIsOptional, 'arguments':arguments}, var)
        var.registers(['identifierIsOptional', 'previousStrict', 'superClass', 'classNode', 'id', 'classBody'])
        var.put('id', var.get("null"))
        var.put('superClass', var.get("null"))
        var.put('classNode', var.get('Node').create())
        var.put('previousStrict', var.get('strict'))
        var.put('strict', var.get('true'))
        var.get('expectKeyword')(Js('class'))
        if (var.get('identifierIsOptional').neg() or PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier'))):
            var.put('id', var.get('parseVariableIdentifier')())
        if var.get('matchKeyword')(Js('extends')):
            var.get('lex')()
            var.put('superClass', var.get('isolateCoverGrammar')(var.get('parseLeftHandSideExpressionAllowCall')))
        var.put('classBody', var.get('parseClassBody')())
        var.put('strict', var.get('previousStrict'))
        return var.get('classNode').callprop('finishClassDeclaration', var.get('id'), var.get('superClass'), var.get('classBody'))
    PyJsHoisted_parseClassDeclaration_.__name__ = 'parseClassDeclaration'
    var.put('parseClassDeclaration', PyJsHoisted_parseClassDeclaration_)
    @Js
    def PyJsHoisted_parseVariableDeclaration_(options, this, arguments, var=var):
        var = Scope({'this':this, 'options':options, 'arguments':arguments}, var)
        var.registers(['node', 'init', 'params', 'id', 'options'])
        var.put('init', var.get("null"))
        var.put('node', var.get('Node').create())
        var.put('params', Js([]))
        var.put('id', var.get('parsePattern')(var.get('params'), Js('var')))
        if (var.get('strict') and var.get('isRestrictedWord')(var.get('id').get('name'))):
            var.get('tolerateError')(var.get('Messages').get('StrictVarName'))
        if var.get('match')(Js('=')):
            var.get('lex')()
            var.put('init', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
        else:
            if (PyJsStrictNeq(var.get('id').get('type'),var.get('Syntax').get('Identifier')) and var.get('options').get('inFor').neg()):
                var.get('expect')(Js('='))
        return var.get('node').callprop('finishVariableDeclarator', var.get('id'), var.get('init'))
    PyJsHoisted_parseVariableDeclaration_.__name__ = 'parseVariableDeclaration'
    var.put('parseVariableDeclaration', PyJsHoisted_parseVariableDeclaration_)
    @Js
    def PyJsHoisted_reinterpretExpressionAsPattern_(expr, this, arguments, var=var):
        var = Scope({'this':this, 'expr':expr, 'arguments':arguments}, var)
        var.registers(['i', 'expr'])
        pass
        while 1:
            SWITCHED = False
            CONDITION = (var.get('expr').get('type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('Identifier')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('MemberExpression')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('RestElement')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('AssignmentPattern')):
                SWITCHED = True
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('SpreadElement')):
                SWITCHED = True
                var.get('expr').put('type', var.get('Syntax').get('RestElement'))
                var.get('reinterpretExpressionAsPattern')(var.get('expr').get('argument'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('ArrayExpression')):
                SWITCHED = True
                var.get('expr').put('type', var.get('Syntax').get('ArrayPattern'))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('expr').get('elements').get('length')):
                    try:
                        if PyJsStrictNeq(var.get('expr').get('elements').get(var.get('i')),var.get("null")):
                            var.get('reinterpretExpressionAsPattern')(var.get('expr').get('elements').get(var.get('i')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('ObjectExpression')):
                SWITCHED = True
                var.get('expr').put('type', var.get('Syntax').get('ObjectPattern'))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('expr').get('properties').get('length')):
                    try:
                        var.get('reinterpretExpressionAsPattern')(var.get('expr').get('properties').get(var.get('i')).get('value'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('AssignmentExpression')):
                SWITCHED = True
                var.get('expr').put('type', var.get('Syntax').get('AssignmentPattern'))
                var.get('reinterpretExpressionAsPattern')(var.get('expr').get('left'))
                break
            if True:
                SWITCHED = True
                break
            SWITCHED = True
            break
    PyJsHoisted_reinterpretExpressionAsPattern_.__name__ = 'reinterpretExpressionAsPattern'
    var.put('reinterpretExpressionAsPattern', PyJsHoisted_reinterpretExpressionAsPattern_)
    @Js
    def PyJsHoisted_getComplexIdentifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['ch', 'cp', 'id'])
        pass
        var.put('cp', var.get('codePointAt')(var.get('index')))
        var.put('id', var.get('fromCodePoint')(var.get('cp')))
        var.put('index', var.get('id').get('length'), '+')
        if PyJsStrictEq(var.get('cp'),Js(92)):
            if PyJsStrictNeq(var.get('source').callprop('charCodeAt', var.get('index')),Js(117)):
                var.get('throwUnexpectedToken')()
            var.put('index',Js(var.get('index').to_number())+Js(1))
            if PyJsStrictEq(var.get('source').get(var.get('index')),Js('{')):
                var.put('index',Js(var.get('index').to_number())+Js(1))
                var.put('ch', var.get('scanUnicodeCodePointEscape')())
            else:
                var.put('ch', var.get('scanHexEscape')(Js('u')))
                var.put('cp', var.get('ch').callprop('charCodeAt', Js(0.0)))
                if ((var.get('ch').neg() or PyJsStrictEq(var.get('ch'),Js('\\'))) or var.get('isIdentifierStart')(var.get('cp')).neg()):
                    var.get('throwUnexpectedToken')()
            var.put('id', var.get('ch'))
        while (var.get('index')<var.get('length')):
            var.put('cp', var.get('codePointAt')(var.get('index')))
            if var.get('isIdentifierPart')(var.get('cp')).neg():
                break
            var.put('ch', var.get('fromCodePoint')(var.get('cp')))
            var.put('id', var.get('ch'), '+')
            var.put('index', var.get('ch').get('length'), '+')
            if PyJsStrictEq(var.get('cp'),Js(92)):
                var.put('id', var.get('id').callprop('substr', Js(0.0), (var.get('id').get('length')-Js(1.0))))
                if PyJsStrictNeq(var.get('source').callprop('charCodeAt', var.get('index')),Js(117)):
                    var.get('throwUnexpectedToken')()
                var.put('index',Js(var.get('index').to_number())+Js(1))
                if PyJsStrictEq(var.get('source').get(var.get('index')),Js('{')):
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                    var.put('ch', var.get('scanUnicodeCodePointEscape')())
                else:
                    var.put('ch', var.get('scanHexEscape')(Js('u')))
                    var.put('cp', var.get('ch').callprop('charCodeAt', Js(0.0)))
                    if ((var.get('ch').neg() or PyJsStrictEq(var.get('ch'),Js('\\'))) or var.get('isIdentifierPart')(var.get('cp')).neg()):
                        var.get('throwUnexpectedToken')()
                var.put('id', var.get('ch'), '+')
        return var.get('id')
    PyJsHoisted_getComplexIdentifier_.__name__ = 'getComplexIdentifier'
    var.put('getComplexIdentifier', PyJsHoisted_getComplexIdentifier_)
    @Js
    def PyJsHoisted_Position_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get("this").put('line', var.get('startLineNumber'))
        var.get("this").put('column', (var.get('startIndex')-var.get('startLineStart')))
    PyJsHoisted_Position_.__name__ = 'Position'
    var.put('Position', PyJsHoisted_Position_)
    @Js
    def PyJsHoisted_isWhiteSpace_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        def PyJs_LONG_9_(var=var):
            return (((((PyJsStrictEq(var.get('ch'),Js(32)) or PyJsStrictEq(var.get('ch'),Js(9))) or PyJsStrictEq(var.get('ch'),Js(11))) or PyJsStrictEq(var.get('ch'),Js(12))) or PyJsStrictEq(var.get('ch'),Js(160))) or ((var.get('ch')>=Js(5760)) and (Js([Js(5760), Js(6158), Js(8192), Js(8193), Js(8194), Js(8195), Js(8196), Js(8197), Js(8198), Js(8199), Js(8200), Js(8201), Js(8202), Js(8239), Js(8287), Js(12288), Js(65279)]).callprop('indexOf', var.get('ch'))>=Js(0.0))))
        return PyJs_LONG_9_()
    PyJsHoisted_isWhiteSpace_.__name__ = 'isWhiteSpace'
    var.put('isWhiteSpace', PyJsHoisted_isWhiteSpace_)
    @Js
    def PyJsHoisted_parseWhileStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['test', 'body', 'node', 'oldInIteration'])
        pass
        var.get('expectKeyword')(Js('while'))
        var.get('expect')(Js('('))
        var.put('test', var.get('parseExpression')())
        var.get('expect')(Js(')'))
        var.put('oldInIteration', var.get('state').get('inIteration'))
        var.get('state').put('inIteration', var.get('true'))
        var.put('body', var.get('parseStatement')())
        var.get('state').put('inIteration', var.get('oldInIteration'))
        return var.get('node').callprop('finishWhileStatement', var.get('test'), var.get('body'))
    PyJsHoisted_parseWhileStatement_.__name__ = 'parseWhileStatement'
    var.put('parseWhileStatement', PyJsHoisted_parseWhileStatement_)
    @Js
    def PyJsHoisted_parseTemplateLiteral_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['quasis', 'node', 'quasi', 'expressions'])
        var.put('node', var.get('Node').create())
        PyJs_Object_128_ = Js({'head':var.get('true')})
        var.put('quasi', var.get('parseTemplateElement')(PyJs_Object_128_))
        var.put('quasis', Js([var.get('quasi')]))
        var.put('expressions', Js([]))
        while var.get('quasi').get('tail').neg():
            var.get('expressions').callprop('push', var.get('parseExpression')())
            PyJs_Object_129_ = Js({'head':Js(False)})
            var.put('quasi', var.get('parseTemplateElement')(PyJs_Object_129_))
            var.get('quasis').callprop('push', var.get('quasi'))
        return var.get('node').callprop('finishTemplateLiteral', var.get('quasis'), var.get('expressions'))
    PyJsHoisted_parseTemplateLiteral_.__name__ = 'parseTemplateLiteral'
    var.put('parseTemplateLiteral', PyJsHoisted_parseTemplateLiteral_)
    @Js
    def PyJsHoisted_parseTemplateElement_(option, this, arguments, var=var):
        var = Scope({'this':this, 'option':option, 'arguments':arguments}, var)
        var.registers(['node', 'token', 'option'])
        pass
        if (PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('Template')) or (var.get('option').get('head') and var.get('lookahead').get('head').neg())):
            var.get('throwUnexpectedToken')()
        var.put('node', var.get('Node').create())
        var.put('token', var.get('lex')())
        PyJs_Object_127_ = Js({'raw':var.get('token').get('value').get('raw'),'cooked':var.get('token').get('value').get('cooked')})
        return var.get('node').callprop('finishTemplateElement', PyJs_Object_127_, var.get('token').get('tail'))
    PyJsHoisted_parseTemplateElement_.__name__ = 'parseTemplateElement'
    var.put('parseTemplateElement', PyJsHoisted_parseTemplateElement_)
    @Js
    def PyJsHoisted_parseGroupExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'expr', 'expressions', 'params', 'startToken'])
        var.put('params', Js([]))
        var.get('expect')(Js('('))
        if var.get('match')(Js(')')):
            var.get('lex')()
            if var.get('match')(Js('=>')).neg():
                var.get('expect')(Js('=>'))
            PyJs_Object_130_ = Js({'type':var.get('PlaceHolders').get('ArrowParameterPlaceHolder'),'params':Js([]),'rawParams':Js([])})
            return PyJs_Object_130_
        var.put('startToken', var.get('lookahead'))
        if var.get('match')(Js('...')):
            var.put('expr', var.get('parseRestElement')(var.get('params')))
            var.get('expect')(Js(')'))
            if var.get('match')(Js('=>')).neg():
                var.get('expect')(Js('=>'))
            PyJs_Object_131_ = Js({'type':var.get('PlaceHolders').get('ArrowParameterPlaceHolder'),'params':Js([var.get('expr')])})
            return PyJs_Object_131_
        var.put('isBindingElement', var.get('true'))
        var.put('expr', var.get('inheritCoverGrammar')(var.get('parseAssignmentExpression')))
        if var.get('match')(Js(',')):
            var.put('isAssignmentTarget', Js(False))
            var.put('expressions', Js([var.get('expr')]))
            while (var.get('startIndex')<var.get('length')):
                if var.get('match')(Js(',')).neg():
                    break
                var.get('lex')()
                if var.get('match')(Js('...')):
                    if var.get('isBindingElement').neg():
                        var.get('throwUnexpectedToken')(var.get('lookahead'))
                    var.get('expressions').callprop('push', var.get('parseRestElement')(var.get('params')))
                    var.get('expect')(Js(')'))
                    if var.get('match')(Js('=>')).neg():
                        var.get('expect')(Js('=>'))
                    var.put('isBindingElement', Js(False))
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('expressions').get('length')):
                        try:
                            var.get('reinterpretExpressionAsPattern')(var.get('expressions').get(var.get('i')))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    PyJs_Object_132_ = Js({'type':var.get('PlaceHolders').get('ArrowParameterPlaceHolder'),'params':var.get('expressions')})
                    return PyJs_Object_132_
                var.get('expressions').callprop('push', var.get('inheritCoverGrammar')(var.get('parseAssignmentExpression')))
            var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishSequenceExpression', var.get('expressions')))
        var.get('expect')(Js(')'))
        if var.get('match')(Js('=>')):
            if (PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('Identifier')) and PyJsStrictEq(var.get('expr').get('name'),Js('yield'))):
                PyJs_Object_133_ = Js({'type':var.get('PlaceHolders').get('ArrowParameterPlaceHolder'),'params':Js([var.get('expr')])})
                return PyJs_Object_133_
            if var.get('isBindingElement').neg():
                var.get('throwUnexpectedToken')(var.get('lookahead'))
            if PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('SequenceExpression')):
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('expr').get('expressions').get('length')):
                    try:
                        var.get('reinterpretExpressionAsPattern')(var.get('expr').get('expressions').get(var.get('i')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            else:
                var.get('reinterpretExpressionAsPattern')(var.get('expr'))
            PyJs_Object_134_ = Js({'type':var.get('PlaceHolders').get('ArrowParameterPlaceHolder'),'params':(var.get('expr').get('expressions') if PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('SequenceExpression')) else Js([var.get('expr')]))})
            var.put('expr', PyJs_Object_134_)
        var.put('isBindingElement', Js(False))
        return var.get('expr')
    PyJsHoisted_parseGroupExpression_.__name__ = 'parseGroupExpression'
    var.put('parseGroupExpression', PyJsHoisted_parseGroupExpression_)
    @Js
    def PyJsHoisted_scanHexLiteral_(start, this, arguments, var=var):
        var = Scope({'this':this, 'start':start, 'arguments':arguments}, var)
        var.registers(['start', 'number'])
        var.put('number', Js(''))
        while (var.get('index')<var.get('length')):
            if var.get('isHexDigit')(var.get('source').get(var.get('index'))).neg():
                break
            var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
        if PyJsStrictEq(var.get('number').get('length'),Js(0.0)):
            var.get('throwUnexpectedToken')()
        if var.get('isIdentifierStart')(var.get('source').callprop('charCodeAt', var.get('index'))):
            var.get('throwUnexpectedToken')()
        PyJs_Object_24_ = Js({'type':var.get('Token').get('NumericLiteral'),'value':var.get('parseInt')((Js('0x')+var.get('number')), Js(16.0)),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_24_
    PyJsHoisted_scanHexLiteral_.__name__ = 'scanHexLiteral'
    var.put('scanHexLiteral', PyJsHoisted_scanHexLiteral_)
    @Js
    def PyJsHoisted_parseBreakStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'key', 'label'])
        var.put('label', var.get("null"))
        var.get('expectKeyword')(Js('break'))
        if PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('lastIndex')),Js(59)):
            var.get('lex')()
            if (var.get('state').get('inIteration') or var.get('state').get('inSwitch')).neg():
                var.get('throwError')(var.get('Messages').get('IllegalBreak'))
            return var.get('node').callprop('finishBreakStatement', var.get("null"))
        if var.get('hasLineTerminator'):
            if (var.get('state').get('inIteration') or var.get('state').get('inSwitch')).neg():
                var.get('throwError')(var.get('Messages').get('IllegalBreak'))
            return var.get('node').callprop('finishBreakStatement', var.get("null"))
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier')):
            var.put('label', var.get('parseVariableIdentifier')())
            var.put('key', (Js('$')+var.get('label').get('name')))
            if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('state').get('labelSet'), var.get('key')).neg():
                var.get('throwError')(var.get('Messages').get('UnknownLabel'), var.get('label').get('name'))
        var.get('consumeSemicolon')()
        if (PyJsStrictEq(var.get('label'),var.get("null")) and (var.get('state').get('inIteration') or var.get('state').get('inSwitch')).neg()):
            var.get('throwError')(var.get('Messages').get('IllegalBreak'))
        return var.get('node').callprop('finishBreakStatement', var.get('label'))
    PyJsHoisted_parseBreakStatement_.__name__ = 'parseBreakStatement'
    var.put('parseBreakStatement', PyJsHoisted_parseBreakStatement_)
    @Js
    def PyJsHoisted_scanBinaryLiteral_(start, this, arguments, var=var):
        var = Scope({'this':this, 'start':start, 'arguments':arguments}, var)
        var.registers(['start', 'ch', 'number'])
        pass
        var.put('number', Js(''))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').get(var.get('index')))
            if (PyJsStrictNeq(var.get('ch'),Js('0')) and PyJsStrictNeq(var.get('ch'),Js('1'))):
                break
            var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
        if PyJsStrictEq(var.get('number').get('length'),Js(0.0)):
            var.get('throwUnexpectedToken')()
        if (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').callprop('charCodeAt', var.get('index')))
            if (var.get('isIdentifierStart')(var.get('ch')) or var.get('isDecimalDigit')(var.get('ch'))):
                var.get('throwUnexpectedToken')()
        PyJs_Object_25_ = Js({'type':var.get('Token').get('NumericLiteral'),'value':var.get('parseInt')(var.get('number'), Js(2.0)),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_25_
    PyJsHoisted_scanBinaryLiteral_.__name__ = 'scanBinaryLiteral'
    var.put('scanBinaryLiteral', PyJsHoisted_scanBinaryLiteral_)
    @Js
    def PyJsHoisted_parseYieldExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'previousAllowYield', 'argument', 'delegate'])
        pass
        var.put('argument', var.get("null"))
        var.put('expr', var.get('Node').create())
        var.get('expectKeyword')(Js('yield'))
        if var.get('hasLineTerminator').neg():
            var.put('previousAllowYield', var.get('state').get('allowYield'))
            var.get('state').put('allowYield', Js(False))
            var.put('delegate', var.get('match')(Js('*')))
            if var.get('delegate'):
                var.get('lex')()
                var.put('argument', var.get('parseAssignmentExpression')())
            else:
                if (((var.get('match')(Js(';')).neg() and var.get('match')(Js('}')).neg()) and var.get('match')(Js(')')).neg()) and PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('EOF'))):
                    var.put('argument', var.get('parseAssignmentExpression')())
            var.get('state').put('allowYield', var.get('previousAllowYield'))
        return var.get('expr').callprop('finishYieldExpression', var.get('argument'), var.get('delegate'))
    PyJsHoisted_parseYieldExpression_.__name__ = 'parseYieldExpression'
    var.put('parseYieldExpression', PyJsHoisted_parseYieldExpression_)
    @Js
    def PyJsHoisted_expectCommaSeparator_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['token'])
        pass
        if var.get('extra').get('errors'):
            var.put('token', var.get('lookahead'))
            if (PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Punctuator')) and PyJsStrictEq(var.get('token').get('value'),Js(','))):
                var.get('lex')()
            else:
                if (PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Punctuator')) and PyJsStrictEq(var.get('token').get('value'),Js(';'))):
                    var.get('lex')()
                    var.get('tolerateUnexpectedToken')(var.get('token'))
                else:
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('UnexpectedToken'))
        else:
            var.get('expect')(Js(','))
    PyJsHoisted_expectCommaSeparator_.__name__ = 'expectCommaSeparator'
    var.put('expectCommaSeparator', PyJsHoisted_expectCommaSeparator_)
    @Js
    def PyJsHoisted_parseParams_(firstRestricted, this, arguments, var=var):
        var = Scope({'this':this, 'firstRestricted':firstRestricted, 'arguments':arguments}, var)
        var.registers(['firstRestricted', 'options'])
        pass
        PyJs_Object_146_ = Js({'params':Js([]),'defaultCount':Js(0.0),'defaults':Js([]),'firstRestricted':var.get('firstRestricted')})
        var.put('options', PyJs_Object_146_)
        var.get('expect')(Js('('))
        if var.get('match')(Js(')')).neg():
            PyJs_Object_147_ = Js({})
            var.get('options').put('paramSet', PyJs_Object_147_)
            while (var.get('startIndex')<var.get('length')):
                if var.get('parseParam')(var.get('options')).neg():
                    break
                var.get('expect')(Js(','))
        var.get('expect')(Js(')'))
        if PyJsStrictEq(var.get('options').get('defaultCount'),Js(0.0)):
            var.get('options').put('defaults', Js([]))
        PyJs_Object_148_ = Js({'params':var.get('options').get('params'),'defaults':var.get('options').get('defaults'),'stricted':var.get('options').get('stricted'),'firstRestricted':var.get('options').get('firstRestricted'),'message':var.get('options').get('message')})
        return PyJs_Object_148_
    PyJsHoisted_parseParams_.__name__ = 'parseParams'
    var.put('parseParams', PyJsHoisted_parseParams_)
    @Js
    def PyJsHoisted_SourceLocation_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get("this").put('start', var.get('Position').create())
        var.get("this").put('end', var.get("null"))
    PyJsHoisted_SourceLocation_.__name__ = 'SourceLocation'
    var.put('SourceLocation', PyJsHoisted_SourceLocation_)
    @Js
    def PyJsHoisted_parsePrimaryExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'expr', 'token', 'type'])
        pass
        if var.get('match')(Js('(')):
            var.put('isBindingElement', Js(False))
            return var.get('inheritCoverGrammar')(var.get('parseGroupExpression'))
        if var.get('match')(Js('[')):
            return var.get('inheritCoverGrammar')(var.get('parseArrayInitializer'))
        if var.get('match')(Js('{')):
            return var.get('inheritCoverGrammar')(var.get('parseObjectInitializer'))
        var.put('type', var.get('lookahead').get('type'))
        var.put('node', var.get('Node').create())
        if PyJsStrictEq(var.get('type'),var.get('Token').get('Identifier')):
            if (PyJsStrictEq(var.get('state').get('sourceType'),Js('module')) and PyJsStrictEq(var.get('lookahead').get('value'),Js('await'))):
                var.get('tolerateUnexpectedToken')(var.get('lookahead'))
            var.put('expr', var.get('node').callprop('finishIdentifier', var.get('lex')().get('value')))
        else:
            if (PyJsStrictEq(var.get('type'),var.get('Token').get('StringLiteral')) or PyJsStrictEq(var.get('type'),var.get('Token').get('NumericLiteral'))):
                var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                if (var.get('strict') and var.get('lookahead').get('octal')):
                    var.get('tolerateUnexpectedToken')(var.get('lookahead'), var.get('Messages').get('StrictOctalLiteral'))
                var.put('expr', var.get('node').callprop('finishLiteral', var.get('lex')()))
            else:
                if PyJsStrictEq(var.get('type'),var.get('Token').get('Keyword')):
                    if ((var.get('strict').neg() and var.get('state').get('allowYield')) and var.get('matchKeyword')(Js('yield'))):
                        return var.get('parseNonComputedProperty')()
                    var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                    if var.get('matchKeyword')(Js('function')):
                        return var.get('parseFunctionExpression')()
                    if var.get('matchKeyword')(Js('this')):
                        var.get('lex')()
                        return var.get('node').callprop('finishThisExpression')
                    if var.get('matchKeyword')(Js('class')):
                        return var.get('parseClassExpression')()
                    var.get('throwUnexpectedToken')(var.get('lex')())
                else:
                    if PyJsStrictEq(var.get('type'),var.get('Token').get('BooleanLiteral')):
                        var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                        var.put('token', var.get('lex')())
                        var.get('token').put('value', PyJsStrictEq(var.get('token').get('value'),Js('true')))
                        var.put('expr', var.get('node').callprop('finishLiteral', var.get('token')))
                    else:
                        if PyJsStrictEq(var.get('type'),var.get('Token').get('NullLiteral')):
                            var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                            var.put('token', var.get('lex')())
                            var.get('token').put('value', var.get("null"))
                            var.put('expr', var.get('node').callprop('finishLiteral', var.get('token')))
                        else:
                            if (var.get('match')(Js('/')) or var.get('match')(Js('/='))):
                                var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                                var.put('index', var.get('startIndex'))
                                if PyJsStrictNeq(var.get('extra').get('tokens').typeof(),Js('undefined')):
                                    var.put('token', var.get('collectRegex')())
                                else:
                                    var.put('token', var.get('scanRegExp')())
                                var.get('lex')()
                                var.put('expr', var.get('node').callprop('finishLiteral', var.get('token')))
                            else:
                                if PyJsStrictEq(var.get('type'),var.get('Token').get('Template')):
                                    var.put('expr', var.get('parseTemplateLiteral')())
                                else:
                                    var.get('throwUnexpectedToken')(var.get('lex')())
        return var.get('expr')
    PyJsHoisted_parsePrimaryExpression_.__name__ = 'parsePrimaryExpression'
    var.put('parsePrimaryExpression', PyJsHoisted_parsePrimaryExpression_)
    @Js
    def PyJsHoisted_scanRegExpFlags_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['restore', 'ch', 'flags', 'str'])
        pass
        var.put('str', Js(''))
        var.put('flags', Js(''))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').get(var.get('index')))
            if var.get('isIdentifierPart')(var.get('ch').callprop('charCodeAt', Js(0.0))).neg():
                break
            var.put('index',Js(var.get('index').to_number())+Js(1))
            if (PyJsStrictEq(var.get('ch'),Js('\\')) and (var.get('index')<var.get('length'))):
                var.put('ch', var.get('source').get(var.get('index')))
                if PyJsStrictEq(var.get('ch'),Js('u')):
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                    var.put('restore', var.get('index'))
                    var.put('ch', var.get('scanHexEscape')(Js('u')))
                    if var.get('ch'):
                        var.put('flags', var.get('ch'), '+')
                        #for JS loop
                        var.put('str', Js('\\u'), '+')
                        while (var.get('restore')<var.get('index')):
                            try:
                                var.put('str', var.get('source').get(var.get('restore')), '+')
                            finally:
                                    var.put('restore',Js(var.get('restore').to_number())+Js(1))
                    else:
                        var.put('index', var.get('restore'))
                        var.put('flags', Js('u'), '+')
                        var.put('str', Js('\\u'), '+')
                    var.get('tolerateUnexpectedToken')()
                else:
                    var.put('str', Js('\\'), '+')
                    var.get('tolerateUnexpectedToken')()
            else:
                var.put('flags', var.get('ch'), '+')
                var.put('str', var.get('ch'), '+')
        PyJs_Object_33_ = Js({'value':var.get('flags'),'literal':var.get('str')})
        return PyJs_Object_33_
    PyJsHoisted_scanRegExpFlags_.__name__ = 'scanRegExpFlags'
    var.put('scanRegExpFlags', PyJsHoisted_scanRegExpFlags_)
    @Js
    def PyJsHoisted_parseImportDeclaration_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'specifiers', 'src'])
        var.put('specifiers', Js([]))
        var.put('node', var.get('Node').create())
        if var.get('state').get('inFunctionBody'):
            var.get('throwError')(var.get('Messages').get('IllegalImportDeclaration'))
        var.get('expectKeyword')(Js('import'))
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('StringLiteral')):
            var.put('src', var.get('parseModuleSpecifier')())
        else:
            if var.get('match')(Js('{')):
                var.put('specifiers', var.get('specifiers').callprop('concat', var.get('parseNamedImports')()))
            else:
                if var.get('match')(Js('*')):
                    var.get('specifiers').callprop('push', var.get('parseImportNamespaceSpecifier')())
                else:
                    if (var.get('isIdentifierName')(var.get('lookahead')) and var.get('matchKeyword')(Js('default')).neg()):
                        var.get('specifiers').callprop('push', var.get('parseImportDefaultSpecifier')())
                        if var.get('match')(Js(',')):
                            var.get('lex')()
                            if var.get('match')(Js('*')):
                                var.get('specifiers').callprop('push', var.get('parseImportNamespaceSpecifier')())
                            else:
                                if var.get('match')(Js('{')):
                                    var.put('specifiers', var.get('specifiers').callprop('concat', var.get('parseNamedImports')()))
                                else:
                                    var.get('throwUnexpectedToken')(var.get('lookahead'))
                    else:
                        var.get('throwUnexpectedToken')(var.get('lex')())
            if var.get('matchContextualKeyword')(Js('from')).neg():
                var.get('throwError')((var.get('Messages').get('UnexpectedToken') if var.get('lookahead').get('value') else var.get('Messages').get('MissingFromClause')), var.get('lookahead').get('value'))
            var.get('lex')()
            var.put('src', var.get('parseModuleSpecifier')())
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishImportDeclaration', var.get('specifiers'), var.get('src'))
    PyJsHoisted_parseImportDeclaration_.__name__ = 'parseImportDeclaration'
    var.put('parseImportDeclaration', PyJsHoisted_parseImportDeclaration_)
    @Js
    def PyJsHoisted_parseVariableDeclarationList_(options, this, arguments, var=var):
        var = Scope({'this':this, 'options':options, 'arguments':arguments}, var)
        var.registers(['list', 'options'])
        var.put('list', Js([]))
        while 1:
            PyJs_Object_139_ = Js({'inFor':var.get('options').get('inFor')})
            var.get('list').callprop('push', var.get('parseVariableDeclaration')(PyJs_Object_139_))
            if var.get('match')(Js(',')).neg():
                break
            var.get('lex')()
            if not (var.get('startIndex')<var.get('length')):
                break
        return var.get('list')
    PyJsHoisted_parseVariableDeclarationList_.__name__ = 'parseVariableDeclarationList'
    var.put('parseVariableDeclarationList', PyJsHoisted_parseVariableDeclarationList_)
    @Js
    def PyJsHoisted_parseFunctionExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['tmp', 'body', 'previousStrict', 'node', 'isGenerator', 'stricted', 'id', 'token', 'params', 'defaults', 'previousAllowYield', 'firstRestricted', 'message'])
        var.put('id', var.get("null"))
        var.put('params', Js([]))
        var.put('defaults', Js([]))
        var.put('node', var.get('Node').create())
        var.put('previousAllowYield', var.get('state').get('allowYield'))
        var.get('expectKeyword')(Js('function'))
        var.put('isGenerator', var.get('match')(Js('*')))
        if var.get('isGenerator'):
            var.get('lex')()
        var.get('state').put('allowYield', var.get('isGenerator').neg())
        if var.get('match')(Js('(')).neg():
            var.put('token', var.get('lookahead'))
            var.put('id', (var.get('parseNonComputedProperty')() if ((var.get('strict').neg() and var.get('isGenerator').neg()) and var.get('matchKeyword')(Js('yield'))) else var.get('parseVariableIdentifier')()))
            if var.get('strict'):
                if var.get('isRestrictedWord')(var.get('token').get('value')):
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictFunctionName'))
            else:
                if var.get('isRestrictedWord')(var.get('token').get('value')):
                    var.put('firstRestricted', var.get('token'))
                    var.put('message', var.get('Messages').get('StrictFunctionName'))
                else:
                    if var.get('isStrictModeReservedWord')(var.get('token').get('value')):
                        var.put('firstRestricted', var.get('token'))
                        var.put('message', var.get('Messages').get('StrictReservedWord'))
        var.put('tmp', var.get('parseParams')(var.get('firstRestricted')))
        var.put('params', var.get('tmp').get('params'))
        var.put('defaults', var.get('tmp').get('defaults'))
        var.put('stricted', var.get('tmp').get('stricted'))
        var.put('firstRestricted', var.get('tmp').get('firstRestricted'))
        if var.get('tmp').get('message'):
            var.put('message', var.get('tmp').get('message'))
        var.put('previousStrict', var.get('strict'))
        var.put('body', var.get('parseFunctionSourceElements')())
        if (var.get('strict') and var.get('firstRestricted')):
            var.get('throwUnexpectedToken')(var.get('firstRestricted'), var.get('message'))
        if (var.get('strict') and var.get('stricted')):
            var.get('tolerateUnexpectedToken')(var.get('stricted'), var.get('message'))
        var.put('strict', var.get('previousStrict'))
        var.get('state').put('allowYield', var.get('previousAllowYield'))
        return var.get('node').callprop('finishFunctionExpression', var.get('id'), var.get('params'), var.get('defaults'), var.get('body'), var.get('isGenerator'))
    PyJsHoisted_parseFunctionExpression_.__name__ = 'parseFunctionExpression'
    var.put('parseFunctionExpression', PyJsHoisted_parseFunctionExpression_)
    @Js
    def PyJsHoisted_parseReturnStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'argument'])
        var.put('argument', var.get("null"))
        var.get('expectKeyword')(Js('return'))
        if var.get('state').get('inFunctionBody').neg():
            var.get('tolerateError')(var.get('Messages').get('IllegalReturn'))
        if PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('lastIndex')),Js(32)):
            if var.get('isIdentifierStart')(var.get('source').callprop('charCodeAt', (var.get('lastIndex')+Js(1.0)))):
                var.put('argument', var.get('parseExpression')())
                var.get('consumeSemicolon')()
                return var.get('node').callprop('finishReturnStatement', var.get('argument'))
        if var.get('hasLineTerminator'):
            return var.get('node').callprop('finishReturnStatement', var.get("null"))
        if var.get('match')(Js(';')).neg():
            if (var.get('match')(Js('}')).neg() and PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('EOF'))):
                var.put('argument', var.get('parseExpression')())
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishReturnStatement', var.get('argument'))
    PyJsHoisted_parseReturnStatement_.__name__ = 'parseReturnStatement'
    var.put('parseReturnStatement', PyJsHoisted_parseReturnStatement_)
    @Js
    def PyJsHoisted_recordError_(error, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'error':error}, var)
        var.registers(['error', 'e', 'existing'])
        pass
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('extra').get('errors').get('length')):
            try:
                var.put('existing', var.get('extra').get('errors').get(var.get('e')))
                if (PyJsStrictEq(var.get('existing').get('index'),var.get('error').get('index')) and PyJsStrictEq(var.get('existing').get('message'),var.get('error').get('message'))):
                    return var.get('undefined')
            finally:
                    (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
        var.get('extra').get('errors').callprop('push', var.get('error'))
    PyJsHoisted_recordError_.__name__ = 'recordError'
    var.put('recordError', PyJsHoisted_recordError_)
    @Js
    def PyJsHoisted_parseExportAllDeclaration_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'src'])
        pass
        var.get('expect')(Js('*'))
        if var.get('matchContextualKeyword')(Js('from')).neg():
            var.get('throwError')((var.get('Messages').get('UnexpectedToken') if var.get('lookahead').get('value') else var.get('Messages').get('MissingFromClause')), var.get('lookahead').get('value'))
        var.get('lex')()
        var.put('src', var.get('parseModuleSpecifier')())
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishExportAllDeclaration', var.get('src'))
    PyJsHoisted_parseExportAllDeclaration_.__name__ = 'parseExportAllDeclaration'
    var.put('parseExportAllDeclaration', PyJsHoisted_parseExportAllDeclaration_)
    @Js
    def PyJsHoisted_collectRegex_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['regex', 'loc', 'token', 'pos'])
        pass
        var.get('skipComment')()
        var.put('pos', var.get('index'))
        PyJs_Object_39_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
        PyJs_Object_38_ = Js({'start':PyJs_Object_39_})
        var.put('loc', PyJs_Object_38_)
        var.put('regex', var.get('scanRegExp')())
        PyJs_Object_40_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
        var.get('loc').put('end', PyJs_Object_40_)
        if var.get('extra').get('tokenize').neg():
            if (var.get('extra').get('tokens').get('length')>Js(0.0)):
                var.put('token', var.get('extra').get('tokens').get((var.get('extra').get('tokens').get('length')-Js(1.0))))
                if (PyJsStrictEq(var.get('token').get('range').get('0'),var.get('pos')) and PyJsStrictEq(var.get('token').get('type'),Js('Punctuator'))):
                    if (PyJsStrictEq(var.get('token').get('value'),Js('/')) or PyJsStrictEq(var.get('token').get('value'),Js('/='))):
                        var.get('extra').get('tokens').callprop('pop')
            PyJs_Object_41_ = Js({'type':Js('RegularExpression'),'value':var.get('regex').get('literal'),'regex':var.get('regex').get('regex'),'range':Js([var.get('pos'), var.get('index')]),'loc':var.get('loc')})
            var.get('extra').get('tokens').callprop('push', PyJs_Object_41_)
        return var.get('regex')
    PyJsHoisted_collectRegex_.__name__ = 'collectRegex'
    var.put('collectRegex', PyJsHoisted_collectRegex_)
    @Js
    def PyJsHoisted_expect_(value, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'value':value}, var)
        var.registers(['token', 'value'])
        var.put('token', var.get('lex')())
        if (PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('Punctuator')) or PyJsStrictNeq(var.get('token').get('value'),var.get('value'))):
            var.get('throwUnexpectedToken')(var.get('token'))
    PyJsHoisted_expect_.__name__ = 'expect'
    var.put('expect', PyJsHoisted_expect_)
    @Js
    def PyJsHoisted_skipMultiLineComment_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['comment', 'start', 'ch', 'loc'])
        pass
        if var.get('extra').get('comments'):
            var.put('start', (var.get('index')-Js(2.0)))
            PyJs_Object_17_ = Js({'line':var.get('lineNumber'),'column':((var.get('index')-var.get('lineStart'))-Js(2.0))})
            PyJs_Object_16_ = Js({'start':PyJs_Object_17_})
            var.put('loc', PyJs_Object_16_)
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').callprop('charCodeAt', var.get('index')))
            if var.get('isLineTerminator')(var.get('ch')):
                if (PyJsStrictEq(var.get('ch'),Js(13)) and PyJsStrictEq(var.get('source').callprop('charCodeAt', (var.get('index')+Js(1.0))),Js(10))):
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                var.put('hasLineTerminator', var.get('true'))
                var.put('lineNumber',Js(var.get('lineNumber').to_number())+Js(1))
                var.put('index',Js(var.get('index').to_number())+Js(1))
                var.put('lineStart', var.get('index'))
            else:
                if PyJsStrictEq(var.get('ch'),Js(42)):
                    if PyJsStrictEq(var.get('source').callprop('charCodeAt', (var.get('index')+Js(1.0))),Js(47)):
                        var.put('index',Js(var.get('index').to_number())+Js(1))
                        var.put('index',Js(var.get('index').to_number())+Js(1))
                        if var.get('extra').get('comments'):
                            var.put('comment', var.get('source').callprop('slice', (var.get('start')+Js(2.0)), (var.get('index')-Js(2.0))))
                            PyJs_Object_18_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
                            var.get('loc').put('end', PyJs_Object_18_)
                            var.get('addComment')(Js('Block'), var.get('comment'), var.get('start'), var.get('index'), var.get('loc'))
                        return var.get('undefined')
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                else:
                    var.put('index',Js(var.get('index').to_number())+Js(1))
        if var.get('extra').get('comments'):
            PyJs_Object_19_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
            var.get('loc').put('end', PyJs_Object_19_)
            var.put('comment', var.get('source').callprop('slice', (var.get('start')+Js(2.0)), var.get('index')))
            var.get('addComment')(Js('Block'), var.get('comment'), var.get('start'), var.get('index'), var.get('loc'))
        var.get('tolerateUnexpectedToken')()
    PyJsHoisted_skipMultiLineComment_.__name__ = 'skipMultiLineComment'
    var.put('skipMultiLineComment', PyJsHoisted_skipMultiLineComment_)
    @Js
    def PyJsHoisted_scanNumericLiteral_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['start', 'ch', 'number'])
        pass
        var.put('ch', var.get('source').get(var.get('index')))
        var.get('assert')((var.get('isDecimalDigit')(var.get('ch').callprop('charCodeAt', Js(0.0))) or PyJsStrictEq(var.get('ch'),Js('.'))), Js('Numeric literal must start with a decimal digit or a decimal point'))
        var.put('start', var.get('index'))
        var.put('number', Js(''))
        if PyJsStrictNeq(var.get('ch'),Js('.')):
            var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            var.put('ch', var.get('source').get(var.get('index')))
            if PyJsStrictEq(var.get('number'),Js('0')):
                if (PyJsStrictEq(var.get('ch'),Js('x')) or PyJsStrictEq(var.get('ch'),Js('X'))):
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                    return var.get('scanHexLiteral')(var.get('start'))
                if (PyJsStrictEq(var.get('ch'),Js('b')) or PyJsStrictEq(var.get('ch'),Js('B'))):
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                    return var.get('scanBinaryLiteral')(var.get('start'))
                if (PyJsStrictEq(var.get('ch'),Js('o')) or PyJsStrictEq(var.get('ch'),Js('O'))):
                    return var.get('scanOctalLiteral')(var.get('ch'), var.get('start'))
                if var.get('isOctalDigit')(var.get('ch')):
                    if var.get('isImplicitOctalLiteral')():
                        return var.get('scanOctalLiteral')(var.get('ch'), var.get('start'))
            while var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', var.get('index'))):
                var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
            var.put('ch', var.get('source').get(var.get('index')))
        if PyJsStrictEq(var.get('ch'),Js('.')):
            var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
            while var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', var.get('index'))):
                var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
            var.put('ch', var.get('source').get(var.get('index')))
        if (PyJsStrictEq(var.get('ch'),Js('e')) or PyJsStrictEq(var.get('ch'),Js('E'))):
            var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
            var.put('ch', var.get('source').get(var.get('index')))
            if (PyJsStrictEq(var.get('ch'),Js('+')) or PyJsStrictEq(var.get('ch'),Js('-'))):
                var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
            if var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', var.get('index'))):
                while var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', var.get('index'))):
                    var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
            else:
                var.get('throwUnexpectedToken')()
        if var.get('isIdentifierStart')(var.get('source').callprop('charCodeAt', var.get('index'))):
            var.get('throwUnexpectedToken')()
        PyJs_Object_27_ = Js({'type':var.get('Token').get('NumericLiteral'),'value':var.get('parseFloat')(var.get('number')),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_27_
    PyJsHoisted_scanNumericLiteral_.__name__ = 'scanNumericLiteral'
    var.put('scanNumericLiteral', PyJsHoisted_scanNumericLiteral_)
    @Js
    def PyJsHoisted_isIdentifierStart_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        return (((((PyJsStrictEq(var.get('ch'),Js(36)) or PyJsStrictEq(var.get('ch'),Js(95))) or ((var.get('ch')>=Js(65)) and (var.get('ch')<=Js(90)))) or ((var.get('ch')>=Js(97)) and (var.get('ch')<=Js(122)))) or PyJsStrictEq(var.get('ch'),Js(92))) or ((var.get('ch')>=Js(128)) and var.get('Regex').get('NonAsciiIdentifierStart').callprop('test', var.get('fromCodePoint')(var.get('ch')))))
    PyJsHoisted_isIdentifierStart_.__name__ = 'isIdentifierStart'
    var.put('isIdentifierStart', PyJsHoisted_isIdentifierStart_)
    @Js
    def PyJsHoisted_parsePropertyMethodFunction_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'params', 'method', 'previousAllowYield'])
        var.put('node', var.get('Node').create())
        var.put('previousAllowYield', var.get('state').get('allowYield'))
        var.get('state').put('allowYield', Js(False))
        var.put('params', var.get('parseParams')())
        var.get('state').put('allowYield', var.get('previousAllowYield'))
        var.get('state').put('allowYield', Js(False))
        var.put('method', var.get('parsePropertyFunction')(var.get('node'), var.get('params'), Js(False)))
        var.get('state').put('allowYield', var.get('previousAllowYield'))
        return var.get('method')
    PyJsHoisted_parsePropertyMethodFunction_.__name__ = 'parsePropertyMethodFunction'
    var.put('parsePropertyMethodFunction', PyJsHoisted_parsePropertyMethodFunction_)
    @Js
    def PyJsHoisted_parseProgram_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'node'])
        pass
        var.get('peek')()
        var.put('node', var.get('Node').create())
        var.put('body', var.get('parseScriptBody')())
        return var.get('node').callprop('finishProgram', var.get('body'), var.get('state').get('sourceType'))
    PyJsHoisted_parseProgram_.__name__ = 'parseProgram'
    var.put('parseProgram', PyJsHoisted_parseProgram_)
    @Js
    def PyJsHoisted_isImplicitOctalLiteral_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'ch'])
        pass
        #for JS loop
        var.put('i', (var.get('index')+Js(1.0)))
        while (var.get('i')<var.get('length')):
            try:
                var.put('ch', var.get('source').get(var.get('i')))
                if (PyJsStrictEq(var.get('ch'),Js('8')) or PyJsStrictEq(var.get('ch'),Js('9'))):
                    return Js(False)
                if var.get('isOctalDigit')(var.get('ch')).neg():
                    return var.get('true')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return var.get('true')
    PyJsHoisted_isImplicitOctalLiteral_.__name__ = 'isImplicitOctalLiteral'
    var.put('isImplicitOctalLiteral', PyJsHoisted_isImplicitOctalLiteral_)
    @Js
    def PyJsHoisted_isOctalDigit_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        return (Js('01234567').callprop('indexOf', var.get('ch'))>=Js(0.0))
    PyJsHoisted_isOctalDigit_.__name__ = 'isOctalDigit'
    var.put('isOctalDigit', PyJsHoisted_isOctalDigit_)
    @Js
    def PyJsHoisted_parseArrayInitializer_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'elements', 'restSpread'])
        var.put('elements', Js([]))
        var.put('node', var.get('Node').create())
        var.get('expect')(Js('['))
        while var.get('match')(Js(']')).neg():
            if var.get('match')(Js(',')):
                var.get('lex')()
                var.get('elements').callprop('push', var.get("null"))
            else:
                if var.get('match')(Js('...')):
                    var.put('restSpread', var.get('Node').create())
                    var.get('lex')()
                    var.get('restSpread').callprop('finishSpreadElement', var.get('inheritCoverGrammar')(var.get('parseAssignmentExpression')))
                    if var.get('match')(Js(']')).neg():
                        var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                        var.get('expect')(Js(','))
                    var.get('elements').callprop('push', var.get('restSpread'))
                else:
                    var.get('elements').callprop('push', var.get('inheritCoverGrammar')(var.get('parseAssignmentExpression')))
                    if var.get('match')(Js(']')).neg():
                        var.get('expect')(Js(','))
        var.get('lex')()
        return var.get('node').callprop('finishArrayExpression', var.get('elements'))
    PyJsHoisted_parseArrayInitializer_.__name__ = 'parseArrayInitializer'
    var.put('parseArrayInitializer', PyJsHoisted_parseArrayInitializer_)
    @Js
    def PyJsHoisted_isDecimalDigit_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        return ((var.get('ch')>=Js(48)) and (var.get('ch')<=Js(57)))
    PyJsHoisted_isDecimalDigit_.__name__ = 'isDecimalDigit'
    var.put('isDecimalDigit', PyJsHoisted_isDecimalDigit_)
    @Js
    def PyJsHoisted_parseClassExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['classNode', 'previousStrict', 'classBody', 'id', 'superClass'])
        var.put('id', var.get("null"))
        var.put('superClass', var.get("null"))
        var.put('classNode', var.get('Node').create())
        var.put('previousStrict', var.get('strict'))
        var.put('strict', var.get('true'))
        var.get('expectKeyword')(Js('class'))
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier')):
            var.put('id', var.get('parseVariableIdentifier')())
        if var.get('matchKeyword')(Js('extends')):
            var.get('lex')()
            var.put('superClass', var.get('isolateCoverGrammar')(var.get('parseLeftHandSideExpressionAllowCall')))
        var.put('classBody', var.get('parseClassBody')())
        var.put('strict', var.get('previousStrict'))
        return var.get('classNode').callprop('finishClassExpression', var.get('id'), var.get('superClass'), var.get('classBody'))
    PyJsHoisted_parseClassExpression_.__name__ = 'parseClassExpression'
    var.put('parseClassExpression', PyJsHoisted_parseClassExpression_)
    @Js
    def PyJsHoisted_parseObjectProperty_(hasProto, this, arguments, var=var):
        var = Scope({'this':this, 'hasProto':hasProto, 'arguments':arguments}, var)
        var.registers(['node', 'hasProto', 'computed', 'proto', 'value', 'token', 'maybeMethod', 'key'])
        var.put('token', var.get('lookahead'))
        var.put('node', var.get('Node').create())
        var.put('computed', var.get('match')(Js('[')))
        if var.get('match')(Js('*')):
            var.get('lex')()
        else:
            var.put('key', var.get('parseObjectPropertyKey')())
        var.put('maybeMethod', var.get('tryParseMethodDefinition')(var.get('token'), var.get('key'), var.get('computed'), var.get('node')))
        if var.get('maybeMethod'):
            return var.get('maybeMethod')
        if var.get('key').neg():
            var.get('throwUnexpectedToken')(var.get('lookahead'))
        if var.get('computed').neg():
            var.put('proto', ((PyJsStrictEq(var.get('key').get('type'),var.get('Syntax').get('Identifier')) and PyJsStrictEq(var.get('key').get('name'),Js('__proto__'))) or (PyJsStrictEq(var.get('key').get('type'),var.get('Syntax').get('Literal')) and PyJsStrictEq(var.get('key').get('value'),Js('__proto__')))))
            if (var.get('hasProto').get('value') and var.get('proto')):
                var.get('tolerateError')(var.get('Messages').get('DuplicateProtoProperty'))
            var.get('hasProto').put('value', var.get('proto'), '|')
        if var.get('match')(Js(':')):
            var.get('lex')()
            var.put('value', var.get('inheritCoverGrammar')(var.get('parseAssignmentExpression')))
            return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), var.get('computed'), var.get('value'), Js(False), Js(False))
        if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Identifier')):
            if var.get('match')(Js('=')):
                var.put('firstCoverInitializedNameError', var.get('lookahead'))
                var.get('lex')()
                var.put('value', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
                return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), var.get('computed'), var.get('WrappingNode').create(var.get('token')).callprop('finishAssignmentPattern', var.get('key'), var.get('value')), Js(False), var.get('true'))
            return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), var.get('computed'), var.get('key'), Js(False), var.get('true'))
        var.get('throwUnexpectedToken')(var.get('lookahead'))
    PyJsHoisted_parseObjectProperty_.__name__ = 'parseObjectProperty'
    var.put('parseObjectProperty', PyJsHoisted_parseObjectProperty_)
    @Js
    def PyJsHoisted_parseCatchClause_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'node', 'i', 'param', 'params', 'key', 'paramMap'])
        var.put('params', Js([]))
        PyJs_Object_144_ = Js({})
        var.put('paramMap', PyJs_Object_144_)
        var.put('node', var.get('Node').create())
        var.get('expectKeyword')(Js('catch'))
        var.get('expect')(Js('('))
        if var.get('match')(Js(')')):
            var.get('throwUnexpectedToken')(var.get('lookahead'))
        var.put('param', var.get('parsePattern')(var.get('params')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('params').get('length')):
            try:
                var.put('key', (Js('$')+var.get('params').get(var.get('i')).get('value')))
                if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('paramMap'), var.get('key')):
                    var.get('tolerateError')(var.get('Messages').get('DuplicateBinding'), var.get('params').get(var.get('i')).get('value'))
                var.get('paramMap').put(var.get('key'), var.get('true'))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if (var.get('strict') and var.get('isRestrictedWord')(var.get('param').get('name'))):
            var.get('tolerateError')(var.get('Messages').get('StrictCatchVariable'))
        var.get('expect')(Js(')'))
        var.put('body', var.get('parseBlock')())
        return var.get('node').callprop('finishCatchClause', var.get('param'), var.get('body'))
    PyJsHoisted_parseCatchClause_.__name__ = 'parseCatchClause'
    var.put('parseCatchClause', PyJsHoisted_parseCatchClause_)
    @Js
    def PyJsHoisted_peek_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.put('scanning', var.get('true'))
        var.get('skipComment')()
        var.put('lastIndex', var.get('index'))
        var.put('lastLineNumber', var.get('lineNumber'))
        var.put('lastLineStart', var.get('lineStart'))
        var.put('startIndex', var.get('index'))
        var.put('startLineNumber', var.get('lineNumber'))
        var.put('startLineStart', var.get('lineStart'))
        var.put('lookahead', (var.get('collectToken')() if PyJsStrictNeq(var.get('extra').get('tokens').typeof(),Js('undefined')) else var.get('advance')()))
        var.put('scanning', Js(False))
    PyJsHoisted_peek_.__name__ = 'peek'
    var.put('peek', PyJsHoisted_peek_)
    @Js
    def PyJsHoisted_parseArguments_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'args'])
        var.put('args', Js([]))
        var.get('expect')(Js('('))
        if var.get('match')(Js(')')).neg():
            while (var.get('startIndex')<var.get('length')):
                if var.get('match')(Js('...')):
                    var.put('expr', var.get('Node').create())
                    var.get('lex')()
                    var.get('expr').callprop('finishSpreadElement', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
                else:
                    var.put('expr', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
                var.get('args').callprop('push', var.get('expr'))
                if var.get('match')(Js(')')):
                    break
                var.get('expectCommaSeparator')()
        var.get('expect')(Js(')'))
        return var.get('args')
    PyJsHoisted_parseArguments_.__name__ = 'parseArguments'
    var.put('parseArguments', PyJsHoisted_parseArguments_)
    @Js
    def PyJsHoisted_testRegExp_(pattern, flags, this, arguments, var=var):
        var = Scope({'this':this, 'pattern':pattern, 'flags':flags, 'arguments':arguments}, var)
        var.registers(['tmp', 'pattern', 'flags', 'astralSubstitute'])
        var.put('astralSubstitute', Js('\uffff'))
        var.put('tmp', var.get('pattern'))
        if (var.get('flags').callprop('indexOf', Js('u'))>=Js(0.0)):
            @Js
            def PyJs_anonymous_31_(PyJsArg_2430_, PyJsArg_2431_, PyJsArg_2432_, this, arguments, var=var):
                var = Scope({'this':this, '$2':PyJsArg_2432_, 'arguments':arguments, '$0':PyJsArg_2430_, '$1':PyJsArg_2431_}, var)
                var.registers(['codePoint', '$2', '$0', '$1'])
                var.put('codePoint', var.get('parseInt')((var.get('$1') or var.get('$2')), Js(16.0)))
                if (var.get('codePoint')>Js(1114111)):
                    var.get('throwUnexpectedToken')(var.get("null"), var.get('Messages').get('InvalidRegExp'))
                if (var.get('codePoint')<=Js(65535)):
                    return var.get('String').callprop('fromCharCode', var.get('codePoint'))
                return var.get('astralSubstitute')
            PyJs_anonymous_31_._set_name('anonymous')
            var.put('tmp', var.get('tmp').callprop('replace', JsRegExp('/\\\\u\\{([0-9a-fA-F]+)\\}|\\\\u([a-fA-F0-9]{4})/g'), PyJs_anonymous_31_).callprop('replace', JsRegExp('/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/g'), var.get('astralSubstitute')))
        try:
            var.get('RegExp')(var.get('tmp'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_65374668 = var.own.get('e')
            var.force_own_put('e', PyExceptionToJs(PyJsTempException))
            try:
                var.get('throwUnexpectedToken')(var.get("null"), var.get('Messages').get('InvalidRegExp'))
            finally:
                if PyJsHolder_65_65374668 is not None:
                    var.own['e'] = PyJsHolder_65_65374668
                else:
                    del var.own['e']
                del PyJsHolder_65_65374668
        try:
            return var.get('RegExp').create(var.get('pattern'), var.get('flags'))
        except PyJsException as PyJsTempException:
            PyJsHolder_657863657074696f6e_9604751 = var.own.get('exception')
            var.force_own_put('exception', PyExceptionToJs(PyJsTempException))
            try:
                return var.get("null")
            finally:
                if PyJsHolder_657863657074696f6e_9604751 is not None:
                    var.own['exception'] = PyJsHolder_657863657074696f6e_9604751
                else:
                    del var.own['exception']
                del PyJsHolder_657863657074696f6e_9604751
    PyJsHoisted_testRegExp_.__name__ = 'testRegExp'
    var.put('testRegExp', PyJsHoisted_testRegExp_)
    @Js
    def PyJsHoisted_octalToDecimal_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['octal', 'ch', 'code'])
        var.put('octal', PyJsStrictNeq(var.get('ch'),Js('0')))
        var.put('code', Js('01234567').callprop('indexOf', var.get('ch')))
        if ((var.get('index')<var.get('length')) and var.get('isOctalDigit')(var.get('source').get(var.get('index')))):
            var.put('octal', var.get('true'))
            var.put('code', ((var.get('code')*Js(8.0))+Js('01234567').callprop('indexOf', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))))
            if (((Js('0123').callprop('indexOf', var.get('ch'))>=Js(0.0)) and (var.get('index')<var.get('length'))) and var.get('isOctalDigit')(var.get('source').get(var.get('index')))):
                var.put('code', ((var.get('code')*Js(8.0))+Js('01234567').callprop('indexOf', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))))
        PyJs_Object_8_ = Js({'code':var.get('code'),'octal':var.get('octal')})
        return PyJs_Object_8_
    PyJsHoisted_octalToDecimal_.__name__ = 'octalToDecimal'
    var.put('octalToDecimal', PyJsHoisted_octalToDecimal_)
    @Js
    def PyJsHoisted_parseExportDeclaration_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node'])
        var.put('node', var.get('Node').create())
        if var.get('state').get('inFunctionBody'):
            var.get('throwError')(var.get('Messages').get('IllegalExportDeclaration'))
        var.get('expectKeyword')(Js('export'))
        if var.get('matchKeyword')(Js('default')):
            return var.get('parseExportDefaultDeclaration')(var.get('node'))
        if var.get('match')(Js('*')):
            return var.get('parseExportAllDeclaration')(var.get('node'))
        return var.get('parseExportNamedDeclaration')(var.get('node'))
    PyJsHoisted_parseExportDeclaration_.__name__ = 'parseExportDeclaration'
    var.put('parseExportDeclaration', PyJsHoisted_parseExportDeclaration_)
    @Js
    def PyJsHoisted_parseStatement_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'expr', 'type', 'key', 'labeledBody'])
        var.put('type', var.get('lookahead').get('type'))
        if PyJsStrictEq(var.get('type'),var.get('Token').get('EOF')):
            var.get('throwUnexpectedToken')(var.get('lookahead'))
        if (PyJsStrictEq(var.get('type'),var.get('Token').get('Punctuator')) and PyJsStrictEq(var.get('lookahead').get('value'),Js('{'))):
            return var.get('parseBlock')()
        var.put('isAssignmentTarget', var.put('isBindingElement', var.get('true')))
        var.put('node', var.get('Node').create())
        if PyJsStrictEq(var.get('type'),var.get('Token').get('Punctuator')):
            while 1:
                SWITCHED = False
                CONDITION = (var.get('lookahead').get('value'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(';')):
                    SWITCHED = True
                    return var.get('parseEmptyStatement')(var.get('node'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('(')):
                    SWITCHED = True
                    return var.get('parseExpressionStatement')(var.get('node'))
                if True:
                    SWITCHED = True
                    break
                SWITCHED = True
                break
        else:
            if PyJsStrictEq(var.get('type'),var.get('Token').get('Keyword')):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('lookahead').get('value'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('break')):
                        SWITCHED = True
                        return var.get('parseBreakStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('continue')):
                        SWITCHED = True
                        return var.get('parseContinueStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('debugger')):
                        SWITCHED = True
                        return var.get('parseDebuggerStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('do')):
                        SWITCHED = True
                        return var.get('parseDoWhileStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('for')):
                        SWITCHED = True
                        return var.get('parseForStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('function')):
                        SWITCHED = True
                        return var.get('parseFunctionDeclaration')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('if')):
                        SWITCHED = True
                        return var.get('parseIfStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('return')):
                        SWITCHED = True
                        return var.get('parseReturnStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('switch')):
                        SWITCHED = True
                        return var.get('parseSwitchStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('throw')):
                        SWITCHED = True
                        return var.get('parseThrowStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('try')):
                        SWITCHED = True
                        return var.get('parseTryStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('var')):
                        SWITCHED = True
                        return var.get('parseVariableStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('while')):
                        SWITCHED = True
                        return var.get('parseWhileStatement')(var.get('node'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('with')):
                        SWITCHED = True
                        return var.get('parseWithStatement')(var.get('node'))
                    if True:
                        SWITCHED = True
                        break
                    SWITCHED = True
                    break
        var.put('expr', var.get('parseExpression')())
        if (PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('Identifier')) and var.get('match')(Js(':'))):
            var.get('lex')()
            var.put('key', (Js('$')+var.get('expr').get('name')))
            if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('state').get('labelSet'), var.get('key')):
                var.get('throwError')(var.get('Messages').get('Redeclaration'), Js('Label'), var.get('expr').get('name'))
            var.get('state').get('labelSet').put(var.get('key'), var.get('true'))
            var.put('labeledBody', var.get('parseStatement')())
            var.get('state').get('labelSet').delete(var.get('key'))
            return var.get('node').callprop('finishLabeledStatement', var.get('expr'), var.get('labeledBody'))
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishExpressionStatement', var.get('expr'))
    PyJsHoisted_parseStatement_.__name__ = 'parseStatement'
    var.put('parseStatement', PyJsHoisted_parseStatement_)
    @Js
    def PyJsHoisted_isLineTerminator_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        return (((PyJsStrictEq(var.get('ch'),Js(10)) or PyJsStrictEq(var.get('ch'),Js(13))) or PyJsStrictEq(var.get('ch'),Js(8232))) or PyJsStrictEq(var.get('ch'),Js(8233)))
    PyJsHoisted_isLineTerminator_.__name__ = 'isLineTerminator'
    var.put('isLineTerminator', PyJsHoisted_isLineTerminator_)
    @Js
    def PyJsHoisted_parseStatementList_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['list'])
        var.put('list', Js([]))
        while (var.get('startIndex')<var.get('length')):
            if var.get('match')(Js('}')):
                break
            var.get('list').callprop('push', var.get('parseStatementListItem')())
        return var.get('list')
    PyJsHoisted_parseStatementList_.__name__ = 'parseStatementList'
    var.put('parseStatementList', PyJsHoisted_parseStatementList_)
    @Js
    def PyJsHoisted_parseNamedImports_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['specifiers'])
        var.put('specifiers', Js([]))
        var.get('expect')(Js('{'))
        while var.get('match')(Js('}')).neg():
            var.get('specifiers').callprop('push', var.get('parseImportSpecifier')())
            if var.get('match')(Js('}')).neg():
                var.get('expect')(Js(','))
                if var.get('match')(Js('}')):
                    break
        var.get('expect')(Js('}'))
        return var.get('specifiers')
    PyJsHoisted_parseNamedImports_.__name__ = 'parseNamedImports'
    var.put('parseNamedImports', PyJsHoisted_parseNamedImports_)
    @Js
    def PyJsHoisted_lex_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['token'])
        pass
        var.put('scanning', var.get('true'))
        var.put('lastIndex', var.get('index'))
        var.put('lastLineNumber', var.get('lineNumber'))
        var.put('lastLineStart', var.get('lineStart'))
        var.get('skipComment')()
        var.put('token', var.get('lookahead'))
        var.put('startIndex', var.get('index'))
        var.put('startLineNumber', var.get('lineNumber'))
        var.put('startLineStart', var.get('lineStart'))
        var.put('lookahead', (var.get('collectToken')() if PyJsStrictNeq(var.get('extra').get('tokens').typeof(),Js('undefined')) else var.get('advance')()))
        var.put('scanning', Js(False))
        return var.get('token')
    PyJsHoisted_lex_.__name__ = 'lex'
    var.put('lex', PyJsHoisted_lex_)
    @Js
    def PyJsHoisted_parseFunctionSourceElements_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'oldInIteration', 'oldInFunctionBody', 'node', 'directive', 'oldInSwitch', 'oldLabelSet', 'token', 'statement', 'firstRestricted', 'oldParenthesisCount'])
        var.put('body', Js([]))
        var.put('node', var.get('Node').create())
        var.get('expect')(Js('{'))
        while (var.get('startIndex')<var.get('length')):
            if PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('StringLiteral')):
                break
            var.put('token', var.get('lookahead'))
            var.put('statement', var.get('parseStatementListItem')())
            var.get('body').callprop('push', var.get('statement'))
            if PyJsStrictNeq(var.get('statement').get('expression').get('type'),var.get('Syntax').get('Literal')):
                break
            var.put('directive', var.get('source').callprop('slice', (var.get('token').get('start')+Js(1.0)), (var.get('token').get('end')-Js(1.0))))
            if PyJsStrictEq(var.get('directive'),Js('use strict')):
                var.put('strict', var.get('true'))
                if var.get('firstRestricted'):
                    var.get('tolerateUnexpectedToken')(var.get('firstRestricted'), var.get('Messages').get('StrictOctalLiteral'))
            else:
                if (var.get('firstRestricted').neg() and var.get('token').get('octal')):
                    var.put('firstRestricted', var.get('token'))
        var.put('oldLabelSet', var.get('state').get('labelSet'))
        var.put('oldInIteration', var.get('state').get('inIteration'))
        var.put('oldInSwitch', var.get('state').get('inSwitch'))
        var.put('oldInFunctionBody', var.get('state').get('inFunctionBody'))
        var.put('oldParenthesisCount', var.get('state').get('parenthesizedCount'))
        PyJs_Object_145_ = Js({})
        var.get('state').put('labelSet', PyJs_Object_145_)
        var.get('state').put('inIteration', Js(False))
        var.get('state').put('inSwitch', Js(False))
        var.get('state').put('inFunctionBody', var.get('true'))
        var.get('state').put('parenthesizedCount', Js(0.0))
        while (var.get('startIndex')<var.get('length')):
            if var.get('match')(Js('}')):
                break
            var.get('body').callprop('push', var.get('parseStatementListItem')())
        var.get('expect')(Js('}'))
        var.get('state').put('labelSet', var.get('oldLabelSet'))
        var.get('state').put('inIteration', var.get('oldInIteration'))
        var.get('state').put('inSwitch', var.get('oldInSwitch'))
        var.get('state').put('inFunctionBody', var.get('oldInFunctionBody'))
        var.get('state').put('parenthesizedCount', var.get('oldParenthesisCount'))
        return var.get('node').callprop('finishBlockStatement', var.get('body'))
    PyJsHoisted_parseFunctionSourceElements_.__name__ = 'parseFunctionSourceElements'
    var.put('parseFunctionSourceElements', PyJsHoisted_parseFunctionSourceElements_)
    @Js
    def PyJsHoisted_isIdentifierName_(token, this, arguments, var=var):
        var = Scope({'this':this, 'token':token, 'arguments':arguments}, var)
        var.registers(['token'])
        return (((PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Identifier')) or PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Keyword'))) or PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('BooleanLiteral'))) or PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('NullLiteral')))
    PyJsHoisted_isIdentifierName_.__name__ = 'isIdentifierName'
    var.put('isIdentifierName', PyJsHoisted_isIdentifierName_)
    @Js
    def PyJsHoisted_advance_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['token', 'cp'])
        pass
        if (var.get('index')>=var.get('length')):
            PyJs_Object_42_ = Js({'type':var.get('Token').get('EOF'),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('index'),'end':var.get('index')})
            return PyJs_Object_42_
        var.put('cp', var.get('source').callprop('charCodeAt', var.get('index')))
        if var.get('isIdentifierStart')(var.get('cp')):
            var.put('token', var.get('scanIdentifier')())
            if (var.get('strict') and var.get('isStrictModeReservedWord')(var.get('token').get('value'))):
                var.get('token').put('type', var.get('Token').get('Keyword'))
            return var.get('token')
        if ((PyJsStrictEq(var.get('cp'),Js(40)) or PyJsStrictEq(var.get('cp'),Js(41))) or PyJsStrictEq(var.get('cp'),Js(59))):
            return var.get('scanPunctuator')()
        if (PyJsStrictEq(var.get('cp'),Js(39)) or PyJsStrictEq(var.get('cp'),Js(34))):
            return var.get('scanStringLiteral')()
        if PyJsStrictEq(var.get('cp'),Js(46)):
            if var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', (var.get('index')+Js(1.0)))):
                return var.get('scanNumericLiteral')()
            return var.get('scanPunctuator')()
        if var.get('isDecimalDigit')(var.get('cp')):
            return var.get('scanNumericLiteral')()
        if (var.get('extra').get('tokenize') and PyJsStrictEq(var.get('cp'),Js(47))):
            return var.get('advanceSlash')()
        if (PyJsStrictEq(var.get('cp'),Js(96)) or (PyJsStrictEq(var.get('cp'),Js(125)) and PyJsStrictEq(var.get('state').get('curlyStack').get((var.get('state').get('curlyStack').get('length')-Js(1.0))),Js('${')))):
            return var.get('scanTemplate')()
        if ((var.get('cp')>=Js(55296)) and (var.get('cp')<Js(57343))):
            var.put('cp', var.get('codePointAt')(var.get('index')))
            if var.get('isIdentifierStart')(var.get('cp')):
                return var.get('scanIdentifier')()
        return var.get('scanPunctuator')()
    PyJsHoisted_advance_.__name__ = 'advance'
    var.put('advance', PyJsHoisted_advance_)
    @Js
    def PyJsHoisted_inheritCoverGrammar_(parser, this, arguments, var=var):
        var = Scope({'this':this, 'parser':parser, 'arguments':arguments}, var)
        var.registers(['oldFirstCoverInitializedNameError', 'parser', 'oldIsBindingElement', 'oldIsAssignmentTarget', 'result'])
        var.put('oldIsBindingElement', var.get('isBindingElement'))
        var.put('oldIsAssignmentTarget', var.get('isAssignmentTarget'))
        var.put('oldFirstCoverInitializedNameError', var.get('firstCoverInitializedNameError'))
        var.put('isBindingElement', var.get('true'))
        var.put('isAssignmentTarget', var.get('true'))
        var.put('firstCoverInitializedNameError', var.get("null"))
        var.put('result', var.get('parser')())
        var.put('isBindingElement', (var.get('isBindingElement') and var.get('oldIsBindingElement')))
        var.put('isAssignmentTarget', (var.get('isAssignmentTarget') and var.get('oldIsAssignmentTarget')))
        var.put('firstCoverInitializedNameError', (var.get('oldFirstCoverInitializedNameError') or var.get('firstCoverInitializedNameError')))
        return var.get('result')
    PyJsHoisted_inheritCoverGrammar_.__name__ = 'inheritCoverGrammar'
    var.put('inheritCoverGrammar', PyJsHoisted_inheritCoverGrammar_)
    @Js
    def PyJsHoisted_reinterpretAsCoverFormalsList_(expr, this, arguments, var=var):
        var = Scope({'this':this, 'expr':expr, 'arguments':arguments}, var)
        var.registers(['i', 'expr', 'param', 'token', 'params', 'len', 'defaults', 'defaultCount', 'options'])
        pass
        var.put('defaults', Js([]))
        var.put('defaultCount', Js(0.0))
        var.put('params', Js([var.get('expr')]))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('expr').get('type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('Identifier')):
                SWITCHED = True
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('PlaceHolders').get('ArrowParameterPlaceHolder')):
                SWITCHED = True
                var.put('params', var.get('expr').get('params'))
                break
            if True:
                SWITCHED = True
                return var.get("null")
            SWITCHED = True
            break
        PyJs_Object_136_ = Js({})
        PyJs_Object_135_ = Js({'paramSet':PyJs_Object_136_})
        var.put('options', PyJs_Object_135_)
        #for JS loop
        PyJsComma(var.put('i', Js(0.0)),var.put('len', var.get('params').get('length')))
        while (var.get('i')<var.get('len')):
            try:
                var.put('param', var.get('params').get(var.get('i')))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('param').get('type'))
                    if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('AssignmentPattern')):
                        SWITCHED = True
                        var.get('params').put(var.get('i'), var.get('param').get('left'))
                        if PyJsStrictEq(var.get('param').get('right').get('type'),var.get('Syntax').get('YieldExpression')):
                            if var.get('param').get('right').get('argument'):
                                var.get('throwUnexpectedToken')(var.get('lookahead'))
                            var.get('param').get('right').put('type', var.get('Syntax').get('Identifier'))
                            var.get('param').get('right').put('name', Js('yield'))
                            var.get('param').get('right').delete('argument')
                            var.get('param').get('right').delete('delegate')
                        var.get('defaults').callprop('push', var.get('param').get('right'))
                        var.put('defaultCount',Js(var.get('defaultCount').to_number())+Js(1))
                        var.get('checkPatternParam')(var.get('options'), var.get('param').get('left'))
                        break
                    if True:
                        SWITCHED = True
                        var.get('checkPatternParam')(var.get('options'), var.get('param'))
                        var.get('params').put(var.get('i'), var.get('param'))
                        var.get('defaults').callprop('push', var.get("null"))
                        break
                    SWITCHED = True
                    break
            finally:
                    var.put('i', Js(1.0), '+')
        if (var.get('strict') or var.get('state').get('allowYield').neg()):
            #for JS loop
            PyJsComma(var.put('i', Js(0.0)),var.put('len', var.get('params').get('length')))
            while (var.get('i')<var.get('len')):
                try:
                    var.put('param', var.get('params').get(var.get('i')))
                    if PyJsStrictEq(var.get('param').get('type'),var.get('Syntax').get('YieldExpression')):
                        var.get('throwUnexpectedToken')(var.get('lookahead'))
                finally:
                        var.put('i', Js(1.0), '+')
        if PyJsStrictEq(var.get('options').get('message'),var.get('Messages').get('StrictParamDupe')):
            var.put('token', (var.get('options').get('stricted') if var.get('strict') else var.get('options').get('firstRestricted')))
            var.get('throwUnexpectedToken')(var.get('token'), var.get('options').get('message'))
        if PyJsStrictEq(var.get('defaultCount'),Js(0.0)):
            var.put('defaults', Js([]))
        PyJs_Object_137_ = Js({'params':var.get('params'),'defaults':var.get('defaults'),'stricted':var.get('options').get('stricted'),'firstRestricted':var.get('options').get('firstRestricted'),'message':var.get('options').get('message')})
        return PyJs_Object_137_
    PyJsHoisted_reinterpretAsCoverFormalsList_.__name__ = 'reinterpretAsCoverFormalsList'
    var.put('reinterpretAsCoverFormalsList', PyJsHoisted_reinterpretAsCoverFormalsList_)
    @Js
    def PyJsHoisted_isFutureReservedWord_(id, this, arguments, var=var):
        var = Scope({'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['id'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get('id'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js('enum')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('export')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('import')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('super')):
                SWITCHED = True
                return var.get('true')
            if True:
                SWITCHED = True
                return Js(False)
            SWITCHED = True
            break
    PyJsHoisted_isFutureReservedWord_.__name__ = 'isFutureReservedWord'
    var.put('isFutureReservedWord', PyJsHoisted_isFutureReservedWord_)
    @Js
    def PyJsHoisted_parseImportNamespaceSpecifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'local'])
        var.put('node', var.get('Node').create())
        var.get('expect')(Js('*'))
        if var.get('matchContextualKeyword')(Js('as')).neg():
            var.get('throwError')(var.get('Messages').get('NoAsAfterImportNamespace'))
        var.get('lex')()
        var.put('local', var.get('parseNonComputedProperty')())
        return var.get('node').callprop('finishImportNamespaceSpecifier', var.get('local'))
    PyJsHoisted_parseImportNamespaceSpecifier_.__name__ = 'parseImportNamespaceSpecifier'
    var.put('parseImportNamespaceSpecifier', PyJsHoisted_parseImportNamespaceSpecifier_)
    @Js
    def PyJsHoisted_parseUnaryExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'token', 'startToken'])
        pass
        if (PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('Punctuator')) and PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('Keyword'))):
            var.put('expr', var.get('parsePostfixExpression')())
        else:
            if (var.get('match')(Js('++')) or var.get('match')(Js('--'))):
                var.put('startToken', var.get('lookahead'))
                var.put('token', var.get('lex')())
                var.put('expr', var.get('inheritCoverGrammar')(var.get('parseUnaryExpression')))
                if ((var.get('strict') and PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('Identifier'))) and var.get('isRestrictedWord')(var.get('expr').get('name'))):
                    var.get('tolerateError')(var.get('Messages').get('StrictLHSPrefix'))
                if var.get('isAssignmentTarget').neg():
                    var.get('tolerateError')(var.get('Messages').get('InvalidLHSInAssignment'))
                var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishUnaryExpression', var.get('token').get('value'), var.get('expr')))
                var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
            else:
                if (((var.get('match')(Js('+')) or var.get('match')(Js('-'))) or var.get('match')(Js('~'))) or var.get('match')(Js('!'))):
                    var.put('startToken', var.get('lookahead'))
                    var.put('token', var.get('lex')())
                    var.put('expr', var.get('inheritCoverGrammar')(var.get('parseUnaryExpression')))
                    var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishUnaryExpression', var.get('token').get('value'), var.get('expr')))
                    var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                else:
                    if ((var.get('matchKeyword')(Js('delete')) or var.get('matchKeyword')(Js('void'))) or var.get('matchKeyword')(Js('typeof'))):
                        var.put('startToken', var.get('lookahead'))
                        var.put('token', var.get('lex')())
                        var.put('expr', var.get('inheritCoverGrammar')(var.get('parseUnaryExpression')))
                        var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishUnaryExpression', var.get('token').get('value'), var.get('expr')))
                        if ((var.get('strict') and PyJsStrictEq(var.get('expr').get('operator'),Js('delete'))) and PyJsStrictEq(var.get('expr').get('argument').get('type'),var.get('Syntax').get('Identifier'))):
                            var.get('tolerateError')(var.get('Messages').get('StrictDelete'))
                        var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                    else:
                        var.put('expr', var.get('parsePostfixExpression')())
        return var.get('expr')
    PyJsHoisted_parseUnaryExpression_.__name__ = 'parseUnaryExpression'
    var.put('parseUnaryExpression', PyJsHoisted_parseUnaryExpression_)
    @Js
    def PyJsHoisted_parseAssignmentExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'token', 'right', 'list', 'startToken'])
        pass
        var.put('startToken', var.get('lookahead'))
        var.put('token', var.get('lookahead'))
        if (var.get('state').get('allowYield').neg() and var.get('matchKeyword')(Js('yield'))):
            return var.get('parseYieldExpression')()
        var.put('expr', var.get('parseConditionalExpression')())
        if (PyJsStrictEq(var.get('expr').get('type'),var.get('PlaceHolders').get('ArrowParameterPlaceHolder')) or var.get('match')(Js('=>'))):
            var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
            var.put('list', var.get('reinterpretAsCoverFormalsList')(var.get('expr')))
            if var.get('list'):
                var.put('firstCoverInitializedNameError', var.get("null"))
                return var.get('parseArrowFunctionExpression')(var.get('list'), var.get('WrappingNode').create(var.get('startToken')))
            return var.get('expr')
        if var.get('matchAssign')():
            if var.get('isAssignmentTarget').neg():
                var.get('tolerateError')(var.get('Messages').get('InvalidLHSInAssignment'))
            if (var.get('strict') and PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('Identifier'))):
                if var.get('isRestrictedWord')(var.get('expr').get('name')):
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictLHSAssignment'))
                if var.get('isStrictModeReservedWord')(var.get('expr').get('name')):
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictReservedWord'))
            if var.get('match')(Js('=')).neg():
                var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
            else:
                var.get('reinterpretExpressionAsPattern')(var.get('expr'))
            var.put('token', var.get('lex')())
            var.put('right', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
            var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishAssignmentExpression', var.get('token').get('value'), var.get('expr'), var.get('right')))
            var.put('firstCoverInitializedNameError', var.get("null"))
        return var.get('expr')
    PyJsHoisted_parseAssignmentExpression_.__name__ = 'parseAssignmentExpression'
    var.put('parseAssignmentExpression', PyJsHoisted_parseAssignmentExpression_)
    @Js
    def PyJsHoisted_isKeyword_(id, this, arguments, var=var):
        var = Scope({'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['id'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get('id').get('length'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                return ((PyJsStrictEq(var.get('id'),Js('if')) or PyJsStrictEq(var.get('id'),Js('in'))) or PyJsStrictEq(var.get('id'),Js('do')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                return ((((PyJsStrictEq(var.get('id'),Js('var')) or PyJsStrictEq(var.get('id'),Js('for'))) or PyJsStrictEq(var.get('id'),Js('new'))) or PyJsStrictEq(var.get('id'),Js('try'))) or PyJsStrictEq(var.get('id'),Js('let')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                return (((((PyJsStrictEq(var.get('id'),Js('this')) or PyJsStrictEq(var.get('id'),Js('else'))) or PyJsStrictEq(var.get('id'),Js('case'))) or PyJsStrictEq(var.get('id'),Js('void'))) or PyJsStrictEq(var.get('id'),Js('with'))) or PyJsStrictEq(var.get('id'),Js('enum')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                return (((((((PyJsStrictEq(var.get('id'),Js('while')) or PyJsStrictEq(var.get('id'),Js('break'))) or PyJsStrictEq(var.get('id'),Js('catch'))) or PyJsStrictEq(var.get('id'),Js('throw'))) or PyJsStrictEq(var.get('id'),Js('const'))) or PyJsStrictEq(var.get('id'),Js('yield'))) or PyJsStrictEq(var.get('id'),Js('class'))) or PyJsStrictEq(var.get('id'),Js('super')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                return (((((PyJsStrictEq(var.get('id'),Js('return')) or PyJsStrictEq(var.get('id'),Js('typeof'))) or PyJsStrictEq(var.get('id'),Js('delete'))) or PyJsStrictEq(var.get('id'),Js('switch'))) or PyJsStrictEq(var.get('id'),Js('export'))) or PyJsStrictEq(var.get('id'),Js('import')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                SWITCHED = True
                return ((PyJsStrictEq(var.get('id'),Js('default')) or PyJsStrictEq(var.get('id'),Js('finally'))) or PyJsStrictEq(var.get('id'),Js('extends')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                SWITCHED = True
                return ((PyJsStrictEq(var.get('id'),Js('function')) or PyJsStrictEq(var.get('id'),Js('continue'))) or PyJsStrictEq(var.get('id'),Js('debugger')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                SWITCHED = True
                return PyJsStrictEq(var.get('id'),Js('instanceof'))
            if True:
                SWITCHED = True
                return Js(False)
            SWITCHED = True
            break
    PyJsHoisted_isKeyword_.__name__ = 'isKeyword'
    var.put('isKeyword', PyJsHoisted_isKeyword_)
    @Js
    def PyJsHoisted_parseLexicalBinding_(kind, options, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'options':options, 'arguments':arguments}, var)
        var.registers(['node', 'kind', 'options', 'init', 'params', 'id'])
        var.put('init', var.get("null"))
        var.put('node', var.get('Node').create())
        var.put('params', Js([]))
        var.put('id', var.get('parsePattern')(var.get('params'), var.get('kind')))
        if ((var.get('strict') and PyJsStrictEq(var.get('id').get('type'),var.get('Syntax').get('Identifier'))) and var.get('isRestrictedWord')(var.get('id').get('name'))):
            var.get('tolerateError')(var.get('Messages').get('StrictVarName'))
        if PyJsStrictEq(var.get('kind'),Js('const')):
            if (var.get('matchKeyword')(Js('in')).neg() and var.get('matchContextualKeyword')(Js('of')).neg()):
                var.get('expect')(Js('='))
                var.put('init', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
        else:
            if ((var.get('options').get('inFor').neg() and PyJsStrictNeq(var.get('id').get('type'),var.get('Syntax').get('Identifier'))) or var.get('match')(Js('='))):
                var.get('expect')(Js('='))
                var.put('init', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
        return var.get('node').callprop('finishVariableDeclarator', var.get('id'), var.get('init'))
    PyJsHoisted_parseLexicalBinding_.__name__ = 'parseLexicalBinding'
    var.put('parseLexicalBinding', PyJsHoisted_parseLexicalBinding_)
    @Js
    def PyJsHoisted_tolerateError_(messageFormat, this, arguments, var=var):
        var = Scope({'this':this, 'messageFormat':messageFormat, 'arguments':arguments}, var)
        var.registers(['msg', 'args', 'messageFormat', 'error'])
        pass
        var.put('args', var.get('Array').get('prototype').get('slice').callprop('call', var.get('arguments'), Js(1.0)))
        @Js
        def PyJs_anonymous_119_(whole, idx, this, arguments, var=var):
            var = Scope({'this':this, 'whole':whole, 'arguments':arguments, 'idx':idx}, var)
            var.registers(['whole', 'idx'])
            var.get('assert')((var.get('idx')<var.get('args').get('length')), Js('Message reference must be in range'))
            return var.get('args').get(var.get('idx'))
        PyJs_anonymous_119_._set_name('anonymous')
        var.put('msg', var.get('messageFormat').callprop('replace', JsRegExp('/%(\\d)/g'), PyJs_anonymous_119_))
        var.put('error', var.get('createError')(var.get('lineNumber'), var.get('lastIndex'), var.get('msg')))
        if var.get('extra').get('errors'):
            var.get('recordError')(var.get('error'))
        else:
            PyJsTempException = JsToPyException(var.get('error'))
            raise PyJsTempException
    PyJsHoisted_tolerateError_.__name__ = 'tolerateError'
    var.put('tolerateError', PyJsHoisted_tolerateError_)
    @Js
    def PyJsHoisted_parseBinaryExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['right', 'i', 'expr', 'prec', 'operator', 'token', 'markers', 'marker', 'stack', 'left'])
        pass
        var.put('marker', var.get('lookahead'))
        var.put('left', var.get('inheritCoverGrammar')(var.get('parseUnaryExpression')))
        var.put('token', var.get('lookahead'))
        var.put('prec', var.get('binaryPrecedence')(var.get('token'), var.get('state').get('allowIn')))
        if PyJsStrictEq(var.get('prec'),Js(0.0)):
            return var.get('left')
        var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
        var.get('token').put('prec', var.get('prec'))
        var.get('lex')()
        var.put('markers', Js([var.get('marker'), var.get('lookahead')]))
        var.put('right', var.get('isolateCoverGrammar')(var.get('parseUnaryExpression')))
        var.put('stack', Js([var.get('left'), var.get('token'), var.get('right')]))
        while (var.put('prec', var.get('binaryPrecedence')(var.get('lookahead'), var.get('state').get('allowIn')))>Js(0.0)):
            while ((var.get('stack').get('length')>Js(2.0)) and (var.get('prec')<=var.get('stack').get((var.get('stack').get('length')-Js(2.0))).get('prec'))):
                var.put('right', var.get('stack').callprop('pop'))
                var.put('operator', var.get('stack').callprop('pop').get('value'))
                var.put('left', var.get('stack').callprop('pop'))
                var.get('markers').callprop('pop')
                var.put('expr', var.get('WrappingNode').create(var.get('markers').get((var.get('markers').get('length')-Js(1.0)))).callprop('finishBinaryExpression', var.get('operator'), var.get('left'), var.get('right')))
                var.get('stack').callprop('push', var.get('expr'))
            var.put('token', var.get('lex')())
            var.get('token').put('prec', var.get('prec'))
            var.get('stack').callprop('push', var.get('token'))
            var.get('markers').callprop('push', var.get('lookahead'))
            var.put('expr', var.get('isolateCoverGrammar')(var.get('parseUnaryExpression')))
            var.get('stack').callprop('push', var.get('expr'))
        var.put('i', (var.get('stack').get('length')-Js(1.0)))
        var.put('expr', var.get('stack').get(var.get('i')))
        var.get('markers').callprop('pop')
        while (var.get('i')>Js(1.0)):
            var.put('expr', var.get('WrappingNode').create(var.get('markers').callprop('pop')).callprop('finishBinaryExpression', var.get('stack').get((var.get('i')-Js(1.0))).get('value'), var.get('stack').get((var.get('i')-Js(2.0))), var.get('expr')))
            var.put('i', Js(2.0), '-')
        return var.get('expr')
    PyJsHoisted_parseBinaryExpression_.__name__ = 'parseBinaryExpression'
    var.put('parseBinaryExpression', PyJsHoisted_parseBinaryExpression_)
    @Js
    def PyJsHoisted_scanIdentifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['start', 'type', 'id'])
        pass
        var.put('start', var.get('index'))
        var.put('id', (var.get('getComplexIdentifier')() if PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('index')),Js(92)) else var.get('getIdentifier')()))
        if PyJsStrictEq(var.get('id').get('length'),Js(1.0)):
            var.put('type', var.get('Token').get('Identifier'))
        else:
            if var.get('isKeyword')(var.get('id')):
                var.put('type', var.get('Token').get('Keyword'))
            else:
                if PyJsStrictEq(var.get('id'),Js('null')):
                    var.put('type', var.get('Token').get('NullLiteral'))
                else:
                    if (PyJsStrictEq(var.get('id'),Js('true')) or PyJsStrictEq(var.get('id'),Js('false'))):
                        var.put('type', var.get('Token').get('BooleanLiteral'))
                    else:
                        var.put('type', var.get('Token').get('Identifier'))
        PyJs_Object_20_ = Js({'type':var.get('type'),'value':var.get('id'),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_20_
    PyJsHoisted_scanIdentifier_.__name__ = 'scanIdentifier'
    var.put('scanIdentifier', PyJsHoisted_scanIdentifier_)
    @Js
    def PyJsHoisted_unexpectedTokenError_(token, message, this, arguments, var=var):
        var = Scope({'this':this, 'token':token, 'message':message, 'arguments':arguments}, var)
        var.registers(['msg', 'token', 'message', 'value'])
        var.put('msg', (var.get('message') or var.get('Messages').get('UnexpectedToken')))
        if var.get('token'):
            if var.get('message').neg():
                def PyJs_LONG_120_(var=var):
                    return (var.get('Messages').get('UnexpectedNumber') if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('NumericLiteral')) else (var.get('Messages').get('UnexpectedString') if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('StringLiteral')) else (var.get('Messages').get('UnexpectedTemplate') if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Template')) else var.get('Messages').get('UnexpectedToken'))))
                var.put('msg', (var.get('Messages').get('UnexpectedEOS') if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('EOF')) else (var.get('Messages').get('UnexpectedIdentifier') if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Identifier')) else PyJs_LONG_120_())))
                if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Keyword')):
                    if var.get('isFutureReservedWord')(var.get('token').get('value')):
                        var.put('msg', var.get('Messages').get('UnexpectedReserved'))
                    else:
                        if (var.get('strict') and var.get('isStrictModeReservedWord')(var.get('token').get('value'))):
                            var.put('msg', var.get('Messages').get('StrictReservedWord'))
            var.put('value', (var.get('token').get('value').get('raw') if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Template')) else var.get('token').get('value')))
        else:
            var.put('value', Js('ILLEGAL'))
        var.put('msg', var.get('msg').callprop('replace', Js('%0'), var.get('value')))
        def PyJs_LONG_121_(var=var):
            return (var.get('createError')(var.get('token').get('lineNumber'), var.get('token').get('start'), var.get('msg')) if (var.get('token') and PyJsStrictEq(var.get('token').get('lineNumber').typeof(),Js('number'))) else var.get('createError')((var.get('lineNumber') if var.get('scanning') else var.get('lastLineNumber')), (var.get('index') if var.get('scanning') else var.get('lastIndex')), var.get('msg')))
        return PyJs_LONG_121_()
    PyJsHoisted_unexpectedTokenError_.__name__ = 'unexpectedTokenError'
    var.put('unexpectedTokenError', PyJsHoisted_unexpectedTokenError_)
    @Js
    def PyJsHoisted_parseNonComputedProperty_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'token'])
        var.put('node', var.get('Node').create())
        var.put('token', var.get('lex')())
        if var.get('isIdentifierName')(var.get('token')).neg():
            var.get('throwUnexpectedToken')(var.get('token'))
        return var.get('node').callprop('finishIdentifier', var.get('token').get('value'))
    PyJsHoisted_parseNonComputedProperty_.__name__ = 'parseNonComputedProperty'
    var.put('parseNonComputedProperty', PyJsHoisted_parseNonComputedProperty_)
    @Js
    def PyJsHoisted_parseModuleSpecifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node'])
        var.put('node', var.get('Node').create())
        if PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('StringLiteral')):
            var.get('throwError')(var.get('Messages').get('InvalidModuleSpecifier'))
        return var.get('node').callprop('finishLiteral', var.get('lex')())
    PyJsHoisted_parseModuleSpecifier_.__name__ = 'parseModuleSpecifier'
    var.put('parseModuleSpecifier', PyJsHoisted_parseModuleSpecifier_)
    @Js
    def PyJsHoisted_parseParam_(options, this, arguments, var=var):
        var = Scope({'this':this, 'options':options, 'arguments':arguments}, var)
        var.registers(['i', 'param', 'token', 'params', 'options', 'def'])
        var.put('params', Js([]))
        var.put('token', var.get('lookahead'))
        if PyJsStrictEq(var.get('token').get('value'),Js('...')):
            var.put('param', var.get('parseRestElement')(var.get('params')))
            var.get('validateParam')(var.get('options'), var.get('param').get('argument'), var.get('param').get('argument').get('name'))
            var.get('options').get('params').callprop('push', var.get('param'))
            var.get('options').get('defaults').callprop('push', var.get("null"))
            return Js(False)
        var.put('param', var.get('parsePatternWithDefault')(var.get('params')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('params').get('length')):
            try:
                var.get('validateParam')(var.get('options'), var.get('params').get(var.get('i')), var.get('params').get(var.get('i')).get('value'))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if PyJsStrictEq(var.get('param').get('type'),var.get('Syntax').get('AssignmentPattern')):
            var.put('def', var.get('param').get('right'))
            var.put('param', var.get('param').get('left'))
            var.get('options').put('defaultCount',Js(var.get('options').get('defaultCount').to_number())+Js(1))
        var.get('options').get('params').callprop('push', var.get('param'))
        var.get('options').get('defaults').callprop('push', var.get('def'))
        return var.get('match')(Js(')')).neg()
    PyJsHoisted_parseParam_.__name__ = 'parseParam'
    var.put('parseParam', PyJsHoisted_parseParam_)
    @Js
    def PyJsHoisted_parseNewExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'args', 'callee'])
        var.put('node', var.get('Node').create())
        var.get('expectKeyword')(Js('new'))
        if var.get('match')(Js('.')):
            var.get('lex')()
            if (PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier')) and PyJsStrictEq(var.get('lookahead').get('value'),Js('target'))):
                if var.get('state').get('inFunctionBody'):
                    var.get('lex')()
                    return var.get('node').callprop('finishMetaProperty', Js('new'), Js('target'))
            var.get('throwUnexpectedToken')(var.get('lookahead'))
        var.put('callee', var.get('isolateCoverGrammar')(var.get('parseLeftHandSideExpression')))
        var.put('args', (var.get('parseArguments')() if var.get('match')(Js('(')) else Js([])))
        var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
        return var.get('node').callprop('finishNewExpression', var.get('callee'), var.get('args'))
    PyJsHoisted_parseNewExpression_.__name__ = 'parseNewExpression'
    var.put('parseNewExpression', PyJsHoisted_parseNewExpression_)
    @Js
    def PyJsHoisted_scanRegExpBody_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'terminated', 'ch', 'classMarker', 'str'])
        pass
        var.put('ch', var.get('source').get(var.get('index')))
        var.get('assert')(PyJsStrictEq(var.get('ch'),Js('/')), Js('Regular expression literal must start with a slash'))
        var.put('str', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        var.put('classMarker', Js(False))
        var.put('terminated', Js(False))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            var.put('str', var.get('ch'), '+')
            if PyJsStrictEq(var.get('ch'),Js('\\')):
                var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                if var.get('isLineTerminator')(var.get('ch').callprop('charCodeAt', Js(0.0))):
                    var.get('throwUnexpectedToken')(var.get("null"), var.get('Messages').get('UnterminatedRegExp'))
                var.put('str', var.get('ch'), '+')
            else:
                if var.get('isLineTerminator')(var.get('ch').callprop('charCodeAt', Js(0.0))):
                    var.get('throwUnexpectedToken')(var.get("null"), var.get('Messages').get('UnterminatedRegExp'))
                else:
                    if var.get('classMarker'):
                        if PyJsStrictEq(var.get('ch'),Js(']')):
                            var.put('classMarker', Js(False))
                    else:
                        if PyJsStrictEq(var.get('ch'),Js('/')):
                            var.put('terminated', var.get('true'))
                            break
                        else:
                            if PyJsStrictEq(var.get('ch'),Js('[')):
                                var.put('classMarker', var.get('true'))
        if var.get('terminated').neg():
            var.get('throwUnexpectedToken')(var.get("null"), var.get('Messages').get('UnterminatedRegExp'))
        var.put('body', var.get('str').callprop('substr', Js(1.0), (var.get('str').get('length')-Js(2.0))))
        PyJs_Object_32_ = Js({'value':var.get('body'),'literal':var.get('str')})
        return PyJs_Object_32_
    PyJsHoisted_scanRegExpBody_.__name__ = 'scanRegExpBody'
    var.put('scanRegExpBody', PyJsHoisted_scanRegExpBody_)
    @Js
    def PyJsHoisted_Node_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if var.get('extra').get('range'):
            var.get("this").put('range', Js([var.get('startIndex'), Js(0.0)]))
        if var.get('extra').get('loc'):
            var.get("this").put('loc', var.get('SourceLocation').create())
    PyJsHoisted_Node_.__name__ = 'Node'
    var.put('Node', PyJsHoisted_Node_)
    @Js
    def PyJsHoisted_collectToken_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['loc', 'token', 'value', 'entry'])
        pass
        PyJs_Object_44_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
        PyJs_Object_43_ = Js({'start':PyJs_Object_44_})
        var.put('loc', PyJs_Object_43_)
        var.put('token', var.get('advance')())
        PyJs_Object_45_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
        var.get('loc').put('end', PyJs_Object_45_)
        if PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('EOF')):
            var.put('value', var.get('source').callprop('slice', var.get('token').get('start'), var.get('token').get('end')))
            PyJs_Object_46_ = Js({'type':var.get('TokenName').get(var.get('token').get('type')),'value':var.get('value'),'range':Js([var.get('token').get('start'), var.get('token').get('end')]),'loc':var.get('loc')})
            var.put('entry', PyJs_Object_46_)
            if var.get('token').get('regex'):
                PyJs_Object_47_ = Js({'pattern':var.get('token').get('regex').get('pattern'),'flags':var.get('token').get('regex').get('flags')})
                var.get('entry').put('regex', PyJs_Object_47_)
            var.get('extra').get('tokens').callprop('push', var.get('entry'))
        return var.get('token')
    PyJsHoisted_collectToken_.__name__ = 'collectToken'
    var.put('collectToken', PyJsHoisted_collectToken_)
    @Js
    def PyJsHoisted_parseWithStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'node', 'object'])
        pass
        if var.get('strict'):
            var.get('tolerateError')(var.get('Messages').get('StrictModeWith'))
        var.get('expectKeyword')(Js('with'))
        var.get('expect')(Js('('))
        var.put('object', var.get('parseExpression')())
        var.get('expect')(Js(')'))
        var.put('body', var.get('parseStatement')())
        return var.get('node').callprop('finishWithStatement', var.get('object'), var.get('body'))
    PyJsHoisted_parseWithStatement_.__name__ = 'parseWithStatement'
    var.put('parseWithStatement', PyJsHoisted_parseWithStatement_)
    @Js
    def PyJsHoisted_parseObjectPattern_(params, kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'params':params, 'arguments':arguments}, var)
        var.registers(['node', 'kind', 'params', 'properties'])
        var.put('node', var.get('Node').create())
        var.put('properties', Js([]))
        var.get('expect')(Js('{'))
        while var.get('match')(Js('}')).neg():
            var.get('properties').callprop('push', var.get('parsePropertyPattern')(var.get('params'), var.get('kind')))
            if var.get('match')(Js('}')).neg():
                var.get('expect')(Js(','))
        var.get('lex')()
        return var.get('node').callprop('finishObjectPattern', var.get('properties'))
    PyJsHoisted_parseObjectPattern_.__name__ = 'parseObjectPattern'
    var.put('parseObjectPattern', PyJsHoisted_parseObjectPattern_)
    @Js
    def PyJsHoisted_parseImportSpecifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'imported', 'local'])
        var.put('node', var.get('Node').create())
        var.put('imported', var.get('parseNonComputedProperty')())
        if var.get('matchContextualKeyword')(Js('as')):
            var.get('lex')()
            var.put('local', var.get('parseVariableIdentifier')())
        return var.get('node').callprop('finishImportSpecifier', var.get('local'), var.get('imported'))
    PyJsHoisted_parseImportSpecifier_.__name__ = 'parseImportSpecifier'
    var.put('parseImportSpecifier', PyJsHoisted_parseImportSpecifier_)
    @Js
    def PyJsHoisted_skipComment_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['start', 'ch'])
        pass
        var.put('hasLineTerminator', Js(False))
        var.put('start', PyJsStrictEq(var.get('index'),Js(0.0)))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').callprop('charCodeAt', var.get('index')))
            if var.get('isWhiteSpace')(var.get('ch')):
                var.put('index',Js(var.get('index').to_number())+Js(1))
            else:
                if var.get('isLineTerminator')(var.get('ch')):
                    var.put('hasLineTerminator', var.get('true'))
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                    if (PyJsStrictEq(var.get('ch'),Js(13)) and PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('index')),Js(10))):
                        var.put('index',Js(var.get('index').to_number())+Js(1))
                    var.put('lineNumber',Js(var.get('lineNumber').to_number())+Js(1))
                    var.put('lineStart', var.get('index'))
                    var.put('start', var.get('true'))
                else:
                    if PyJsStrictEq(var.get('ch'),Js(47)):
                        var.put('ch', var.get('source').callprop('charCodeAt', (var.get('index')+Js(1.0))))
                        if PyJsStrictEq(var.get('ch'),Js(47)):
                            var.put('index',Js(var.get('index').to_number())+Js(1))
                            var.put('index',Js(var.get('index').to_number())+Js(1))
                            var.get('skipSingleLineComment')(Js(2.0))
                            var.put('start', var.get('true'))
                        else:
                            if PyJsStrictEq(var.get('ch'),Js(42)):
                                var.put('index',Js(var.get('index').to_number())+Js(1))
                                var.put('index',Js(var.get('index').to_number())+Js(1))
                                var.get('skipMultiLineComment')()
                            else:
                                break
                    else:
                        if (var.get('start') and PyJsStrictEq(var.get('ch'),Js(45))):
                            if (PyJsStrictEq(var.get('source').callprop('charCodeAt', (var.get('index')+Js(1.0))),Js(45)) and PyJsStrictEq(var.get('source').callprop('charCodeAt', (var.get('index')+Js(2.0))),Js(62))):
                                var.put('index', Js(3.0), '+')
                                var.get('skipSingleLineComment')(Js(3.0))
                            else:
                                break
                        else:
                            if PyJsStrictEq(var.get('ch'),Js(60)):
                                if PyJsStrictEq(var.get('source').callprop('slice', (var.get('index')+Js(1.0)), (var.get('index')+Js(4.0))),Js('!--')):
                                    var.put('index',Js(var.get('index').to_number())+Js(1))
                                    var.put('index',Js(var.get('index').to_number())+Js(1))
                                    var.put('index',Js(var.get('index').to_number())+Js(1))
                                    var.put('index',Js(var.get('index').to_number())+Js(1))
                                    var.get('skipSingleLineComment')(Js(4.0))
                                else:
                                    break
                            else:
                                break
    PyJsHoisted_skipComment_.__name__ = 'skipComment'
    var.put('skipComment', PyJsHoisted_skipComment_)
    @Js
    def PyJsHoisted_parseVariableStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'declarations'])
        pass
        var.get('expectKeyword')(Js('var'))
        PyJs_Object_140_ = Js({'inFor':Js(False)})
        var.put('declarations', var.get('parseVariableDeclarationList')(PyJs_Object_140_))
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishVariableDeclaration', var.get('declarations'))
    PyJsHoisted_parseVariableStatement_.__name__ = 'parseVariableStatement'
    var.put('parseVariableStatement', PyJsHoisted_parseVariableStatement_)
    @Js
    def PyJsHoisted_parseDebuggerStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node'])
        var.get('expectKeyword')(Js('debugger'))
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishDebuggerStatement')
    PyJsHoisted_parseDebuggerStatement_.__name__ = 'parseDebuggerStatement'
    var.put('parseDebuggerStatement', PyJsHoisted_parseDebuggerStatement_)
    @Js
    def PyJsHoisted_lookaheadPropertyName_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        while 1:
            SWITCHED = False
            CONDITION = (var.get('lookahead').get('type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('Identifier')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('StringLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('BooleanLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('NullLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('NumericLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('Keyword')):
                SWITCHED = True
                return var.get('true')
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('Punctuator')):
                SWITCHED = True
                return PyJsStrictEq(var.get('lookahead').get('value'),Js('['))
            SWITCHED = True
            break
        return Js(False)
    PyJsHoisted_lookaheadPropertyName_.__name__ = 'lookaheadPropertyName'
    var.put('lookaheadPropertyName', PyJsHoisted_lookaheadPropertyName_)
    @Js
    def PyJsHoisted_tokenize_(code, options, this, arguments, var=var):
        var = Scope({'this':this, 'code':code, 'options':options, 'arguments':arguments}, var)
        var.registers(['tokens', 'code', 'toString', 'options'])
        pass
        var.put('toString', var.get('String'))
        if (PyJsStrictNeq(var.get('code',throw=False).typeof(),Js('string')) and var.get('code').instanceof(var.get('String')).neg()):
            var.put('code', var.get('toString')(var.get('code')))
        var.put('source', var.get('code'))
        var.put('index', Js(0.0))
        var.put('lineNumber', (Js(1.0) if (var.get('source').get('length')>Js(0.0)) else Js(0.0)))
        var.put('lineStart', Js(0.0))
        var.put('startIndex', var.get('index'))
        var.put('startLineNumber', var.get('lineNumber'))
        var.put('startLineStart', var.get('lineStart'))
        var.put('length', var.get('source').get('length'))
        var.put('lookahead', var.get("null"))
        PyJs_Object_152_ = Js({})
        PyJs_Object_151_ = Js({'allowIn':var.get('true'),'allowYield':var.get('true'),'labelSet':PyJs_Object_152_,'inFunctionBody':Js(False),'inIteration':Js(False),'inSwitch':Js(False),'lastCommentStart':(-Js(1.0)),'curlyStack':Js([])})
        var.put('state', PyJs_Object_151_)
        PyJs_Object_153_ = Js({})
        var.put('extra', PyJs_Object_153_)
        PyJs_Object_154_ = Js({})
        var.put('options', (var.get('options') or PyJs_Object_154_))
        var.get('options').put('tokens', var.get('true'))
        var.get('extra').put('tokens', Js([]))
        var.get('extra').put('tokenize', var.get('true'))
        var.get('extra').put('openParenToken', (-Js(1.0)))
        var.get('extra').put('openCurlyToken', (-Js(1.0)))
        var.get('extra').put('range', (PyJsStrictEq(var.get('options').get('range').typeof(),Js('boolean')) and var.get('options').get('range')))
        var.get('extra').put('loc', (PyJsStrictEq(var.get('options').get('loc').typeof(),Js('boolean')) and var.get('options').get('loc')))
        if (PyJsStrictEq(var.get('options').get('comment').typeof(),Js('boolean')) and var.get('options').get('comment')):
            var.get('extra').put('comments', Js([]))
        if (PyJsStrictEq(var.get('options').get('tolerant').typeof(),Js('boolean')) and var.get('options').get('tolerant')):
            var.get('extra').put('errors', Js([]))
        try:
            var.get('peek')()
            if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('EOF')):
                return var.get('extra').get('tokens')
            var.get('lex')()
            while PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('EOF')):
                try:
                    var.get('lex')()
                except PyJsException as PyJsTempException:
                    PyJsHolder_6c65784572726f72_76841511 = var.own.get('lexError')
                    var.force_own_put('lexError', PyExceptionToJs(PyJsTempException))
                    try:
                        if var.get('extra').get('errors'):
                            var.get('recordError')(var.get('lexError'))
                            break
                        else:
                            PyJsTempException = JsToPyException(var.get('lexError'))
                            raise PyJsTempException
                    finally:
                        if PyJsHolder_6c65784572726f72_76841511 is not None:
                            var.own['lexError'] = PyJsHolder_6c65784572726f72_76841511
                        else:
                            del var.own['lexError']
                        del PyJsHolder_6c65784572726f72_76841511
            var.get('filterTokenLocation')()
            var.put('tokens', var.get('extra').get('tokens'))
            if PyJsStrictNeq(var.get('extra').get('comments').typeof(),Js('undefined')):
                var.get('tokens').put('comments', var.get('extra').get('comments'))
            if PyJsStrictNeq(var.get('extra').get('errors').typeof(),Js('undefined')):
                var.get('tokens').put('errors', var.get('extra').get('errors'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_58840235 = var.own.get('e')
            var.force_own_put('e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get('e'))
                raise PyJsTempException
            finally:
                if PyJsHolder_65_58840235 is not None:
                    var.own['e'] = PyJsHolder_65_58840235
                else:
                    del var.own['e']
                del PyJsHolder_65_58840235
        finally:
            PyJs_Object_155_ = Js({})
            var.put('extra', PyJs_Object_155_)
        return var.get('tokens')
    PyJsHoisted_tokenize_.__name__ = 'tokenize'
    var.put('tokenize', PyJsHoisted_tokenize_)
    @Js
    def PyJsHoisted_parseExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'expressions', 'startToken'])
        var.put('startToken', var.get('lookahead'))
        var.put('expr', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
        if var.get('match')(Js(',')):
            var.put('expressions', Js([var.get('expr')]))
            while (var.get('startIndex')<var.get('length')):
                if var.get('match')(Js(',')).neg():
                    break
                var.get('lex')()
                var.get('expressions').callprop('push', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
            var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishSequenceExpression', var.get('expressions')))
        return var.get('expr')
    PyJsHoisted_parseExpression_.__name__ = 'parseExpression'
    var.put('parseExpression', PyJsHoisted_parseExpression_)
    @Js
    def PyJsHoisted_constructError_(msg, column, this, arguments, var=var):
        var = Scope({'msg':msg, 'column':column, 'this':this, 'arguments':arguments}, var)
        var.registers(['msg', 'column', 'error'])
        var.put('error', var.get('Error').create(var.get('msg')))
        try:
            PyJsTempException = JsToPyException(var.get('error'))
            raise PyJsTempException
        except PyJsException as PyJsTempException:
            PyJsHolder_62617365_41349638 = var.own.get('base')
            var.force_own_put('base', PyExceptionToJs(PyJsTempException))
            try:
                if (var.get('Object').get('create') and var.get('Object').get('defineProperty')):
                    var.put('error', var.get('Object').callprop('create', var.get('base')))
                    PyJs_Object_117_ = Js({'value':var.get('column')})
                    var.get('Object').callprop('defineProperty', var.get('error'), Js('column'), PyJs_Object_117_)
            finally:
                if PyJsHolder_62617365_41349638 is not None:
                    var.own['base'] = PyJsHolder_62617365_41349638
                else:
                    del var.own['base']
                del PyJsHolder_62617365_41349638
        finally:
            return var.get('error')
    PyJsHoisted_constructError_.__name__ = 'constructError'
    var.put('constructError', PyJsHoisted_constructError_)
    @Js
    def PyJsHoisted_parseObjectPropertyKey_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'expr', 'token'])
        var.put('node', var.get('Node').create())
        var.put('token', var.get('lex')())
        while 1:
            SWITCHED = False
            CONDITION = (var.get('token').get('type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('StringLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('NumericLiteral')):
                SWITCHED = True
                if (var.get('strict') and var.get('token').get('octal')):
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictOctalLiteral'))
                return var.get('node').callprop('finishLiteral', var.get('token'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('Identifier')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('BooleanLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('NullLiteral')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('Keyword')):
                SWITCHED = True
                return var.get('node').callprop('finishIdentifier', var.get('token').get('value'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Token').get('Punctuator')):
                SWITCHED = True
                if PyJsStrictEq(var.get('token').get('value'),Js('[')):
                    var.put('expr', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
                    var.get('expect')(Js(']'))
                    return var.get('expr')
                break
            SWITCHED = True
            break
        var.get('throwUnexpectedToken')(var.get('token'))
    PyJsHoisted_parseObjectPropertyKey_.__name__ = 'parseObjectPropertyKey'
    var.put('parseObjectPropertyKey', PyJsHoisted_parseObjectPropertyKey_)
    @Js
    def PyJsHoisted_parseArrayPattern_(params, kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'params':params, 'arguments':arguments}, var)
        var.registers(['node', 'kind', 'elements', 'restNode', 'rest', 'params'])
        var.put('node', var.get('Node').create())
        var.put('elements', Js([]))
        var.get('expect')(Js('['))
        while var.get('match')(Js(']')).neg():
            if var.get('match')(Js(',')):
                var.get('lex')()
                var.get('elements').callprop('push', var.get("null"))
            else:
                if var.get('match')(Js('...')):
                    var.put('restNode', var.get('Node').create())
                    var.get('lex')()
                    var.get('params').callprop('push', var.get('lookahead'))
                    var.put('rest', var.get('parseVariableIdentifier')(var.get('params'), var.get('kind')))
                    var.get('elements').callprop('push', var.get('restNode').callprop('finishRestElement', var.get('rest')))
                    break
                else:
                    var.get('elements').callprop('push', var.get('parsePatternWithDefault')(var.get('params'), var.get('kind')))
                if var.get('match')(Js(']')).neg():
                    var.get('expect')(Js(','))
        var.get('expect')(Js(']'))
        return var.get('node').callprop('finishArrayPattern', var.get('elements'))
    PyJsHoisted_parseArrayPattern_.__name__ = 'parseArrayPattern'
    var.put('parseArrayPattern', PyJsHoisted_parseArrayPattern_)
    @Js
    def PyJsHoisted_expectKeyword_(keyword, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'keyword':keyword}, var)
        var.registers(['token', 'keyword'])
        var.put('token', var.get('lex')())
        if (PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('Keyword')) or PyJsStrictNeq(var.get('token').get('value'),var.get('keyword'))):
            var.get('throwUnexpectedToken')(var.get('token'))
    PyJsHoisted_expectKeyword_.__name__ = 'expectKeyword'
    var.put('expectKeyword', PyJsHoisted_expectKeyword_)
    @Js
    def PyJsHoisted_assert_(condition, message, this, arguments, var=var):
        var = Scope({'this':this, 'message':message, 'arguments':arguments, 'condition':condition}, var)
        var.registers(['message', 'condition'])
        if var.get('condition').neg():
            PyJsTempException = JsToPyException(var.get('Error').create((Js('ASSERT: ')+var.get('message'))))
            raise PyJsTempException
    PyJsHoisted_assert_.__name__ = 'assert'
    var.put('assert', PyJsHoisted_assert_)
    @Js
    def PyJsHoisted_parseConciseBody_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if var.get('match')(Js('{')):
            return var.get('parseFunctionSourceElements')()
        return var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression'))
    PyJsHoisted_parseConciseBody_.__name__ = 'parseConciseBody'
    var.put('parseConciseBody', PyJsHoisted_parseConciseBody_)
    @Js
    def PyJsHoisted_createError_(line, pos, description, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'line':line, 'pos':pos, 'description':description}, var)
        var.registers(['description', 'column', 'pos', 'error', 'msg', 'line'])
        pass
        var.put('msg', (((Js('Line ')+var.get('line'))+Js(': '))+var.get('description')))
        var.put('column', ((var.get('pos')-(var.get('lineStart') if var.get('scanning') else var.get('lastLineStart')))+Js(1.0)))
        var.put('error', var.get('constructError')(var.get('msg'), var.get('column')))
        var.get('error').put('lineNumber', var.get('line'))
        var.get('error').put('description', var.get('description'))
        var.get('error').put('index', var.get('pos'))
        return var.get('error')
    PyJsHoisted_createError_.__name__ = 'createError'
    var.put('createError', PyJsHoisted_createError_)
    @Js
    def PyJsHoisted_parseLeftHandSideExpressionAllowCall_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['previousAllowIn', 'expr', 'args', 'quasi', 'startToken', 'property'])
        var.put('previousAllowIn', var.get('state').get('allowIn'))
        var.put('startToken', var.get('lookahead'))
        var.get('state').put('allowIn', var.get('true'))
        if (var.get('matchKeyword')(Js('super')) and var.get('state').get('inFunctionBody')):
            var.put('expr', var.get('Node').create())
            var.get('lex')()
            var.put('expr', var.get('expr').callprop('finishSuper'))
            if ((var.get('match')(Js('(')).neg() and var.get('match')(Js('.')).neg()) and var.get('match')(Js('[')).neg()):
                var.get('throwUnexpectedToken')(var.get('lookahead'))
        else:
            var.put('expr', var.get('inheritCoverGrammar')((var.get('parseNewExpression') if var.get('matchKeyword')(Js('new')) else var.get('parsePrimaryExpression'))))
        #for JS loop

        while 1:
            if var.get('match')(Js('.')):
                var.put('isBindingElement', Js(False))
                var.put('isAssignmentTarget', var.get('true'))
                var.put('property', var.get('parseNonComputedMember')())
                var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishMemberExpression', Js('.'), var.get('expr'), var.get('property')))
            else:
                if var.get('match')(Js('(')):
                    var.put('isBindingElement', Js(False))
                    var.put('isAssignmentTarget', Js(False))
                    var.put('args', var.get('parseArguments')())
                    var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishCallExpression', var.get('expr'), var.get('args')))
                else:
                    if var.get('match')(Js('[')):
                        var.put('isBindingElement', Js(False))
                        var.put('isAssignmentTarget', var.get('true'))
                        var.put('property', var.get('parseComputedMember')())
                        var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishMemberExpression', Js('['), var.get('expr'), var.get('property')))
                    else:
                        if (PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Template')) and var.get('lookahead').get('head')):
                            var.put('quasi', var.get('parseTemplateLiteral')())
                            var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishTaggedTemplateExpression', var.get('expr'), var.get('quasi')))
                        else:
                            break

        var.get('state').put('allowIn', var.get('previousAllowIn'))
        return var.get('expr')
    PyJsHoisted_parseLeftHandSideExpressionAllowCall_.__name__ = 'parseLeftHandSideExpressionAllowCall'
    var.put('parseLeftHandSideExpressionAllowCall', PyJsHoisted_parseLeftHandSideExpressionAllowCall_)
    @Js
    def PyJsHoisted_fromCodePoint_(cp, this, arguments, var=var):
        var = Scope({'this':this, 'cp':cp, 'arguments':arguments}, var)
        var.registers(['cp'])
        return (var.get('String').callprop('fromCharCode', var.get('cp')) if (var.get('cp')<Js(65536)) else (var.get('String').callprop('fromCharCode', (Js(55296)+((var.get('cp')-Js(65536))>>Js(10.0))))+var.get('String').callprop('fromCharCode', (Js(56320)+((var.get('cp')-Js(65536))&Js(1023.0))))))
    PyJsHoisted_fromCodePoint_.__name__ = 'fromCodePoint'
    var.put('fromCodePoint', PyJsHoisted_fromCodePoint_)
    @Js
    def PyJsHoisted_parseExportNamedDeclaration_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'src', 'specifiers', 'isExportFromIdentifier', 'declaration'])
        var.put('declaration', var.get("null"))
        var.put('src', var.get("null"))
        var.put('specifiers', Js([]))
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Keyword')):
            while 1:
                SWITCHED = False
                CONDITION = (var.get('lookahead').get('value'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('let')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('const')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('var')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('class')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('function')):
                    SWITCHED = True
                    var.put('declaration', var.get('parseStatementListItem')())
                    return var.get('node').callprop('finishExportNamedDeclaration', var.get('declaration'), var.get('specifiers'), var.get("null"))
                SWITCHED = True
                break
        var.get('expect')(Js('{'))
        while var.get('match')(Js('}')).neg():
            var.put('isExportFromIdentifier', (var.get('isExportFromIdentifier') or var.get('matchKeyword')(Js('default'))))
            var.get('specifiers').callprop('push', var.get('parseExportSpecifier')())
            if var.get('match')(Js('}')).neg():
                var.get('expect')(Js(','))
                if var.get('match')(Js('}')):
                    break
        var.get('expect')(Js('}'))
        if var.get('matchContextualKeyword')(Js('from')):
            var.get('lex')()
            var.put('src', var.get('parseModuleSpecifier')())
            var.get('consumeSemicolon')()
        else:
            if var.get('isExportFromIdentifier'):
                var.get('throwError')((var.get('Messages').get('UnexpectedToken') if var.get('lookahead').get('value') else var.get('Messages').get('MissingFromClause')), var.get('lookahead').get('value'))
            else:
                var.get('consumeSemicolon')()
        return var.get('node').callprop('finishExportNamedDeclaration', var.get('declaration'), var.get('specifiers'), var.get('src'))
    PyJsHoisted_parseExportNamedDeclaration_.__name__ = 'parseExportNamedDeclaration'
    var.put('parseExportNamedDeclaration', PyJsHoisted_parseExportNamedDeclaration_)
    @Js
    def PyJsHoisted_parseBlock_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'block'])
        var.put('node', var.get('Node').create())
        var.get('expect')(Js('{'))
        var.put('block', var.get('parseStatementList')())
        var.get('expect')(Js('}'))
        return var.get('node').callprop('finishBlockStatement', var.get('block'))
    PyJsHoisted_parseBlock_.__name__ = 'parseBlock'
    var.put('parseBlock', PyJsHoisted_parseBlock_)
    @Js
    def PyJsHoisted_parseExportSpecifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'local', 'exported', 'def'])
        var.put('node', var.get('Node').create())
        if var.get('matchKeyword')(Js('default')):
            var.put('def', var.get('Node').create())
            var.get('lex')()
            var.put('local', var.get('def').callprop('finishIdentifier', Js('default')))
        else:
            var.put('local', var.get('parseVariableIdentifier')())
        if var.get('matchContextualKeyword')(Js('as')):
            var.get('lex')()
            var.put('exported', var.get('parseNonComputedProperty')())
        return var.get('node').callprop('finishExportSpecifier', var.get('local'), var.get('exported'))
    PyJsHoisted_parseExportSpecifier_.__name__ = 'parseExportSpecifier'
    var.put('parseExportSpecifier', PyJsHoisted_parseExportSpecifier_)
    @Js
    def PyJsHoisted_skipSingleLineComment_(offset, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'offset':offset}, var)
        var.registers(['comment', 'start', 'ch', 'offset', 'loc'])
        pass
        var.put('start', (var.get('index')-var.get('offset')))
        PyJs_Object_13_ = Js({'line':var.get('lineNumber'),'column':((var.get('index')-var.get('lineStart'))-var.get('offset'))})
        PyJs_Object_12_ = Js({'start':PyJs_Object_13_})
        var.put('loc', PyJs_Object_12_)
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').callprop('charCodeAt', var.get('index')))
            var.put('index',Js(var.get('index').to_number())+Js(1))
            if var.get('isLineTerminator')(var.get('ch')):
                var.put('hasLineTerminator', var.get('true'))
                if var.get('extra').get('comments'):
                    var.put('comment', var.get('source').callprop('slice', (var.get('start')+var.get('offset')), (var.get('index')-Js(1.0))))
                    PyJs_Object_14_ = Js({'line':var.get('lineNumber'),'column':((var.get('index')-var.get('lineStart'))-Js(1.0))})
                    var.get('loc').put('end', PyJs_Object_14_)
                    var.get('addComment')(Js('Line'), var.get('comment'), var.get('start'), (var.get('index')-Js(1.0)), var.get('loc'))
                if (PyJsStrictEq(var.get('ch'),Js(13.0)) and PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('index')),Js(10.0))):
                    var.put('index',Js(var.get('index').to_number())+Js(1))
                var.put('lineNumber',Js(var.get('lineNumber').to_number())+Js(1))
                var.put('lineStart', var.get('index'))
                return var.get('undefined')
        if var.get('extra').get('comments'):
            var.put('comment', var.get('source').callprop('slice', (var.get('start')+var.get('offset')), var.get('index')))
            PyJs_Object_15_ = Js({'line':var.get('lineNumber'),'column':(var.get('index')-var.get('lineStart'))})
            var.get('loc').put('end', PyJs_Object_15_)
            var.get('addComment')(Js('Line'), var.get('comment'), var.get('start'), var.get('index'), var.get('loc'))
    PyJsHoisted_skipSingleLineComment_.__name__ = 'skipSingleLineComment'
    var.put('skipSingleLineComment', PyJsHoisted_skipSingleLineComment_)
    @Js
    def PyJsHoisted_parseDoWhileStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'test', 'node', 'oldInIteration'])
        pass
        var.get('expectKeyword')(Js('do'))
        var.put('oldInIteration', var.get('state').get('inIteration'))
        var.get('state').put('inIteration', var.get('true'))
        var.put('body', var.get('parseStatement')())
        var.get('state').put('inIteration', var.get('oldInIteration'))
        var.get('expectKeyword')(Js('while'))
        var.get('expect')(Js('('))
        var.put('test', var.get('parseExpression')())
        var.get('expect')(Js(')'))
        if var.get('match')(Js(';')):
            var.get('lex')()
        return var.get('node').callprop('finishDoWhileStatement', var.get('body'), var.get('test'))
    PyJsHoisted_parseDoWhileStatement_.__name__ = 'parseDoWhileStatement'
    var.put('parseDoWhileStatement', PyJsHoisted_parseDoWhileStatement_)
    @Js
    def PyJsHoisted_codePointAt_(i, this, arguments, var=var):
        var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'second', 'cp', 'first'])
        pass
        var.put('cp', var.get('source').callprop('charCodeAt', var.get('i')))
        if ((var.get('cp')>=Js(55296)) and (var.get('cp')<=Js(56319))):
            var.put('second', var.get('source').callprop('charCodeAt', (var.get('i')+Js(1.0))))
            if ((var.get('second')>=Js(56320)) and (var.get('second')<=Js(57343))):
                var.put('first', var.get('cp'))
                var.put('cp', (((((var.get('first')-Js(55296))*Js(1024))+var.get('second'))-Js(56320))+Js(65536)))
        return var.get('cp')
    PyJsHoisted_codePointAt_.__name__ = 'codePointAt'
    var.put('codePointAt', PyJsHoisted_codePointAt_)
    @Js
    def PyJsHoisted_scanHexEscape_(prefix, this, arguments, var=var):
        var = Scope({'this':this, 'prefix':prefix, 'arguments':arguments}, var)
        var.registers(['i', 'prefix', 'ch', 'len', 'code'])
        var.put('code', Js(0.0))
        var.put('len', (Js(4.0) if PyJsStrictEq(var.get('prefix'),Js('u')) else Js(2.0)))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('len')):
            try:
                if ((var.get('index')<var.get('length')) and var.get('isHexDigit')(var.get('source').get(var.get('index')))):
                    var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                    var.put('code', ((var.get('code')*Js(16.0))+Js('0123456789abcdef').callprop('indexOf', var.get('ch').callprop('toLowerCase'))))
                else:
                    return Js('')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return var.get('String').callprop('fromCharCode', var.get('code'))
    PyJsHoisted_scanHexEscape_.__name__ = 'scanHexEscape'
    var.put('scanHexEscape', PyJsHoisted_scanHexEscape_)
    @Js
    def PyJsHoisted_isHexDigit_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        return (Js('0123456789abcdefABCDEF').callprop('indexOf', var.get('ch'))>=Js(0.0))
    PyJsHoisted_isHexDigit_.__name__ = 'isHexDigit'
    var.put('isHexDigit', PyJsHoisted_isHexDigit_)
    @Js
    def PyJsHoisted_matchContextualKeyword_(keyword, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'keyword':keyword}, var)
        var.registers(['keyword'])
        return (PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier')) and PyJsStrictEq(var.get('lookahead').get('value'),var.get('keyword')))
    PyJsHoisted_matchContextualKeyword_.__name__ = 'matchContextualKeyword'
    var.put('matchContextualKeyword', PyJsHoisted_matchContextualKeyword_)
    @Js
    def PyJsHoisted_isStrictModeReservedWord_(id, this, arguments, var=var):
        var = Scope({'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['id'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get('id'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js('implements')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('interface')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('package')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('private')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('protected')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('public')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('static')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('yield')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('let')):
                SWITCHED = True
                return var.get('true')
            if True:
                SWITCHED = True
                return Js(False)
            SWITCHED = True
            break
    PyJsHoisted_isStrictModeReservedWord_.__name__ = 'isStrictModeReservedWord'
    var.put('isStrictModeReservedWord', PyJsHoisted_isStrictModeReservedWord_)
    @Js
    def PyJsHoisted_binaryPrecedence_(token, allowIn, this, arguments, var=var):
        var = Scope({'this':this, 'allowIn':allowIn, 'token':token, 'arguments':arguments}, var)
        var.registers(['allowIn', 'token', 'prec'])
        var.put('prec', Js(0.0))
        if (PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('Punctuator')) and PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('Keyword'))):
            return Js(0.0)
        while 1:
            SWITCHED = False
            CONDITION = (var.get('token').get('value'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js('||')):
                SWITCHED = True
                var.put('prec', Js(1.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('&&')):
                SWITCHED = True
                var.put('prec', Js(2.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('|')):
                SWITCHED = True
                var.put('prec', Js(3.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('^')):
                SWITCHED = True
                var.put('prec', Js(4.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('&')):
                SWITCHED = True
                var.put('prec', Js(5.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('==')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('!=')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('===')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('!==')):
                SWITCHED = True
                var.put('prec', Js(6.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('<')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('>')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('<=')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('>=')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('instanceof')):
                SWITCHED = True
                var.put('prec', Js(7.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('in')):
                SWITCHED = True
                var.put('prec', (Js(7.0) if var.get('allowIn') else Js(0.0)))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('<<')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('>>')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('>>>')):
                SWITCHED = True
                var.put('prec', Js(8.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('+')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('-')):
                SWITCHED = True
                var.put('prec', Js(9.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('*')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('/')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('%')):
                SWITCHED = True
                var.put('prec', Js(11.0))
                break
            if True:
                SWITCHED = True
                break
            SWITCHED = True
            break
        return var.get('prec')
    PyJsHoisted_binaryPrecedence_.__name__ = 'binaryPrecedence'
    var.put('binaryPrecedence', PyJsHoisted_binaryPrecedence_)
    @Js
    def PyJsHoisted_parse_(code, options, this, arguments, var=var):
        var = Scope({'this':this, 'code':code, 'options':options, 'arguments':arguments}, var)
        var.registers(['code', 'program', 'toString', 'options'])
        pass
        var.put('toString', var.get('String'))
        if (PyJsStrictNeq(var.get('code',throw=False).typeof(),Js('string')) and var.get('code').instanceof(var.get('String')).neg()):
            var.put('code', var.get('toString')(var.get('code')))
        var.put('source', var.get('code'))
        var.put('index', Js(0.0))
        var.put('lineNumber', (Js(1.0) if (var.get('source').get('length')>Js(0.0)) else Js(0.0)))
        var.put('lineStart', Js(0.0))
        var.put('startIndex', var.get('index'))
        var.put('startLineNumber', var.get('lineNumber'))
        var.put('startLineStart', var.get('lineStart'))
        var.put('length', var.get('source').get('length'))
        var.put('lookahead', var.get("null"))
        PyJs_Object_157_ = Js({})
        PyJs_Object_156_ = Js({'allowIn':var.get('true'),'allowYield':var.get('true'),'labelSet':PyJs_Object_157_,'inFunctionBody':Js(False),'inIteration':Js(False),'inSwitch':Js(False),'lastCommentStart':(-Js(1.0)),'curlyStack':Js([]),'sourceType':Js('script')})
        var.put('state', PyJs_Object_156_)
        var.put('strict', Js(False))
        PyJs_Object_158_ = Js({})
        var.put('extra', PyJs_Object_158_)
        if PyJsStrictNeq(var.get('options',throw=False).typeof(),Js('undefined')):
            var.get('extra').put('range', (PyJsStrictEq(var.get('options').get('range').typeof(),Js('boolean')) and var.get('options').get('range')))
            var.get('extra').put('loc', (PyJsStrictEq(var.get('options').get('loc').typeof(),Js('boolean')) and var.get('options').get('loc')))
            var.get('extra').put('attachComment', (PyJsStrictEq(var.get('options').get('attachComment').typeof(),Js('boolean')) and var.get('options').get('attachComment')))
            if ((var.get('extra').get('loc') and PyJsStrictNeq(var.get('options').get('source'),var.get("null"))) and PyJsStrictNeq(var.get('options').get('source'),var.get('undefined'))):
                var.get('extra').put('source', var.get('toString')(var.get('options').get('source')))
            if (PyJsStrictEq(var.get('options').get('tokens').typeof(),Js('boolean')) and var.get('options').get('tokens')):
                var.get('extra').put('tokens', Js([]))
            if (PyJsStrictEq(var.get('options').get('comment').typeof(),Js('boolean')) and var.get('options').get('comment')):
                var.get('extra').put('comments', Js([]))
            if (PyJsStrictEq(var.get('options').get('tolerant').typeof(),Js('boolean')) and var.get('options').get('tolerant')):
                var.get('extra').put('errors', Js([]))
            if var.get('extra').get('attachComment'):
                var.get('extra').put('range', var.get('true'))
                var.get('extra').put('comments', Js([]))
                var.get('extra').put('bottomRightStack', Js([]))
                var.get('extra').put('trailingComments', Js([]))
                var.get('extra').put('leadingComments', Js([]))
            if PyJsStrictEq(var.get('options').get('sourceType'),Js('module')):
                var.get('state').put('sourceType', var.get('options').get('sourceType'))
                var.put('strict', var.get('true'))
        try:
            var.put('program', var.get('parseProgram')())
            if PyJsStrictNeq(var.get('extra').get('comments').typeof(),Js('undefined')):
                var.get('program').put('comments', var.get('extra').get('comments'))
            if PyJsStrictNeq(var.get('extra').get('tokens').typeof(),Js('undefined')):
                var.get('filterTokenLocation')()
                var.get('program').put('tokens', var.get('extra').get('tokens'))
            if PyJsStrictNeq(var.get('extra').get('errors').typeof(),Js('undefined')):
                var.get('program').put('errors', var.get('extra').get('errors'))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_51248354 = var.own.get('e')
            var.force_own_put('e', PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(var.get('e'))
                raise PyJsTempException
            finally:
                if PyJsHolder_65_51248354 is not None:
                    var.own['e'] = PyJsHolder_65_51248354
                else:
                    del var.own['e']
                del PyJsHolder_65_51248354
        finally:
            PyJs_Object_159_ = Js({})
            var.put('extra', PyJs_Object_159_)
        return var.get('program')
    PyJsHoisted_parse_.__name__ = 'parse'
    var.put('parse', PyJsHoisted_parse_)
    @Js
    def PyJsHoisted_matchAssign_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['op'])
        pass
        if PyJsStrictNeq(var.get('lookahead').get('type'),var.get('Token').get('Punctuator')):
            return Js(False)
        var.put('op', var.get('lookahead').get('value'))
        def PyJs_LONG_122_(var=var):
            return (((((((((PyJsStrictEq(var.get('op'),Js('=')) or PyJsStrictEq(var.get('op'),Js('*='))) or PyJsStrictEq(var.get('op'),Js('/='))) or PyJsStrictEq(var.get('op'),Js('%='))) or PyJsStrictEq(var.get('op'),Js('+='))) or PyJsStrictEq(var.get('op'),Js('-='))) or PyJsStrictEq(var.get('op'),Js('<<='))) or PyJsStrictEq(var.get('op'),Js('>>='))) or PyJsStrictEq(var.get('op'),Js('>>>='))) or PyJsStrictEq(var.get('op'),Js('&=')))
        return ((PyJs_LONG_122_() or PyJsStrictEq(var.get('op'),Js('^='))) or PyJsStrictEq(var.get('op'),Js('|=')))
    PyJsHoisted_matchAssign_.__name__ = 'matchAssign'
    var.put('matchAssign', PyJsHoisted_matchAssign_)
    @Js
    def PyJsHoisted_WrappingNode_(startToken, this, arguments, var=var):
        var = Scope({'this':this, 'startToken':startToken, 'arguments':arguments}, var)
        var.registers(['startToken'])
        if var.get('extra').get('range'):
            var.get("this").put('range', Js([var.get('startToken').get('start'), Js(0.0)]))
        if var.get('extra').get('loc'):
            var.get("this").put('loc', var.get('WrappingSourceLocation').create(var.get('startToken')))
    PyJsHoisted_WrappingNode_.__name__ = 'WrappingNode'
    var.put('WrappingNode', PyJsHoisted_WrappingNode_)
    @Js
    def PyJsHoisted_parseObjectInitializer_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'hasProto', 'properties'])
        var.put('properties', Js([]))
        PyJs_Object_126_ = Js({'value':Js(False)})
        var.put('hasProto', PyJs_Object_126_)
        var.put('node', var.get('Node').create())
        var.get('expect')(Js('{'))
        while var.get('match')(Js('}')).neg():
            var.get('properties').callprop('push', var.get('parseObjectProperty')(var.get('hasProto')))
            if var.get('match')(Js('}')).neg():
                var.get('expectCommaSeparator')()
        var.get('expect')(Js('}'))
        return var.get('node').callprop('finishObjectExpression', var.get('properties'))
    PyJsHoisted_parseObjectInitializer_.__name__ = 'parseObjectInitializer'
    var.put('parseObjectInitializer', PyJsHoisted_parseObjectInitializer_)
    @Js
    def PyJsHoisted_getIdentifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['start', 'ch'])
        pass
        var.put('start', (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').callprop('charCodeAt', var.get('index')))
            if PyJsStrictEq(var.get('ch'),Js(92)):
                var.put('index', var.get('start'))
                return var.get('getComplexIdentifier')()
            else:
                if ((var.get('ch')>=Js(55296)) and (var.get('ch')<Js(57343))):
                    var.put('index', var.get('start'))
                    return var.get('getComplexIdentifier')()
            if var.get('isIdentifierPart')(var.get('ch')):
                var.put('index',Js(var.get('index').to_number())+Js(1))
            else:
                break
        return var.get('source').callprop('slice', var.get('start'), var.get('index'))
    PyJsHoisted_getIdentifier_.__name__ = 'getIdentifier'
    var.put('getIdentifier', PyJsHoisted_getIdentifier_)
    @Js
    def PyJsHoisted_isRestrictedWord_(id, this, arguments, var=var):
        var = Scope({'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['id'])
        return (PyJsStrictEq(var.get('id'),Js('eval')) or PyJsStrictEq(var.get('id'),Js('arguments')))
    PyJsHoisted_isRestrictedWord_.__name__ = 'isRestrictedWord'
    var.put('isRestrictedWord', PyJsHoisted_isRestrictedWord_)
    @Js
    def PyJsHoisted_parseSwitchCase_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['test', 'node', 'statement', 'consequent'])
        var.put('consequent', Js([]))
        var.put('node', var.get('Node').create())
        if var.get('matchKeyword')(Js('default')):
            var.get('lex')()
            var.put('test', var.get("null"))
        else:
            var.get('expectKeyword')(Js('case'))
            var.put('test', var.get('parseExpression')())
        var.get('expect')(Js(':'))
        while (var.get('startIndex')<var.get('length')):
            if ((var.get('match')(Js('}')) or var.get('matchKeyword')(Js('default'))) or var.get('matchKeyword')(Js('case'))):
                break
            var.put('statement', var.get('parseStatementListItem')())
            var.get('consequent').callprop('push', var.get('statement'))
        return var.get('node').callprop('finishSwitchCase', var.get('test'), var.get('consequent'))
    PyJsHoisted_parseSwitchCase_.__name__ = 'parseSwitchCase'
    var.put('parseSwitchCase', PyJsHoisted_parseSwitchCase_)
    @Js
    def PyJsHoisted_parsePropertyPattern_(params, kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'params':params, 'arguments':arguments}, var)
        var.registers(['node', 'kind', 'computed', 'init', 'params', 'key', 'keyToken'])
        var.put('node', var.get('Node').create())
        var.put('computed', var.get('match')(Js('[')))
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier')):
            var.put('keyToken', var.get('lookahead'))
            var.put('key', var.get('parseVariableIdentifier')())
            if var.get('match')(Js('=')):
                var.get('params').callprop('push', var.get('keyToken'))
                var.get('lex')()
                var.put('init', var.get('parseAssignmentExpression')())
                return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), Js(False), var.get('WrappingNode').create(var.get('keyToken')).callprop('finishAssignmentPattern', var.get('key'), var.get('init')), Js(False), Js(False))
            else:
                if var.get('match')(Js(':')).neg():
                    var.get('params').callprop('push', var.get('keyToken'))
                    return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), Js(False), var.get('key'), Js(False), var.get('true'))
        else:
            var.put('key', var.get('parseObjectPropertyKey')(var.get('params'), var.get('kind')))
        var.get('expect')(Js(':'))
        var.put('init', var.get('parsePatternWithDefault')(var.get('params'), var.get('kind')))
        return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), var.get('computed'), var.get('init'), Js(False), Js(False))
    PyJsHoisted_parsePropertyPattern_.__name__ = 'parsePropertyPattern'
    var.put('parsePropertyPattern', PyJsHoisted_parsePropertyPattern_)
    @Js
    def PyJsHoisted_parseFunctionDeclaration_(node, identifierIsOptional, this, arguments, var=var):
        var = Scope({'node':node, 'identifierIsOptional':identifierIsOptional, 'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'tmp', 'previousStrict', 'node', 'identifierIsOptional', 'isGenerator', 'message', 'stricted', 'token', 'params', 'defaults', 'previousAllowYield', 'firstRestricted', 'id'])
        var.put('id', var.get("null"))
        var.put('params', Js([]))
        var.put('defaults', Js([]))
        var.put('previousAllowYield', var.get('state').get('allowYield'))
        var.get('expectKeyword')(Js('function'))
        var.put('isGenerator', var.get('match')(Js('*')))
        if var.get('isGenerator'):
            var.get('lex')()
        if (var.get('identifierIsOptional').neg() or var.get('match')(Js('(')).neg()):
            var.put('token', var.get('lookahead'))
            var.put('id', var.get('parseVariableIdentifier')())
            if var.get('strict'):
                if var.get('isRestrictedWord')(var.get('token').get('value')):
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictFunctionName'))
            else:
                if var.get('isRestrictedWord')(var.get('token').get('value')):
                    var.put('firstRestricted', var.get('token'))
                    var.put('message', var.get('Messages').get('StrictFunctionName'))
                else:
                    if var.get('isStrictModeReservedWord')(var.get('token').get('value')):
                        var.put('firstRestricted', var.get('token'))
                        var.put('message', var.get('Messages').get('StrictReservedWord'))
        var.get('state').put('allowYield', var.get('isGenerator').neg())
        var.put('tmp', var.get('parseParams')(var.get('firstRestricted')))
        var.put('params', var.get('tmp').get('params'))
        var.put('defaults', var.get('tmp').get('defaults'))
        var.put('stricted', var.get('tmp').get('stricted'))
        var.put('firstRestricted', var.get('tmp').get('firstRestricted'))
        if var.get('tmp').get('message'):
            var.put('message', var.get('tmp').get('message'))
        var.put('previousStrict', var.get('strict'))
        var.put('body', var.get('parseFunctionSourceElements')())
        if (var.get('strict') and var.get('firstRestricted')):
            var.get('throwUnexpectedToken')(var.get('firstRestricted'), var.get('message'))
        if (var.get('strict') and var.get('stricted')):
            var.get('tolerateUnexpectedToken')(var.get('stricted'), var.get('message'))
        var.put('strict', var.get('previousStrict'))
        var.get('state').put('allowYield', var.get('previousAllowYield'))
        return var.get('node').callprop('finishFunctionDeclaration', var.get('id'), var.get('params'), var.get('defaults'), var.get('body'), var.get('isGenerator'))
    PyJsHoisted_parseFunctionDeclaration_.__name__ = 'parseFunctionDeclaration'
    var.put('parseFunctionDeclaration', PyJsHoisted_parseFunctionDeclaration_)
    @Js
    def PyJsHoisted_parsePostfixExpression_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr', 'token', 'startToken'])
        var.put('startToken', var.get('lookahead'))
        var.put('expr', var.get('inheritCoverGrammar')(var.get('parseLeftHandSideExpressionAllowCall')))
        if (var.get('hasLineTerminator').neg() and PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Punctuator'))):
            if (var.get('match')(Js('++')) or var.get('match')(Js('--'))):
                if ((var.get('strict') and PyJsStrictEq(var.get('expr').get('type'),var.get('Syntax').get('Identifier'))) and var.get('isRestrictedWord')(var.get('expr').get('name'))):
                    var.get('tolerateError')(var.get('Messages').get('StrictLHSPostfix'))
                if var.get('isAssignmentTarget').neg():
                    var.get('tolerateError')(var.get('Messages').get('InvalidLHSInAssignment'))
                var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
                var.put('token', var.get('lex')())
                var.put('expr', var.get('WrappingNode').create(var.get('startToken')).callprop('finishPostfixExpression', var.get('token').get('value'), var.get('expr')))
        return var.get('expr')
    PyJsHoisted_parsePostfixExpression_.__name__ = 'parsePostfixExpression'
    var.put('parsePostfixExpression', PyJsHoisted_parsePostfixExpression_)
    @Js
    def PyJsHoisted_parseNonComputedMember_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('expect')(Js('.'))
        return var.get('parseNonComputedProperty')()
    PyJsHoisted_parseNonComputedMember_.__name__ = 'parseNonComputedMember'
    var.put('parseNonComputedMember', PyJsHoisted_parseNonComputedMember_)
    @Js
    def PyJsHoisted_parseExportDefaultDeclaration_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'expression', 'declaration'])
        var.put('declaration', var.get("null"))
        var.put('expression', var.get("null"))
        var.get('expectKeyword')(Js('default'))
        if var.get('matchKeyword')(Js('function')):
            var.put('declaration', var.get('parseFunctionDeclaration')(var.get('Node').create(), var.get('true')))
            return var.get('node').callprop('finishExportDefaultDeclaration', var.get('declaration'))
        if var.get('matchKeyword')(Js('class')):
            var.put('declaration', var.get('parseClassDeclaration')(var.get('true')))
            return var.get('node').callprop('finishExportDefaultDeclaration', var.get('declaration'))
        if var.get('matchContextualKeyword')(Js('from')):
            var.get('throwError')(var.get('Messages').get('UnexpectedToken'), var.get('lookahead').get('value'))
        if var.get('match')(Js('{')):
            var.put('expression', var.get('parseObjectInitializer')())
        else:
            if var.get('match')(Js('[')):
                var.put('expression', var.get('parseArrayInitializer')())
            else:
                var.put('expression', var.get('parseAssignmentExpression')())
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishExportDefaultDeclaration', var.get('expression'))
    PyJsHoisted_parseExportDefaultDeclaration_.__name__ = 'parseExportDefaultDeclaration'
    var.put('parseExportDefaultDeclaration', PyJsHoisted_parseExportDefaultDeclaration_)
    @Js
    def PyJsHoisted_parseRestElement_(params, this, arguments, var=var):
        var = Scope({'this':this, 'params':params, 'arguments':arguments}, var)
        var.registers(['node', 'params', 'param'])
        var.put('node', var.get('Node').create())
        var.get('lex')()
        if var.get('match')(Js('{')):
            var.get('throwError')(var.get('Messages').get('ObjectPatternAsRestParameter'))
        var.get('params').callprop('push', var.get('lookahead'))
        var.put('param', var.get('parseVariableIdentifier')())
        if var.get('match')(Js('=')):
            var.get('throwError')(var.get('Messages').get('DefaultRestParameter'))
        if var.get('match')(Js(')')).neg():
            var.get('throwError')(var.get('Messages').get('ParameterAfterRestParameter'))
        return var.get('node').callprop('finishRestElement', var.get('param'))
    PyJsHoisted_parseRestElement_.__name__ = 'parseRestElement'
    var.put('parseRestElement', PyJsHoisted_parseRestElement_)
    @Js
    def PyJsHoisted_parseScriptBody_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'firstRestricted', 'token', 'directive', 'statement'])
        var.put('body', Js([]))
        while (var.get('startIndex')<var.get('length')):
            var.put('token', var.get('lookahead'))
            if PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('StringLiteral')):
                break
            var.put('statement', var.get('parseStatementListItem')())
            var.get('body').callprop('push', var.get('statement'))
            if PyJsStrictNeq(var.get('statement').get('expression').get('type'),var.get('Syntax').get('Literal')):
                break
            var.put('directive', var.get('source').callprop('slice', (var.get('token').get('start')+Js(1.0)), (var.get('token').get('end')-Js(1.0))))
            if PyJsStrictEq(var.get('directive'),Js('use strict')):
                var.put('strict', var.get('true'))
                if var.get('firstRestricted'):
                    var.get('tolerateUnexpectedToken')(var.get('firstRestricted'), var.get('Messages').get('StrictOctalLiteral'))
            else:
                if (var.get('firstRestricted').neg() and var.get('token').get('octal')):
                    var.put('firstRestricted', var.get('token'))
        while (var.get('startIndex')<var.get('length')):
            var.put('statement', var.get('parseStatementListItem')())
            if PyJsStrictEq(var.get('statement',throw=False).typeof(),Js('undefined')):
                break
            var.get('body').callprop('push', var.get('statement'))
        return var.get('body')
    PyJsHoisted_parseScriptBody_.__name__ = 'parseScriptBody'
    var.put('parseScriptBody', PyJsHoisted_parseScriptBody_)
    @Js
    def PyJsHoisted_parseBindingList_(kind, options, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'options':options, 'arguments':arguments}, var)
        var.registers(['kind', 'list', 'options'])
        var.put('list', Js([]))
        while 1:
            var.get('list').callprop('push', var.get('parseLexicalBinding')(var.get('kind'), var.get('options')))
            if var.get('match')(Js(',')).neg():
                break
            var.get('lex')()
            if not (var.get('startIndex')<var.get('length')):
                break
        return var.get('list')
    PyJsHoisted_parseBindingList_.__name__ = 'parseBindingList'
    var.put('parseBindingList', PyJsHoisted_parseBindingList_)
    @Js
    def PyJsHoisted_scanTemplate_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['terminated', 'rawOffset', 'ch', 'start', 'unescaped', 'head', 'cooked', 'tail', 'restore'])
        var.put('cooked', Js(''))
        var.put('terminated', Js(False))
        var.put('tail', Js(False))
        var.put('start', var.get('index'))
        var.put('head', PyJsStrictEq(var.get('source').get(var.get('index')),Js('`')))
        var.put('rawOffset', Js(2.0))
        var.put('index',Js(var.get('index').to_number())+Js(1))
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if PyJsStrictEq(var.get('ch'),Js('`')):
                var.put('rawOffset', Js(1.0))
                var.put('tail', var.get('true'))
                var.put('terminated', var.get('true'))
                break
            else:
                if PyJsStrictEq(var.get('ch'),Js('$')):
                    if PyJsStrictEq(var.get('source').get(var.get('index')),Js('{')):
                        var.get('state').get('curlyStack').callprop('push', Js('${'))
                        var.put('index',Js(var.get('index').to_number())+Js(1))
                        var.put('terminated', var.get('true'))
                        break
                    var.put('cooked', var.get('ch'), '+')
                else:
                    if PyJsStrictEq(var.get('ch'),Js('\\')):
                        var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                        if var.get('isLineTerminator')(var.get('ch').callprop('charCodeAt', Js(0.0))).neg():
                            while 1:
                                SWITCHED = False
                                CONDITION = (var.get('ch'))
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                                    SWITCHED = True
                                    var.put('cooked', Js('\n'), '+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                                    SWITCHED = True
                                    var.put('cooked', Js('\r'), '+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('t')):
                                    SWITCHED = True
                                    var.put('cooked', Js('\t'), '+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('u')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('x')):
                                    SWITCHED = True
                                    if PyJsStrictEq(var.get('source').get(var.get('index')),Js('{')):
                                        var.put('index',Js(var.get('index').to_number())+Js(1))
                                        var.put('cooked', var.get('scanUnicodeCodePointEscape')(), '+')
                                    else:
                                        var.put('restore', var.get('index'))
                                        var.put('unescaped', var.get('scanHexEscape')(var.get('ch')))
                                        if var.get('unescaped'):
                                            var.put('cooked', var.get('unescaped'), '+')
                                        else:
                                            var.put('index', var.get('restore'))
                                            var.put('cooked', var.get('ch'), '+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                                    SWITCHED = True
                                    var.put('cooked', Js('\x08'), '+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                                    SWITCHED = True
                                    var.put('cooked', Js('\x0c'), '+')
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('v')):
                                    SWITCHED = True
                                    var.put('cooked', Js('\x0b'), '+')
                                    break
                                if True:
                                    SWITCHED = True
                                    if PyJsStrictEq(var.get('ch'),Js('0')):
                                        if var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', var.get('index'))):
                                            var.get('throwError')(var.get('Messages').get('TemplateOctalLiteral'))
                                        var.put('cooked', Js('\x00'), '+')
                                    else:
                                        if var.get('isOctalDigit')(var.get('ch')):
                                            var.get('throwError')(var.get('Messages').get('TemplateOctalLiteral'))
                                        else:
                                            var.put('cooked', var.get('ch'), '+')
                                    break
                                SWITCHED = True
                                break
                        else:
                            var.put('lineNumber',Js(var.get('lineNumber').to_number())+Js(1))
                            if (PyJsStrictEq(var.get('ch'),Js('\r')) and PyJsStrictEq(var.get('source').get(var.get('index')),Js('\n'))):
                                var.put('index',Js(var.get('index').to_number())+Js(1))
                            var.put('lineStart', var.get('index'))
                    else:
                        if var.get('isLineTerminator')(var.get('ch').callprop('charCodeAt', Js(0.0))):
                            var.put('lineNumber',Js(var.get('lineNumber').to_number())+Js(1))
                            if (PyJsStrictEq(var.get('ch'),Js('\r')) and PyJsStrictEq(var.get('source').get(var.get('index')),Js('\n'))):
                                var.put('index',Js(var.get('index').to_number())+Js(1))
                            var.put('lineStart', var.get('index'))
                            var.put('cooked', Js('\n'), '+')
                        else:
                            var.put('cooked', var.get('ch'), '+')
        if var.get('terminated').neg():
            var.get('throwUnexpectedToken')()
        if var.get('head').neg():
            var.get('state').get('curlyStack').callprop('pop')
        PyJs_Object_30_ = Js({'cooked':var.get('cooked'),'raw':var.get('source').callprop('slice', (var.get('start')+Js(1.0)), (var.get('index')-var.get('rawOffset')))})
        PyJs_Object_29_ = Js({'type':var.get('Token').get('Template'),'value':PyJs_Object_30_,'head':var.get('head'),'tail':var.get('tail'),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_29_
    PyJsHoisted_scanTemplate_.__name__ = 'scanTemplate'
    var.put('scanTemplate', PyJsHoisted_scanTemplate_)
    @Js
    def PyJsHoisted_parseLexicalDeclaration_(options, this, arguments, var=var):
        var = Scope({'this':this, 'options':options, 'arguments':arguments}, var)
        var.registers(['node', 'kind', 'declarations', 'options'])
        var.put('node', var.get('Node').create())
        var.put('kind', var.get('lex')().get('value'))
        var.get('assert')((PyJsStrictEq(var.get('kind'),Js('let')) or PyJsStrictEq(var.get('kind'),Js('const'))), Js('Lexical declaration must be either let or const'))
        var.put('declarations', var.get('parseBindingList')(var.get('kind'), var.get('options')))
        var.get('consumeSemicolon')()
        return var.get('node').callprop('finishLexicalDeclaration', var.get('declarations'), var.get('kind'))
    PyJsHoisted_parseLexicalDeclaration_.__name__ = 'parseLexicalDeclaration'
    var.put('parseLexicalDeclaration', PyJsHoisted_parseLexicalDeclaration_)
    @Js
    def PyJsHoisted_checkPatternParam_(options, param, this, arguments, var=var):
        var = Scope({'this':this, 'options':options, 'param':param, 'arguments':arguments}, var)
        var.registers(['i', 'options', 'param'])
        pass
        while 1:
            SWITCHED = False
            CONDITION = (var.get('param').get('type'))
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('Identifier')):
                SWITCHED = True
                var.get('validateParam')(var.get('options'), var.get('param'), var.get('param').get('name'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('RestElement')):
                SWITCHED = True
                var.get('checkPatternParam')(var.get('options'), var.get('param').get('argument'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('AssignmentPattern')):
                SWITCHED = True
                var.get('checkPatternParam')(var.get('options'), var.get('param').get('left'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('ArrayPattern')):
                SWITCHED = True
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('param').get('elements').get('length')):
                    try:
                        if PyJsStrictNeq(var.get('param').get('elements').get(var.get('i')),var.get("null")):
                            var.get('checkPatternParam')(var.get('options'), var.get('param').get('elements').get(var.get('i')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, var.get('Syntax').get('YieldExpression')):
                SWITCHED = True
                break
            if True:
                SWITCHED = True
                var.get('assert')(PyJsStrictEq(var.get('param').get('type'),var.get('Syntax').get('ObjectPattern')), Js('Invalid type'))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('param').get('properties').get('length')):
                    try:
                        var.get('checkPatternParam')(var.get('options'), var.get('param').get('properties').get(var.get('i')).get('value'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                break
            SWITCHED = True
            break
    PyJsHoisted_checkPatternParam_.__name__ = 'checkPatternParam'
    var.put('checkPatternParam', PyJsHoisted_checkPatternParam_)
    @Js
    def PyJsHoisted_parsePropertyFunction_(node, paramInfo, isGenerator, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'paramInfo':paramInfo, 'isGenerator':isGenerator, 'arguments':arguments}, var)
        var.registers(['body', 'node', 'previousStrict', 'isGenerator', 'paramInfo'])
        pass
        var.put('isAssignmentTarget', var.put('isBindingElement', Js(False)))
        var.put('previousStrict', var.get('strict'))
        var.put('body', var.get('isolateCoverGrammar')(var.get('parseFunctionSourceElements')))
        if (var.get('strict') and var.get('paramInfo').get('firstRestricted')):
            var.get('tolerateUnexpectedToken')(var.get('paramInfo').get('firstRestricted'), var.get('paramInfo').get('message'))
        if (var.get('strict') and var.get('paramInfo').get('stricted')):
            var.get('tolerateUnexpectedToken')(var.get('paramInfo').get('stricted'), var.get('paramInfo').get('message'))
        var.put('strict', var.get('previousStrict'))
        return var.get('node').callprop('finishFunctionExpression', var.get("null"), var.get('paramInfo').get('params'), var.get('paramInfo').get('defaults'), var.get('body'), var.get('isGenerator'))
    PyJsHoisted_parsePropertyFunction_.__name__ = 'parsePropertyFunction'
    var.put('parsePropertyFunction', PyJsHoisted_parsePropertyFunction_)
    @Js
    def PyJsHoisted_scanPunctuator_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['token', 'str'])
        pass
        PyJs_Object_21_ = Js({'type':var.get('Token').get('Punctuator'),'value':Js(''),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('index'),'end':var.get('index')})
        var.put('token', PyJs_Object_21_)
        var.put('str', var.get('source').get(var.get('index')))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('str'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js('(')):
                SWITCHED = True
                if var.get('extra').get('tokenize'):
                    var.get('extra').put('openParenToken', var.get('extra').get('tokens').get('length'))
                var.put('index',Js(var.get('index').to_number())+Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('{')):
                SWITCHED = True
                if var.get('extra').get('tokenize'):
                    var.get('extra').put('openCurlyToken', var.get('extra').get('tokens').get('length'))
                var.get('state').get('curlyStack').callprop('push', Js('{'))
                var.put('index',Js(var.get('index').to_number())+Js(1))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('.')):
                SWITCHED = True
                var.put('index',Js(var.get('index').to_number())+Js(1))
                if (PyJsStrictEq(var.get('source').get(var.get('index')),Js('.')) and PyJsStrictEq(var.get('source').get((var.get('index')+Js(1.0))),Js('.'))):
                    var.put('index', Js(2.0), '+')
                    var.put('str', Js('...'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js('}')):
                SWITCHED = True
                var.put('index',Js(var.get('index').to_number())+Js(1))
                var.get('state').get('curlyStack').callprop('pop')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(')')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(';')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(',')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('[')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(']')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js(':')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('?')):
                SWITCHED = True
                pass
            if SWITCHED or PyJsStrictEq(CONDITION, Js('~')):
                SWITCHED = True
                var.put('index',Js(var.get('index').to_number())+Js(1))
                break
            if True:
                SWITCHED = True
                var.put('str', var.get('source').callprop('substr', var.get('index'), Js(4.0)))
                if PyJsStrictEq(var.get('str'),Js('>>>=')):
                    var.put('index', Js(4.0), '+')
                else:
                    var.put('str', var.get('str').callprop('substr', Js(0.0), Js(3.0)))
                    if ((((PyJsStrictEq(var.get('str'),Js('===')) or PyJsStrictEq(var.get('str'),Js('!=='))) or PyJsStrictEq(var.get('str'),Js('>>>'))) or PyJsStrictEq(var.get('str'),Js('<<='))) or PyJsStrictEq(var.get('str'),Js('>>='))):
                        var.put('index', Js(3.0), '+')
                    else:
                        var.put('str', var.get('str').callprop('substr', Js(0.0), Js(2.0)))
                        def PyJs_LONG_23_(var=var):
                            def PyJs_LONG_22_(var=var):
                                return (((((((((PyJsStrictEq(var.get('str'),Js('&&')) or PyJsStrictEq(var.get('str'),Js('||'))) or PyJsStrictEq(var.get('str'),Js('=='))) or PyJsStrictEq(var.get('str'),Js('!='))) or PyJsStrictEq(var.get('str'),Js('+='))) or PyJsStrictEq(var.get('str'),Js('-='))) or PyJsStrictEq(var.get('str'),Js('*='))) or PyJsStrictEq(var.get('str'),Js('/='))) or PyJsStrictEq(var.get('str'),Js('++'))) or PyJsStrictEq(var.get('str'),Js('--')))
                            return (((((((((PyJs_LONG_22_() or PyJsStrictEq(var.get('str'),Js('<<'))) or PyJsStrictEq(var.get('str'),Js('>>'))) or PyJsStrictEq(var.get('str'),Js('&='))) or PyJsStrictEq(var.get('str'),Js('|='))) or PyJsStrictEq(var.get('str'),Js('^='))) or PyJsStrictEq(var.get('str'),Js('%='))) or PyJsStrictEq(var.get('str'),Js('<='))) or PyJsStrictEq(var.get('str'),Js('>='))) or PyJsStrictEq(var.get('str'),Js('=>')))
                        if PyJs_LONG_23_():
                            var.put('index', Js(2.0), '+')
                        else:
                            var.put('str', var.get('source').get(var.get('index')))
                            if (Js('<>=!+-*%&|^/').callprop('indexOf', var.get('str'))>=Js(0.0)):
                                var.put('index',Js(var.get('index').to_number())+Js(1))
            SWITCHED = True
            break
        if PyJsStrictEq(var.get('index'),var.get('token').get('start')):
            var.get('throwUnexpectedToken')()
        var.get('token').put('end', var.get('index'))
        var.get('token').put('value', var.get('str'))
        return var.get('token')
    PyJsHoisted_scanPunctuator_.__name__ = 'scanPunctuator'
    var.put('scanPunctuator', PyJsHoisted_scanPunctuator_)
    @Js
    def PyJsHoisted_parseArrowFunctionExpression_(options, node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'options':options, 'arguments':arguments}, var)
        var.registers(['body', 'node', 'previousStrict', 'options', 'previousAllowYield'])
        pass
        if var.get('hasLineTerminator'):
            var.get('tolerateUnexpectedToken')(var.get('lookahead'))
        var.get('expect')(Js('=>'))
        var.put('previousStrict', var.get('strict'))
        var.put('previousAllowYield', var.get('state').get('allowYield'))
        var.get('state').put('allowYield', var.get('true'))
        var.put('body', var.get('parseConciseBody')())
        if (var.get('strict') and var.get('options').get('firstRestricted')):
            var.get('throwUnexpectedToken')(var.get('options').get('firstRestricted'), var.get('options').get('message'))
        if (var.get('strict') and var.get('options').get('stricted')):
            var.get('tolerateUnexpectedToken')(var.get('options').get('stricted'), var.get('options').get('message'))
        var.put('strict', var.get('previousStrict'))
        var.get('state').put('allowYield', var.get('previousAllowYield'))
        return var.get('node').callprop('finishArrowFunctionExpression', var.get('options').get('params'), var.get('options').get('defaults'), var.get('body'), PyJsStrictNeq(var.get('body').get('type'),var.get('Syntax').get('BlockStatement')))
    PyJsHoisted_parseArrowFunctionExpression_.__name__ = 'parseArrowFunctionExpression'
    var.put('parseArrowFunctionExpression', PyJsHoisted_parseArrowFunctionExpression_)
    @Js
    def PyJsHoisted_throwError_(messageFormat, this, arguments, var=var):
        var = Scope({'this':this, 'messageFormat':messageFormat, 'arguments':arguments}, var)
        var.registers(['msg', 'args', 'messageFormat'])
        pass
        var.put('args', var.get('Array').get('prototype').get('slice').callprop('call', var.get('arguments'), Js(1.0)))
        @Js
        def PyJs_anonymous_118_(whole, idx, this, arguments, var=var):
            var = Scope({'this':this, 'whole':whole, 'arguments':arguments, 'idx':idx}, var)
            var.registers(['whole', 'idx'])
            var.get('assert')((var.get('idx')<var.get('args').get('length')), Js('Message reference must be in range'))
            return var.get('args').get(var.get('idx'))
        PyJs_anonymous_118_._set_name('anonymous')
        var.put('msg', var.get('messageFormat').callprop('replace', JsRegExp('/%(\\d)/g'), PyJs_anonymous_118_))
        PyJsTempException = JsToPyException(var.get('createError')(var.get('lastLineNumber'), var.get('lastIndex'), var.get('msg')))
        raise PyJsTempException
    PyJsHoisted_throwError_.__name__ = 'throwError'
    var.put('throwError', PyJsHoisted_throwError_)
    @Js
    def PyJsHoisted_scanUnicodeCodePointEscape_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['code', 'ch'])
        pass
        var.put('ch', var.get('source').get(var.get('index')))
        var.put('code', Js(0.0))
        if PyJsStrictEq(var.get('ch'),Js('}')):
            var.get('throwUnexpectedToken')()
        while (var.get('index')<var.get('length')):
            var.put('ch', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if var.get('isHexDigit')(var.get('ch')).neg():
                break
            var.put('code', ((var.get('code')*Js(16.0))+Js('0123456789abcdef').callprop('indexOf', var.get('ch').callprop('toLowerCase'))))
        if ((var.get('code')>Js(1114111)) or PyJsStrictNeq(var.get('ch'),Js('}'))):
            var.get('throwUnexpectedToken')()
        return var.get('fromCodePoint')(var.get('code'))
    PyJsHoisted_scanUnicodeCodePointEscape_.__name__ = 'scanUnicodeCodePointEscape'
    var.put('scanUnicodeCodePointEscape', PyJsHoisted_scanUnicodeCodePointEscape_)
    @Js
    def PyJsHoisted_scanOctalLiteral_(prefix, start, this, arguments, var=var):
        var = Scope({'this':this, 'start':start, 'prefix':prefix, 'arguments':arguments}, var)
        var.registers(['octal', 'start', 'prefix', 'number'])
        pass
        if var.get('isOctalDigit')(var.get('prefix')):
            var.put('octal', var.get('true'))
            var.put('number', (Js('0')+var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        else:
            var.put('octal', Js(False))
            var.put('index',Js(var.get('index').to_number())+Js(1))
            var.put('number', Js(''))
        while (var.get('index')<var.get('length')):
            if var.get('isOctalDigit')(var.get('source').get(var.get('index'))).neg():
                break
            var.put('number', var.get('source').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), '+')
        if (var.get('octal').neg() and PyJsStrictEq(var.get('number').get('length'),Js(0.0))):
            var.get('throwUnexpectedToken')()
        if (var.get('isIdentifierStart')(var.get('source').callprop('charCodeAt', var.get('index'))) or var.get('isDecimalDigit')(var.get('source').callprop('charCodeAt', var.get('index')))):
            var.get('throwUnexpectedToken')()
        PyJs_Object_26_ = Js({'type':var.get('Token').get('NumericLiteral'),'value':var.get('parseInt')(var.get('number'), Js(8.0)),'octal':var.get('octal'),'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_26_
    PyJsHoisted_scanOctalLiteral_.__name__ = 'scanOctalLiteral'
    var.put('scanOctalLiteral', PyJsHoisted_scanOctalLiteral_)
    @Js
    def PyJsHoisted_scanRegExp_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'start', 'flags', 'value'])
        pass
        var.put('scanning', var.get('true'))
        var.put('lookahead', var.get("null"))
        var.get('skipComment')()
        var.put('start', var.get('index'))
        var.put('body', var.get('scanRegExpBody')())
        var.put('flags', var.get('scanRegExpFlags')())
        var.put('value', var.get('testRegExp')(var.get('body').get('value'), var.get('flags').get('value')))
        var.put('scanning', Js(False))
        if var.get('extra').get('tokenize'):
            PyJs_Object_35_ = Js({'pattern':var.get('body').get('value'),'flags':var.get('flags').get('value')})
            PyJs_Object_34_ = Js({'type':var.get('Token').get('RegularExpression'),'value':var.get('value'),'regex':PyJs_Object_35_,'lineNumber':var.get('lineNumber'),'lineStart':var.get('lineStart'),'start':var.get('start'),'end':var.get('index')})
            return PyJs_Object_34_
        PyJs_Object_37_ = Js({'pattern':var.get('body').get('value'),'flags':var.get('flags').get('value')})
        PyJs_Object_36_ = Js({'literal':(var.get('body').get('literal')+var.get('flags').get('literal')),'value':var.get('value'),'regex':PyJs_Object_37_,'start':var.get('start'),'end':var.get('index')})
        return PyJs_Object_36_
    PyJsHoisted_scanRegExp_.__name__ = 'scanRegExp'
    var.put('scanRegExp', PyJsHoisted_scanRegExp_)
    @Js
    def PyJsHoisted_parseImportDefaultSpecifier_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'local'])
        var.put('node', var.get('Node').create())
        var.put('local', var.get('parseNonComputedProperty')())
        return var.get('node').callprop('finishImportDefaultSpecifier', var.get('local'))
    PyJsHoisted_parseImportDefaultSpecifier_.__name__ = 'parseImportDefaultSpecifier'
    var.put('parseImportDefaultSpecifier', PyJsHoisted_parseImportDefaultSpecifier_)
    @Js
    def PyJsHoisted_parsePattern_(params, kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'params':params, 'arguments':arguments}, var)
        var.registers(['kind', 'params'])
        if var.get('match')(Js('[')):
            return var.get('parseArrayPattern')(var.get('params'), var.get('kind'))
        else:
            if var.get('match')(Js('{')):
                return var.get('parseObjectPattern')(var.get('params'), var.get('kind'))
        var.get('params').callprop('push', var.get('lookahead'))
        return var.get('parseVariableIdentifier')(var.get('kind'))
    PyJsHoisted_parsePattern_.__name__ = 'parsePattern'
    var.put('parsePattern', PyJsHoisted_parsePattern_)
    @Js
    def PyJsHoisted_parseVariableIdentifier_(kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'arguments':arguments}, var)
        var.registers(['node', 'token', 'kind'])
        var.put('node', var.get('Node').create())
        var.put('token', var.get('lex')())
        if (PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Keyword')) and PyJsStrictEq(var.get('token').get('value'),Js('yield'))):
            if var.get('strict'):
                var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictReservedWord'))
            if var.get('state').get('allowYield').neg():
                var.get('throwUnexpectedToken')(var.get('token'))
        else:
            if PyJsStrictNeq(var.get('token').get('type'),var.get('Token').get('Identifier')):
                if ((var.get('strict') and PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Keyword'))) and var.get('isStrictModeReservedWord')(var.get('token').get('value'))):
                    var.get('tolerateUnexpectedToken')(var.get('token'), var.get('Messages').get('StrictReservedWord'))
                else:
                    if ((var.get('strict') or PyJsStrictNeq(var.get('token').get('value'),Js('let'))) or PyJsStrictNeq(var.get('kind'),Js('var'))):
                        var.get('throwUnexpectedToken')(var.get('token'))
            else:
                if ((PyJsStrictEq(var.get('state').get('sourceType'),Js('module')) and PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Identifier'))) and PyJsStrictEq(var.get('token').get('value'),Js('await'))):
                    var.get('tolerateUnexpectedToken')(var.get('token'))
        return var.get('node').callprop('finishIdentifier', var.get('token').get('value'))
    PyJsHoisted_parseVariableIdentifier_.__name__ = 'parseVariableIdentifier'
    var.put('parseVariableIdentifier', PyJsHoisted_parseVariableIdentifier_)
    @Js
    def PyJsHoisted_parseForStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'oldInIteration', 'kind', 'right', 'node', 'previousAllowIn', 'declarations', 'update', 'init', 'initSeq', 'test', 'forIn', 'initStartToken', 'left'])
        var.put('previousAllowIn', var.get('state').get('allowIn'))
        var.put('init', var.put('test', var.put('update', var.get("null"))))
        var.put('forIn', var.get('true'))
        var.get('expectKeyword')(Js('for'))
        var.get('expect')(Js('('))
        if var.get('match')(Js(';')):
            var.get('lex')()
        else:
            if var.get('matchKeyword')(Js('var')):
                var.put('init', var.get('Node').create())
                var.get('lex')()
                var.get('state').put('allowIn', Js(False))
                PyJs_Object_141_ = Js({'inFor':var.get('true')})
                var.put('declarations', var.get('parseVariableDeclarationList')(PyJs_Object_141_))
                var.get('state').put('allowIn', var.get('previousAllowIn'))
                if (PyJsStrictEq(var.get('declarations').get('length'),Js(1.0)) and var.get('matchKeyword')(Js('in'))):
                    var.put('init', var.get('init').callprop('finishVariableDeclaration', var.get('declarations')))
                    var.get('lex')()
                    var.put('left', var.get('init'))
                    var.put('right', var.get('parseExpression')())
                    var.put('init', var.get("null"))
                else:
                    if ((PyJsStrictEq(var.get('declarations').get('length'),Js(1.0)) and PyJsStrictEq(var.get('declarations').get('0').get('init'),var.get("null"))) and var.get('matchContextualKeyword')(Js('of'))):
                        var.put('init', var.get('init').callprop('finishVariableDeclaration', var.get('declarations')))
                        var.get('lex')()
                        var.put('left', var.get('init'))
                        var.put('right', var.get('parseAssignmentExpression')())
                        var.put('init', var.get("null"))
                        var.put('forIn', Js(False))
                    else:
                        var.put('init', var.get('init').callprop('finishVariableDeclaration', var.get('declarations')))
                        var.get('expect')(Js(';'))
            else:
                if (var.get('matchKeyword')(Js('const')) or var.get('matchKeyword')(Js('let'))):
                    var.put('init', var.get('Node').create())
                    var.put('kind', var.get('lex')().get('value'))
                    var.get('state').put('allowIn', Js(False))
                    PyJs_Object_142_ = Js({'inFor':var.get('true')})
                    var.put('declarations', var.get('parseBindingList')(var.get('kind'), PyJs_Object_142_))
                    var.get('state').put('allowIn', var.get('previousAllowIn'))
                    if ((PyJsStrictEq(var.get('declarations').get('length'),Js(1.0)) and PyJsStrictEq(var.get('declarations').get('0').get('init'),var.get("null"))) and var.get('matchKeyword')(Js('in'))):
                        var.put('init', var.get('init').callprop('finishLexicalDeclaration', var.get('declarations'), var.get('kind')))
                        var.get('lex')()
                        var.put('left', var.get('init'))
                        var.put('right', var.get('parseExpression')())
                        var.put('init', var.get("null"))
                    else:
                        if ((PyJsStrictEq(var.get('declarations').get('length'),Js(1.0)) and PyJsStrictEq(var.get('declarations').get('0').get('init'),var.get("null"))) and var.get('matchContextualKeyword')(Js('of'))):
                            var.put('init', var.get('init').callprop('finishLexicalDeclaration', var.get('declarations'), var.get('kind')))
                            var.get('lex')()
                            var.put('left', var.get('init'))
                            var.put('right', var.get('parseAssignmentExpression')())
                            var.put('init', var.get("null"))
                            var.put('forIn', Js(False))
                        else:
                            var.get('consumeSemicolon')()
                            var.put('init', var.get('init').callprop('finishLexicalDeclaration', var.get('declarations'), var.get('kind')))
                else:
                    var.put('initStartToken', var.get('lookahead'))
                    var.get('state').put('allowIn', Js(False))
                    var.put('init', var.get('inheritCoverGrammar')(var.get('parseAssignmentExpression')))
                    var.get('state').put('allowIn', var.get('previousAllowIn'))
                    if var.get('matchKeyword')(Js('in')):
                        if var.get('isAssignmentTarget').neg():
                            var.get('tolerateError')(var.get('Messages').get('InvalidLHSInForIn'))
                        var.get('lex')()
                        var.get('reinterpretExpressionAsPattern')(var.get('init'))
                        var.put('left', var.get('init'))
                        var.put('right', var.get('parseExpression')())
                        var.put('init', var.get("null"))
                    else:
                        if var.get('matchContextualKeyword')(Js('of')):
                            if var.get('isAssignmentTarget').neg():
                                var.get('tolerateError')(var.get('Messages').get('InvalidLHSInForLoop'))
                            var.get('lex')()
                            var.get('reinterpretExpressionAsPattern')(var.get('init'))
                            var.put('left', var.get('init'))
                            var.put('right', var.get('parseAssignmentExpression')())
                            var.put('init', var.get("null"))
                            var.put('forIn', Js(False))
                        else:
                            if var.get('match')(Js(',')):
                                var.put('initSeq', Js([var.get('init')]))
                                while var.get('match')(Js(',')):
                                    var.get('lex')()
                                    var.get('initSeq').callprop('push', var.get('isolateCoverGrammar')(var.get('parseAssignmentExpression')))
                                var.put('init', var.get('WrappingNode').create(var.get('initStartToken')).callprop('finishSequenceExpression', var.get('initSeq')))
                            var.get('expect')(Js(';'))
        if PyJsStrictEq(var.get('left',throw=False).typeof(),Js('undefined')):
            if var.get('match')(Js(';')).neg():
                var.put('test', var.get('parseExpression')())
            var.get('expect')(Js(';'))
            if var.get('match')(Js(')')).neg():
                var.put('update', var.get('parseExpression')())
        var.get('expect')(Js(')'))
        var.put('oldInIteration', var.get('state').get('inIteration'))
        var.get('state').put('inIteration', var.get('true'))
        var.put('body', var.get('isolateCoverGrammar')(var.get('parseStatement')))
        var.get('state').put('inIteration', var.get('oldInIteration'))
        def PyJs_LONG_143_(var=var):
            return (var.get('node').callprop('finishForStatement', var.get('init'), var.get('test'), var.get('update'), var.get('body')) if PyJsStrictEq(var.get('left',throw=False).typeof(),Js('undefined')) else (var.get('node').callprop('finishForInStatement', var.get('left'), var.get('right'), var.get('body')) if var.get('forIn') else var.get('node').callprop('finishForOfStatement', var.get('left'), var.get('right'), var.get('body'))))
        return PyJs_LONG_143_()
    PyJsHoisted_parseForStatement_.__name__ = 'parseForStatement'
    var.put('parseForStatement', PyJsHoisted_parseForStatement_)
    @Js
    def PyJsHoisted_isIdentifierPart_(ch, this, arguments, var=var):
        var = Scope({'this':this, 'ch':ch, 'arguments':arguments}, var)
        var.registers(['ch'])
        def PyJs_LONG_10_(var=var):
            return ((((((PyJsStrictEq(var.get('ch'),Js(36)) or PyJsStrictEq(var.get('ch'),Js(95))) or ((var.get('ch')>=Js(65)) and (var.get('ch')<=Js(90)))) or ((var.get('ch')>=Js(97)) and (var.get('ch')<=Js(122)))) or ((var.get('ch')>=Js(48)) and (var.get('ch')<=Js(57)))) or PyJsStrictEq(var.get('ch'),Js(92))) or ((var.get('ch')>=Js(128)) and var.get('Regex').get('NonAsciiIdentifierPart').callprop('test', var.get('fromCodePoint')(var.get('ch')))))
        return PyJs_LONG_10_()
    PyJsHoisted_isIdentifierPart_.__name__ = 'isIdentifierPart'
    var.put('isIdentifierPart', PyJsHoisted_isIdentifierPart_)
    @Js
    def PyJsHoisted_matchKeyword_(keyword, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'keyword':keyword}, var)
        var.registers(['keyword'])
        return (PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Keyword')) and PyJsStrictEq(var.get('lookahead').get('value'),var.get('keyword')))
    PyJsHoisted_matchKeyword_.__name__ = 'matchKeyword'
    var.put('matchKeyword', PyJsHoisted_matchKeyword_)
    @Js
    def PyJsHoisted_parseTryStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'finalizer', 'handler', 'block'])
        var.put('handler', var.get("null"))
        var.put('finalizer', var.get("null"))
        var.get('expectKeyword')(Js('try'))
        var.put('block', var.get('parseBlock')())
        if var.get('matchKeyword')(Js('catch')):
            var.put('handler', var.get('parseCatchClause')())
        if var.get('matchKeyword')(Js('finally')):
            var.get('lex')()
            var.put('finalizer', var.get('parseBlock')())
        if (var.get('handler').neg() and var.get('finalizer').neg()):
            var.get('throwError')(var.get('Messages').get('NoCatchOrFinally'))
        return var.get('node').callprop('finishTryStatement', var.get('block'), var.get('handler'), var.get('finalizer'))
    PyJsHoisted_parseTryStatement_.__name__ = 'parseTryStatement'
    var.put('parseTryStatement', PyJsHoisted_parseTryStatement_)
    @Js
    def PyJsHoisted_parseComputedMember_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['expr'])
        pass
        var.get('expect')(Js('['))
        var.put('expr', var.get('isolateCoverGrammar')(var.get('parseExpression')))
        var.get('expect')(Js(']'))
        return var.get('expr')
    PyJsHoisted_parseComputedMember_.__name__ = 'parseComputedMember'
    var.put('parseComputedMember', PyJsHoisted_parseComputedMember_)
    @Js
    def PyJsHoisted_parseContinueStatement_(node, this, arguments, var=var):
        var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'key', 'label'])
        var.put('label', var.get("null"))
        var.get('expectKeyword')(Js('continue'))
        if PyJsStrictEq(var.get('source').callprop('charCodeAt', var.get('startIndex')),Js(59)):
            var.get('lex')()
            if var.get('state').get('inIteration').neg():
                var.get('throwError')(var.get('Messages').get('IllegalContinue'))
            return var.get('node').callprop('finishContinueStatement', var.get("null"))
        if var.get('hasLineTerminator'):
            if var.get('state').get('inIteration').neg():
                var.get('throwError')(var.get('Messages').get('IllegalContinue'))
            return var.get('node').callprop('finishContinueStatement', var.get("null"))
        if PyJsStrictEq(var.get('lookahead').get('type'),var.get('Token').get('Identifier')):
            var.put('label', var.get('parseVariableIdentifier')())
            var.put('key', (Js('$')+var.get('label').get('name')))
            if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('state').get('labelSet'), var.get('key')).neg():
                var.get('throwError')(var.get('Messages').get('UnknownLabel'), var.get('label').get('name'))
        var.get('consumeSemicolon')()
        if (PyJsStrictEq(var.get('label'),var.get("null")) and var.get('state').get('inIteration').neg()):
            var.get('throwError')(var.get('Messages').get('IllegalContinue'))
        return var.get('node').callprop('finishContinueStatement', var.get('label'))
    PyJsHoisted_parseContinueStatement_.__name__ = 'parseContinueStatement'
    var.put('parseContinueStatement', PyJsHoisted_parseContinueStatement_)
    @Js
    def PyJsHoisted_tryParseMethodDefinition_(token, key, computed, node, this, arguments, var=var):
        var = Scope({'node':node, 'token':token, 'computed':computed, 'key':key, 'this':this, 'arguments':arguments}, var)
        var.registers(['node', 'computed', 'value', 'token', 'params', 'key', 'previousAllowYield', 'methodNode', 'options'])
        var.put('previousAllowYield', var.get('state').get('allowYield'))
        if PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Identifier')):
            if (PyJsStrictEq(var.get('token').get('value'),Js('get')) and var.get('lookaheadPropertyName')()):
                var.put('computed', var.get('match')(Js('[')))
                var.put('key', var.get('parseObjectPropertyKey')())
                var.put('methodNode', var.get('Node').create())
                var.get('expect')(Js('('))
                var.get('expect')(Js(')'))
                var.get('state').put('allowYield', Js(False))
                PyJs_Object_123_ = Js({'params':Js([]),'defaults':Js([]),'stricted':var.get("null"),'firstRestricted':var.get("null"),'message':var.get("null")})
                var.put('value', var.get('parsePropertyFunction')(var.get('methodNode'), PyJs_Object_123_, Js(False)))
                var.get('state').put('allowYield', var.get('previousAllowYield'))
                return var.get('node').callprop('finishProperty', Js('get'), var.get('key'), var.get('computed'), var.get('value'), Js(False), Js(False))
            else:
                if (PyJsStrictEq(var.get('token').get('value'),Js('set')) and var.get('lookaheadPropertyName')()):
                    var.put('computed', var.get('match')(Js('[')))
                    var.put('key', var.get('parseObjectPropertyKey')())
                    var.put('methodNode', var.get('Node').create())
                    var.get('expect')(Js('('))
                    PyJs_Object_125_ = Js({})
                    PyJs_Object_124_ = Js({'params':Js([]),'defaultCount':Js(0.0),'defaults':Js([]),'firstRestricted':var.get("null"),'paramSet':PyJs_Object_125_})
                    var.put('options', PyJs_Object_124_)
                    if var.get('match')(Js(')')):
                        var.get('tolerateUnexpectedToken')(var.get('lookahead'))
                    else:
                        var.get('state').put('allowYield', Js(False))
                        var.get('parseParam')(var.get('options'))
                        var.get('state').put('allowYield', var.get('previousAllowYield'))
                        if PyJsStrictEq(var.get('options').get('defaultCount'),Js(0.0)):
                            var.get('options').put('defaults', Js([]))
                    var.get('expect')(Js(')'))
                    var.get('state').put('allowYield', Js(False))
                    var.put('value', var.get('parsePropertyFunction')(var.get('methodNode'), var.get('options'), Js(False)))
                    var.get('state').put('allowYield', var.get('previousAllowYield'))
                    return var.get('node').callprop('finishProperty', Js('set'), var.get('key'), var.get('computed'), var.get('value'), Js(False), Js(False))
        else:
            if ((PyJsStrictEq(var.get('token').get('type'),var.get('Token').get('Punctuator')) and PyJsStrictEq(var.get('token').get('value'),Js('*'))) and var.get('lookaheadPropertyName')()):
                var.put('computed', var.get('match')(Js('[')))
                var.put('key', var.get('parseObjectPropertyKey')())
                var.put('methodNode', var.get('Node').create())
                var.get('state').put('allowYield', var.get('true'))
                var.put('params', var.get('parseParams')())
                var.get('state').put('allowYield', var.get('previousAllowYield'))
                var.get('state').put('allowYield', Js(False))
                var.put('value', var.get('parsePropertyFunction')(var.get('methodNode'), var.get('params'), var.get('true')))
                var.get('state').put('allowYield', var.get('previousAllowYield'))
                return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), var.get('computed'), var.get('value'), var.get('true'), Js(False))
        if (var.get('key') and var.get('match')(Js('('))):
            var.put('value', var.get('parsePropertyMethodFunction')())
            return var.get('node').callprop('finishProperty', Js('init'), var.get('key'), var.get('computed'), var.get('value'), var.get('true'), Js(False))
        return var.get("null")
    PyJsHoisted_tryParseMethodDefinition_.__name__ = 'tryParseMethodDefinition'
    var.put('tryParseMethodDefinition', PyJsHoisted_tryParseMethodDefinition_)
    @Js
    def PyJsHoisted_parseClassBody_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'isStatic', 'computed', 'token', 'classBody', 'key', 'hasConstructor', 'method'])
        var.put('hasConstructor', Js(False))
        var.put('classBody', var.get('Node').create())
        var.get('expect')(Js('{'))
        var.put('body', Js([]))
        while var.get('match')(Js('}')).neg():
            if var.get('match')(Js(';')):
                var.get('lex')()
            else:
                var.put('method', var.get('Node').create())
                var.put('token', var.get('lookahead'))
                var.put('isStatic', Js(False))
                var.put('computed', var.get('match')(Js('[')))
                if var.get('match')(Js('*')):
                    var.get('lex')()
                else:
                    var.put('key', var.get('parseObjectPropertyKey')())
                    if (PyJsStrictEq(var.get('key').get('name'),Js('static')) and (var.get('lookaheadPropertyName')() or var.get('match')(Js('*')))):
                        var.put('token', var.get('lookahead'))
                        var.put('isStatic', var.get('true'))
                        var.put('computed', var.get('match')(Js('[')))
                        if var.get('match')(Js('*')):
                            var.get('lex')()
                        else:
                            var.put('key', var.get('parseObjectPropertyKey')())
                var.put('method', var.get('tryParseMethodDefinition')(var.get('token'), var.get('key'), var.get('computed'), var.get('method')))
                if var.get('method'):
                    var.get('method').put('static', var.get('isStatic'))
                    if PyJsStrictEq(var.get('method').get('kind'),Js('init')):
                        var.get('method').put('kind', Js('method'))
                    if var.get('isStatic').neg():
                        if (var.get('method').get('computed').neg() and PyJsStrictEq((var.get('method').get('key').get('name') or var.get('method').get('key').get('value').callprop('toString')),Js('constructor'))):
                            if ((PyJsStrictNeq(var.get('method').get('kind'),Js('method')) or var.get('method').get('method').neg()) or var.get('method').get('value').get('generator')):
                                var.get('throwUnexpectedToken')(var.get('token'), var.get('Messages').get('ConstructorSpecialMethod'))
                            if var.get('hasConstructor'):
                                var.get('throwUnexpectedToken')(var.get('token'), var.get('Messages').get('DuplicateConstructor'))
                            else:
                                var.put('hasConstructor', var.get('true'))
                            var.get('method').put('kind', Js('constructor'))
                    else:
                        if (var.get('method').get('computed').neg() and PyJsStrictEq((var.get('method').get('key').get('name') or var.get('method').get('key').get('value').callprop('toString')),Js('prototype'))):
                            var.get('throwUnexpectedToken')(var.get('token'), var.get('Messages').get('StaticPrototype'))
                    var.get('method').put('type', var.get('Syntax').get('MethodDefinition'))
                    var.get('method').delete('method')
                    var.get('method').delete('shorthand')
                    var.get('body').callprop('push', var.get('method'))
                else:
                    var.get('throwUnexpectedToken')(var.get('lookahead'))
        var.get('lex')()
        return var.get('classBody').callprop('finishClassBody', var.get('body'))
    PyJsHoisted_parseClassBody_.__name__ = 'parseClassBody'
    var.put('parseClassBody', PyJsHoisted_parseClassBody_)
    @Js
    def PyJsHoisted_filterTokenLocation_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'entry', 'token', 'tokens'])
        var.put('tokens', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('extra').get('tokens').get('length')):
            try:
                var.put('entry', var.get('extra').get('tokens').get(var.get('i')))
                PyJs_Object_149_ = Js({'type':var.get('entry').get('type'),'value':var.get('entry').get('value')})
                var.put('token', PyJs_Object_149_)
                if var.get('entry').get('regex'):
                    PyJs_Object_150_ = Js({'pattern':var.get('entry').get('regex').get('pattern'),'flags':var.get('entry').get('regex').get('flags')})
                    var.get('token').put('regex', PyJs_Object_150_)
                if var.get('extra').get('range'):
                    var.get('token').put('range', var.get('entry').get('range'))
                if var.get('extra').get('loc'):
                    var.get('token').put('loc', var.get('entry').get('loc'))
                var.get('tokens').callprop('push', var.get('token'))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('extra').put('tokens', var.get('tokens'))
    PyJsHoisted_filterTokenLocation_.__name__ = 'filterTokenLocation'
    var.put('filterTokenLocation', PyJsHoisted_filterTokenLocation_)
    Js('use strict')
    pass
    PyJs_Object_1_ = Js({'BooleanLiteral':Js(1.0),'EOF':Js(2.0),'Identifier':Js(3.0),'Keyword':Js(4.0),'NullLiteral':Js(5.0),'NumericLiteral':Js(6.0),'Punctuator':Js(7.0),'StringLiteral':Js(8.0),'RegularExpression':Js(9.0),'Template':Js(10.0)})
    var.put('Token', PyJs_Object_1_)
    PyJs_Object_2_ = Js({})
    var.put('TokenName', PyJs_Object_2_)
    var.get('TokenName').put(var.get('Token').get('BooleanLiteral'), Js('Boolean'))
    var.get('TokenName').put(var.get('Token').get('EOF'), Js('<end>'))
    var.get('TokenName').put(var.get('Token').get('Identifier'), Js('Identifier'))
    var.get('TokenName').put(var.get('Token').get('Keyword'), Js('Keyword'))
    var.get('TokenName').put(var.get('Token').get('NullLiteral'), Js('Null'))
    var.get('TokenName').put(var.get('Token').get('NumericLiteral'), Js('Numeric'))
    var.get('TokenName').put(var.get('Token').get('Punctuator'), Js('Punctuator'))
    var.get('TokenName').put(var.get('Token').get('StringLiteral'), Js('String'))
    var.get('TokenName').put(var.get('Token').get('RegularExpression'), Js('RegularExpression'))
    var.get('TokenName').put(var.get('Token').get('Template'), Js('Template'))
    def PyJs_LONG_3_(var=var):
        return var.put('FnExprTokens', Js([Js('('), Js('{'), Js('['), Js('in'), Js('typeof'), Js('instanceof'), Js('new'), Js('return'), Js('case'), Js('delete'), Js('throw'), Js('void'), Js('='), Js('+='), Js('-='), Js('*='), Js('/='), Js('%='), Js('<<='), Js('>>='), Js('>>>='), Js('&='), Js('|='), Js('^='), Js(','), Js('+'), Js('-'), Js('*'), Js('/'), Js('%'), Js('++'), Js('--'), Js('<<'), Js('>>'), Js('>>>'), Js('&'), Js('|'), Js('^'), Js('!'), Js('~'), Js('&&'), Js('||'), Js('?'), Js(':'), Js('==='), Js('=='), Js('>='), Js('<='), Js('<'), Js('>'), Js('!='), Js('!==')]))
    PyJs_LONG_3_()
    PyJs_Object_4_ = Js({'AssignmentExpression':Js('AssignmentExpression'),'AssignmentPattern':Js('AssignmentPattern'),'ArrayExpression':Js('ArrayExpression'),'ArrayPattern':Js('ArrayPattern'),'ArrowFunctionExpression':Js('ArrowFunctionExpression'),'BlockStatement':Js('BlockStatement'),'BinaryExpression':Js('BinaryExpression'),'BreakStatement':Js('BreakStatement'),'CallExpression':Js('CallExpression'),'CatchClause':Js('CatchClause'),'ClassBody':Js('ClassBody'),'ClassDeclaration':Js('ClassDeclaration'),'ClassExpression':Js('ClassExpression'),'ConditionalExpression':Js('ConditionalExpression'),'ContinueStatement':Js('ContinueStatement'),'DoWhileStatement':Js('DoWhileStatement'),'DebuggerStatement':Js('DebuggerStatement'),'EmptyStatement':Js('EmptyStatement'),'ExportAllDeclaration':Js('ExportAllDeclaration'),'ExportDefaultDeclaration':Js('ExportDefaultDeclaration'),'ExportNamedDeclaration':Js('ExportNamedDeclaration'),'ExportSpecifier':Js('ExportSpecifier'),'ExpressionStatement':Js('ExpressionStatement'),'ForStatement':Js('ForStatement'),'ForOfStatement':Js('ForOfStatement'),'ForInStatement':Js('ForInStatement'),'FunctionDeclaration':Js('FunctionDeclaration'),'FunctionExpression':Js('FunctionExpression'),'Identifier':Js('Identifier'),'IfStatement':Js('IfStatement'),'ImportDeclaration':Js('ImportDeclaration'),'ImportDefaultSpecifier':Js('ImportDefaultSpecifier'),'ImportNamespaceSpecifier':Js('ImportNamespaceSpecifier'),'ImportSpecifier':Js('ImportSpecifier'),'Literal':Js('Literal'),'LabeledStatement':Js('LabeledStatement'),'LogicalExpression':Js('LogicalExpression'),'MemberExpression':Js('MemberExpression'),'MetaProperty':Js('MetaProperty'),'MethodDefinition':Js('MethodDefinition'),'NewExpression':Js('NewExpression'),'ObjectExpression':Js('ObjectExpression'),'ObjectPattern':Js('ObjectPattern'),'Program':Js('Program'),'Property':Js('Property'),'RestElement':Js('RestElement'),'ReturnStatement':Js('ReturnStatement'),'SequenceExpression':Js('SequenceExpression'),'SpreadElement':Js('SpreadElement'),'Super':Js('Super'),'SwitchCase':Js('SwitchCase'),'SwitchStatement':Js('SwitchStatement'),'TaggedTemplateExpression':Js('TaggedTemplateExpression'),'TemplateElement':Js('TemplateElement'),'TemplateLiteral':Js('TemplateLiteral'),'ThisExpression':Js('ThisExpression'),'ThrowStatement':Js('ThrowStatement'),'TryStatement':Js('TryStatement'),'UnaryExpression':Js('UnaryExpression'),'UpdateExpression':Js('UpdateExpression'),'VariableDeclaration':Js('VariableDeclaration'),'VariableDeclarator':Js('VariableDeclarator'),'WhileStatement':Js('WhileStatement'),'WithStatement':Js('WithStatement'),'YieldExpression':Js('YieldExpression')})
    var.put('Syntax', PyJs_Object_4_)
    PyJs_Object_5_ = Js({'ArrowParameterPlaceHolder':Js('ArrowParameterPlaceHolder')})
    var.put('PlaceHolders', PyJs_Object_5_)
    PyJs_Object_6_ = Js({'UnexpectedToken':Js('Unexpected token %0'),'UnexpectedNumber':Js('Unexpected number'),'UnexpectedString':Js('Unexpected string'),'UnexpectedIdentifier':Js('Unexpected identifier'),'UnexpectedReserved':Js('Unexpected reserved word'),'UnexpectedTemplate':Js('Unexpected quasi %0'),'UnexpectedEOS':Js('Unexpected end of input'),'NewlineAfterThrow':Js('Illegal newline after throw'),'InvalidRegExp':Js('Invalid regular expression'),'UnterminatedRegExp':Js('Invalid regular expression: missing /'),'InvalidLHSInAssignment':Js('Invalid left-hand side in assignment'),'InvalidLHSInForIn':Js('Invalid left-hand side in for-in'),'InvalidLHSInForLoop':Js('Invalid left-hand side in for-loop'),'MultipleDefaultsInSwitch':Js('More than one default clause in switch statement'),'NoCatchOrFinally':Js('Missing catch or finally after try'),'UnknownLabel':Js("Undefined label '%0'"),'Redeclaration':Js("%0 '%1' has already been declared"),'IllegalContinue':Js('Illegal continue statement'),'IllegalBreak':Js('Illegal break statement'),'IllegalReturn':Js('Illegal return statement'),'StrictModeWith':Js('Strict mode code may not include a with statement'),'StrictCatchVariable':Js('Catch variable may not be eval or arguments in strict mode'),'StrictVarName':Js('Variable name may not be eval or arguments in strict mode'),'StrictParamName':Js('Parameter name eval or arguments is not allowed in strict mode'),'StrictParamDupe':Js('Strict mode function may not have duplicate parameter names'),'StrictFunctionName':Js('Function name may not be eval or arguments in strict mode'),'StrictOctalLiteral':Js('Octal literals are not allowed in strict mode.'),'StrictDelete':Js('Delete of an unqualified identifier in strict mode.'),'StrictLHSAssignment':Js('Assignment to eval or arguments is not allowed in strict mode'),'StrictLHSPostfix':Js('Postfix increment/decrement may not have eval or arguments operand in strict mode'),'StrictLHSPrefix':Js('Prefix increment/decrement may not have eval or arguments operand in strict mode'),'StrictReservedWord':Js('Use of future reserved word in strict mode'),'TemplateOctalLiteral':Js('Octal literals are not allowed in template strings.'),'ParameterAfterRestParameter':Js('Rest parameter must be last formal parameter'),'DefaultRestParameter':Js('Unexpected token ='),'ObjectPatternAsRestParameter':Js('Unexpected token {'),'DuplicateProtoProperty':Js('Duplicate __proto__ fields are not allowed in object literals'),'ConstructorSpecialMethod':Js('Class constructor may not be an accessor'),'DuplicateConstructor':Js('A class may only have one constructor'),'StaticPrototype':Js('Classes may not have static property named prototype'),'MissingFromClause':Js('Unexpected token'),'NoAsAfterImportNamespace':Js('Unexpected token'),'InvalidModuleSpecifier':Js('Unexpected token'),'IllegalImportDeclaration':Js('Unexpected token'),'IllegalExportDeclaration':Js('Unexpected token'),'DuplicateBinding':Js('Duplicate binding %0')})
    var.put('Messages', PyJs_Object_6_)
    PyJs_Object_7_ = Js({'NonAsciiIdentifierStart':JsRegExp('/[\\xAA\\xB5\\xBA\\xC0-\\xD6\\xD8-\\xF6\\xF8-\\u02C1\\u02C6-\\u02D1\\u02E0-\\u02E4\\u02EC\\u02EE\\u0370-\\u0374\\u0376\\u0377\\u037A-\\u037D\\u037F\\u0386\\u0388-\\u038A\\u038C\\u038E-\\u03A1\\u03A3-\\u03F5\\u03F7-\\u0481\\u048A-\\u052F\\u0531-\\u0556\\u0559\\u0561-\\u0587\\u05D0-\\u05EA\\u05F0-\\u05F2\\u0620-\\u064A\\u066E\\u066F\\u0671-\\u06D3\\u06D5\\u06E5\\u06E6\\u06EE\\u06EF\\u06FA-\\u06FC\\u06FF\\u0710\\u0712-\\u072F\\u074D-\\u07A5\\u07B1\\u07CA-\\u07EA\\u07F4\\u07F5\\u07FA\\u0800-\\u0815\\u081A\\u0824\\u0828\\u0840-\\u0858\\u08A0-\\u08B2\\u0904-\\u0939\\u093D\\u0950\\u0958-\\u0961\\u0971-\\u0980\\u0985-\\u098C\\u098F\\u0990\\u0993-\\u09A8\\u09AA-\\u09B0\\u09B2\\u09B6-\\u09B9\\u09BD\\u09CE\\u09DC\\u09DD\\u09DF-\\u09E1\\u09F0\\u09F1\\u0A05-\\u0A0A\\u0A0F\\u0A10\\u0A13-\\u0A28\\u0A2A-\\u0A30\\u0A32\\u0A33\\u0A35\\u0A36\\u0A38\\u0A39\\u0A59-\\u0A5C\\u0A5E\\u0A72-\\u0A74\\u0A85-\\u0A8D\\u0A8F-\\u0A91\\u0A93-\\u0AA8\\u0AAA-\\u0AB0\\u0AB2\\u0AB3\\u0AB5-\\u0AB9\\u0ABD\\u0AD0\\u0AE0\\u0AE1\\u0B05-\\u0B0C\\u0B0F\\u0B10\\u0B13-\\u0B28\\u0B2A-\\u0B30\\u0B32\\u0B33\\u0B35-\\u0B39\\u0B3D\\u0B5C\\u0B5D\\u0B5F-\\u0B61\\u0B71\\u0B83\\u0B85-\\u0B8A\\u0B8E-\\u0B90\\u0B92-\\u0B95\\u0B99\\u0B9A\\u0B9C\\u0B9E\\u0B9F\\u0BA3\\u0BA4\\u0BA8-\\u0BAA\\u0BAE-\\u0BB9\\u0BD0\\u0C05-\\u0C0C\\u0C0E-\\u0C10\\u0C12-\\u0C28\\u0C2A-\\u0C39\\u0C3D\\u0C58\\u0C59\\u0C60\\u0C61\\u0C85-\\u0C8C\\u0C8E-\\u0C90\\u0C92-\\u0CA8\\u0CAA-\\u0CB3\\u0CB5-\\u0CB9\\u0CBD\\u0CDE\\u0CE0\\u0CE1\\u0CF1\\u0CF2\\u0D05-\\u0D0C\\u0D0E-\\u0D10\\u0D12-\\u0D3A\\u0D3D\\u0D4E\\u0D60\\u0D61\\u0D7A-\\u0D7F\\u0D85-\\u0D96\\u0D9A-\\u0DB1\\u0DB3-\\u0DBB\\u0DBD\\u0DC0-\\u0DC6\\u0E01-\\u0E30\\u0E32\\u0E33\\u0E40-\\u0E46\\u0E81\\u0E82\\u0E84\\u0E87\\u0E88\\u0E8A\\u0E8D\\u0E94-\\u0E97\\u0E99-\\u0E9F\\u0EA1-\\u0EA3\\u0EA5\\u0EA7\\u0EAA\\u0EAB\\u0EAD-\\u0EB0\\u0EB2\\u0EB3\\u0EBD\\u0EC0-\\u0EC4\\u0EC6\\u0EDC-\\u0EDF\\u0F00\\u0F40-\\u0F47\\u0F49-\\u0F6C\\u0F88-\\u0F8C\\u1000-\\u102A\\u103F\\u1050-\\u1055\\u105A-\\u105D\\u1061\\u1065\\u1066\\u106E-\\u1070\\u1075-\\u1081\\u108E\\u10A0-\\u10C5\\u10C7\\u10CD\\u10D0-\\u10FA\\u10FC-\\u1248\\u124A-\\u124D\\u1250-\\u1256\\u1258\\u125A-\\u125D\\u1260-\\u1288\\u128A-\\u128D\\u1290-\\u12B0\\u12B2-\\u12B5\\u12B8-\\u12BE\\u12C0\\u12C2-\\u12C5\\u12C8-\\u12D6\\u12D8-\\u1310\\u1312-\\u1315\\u1318-\\u135A\\u1380-\\u138F\\u13A0-\\u13F4\\u1401-\\u166C\\u166F-\\u167F\\u1681-\\u169A\\u16A0-\\u16EA\\u16EE-\\u16F8\\u1700-\\u170C\\u170E-\\u1711\\u1720-\\u1731\\u1740-\\u1751\\u1760-\\u176C\\u176E-\\u1770\\u1780-\\u17B3\\u17D7\\u17DC\\u1820-\\u1877\\u1880-\\u18A8\\u18AA\\u18B0-\\u18F5\\u1900-\\u191E\\u1950-\\u196D\\u1970-\\u1974\\u1980-\\u19AB\\u19C1-\\u19C7\\u1A00-\\u1A16\\u1A20-\\u1A54\\u1AA7\\u1B05-\\u1B33\\u1B45-\\u1B4B\\u1B83-\\u1BA0\\u1BAE\\u1BAF\\u1BBA-\\u1BE5\\u1C00-\\u1C23\\u1C4D-\\u1C4F\\u1C5A-\\u1C7D\\u1CE9-\\u1CEC\\u1CEE-\\u1CF1\\u1CF5\\u1CF6\\u1D00-\\u1DBF\\u1E00-\\u1F15\\u1F18-\\u1F1D\\u1F20-\\u1F45\\u1F48-\\u1F4D\\u1F50-\\u1F57\\u1F59\\u1F5B\\u1F5D\\u1F5F-\\u1F7D\\u1F80-\\u1FB4\\u1FB6-\\u1FBC\\u1FBE\\u1FC2-\\u1FC4\\u1FC6-\\u1FCC\\u1FD0-\\u1FD3\\u1FD6-\\u1FDB\\u1FE0-\\u1FEC\\u1FF2-\\u1FF4\\u1FF6-\\u1FFC\\u2071\\u207F\\u2090-\\u209C\\u2102\\u2107\\u210A-\\u2113\\u2115\\u2118-\\u211D\\u2124\\u2126\\u2128\\u212A-\\u2139\\u213C-\\u213F\\u2145-\\u2149\\u214E\\u2160-\\u2188\\u2C00-\\u2C2E\\u2C30-\\u2C5E\\u2C60-\\u2CE4\\u2CEB-\\u2CEE\\u2CF2\\u2CF3\\u2D00-\\u2D25\\u2D27\\u2D2D\\u2D30-\\u2D67\\u2D6F\\u2D80-\\u2D96\\u2DA0-\\u2DA6\\u2DA8-\\u2DAE\\u2DB0-\\u2DB6\\u2DB8-\\u2DBE\\u2DC0-\\u2DC6\\u2DC8-\\u2DCE\\u2DD0-\\u2DD6\\u2DD8-\\u2DDE\\u3005-\\u3007\\u3021-\\u3029\\u3031-\\u3035\\u3038-\\u303C\\u3041-\\u3096\\u309B-\\u309F\\u30A1-\\u30FA\\u30FC-\\u30FF\\u3105-\\u312D\\u3131-\\u318E\\u31A0-\\u31BA\\u31F0-\\u31FF\\u3400-\\u4DB5\\u4E00-\\u9FCC\\uA000-\\uA48C\\uA4D0-\\uA4FD\\uA500-\\uA60C\\uA610-\\uA61F\\uA62A\\uA62B\\uA640-\\uA66E\\uA67F-\\uA69D\\uA6A0-\\uA6EF\\uA717-\\uA71F\\uA722-\\uA788\\uA78B-\\uA78E\\uA790-\\uA7AD\\uA7B0\\uA7B1\\uA7F7-\\uA801\\uA803-\\uA805\\uA807-\\uA80A\\uA80C-\\uA822\\uA840-\\uA873\\uA882-\\uA8B3\\uA8F2-\\uA8F7\\uA8FB\\uA90A-\\uA925\\uA930-\\uA946\\uA960-\\uA97C\\uA984-\\uA9B2\\uA9CF\\uA9E0-\\uA9E4\\uA9E6-\\uA9EF\\uA9FA-\\uA9FE\\uAA00-\\uAA28\\uAA40-\\uAA42\\uAA44-\\uAA4B\\uAA60-\\uAA76\\uAA7A\\uAA7E-\\uAAAF\\uAAB1\\uAAB5\\uAAB6\\uAAB9-\\uAABD\\uAAC0\\uAAC2\\uAADB-\\uAADD\\uAAE0-\\uAAEA\\uAAF2-\\uAAF4\\uAB01-\\uAB06\\uAB09-\\uAB0E\\uAB11-\\uAB16\\uAB20-\\uAB26\\uAB28-\\uAB2E\\uAB30-\\uAB5A\\uAB5C-\\uAB5F\\uAB64\\uAB65\\uABC0-\\uABE2\\uAC00-\\uD7A3\\uD7B0-\\uD7C6\\uD7CB-\\uD7FB\\uF900-\\uFA6D\\uFA70-\\uFAD9\\uFB00-\\uFB06\\uFB13-\\uFB17\\uFB1D\\uFB1F-\\uFB28\\uFB2A-\\uFB36\\uFB38-\\uFB3C\\uFB3E\\uFB40\\uFB41\\uFB43\\uFB44\\uFB46-\\uFBB1\\uFBD3-\\uFD3D\\uFD50-\\uFD8F\\uFD92-\\uFDC7\\uFDF0-\\uFDFB\\uFE70-\\uFE74\\uFE76-\\uFEFC\\uFF21-\\uFF3A\\uFF41-\\uFF5A\\uFF66-\\uFFBE\\uFFC2-\\uFFC7\\uFFCA-\\uFFCF\\uFFD2-\\uFFD7\\uFFDA-\\uFFDC]|\\uD800[\\uDC00-\\uDC0B\\uDC0D-\\uDC26\\uDC28-\\uDC3A\\uDC3C\\uDC3D\\uDC3F-\\uDC4D\\uDC50-\\uDC5D\\uDC80-\\uDCFA\\uDD40-\\uDD74\\uDE80-\\uDE9C\\uDEA0-\\uDED0\\uDF00-\\uDF1F\\uDF30-\\uDF4A\\uDF50-\\uDF75\\uDF80-\\uDF9D\\uDFA0-\\uDFC3\\uDFC8-\\uDFCF\\uDFD1-\\uDFD5]|\\uD801[\\uDC00-\\uDC9D\\uDD00-\\uDD27\\uDD30-\\uDD63\\uDE00-\\uDF36\\uDF40-\\uDF55\\uDF60-\\uDF67]|\\uD802[\\uDC00-\\uDC05\\uDC08\\uDC0A-\\uDC35\\uDC37\\uDC38\\uDC3C\\uDC3F-\\uDC55\\uDC60-\\uDC76\\uDC80-\\uDC9E\\uDD00-\\uDD15\\uDD20-\\uDD39\\uDD80-\\uDDB7\\uDDBE\\uDDBF\\uDE00\\uDE10-\\uDE13\\uDE15-\\uDE17\\uDE19-\\uDE33\\uDE60-\\uDE7C\\uDE80-\\uDE9C\\uDEC0-\\uDEC7\\uDEC9-\\uDEE4\\uDF00-\\uDF35\\uDF40-\\uDF55\\uDF60-\\uDF72\\uDF80-\\uDF91]|\\uD803[\\uDC00-\\uDC48]|\\uD804[\\uDC03-\\uDC37\\uDC83-\\uDCAF\\uDCD0-\\uDCE8\\uDD03-\\uDD26\\uDD50-\\uDD72\\uDD76\\uDD83-\\uDDB2\\uDDC1-\\uDDC4\\uDDDA\\uDE00-\\uDE11\\uDE13-\\uDE2B\\uDEB0-\\uDEDE\\uDF05-\\uDF0C\\uDF0F\\uDF10\\uDF13-\\uDF28\\uDF2A-\\uDF30\\uDF32\\uDF33\\uDF35-\\uDF39\\uDF3D\\uDF5D-\\uDF61]|\\uD805[\\uDC80-\\uDCAF\\uDCC4\\uDCC5\\uDCC7\\uDD80-\\uDDAE\\uDE00-\\uDE2F\\uDE44\\uDE80-\\uDEAA]|\\uD806[\\uDCA0-\\uDCDF\\uDCFF\\uDEC0-\\uDEF8]|\\uD808[\\uDC00-\\uDF98]|\\uD809[\\uDC00-\\uDC6E]|[\\uD80C\\uD840-\\uD868\\uD86A-\\uD86C][\\uDC00-\\uDFFF]|\\uD80D[\\uDC00-\\uDC2E]|\\uD81A[\\uDC00-\\uDE38\\uDE40-\\uDE5E\\uDED0-\\uDEED\\uDF00-\\uDF2F\\uDF40-\\uDF43\\uDF63-\\uDF77\\uDF7D-\\uDF8F]|\\uD81B[\\uDF00-\\uDF44\\uDF50\\uDF93-\\uDF9F]|\\uD82C[\\uDC00\\uDC01]|\\uD82F[\\uDC00-\\uDC6A\\uDC70-\\uDC7C\\uDC80-\\uDC88\\uDC90-\\uDC99]|\\uD835[\\uDC00-\\uDC54\\uDC56-\\uDC9C\\uDC9E\\uDC9F\\uDCA2\\uDCA5\\uDCA6\\uDCA9-\\uDCAC\\uDCAE-\\uDCB9\\uDCBB\\uDCBD-\\uDCC3\\uDCC5-\\uDD05\\uDD07-\\uDD0A\\uDD0D-\\uDD14\\uDD16-\\uDD1C\\uDD1E-\\uDD39\\uDD3B-\\uDD3E\\uDD40-\\uDD44\\uDD46\\uDD4A-\\uDD50\\uDD52-\\uDEA5\\uDEA8-\\uDEC0\\uDEC2-\\uDEDA\\uDEDC-\\uDEFA\\uDEFC-\\uDF14\\uDF16-\\uDF34\\uDF36-\\uDF4E\\uDF50-\\uDF6E\\uDF70-\\uDF88\\uDF8A-\\uDFA8\\uDFAA-\\uDFC2\\uDFC4-\\uDFCB]|\\uD83A[\\uDC00-\\uDCC4]|\\uD83B[\\uDE00-\\uDE03\\uDE05-\\uDE1F\\uDE21\\uDE22\\uDE24\\uDE27\\uDE29-\\uDE32\\uDE34-\\uDE37\\uDE39\\uDE3B\\uDE42\\uDE47\\uDE49\\uDE4B\\uDE4D-\\uDE4F\\uDE51\\uDE52\\uDE54\\uDE57\\uDE59\\uDE5B\\uDE5D\\uDE5F\\uDE61\\uDE62\\uDE64\\uDE67-\\uDE6A\\uDE6C-\\uDE72\\uDE74-\\uDE77\\uDE79-\\uDE7C\\uDE7E\\uDE80-\\uDE89\\uDE8B-\\uDE9B\\uDEA1-\\uDEA3\\uDEA5-\\uDEA9\\uDEAB-\\uDEBB]|\\uD869[\\uDC00-\\uDED6\\uDF00-\\uDFFF]|\\uD86D[\\uDC00-\\uDF34\\uDF40-\\uDFFF]|\\uD86E[\\uDC00-\\uDC1D]|\\uD87E[\\uDC00-\\uDE1D]/'),'NonAsciiIdentifierPart':JsRegExp('/[\\xAA\\xB5\\xB7\\xBA\\xC0-\\xD6\\xD8-\\xF6\\xF8-\\u02C1\\u02C6-\\u02D1\\u02E0-\\u02E4\\u02EC\\u02EE\\u0300-\\u0374\\u0376\\u0377\\u037A-\\u037D\\u037F\\u0386-\\u038A\\u038C\\u038E-\\u03A1\\u03A3-\\u03F5\\u03F7-\\u0481\\u0483-\\u0487\\u048A-\\u052F\\u0531-\\u0556\\u0559\\u0561-\\u0587\\u0591-\\u05BD\\u05BF\\u05C1\\u05C2\\u05C4\\u05C5\\u05C7\\u05D0-\\u05EA\\u05F0-\\u05F2\\u0610-\\u061A\\u0620-\\u0669\\u066E-\\u06D3\\u06D5-\\u06DC\\u06DF-\\u06E8\\u06EA-\\u06FC\\u06FF\\u0710-\\u074A\\u074D-\\u07B1\\u07C0-\\u07F5\\u07FA\\u0800-\\u082D\\u0840-\\u085B\\u08A0-\\u08B2\\u08E4-\\u0963\\u0966-\\u096F\\u0971-\\u0983\\u0985-\\u098C\\u098F\\u0990\\u0993-\\u09A8\\u09AA-\\u09B0\\u09B2\\u09B6-\\u09B9\\u09BC-\\u09C4\\u09C7\\u09C8\\u09CB-\\u09CE\\u09D7\\u09DC\\u09DD\\u09DF-\\u09E3\\u09E6-\\u09F1\\u0A01-\\u0A03\\u0A05-\\u0A0A\\u0A0F\\u0A10\\u0A13-\\u0A28\\u0A2A-\\u0A30\\u0A32\\u0A33\\u0A35\\u0A36\\u0A38\\u0A39\\u0A3C\\u0A3E-\\u0A42\\u0A47\\u0A48\\u0A4B-\\u0A4D\\u0A51\\u0A59-\\u0A5C\\u0A5E\\u0A66-\\u0A75\\u0A81-\\u0A83\\u0A85-\\u0A8D\\u0A8F-\\u0A91\\u0A93-\\u0AA8\\u0AAA-\\u0AB0\\u0AB2\\u0AB3\\u0AB5-\\u0AB9\\u0ABC-\\u0AC5\\u0AC7-\\u0AC9\\u0ACB-\\u0ACD\\u0AD0\\u0AE0-\\u0AE3\\u0AE6-\\u0AEF\\u0B01-\\u0B03\\u0B05-\\u0B0C\\u0B0F\\u0B10\\u0B13-\\u0B28\\u0B2A-\\u0B30\\u0B32\\u0B33\\u0B35-\\u0B39\\u0B3C-\\u0B44\\u0B47\\u0B48\\u0B4B-\\u0B4D\\u0B56\\u0B57\\u0B5C\\u0B5D\\u0B5F-\\u0B63\\u0B66-\\u0B6F\\u0B71\\u0B82\\u0B83\\u0B85-\\u0B8A\\u0B8E-\\u0B90\\u0B92-\\u0B95\\u0B99\\u0B9A\\u0B9C\\u0B9E\\u0B9F\\u0BA3\\u0BA4\\u0BA8-\\u0BAA\\u0BAE-\\u0BB9\\u0BBE-\\u0BC2\\u0BC6-\\u0BC8\\u0BCA-\\u0BCD\\u0BD0\\u0BD7\\u0BE6-\\u0BEF\\u0C00-\\u0C03\\u0C05-\\u0C0C\\u0C0E-\\u0C10\\u0C12-\\u0C28\\u0C2A-\\u0C39\\u0C3D-\\u0C44\\u0C46-\\u0C48\\u0C4A-\\u0C4D\\u0C55\\u0C56\\u0C58\\u0C59\\u0C60-\\u0C63\\u0C66-\\u0C6F\\u0C81-\\u0C83\\u0C85-\\u0C8C\\u0C8E-\\u0C90\\u0C92-\\u0CA8\\u0CAA-\\u0CB3\\u0CB5-\\u0CB9\\u0CBC-\\u0CC4\\u0CC6-\\u0CC8\\u0CCA-\\u0CCD\\u0CD5\\u0CD6\\u0CDE\\u0CE0-\\u0CE3\\u0CE6-\\u0CEF\\u0CF1\\u0CF2\\u0D01-\\u0D03\\u0D05-\\u0D0C\\u0D0E-\\u0D10\\u0D12-\\u0D3A\\u0D3D-\\u0D44\\u0D46-\\u0D48\\u0D4A-\\u0D4E\\u0D57\\u0D60-\\u0D63\\u0D66-\\u0D6F\\u0D7A-\\u0D7F\\u0D82\\u0D83\\u0D85-\\u0D96\\u0D9A-\\u0DB1\\u0DB3-\\u0DBB\\u0DBD\\u0DC0-\\u0DC6\\u0DCA\\u0DCF-\\u0DD4\\u0DD6\\u0DD8-\\u0DDF\\u0DE6-\\u0DEF\\u0DF2\\u0DF3\\u0E01-\\u0E3A\\u0E40-\\u0E4E\\u0E50-\\u0E59\\u0E81\\u0E82\\u0E84\\u0E87\\u0E88\\u0E8A\\u0E8D\\u0E94-\\u0E97\\u0E99-\\u0E9F\\u0EA1-\\u0EA3\\u0EA5\\u0EA7\\u0EAA\\u0EAB\\u0EAD-\\u0EB9\\u0EBB-\\u0EBD\\u0EC0-\\u0EC4\\u0EC6\\u0EC8-\\u0ECD\\u0ED0-\\u0ED9\\u0EDC-\\u0EDF\\u0F00\\u0F18\\u0F19\\u0F20-\\u0F29\\u0F35\\u0F37\\u0F39\\u0F3E-\\u0F47\\u0F49-\\u0F6C\\u0F71-\\u0F84\\u0F86-\\u0F97\\u0F99-\\u0FBC\\u0FC6\\u1000-\\u1049\\u1050-\\u109D\\u10A0-\\u10C5\\u10C7\\u10CD\\u10D0-\\u10FA\\u10FC-\\u1248\\u124A-\\u124D\\u1250-\\u1256\\u1258\\u125A-\\u125D\\u1260-\\u1288\\u128A-\\u128D\\u1290-\\u12B0\\u12B2-\\u12B5\\u12B8-\\u12BE\\u12C0\\u12C2-\\u12C5\\u12C8-\\u12D6\\u12D8-\\u1310\\u1312-\\u1315\\u1318-\\u135A\\u135D-\\u135F\\u1369-\\u1371\\u1380-\\u138F\\u13A0-\\u13F4\\u1401-\\u166C\\u166F-\\u167F\\u1681-\\u169A\\u16A0-\\u16EA\\u16EE-\\u16F8\\u1700-\\u170C\\u170E-\\u1714\\u1720-\\u1734\\u1740-\\u1753\\u1760-\\u176C\\u176E-\\u1770\\u1772\\u1773\\u1780-\\u17D3\\u17D7\\u17DC\\u17DD\\u17E0-\\u17E9\\u180B-\\u180D\\u1810-\\u1819\\u1820-\\u1877\\u1880-\\u18AA\\u18B0-\\u18F5\\u1900-\\u191E\\u1920-\\u192B\\u1930-\\u193B\\u1946-\\u196D\\u1970-\\u1974\\u1980-\\u19AB\\u19B0-\\u19C9\\u19D0-\\u19DA\\u1A00-\\u1A1B\\u1A20-\\u1A5E\\u1A60-\\u1A7C\\u1A7F-\\u1A89\\u1A90-\\u1A99\\u1AA7\\u1AB0-\\u1ABD\\u1B00-\\u1B4B\\u1B50-\\u1B59\\u1B6B-\\u1B73\\u1B80-\\u1BF3\\u1C00-\\u1C37\\u1C40-\\u1C49\\u1C4D-\\u1C7D\\u1CD0-\\u1CD2\\u1CD4-\\u1CF6\\u1CF8\\u1CF9\\u1D00-\\u1DF5\\u1DFC-\\u1F15\\u1F18-\\u1F1D\\u1F20-\\u1F45\\u1F48-\\u1F4D\\u1F50-\\u1F57\\u1F59\\u1F5B\\u1F5D\\u1F5F-\\u1F7D\\u1F80-\\u1FB4\\u1FB6-\\u1FBC\\u1FBE\\u1FC2-\\u1FC4\\u1FC6-\\u1FCC\\u1FD0-\\u1FD3\\u1FD6-\\u1FDB\\u1FE0-\\u1FEC\\u1FF2-\\u1FF4\\u1FF6-\\u1FFC\\u200C\\u200D\\u203F\\u2040\\u2054\\u2071\\u207F\\u2090-\\u209C\\u20D0-\\u20DC\\u20E1\\u20E5-\\u20F0\\u2102\\u2107\\u210A-\\u2113\\u2115\\u2118-\\u211D\\u2124\\u2126\\u2128\\u212A-\\u2139\\u213C-\\u213F\\u2145-\\u2149\\u214E\\u2160-\\u2188\\u2C00-\\u2C2E\\u2C30-\\u2C5E\\u2C60-\\u2CE4\\u2CEB-\\u2CF3\\u2D00-\\u2D25\\u2D27\\u2D2D\\u2D30-\\u2D67\\u2D6F\\u2D7F-\\u2D96\\u2DA0-\\u2DA6\\u2DA8-\\u2DAE\\u2DB0-\\u2DB6\\u2DB8-\\u2DBE\\u2DC0-\\u2DC6\\u2DC8-\\u2DCE\\u2DD0-\\u2DD6\\u2DD8-\\u2DDE\\u2DE0-\\u2DFF\\u3005-\\u3007\\u3021-\\u302F\\u3031-\\u3035\\u3038-\\u303C\\u3041-\\u3096\\u3099-\\u309F\\u30A1-\\u30FA\\u30FC-\\u30FF\\u3105-\\u312D\\u3131-\\u318E\\u31A0-\\u31BA\\u31F0-\\u31FF\\u3400-\\u4DB5\\u4E00-\\u9FCC\\uA000-\\uA48C\\uA4D0-\\uA4FD\\uA500-\\uA60C\\uA610-\\uA62B\\uA640-\\uA66F\\uA674-\\uA67D\\uA67F-\\uA69D\\uA69F-\\uA6F1\\uA717-\\uA71F\\uA722-\\uA788\\uA78B-\\uA78E\\uA790-\\uA7AD\\uA7B0\\uA7B1\\uA7F7-\\uA827\\uA840-\\uA873\\uA880-\\uA8C4\\uA8D0-\\uA8D9\\uA8E0-\\uA8F7\\uA8FB\\uA900-\\uA92D\\uA930-\\uA953\\uA960-\\uA97C\\uA980-\\uA9C0\\uA9CF-\\uA9D9\\uA9E0-\\uA9FE\\uAA00-\\uAA36\\uAA40-\\uAA4D\\uAA50-\\uAA59\\uAA60-\\uAA76\\uAA7A-\\uAAC2\\uAADB-\\uAADD\\uAAE0-\\uAAEF\\uAAF2-\\uAAF6\\uAB01-\\uAB06\\uAB09-\\uAB0E\\uAB11-\\uAB16\\uAB20-\\uAB26\\uAB28-\\uAB2E\\uAB30-\\uAB5A\\uAB5C-\\uAB5F\\uAB64\\uAB65\\uABC0-\\uABEA\\uABEC\\uABED\\uABF0-\\uABF9\\uAC00-\\uD7A3\\uD7B0-\\uD7C6\\uD7CB-\\uD7FB\\uF900-\\uFA6D\\uFA70-\\uFAD9\\uFB00-\\uFB06\\uFB13-\\uFB17\\uFB1D-\\uFB28\\uFB2A-\\uFB36\\uFB38-\\uFB3C\\uFB3E\\uFB40\\uFB41\\uFB43\\uFB44\\uFB46-\\uFBB1\\uFBD3-\\uFD3D\\uFD50-\\uFD8F\\uFD92-\\uFDC7\\uFDF0-\\uFDFB\\uFE00-\\uFE0F\\uFE20-\\uFE2D\\uFE33\\uFE34\\uFE4D-\\uFE4F\\uFE70-\\uFE74\\uFE76-\\uFEFC\\uFF10-\\uFF19\\uFF21-\\uFF3A\\uFF3F\\uFF41-\\uFF5A\\uFF66-\\uFFBE\\uFFC2-\\uFFC7\\uFFCA-\\uFFCF\\uFFD2-\\uFFD7\\uFFDA-\\uFFDC]|\\uD800[\\uDC00-\\uDC0B\\uDC0D-\\uDC26\\uDC28-\\uDC3A\\uDC3C\\uDC3D\\uDC3F-\\uDC4D\\uDC50-\\uDC5D\\uDC80-\\uDCFA\\uDD40-\\uDD74\\uDDFD\\uDE80-\\uDE9C\\uDEA0-\\uDED0\\uDEE0\\uDF00-\\uDF1F\\uDF30-\\uDF4A\\uDF50-\\uDF7A\\uDF80-\\uDF9D\\uDFA0-\\uDFC3\\uDFC8-\\uDFCF\\uDFD1-\\uDFD5]|\\uD801[\\uDC00-\\uDC9D\\uDCA0-\\uDCA9\\uDD00-\\uDD27\\uDD30-\\uDD63\\uDE00-\\uDF36\\uDF40-\\uDF55\\uDF60-\\uDF67]|\\uD802[\\uDC00-\\uDC05\\uDC08\\uDC0A-\\uDC35\\uDC37\\uDC38\\uDC3C\\uDC3F-\\uDC55\\uDC60-\\uDC76\\uDC80-\\uDC9E\\uDD00-\\uDD15\\uDD20-\\uDD39\\uDD80-\\uDDB7\\uDDBE\\uDDBF\\uDE00-\\uDE03\\uDE05\\uDE06\\uDE0C-\\uDE13\\uDE15-\\uDE17\\uDE19-\\uDE33\\uDE38-\\uDE3A\\uDE3F\\uDE60-\\uDE7C\\uDE80-\\uDE9C\\uDEC0-\\uDEC7\\uDEC9-\\uDEE6\\uDF00-\\uDF35\\uDF40-\\uDF55\\uDF60-\\uDF72\\uDF80-\\uDF91]|\\uD803[\\uDC00-\\uDC48]|\\uD804[\\uDC00-\\uDC46\\uDC66-\\uDC6F\\uDC7F-\\uDCBA\\uDCD0-\\uDCE8\\uDCF0-\\uDCF9\\uDD00-\\uDD34\\uDD36-\\uDD3F\\uDD50-\\uDD73\\uDD76\\uDD80-\\uDDC4\\uDDD0-\\uDDDA\\uDE00-\\uDE11\\uDE13-\\uDE37\\uDEB0-\\uDEEA\\uDEF0-\\uDEF9\\uDF01-\\uDF03\\uDF05-\\uDF0C\\uDF0F\\uDF10\\uDF13-\\uDF28\\uDF2A-\\uDF30\\uDF32\\uDF33\\uDF35-\\uDF39\\uDF3C-\\uDF44\\uDF47\\uDF48\\uDF4B-\\uDF4D\\uDF57\\uDF5D-\\uDF63\\uDF66-\\uDF6C\\uDF70-\\uDF74]|\\uD805[\\uDC80-\\uDCC5\\uDCC7\\uDCD0-\\uDCD9\\uDD80-\\uDDB5\\uDDB8-\\uDDC0\\uDE00-\\uDE40\\uDE44\\uDE50-\\uDE59\\uDE80-\\uDEB7\\uDEC0-\\uDEC9]|\\uD806[\\uDCA0-\\uDCE9\\uDCFF\\uDEC0-\\uDEF8]|\\uD808[\\uDC00-\\uDF98]|\\uD809[\\uDC00-\\uDC6E]|[\\uD80C\\uD840-\\uD868\\uD86A-\\uD86C][\\uDC00-\\uDFFF]|\\uD80D[\\uDC00-\\uDC2E]|\\uD81A[\\uDC00-\\uDE38\\uDE40-\\uDE5E\\uDE60-\\uDE69\\uDED0-\\uDEED\\uDEF0-\\uDEF4\\uDF00-\\uDF36\\uDF40-\\uDF43\\uDF50-\\uDF59\\uDF63-\\uDF77\\uDF7D-\\uDF8F]|\\uD81B[\\uDF00-\\uDF44\\uDF50-\\uDF7E\\uDF8F-\\uDF9F]|\\uD82C[\\uDC00\\uDC01]|\\uD82F[\\uDC00-\\uDC6A\\uDC70-\\uDC7C\\uDC80-\\uDC88\\uDC90-\\uDC99\\uDC9D\\uDC9E]|\\uD834[\\uDD65-\\uDD69\\uDD6D-\\uDD72\\uDD7B-\\uDD82\\uDD85-\\uDD8B\\uDDAA-\\uDDAD\\uDE42-\\uDE44]|\\uD835[\\uDC00-\\uDC54\\uDC56-\\uDC9C\\uDC9E\\uDC9F\\uDCA2\\uDCA5\\uDCA6\\uDCA9-\\uDCAC\\uDCAE-\\uDCB9\\uDCBB\\uDCBD-\\uDCC3\\uDCC5-\\uDD05\\uDD07-\\uDD0A\\uDD0D-\\uDD14\\uDD16-\\uDD1C\\uDD1E-\\uDD39\\uDD3B-\\uDD3E\\uDD40-\\uDD44\\uDD46\\uDD4A-\\uDD50\\uDD52-\\uDEA5\\uDEA8-\\uDEC0\\uDEC2-\\uDEDA\\uDEDC-\\uDEFA\\uDEFC-\\uDF14\\uDF16-\\uDF34\\uDF36-\\uDF4E\\uDF50-\\uDF6E\\uDF70-\\uDF88\\uDF8A-\\uDFA8\\uDFAA-\\uDFC2\\uDFC4-\\uDFCB\\uDFCE-\\uDFFF]|\\uD83A[\\uDC00-\\uDCC4\\uDCD0-\\uDCD6]|\\uD83B[\\uDE00-\\uDE03\\uDE05-\\uDE1F\\uDE21\\uDE22\\uDE24\\uDE27\\uDE29-\\uDE32\\uDE34-\\uDE37\\uDE39\\uDE3B\\uDE42\\uDE47\\uDE49\\uDE4B\\uDE4D-\\uDE4F\\uDE51\\uDE52\\uDE54\\uDE57\\uDE59\\uDE5B\\uDE5D\\uDE5F\\uDE61\\uDE62\\uDE64\\uDE67-\\uDE6A\\uDE6C-\\uDE72\\uDE74-\\uDE77\\uDE79-\\uDE7C\\uDE7E\\uDE80-\\uDE89\\uDE8B-\\uDE9B\\uDEA1-\\uDEA3\\uDEA5-\\uDEA9\\uDEAB-\\uDEBB]|\\uD869[\\uDC00-\\uDED6\\uDF00-\\uDFFF]|\\uD86D[\\uDC00-\\uDF34\\uDF40-\\uDFFF]|\\uD86E[\\uDC00-\\uDC1D]|\\uD87E[\\uDC00-\\uDE1D]|\\uDB40[\\uDD00-\\uDDEF]/')})
    var.put('Regex', PyJs_Object_7_)
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    @Js
    def PyJs_anonymous_50_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['comment', 'leadingComments', 'last', 'bottomRight', 'i', 'trailingComments', 'lastChild'])
        var.put('bottomRight', var.get('extra').get('bottomRightStack'))
        var.put('last', var.get('bottomRight').get((var.get('bottomRight').get('length')-Js(1.0))))
        if PyJsStrictEq(var.get("this").get('type'),var.get('Syntax').get('Program')):
            if (var.get("this").get('body').get('length')>Js(0.0)):
                return var.get('undefined')
        if (var.get('extra').get('trailingComments').get('length')>Js(0.0)):
            var.put('trailingComments', Js([]))
            #for JS loop
            var.put('i', (var.get('extra').get('trailingComments').get('length')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.put('comment', var.get('extra').get('trailingComments').get(var.get('i')))
                    if (var.get('comment').get('range').get('0')>=var.get("this").get('range').get('1')):
                        var.get('trailingComments').callprop('unshift', var.get('comment'))
                        var.get('extra').get('trailingComments').callprop('splice', var.get('i'), Js(1.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            var.get('extra').put('trailingComments', Js([]))
        else:
            if ((var.get('last') and var.get('last').get('trailingComments')) and (var.get('last').get('trailingComments').get('0').get('range').get('0')>=var.get("this").get('range').get('1'))):
                var.put('trailingComments', var.get('last').get('trailingComments'))
                var.get('last').delete('trailingComments')
        while (var.get('last') and (var.get('last').get('range').get('0')>=var.get("this").get('range').get('0'))):
            var.put('lastChild', var.get('bottomRight').callprop('pop'))
            var.put('last', var.get('bottomRight').get((var.get('bottomRight').get('length')-Js(1.0))))
        if var.get('lastChild'):
            if var.get('lastChild').get('leadingComments'):
                var.put('leadingComments', Js([]))
                #for JS loop
                var.put('i', (var.get('lastChild').get('leadingComments').get('length')-Js(1.0)))
                while (var.get('i')>=Js(0.0)):
                    try:
                        var.put('comment', var.get('lastChild').get('leadingComments').get(var.get('i')))
                        if (var.get('comment').get('range').get('1')<=var.get("this").get('range').get('0')):
                            var.get('leadingComments').callprop('unshift', var.get('comment'))
                            var.get('lastChild').get('leadingComments').callprop('splice', var.get('i'), Js(1.0))
                    finally:
                            var.put('i',Js(var.get('i').to_number())-Js(1))
                if var.get('lastChild').get('leadingComments').get('length').neg():
                    var.get('lastChild').put('leadingComments', var.get('undefined'))
        else:
            if (var.get('extra').get('leadingComments').get('length')>Js(0.0)):
                var.put('leadingComments', Js([]))
                #for JS loop
                var.put('i', (var.get('extra').get('leadingComments').get('length')-Js(1.0)))
                while (var.get('i')>=Js(0.0)):
                    try:
                        var.put('comment', var.get('extra').get('leadingComments').get(var.get('i')))
                        if (var.get('comment').get('range').get('1')<=var.get("this").get('range').get('0')):
                            var.get('leadingComments').callprop('unshift', var.get('comment'))
                            var.get('extra').get('leadingComments').callprop('splice', var.get('i'), Js(1.0))
                    finally:
                            var.put('i',Js(var.get('i').to_number())-Js(1))
        if (var.get('leadingComments') and (var.get('leadingComments').get('length')>Js(0.0))):
            var.get("this").put('leadingComments', var.get('leadingComments'))
        if (var.get('trailingComments') and (var.get('trailingComments').get('length')>Js(0.0))):
            var.get("this").put('trailingComments', var.get('trailingComments'))
        var.get('bottomRight').callprop('push', var.get("this"))
    PyJs_anonymous_50_._set_name('anonymous')
    @Js
    def PyJs_anonymous_51_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if var.get('extra').get('range'):
            var.get("this").get('range').put('1', var.get('lastIndex'))
        if var.get('extra').get('loc'):
            PyJs_Object_52_ = Js({'line':var.get('lastLineNumber'),'column':(var.get('lastIndex')-var.get('lastLineStart'))})
            var.get("this").get('loc').put('end', PyJs_Object_52_)
            if var.get('extra').get('source'):
                var.get("this").get('loc').put('source', var.get('extra').get('source'))
        if var.get('extra').get('attachComment'):
            var.get("this").callprop('processComment')
    PyJs_anonymous_51_._set_name('anonymous')
    @Js
    def PyJs_anonymous_53_(elements, this, arguments, var=var):
        var = Scope({'this':this, 'elements':elements, 'arguments':arguments}, var)
        var.registers(['elements'])
        var.get("this").put('type', var.get('Syntax').get('ArrayExpression'))
        var.get("this").put('elements', var.get('elements'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_53_._set_name('anonymous')
    @Js
    def PyJs_anonymous_54_(elements, this, arguments, var=var):
        var = Scope({'this':this, 'elements':elements, 'arguments':arguments}, var)
        var.registers(['elements'])
        var.get("this").put('type', var.get('Syntax').get('ArrayPattern'))
        var.get("this").put('elements', var.get('elements'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_54_._set_name('anonymous')
    @Js
    def PyJs_anonymous_55_(params, defaults, body, expression, this, arguments, var=var):
        var = Scope({'body':body, 'params':params, 'arguments':arguments, 'defaults':defaults, 'this':this, 'expression':expression}, var)
        var.registers(['body', 'expression', 'params', 'defaults'])
        var.get("this").put('type', var.get('Syntax').get('ArrowFunctionExpression'))
        var.get("this").put('id', var.get("null"))
        var.get("this").put('params', var.get('params'))
        var.get("this").put('defaults', var.get('defaults'))
        var.get("this").put('body', var.get('body'))
        var.get("this").put('generator', Js(False))
        var.get("this").put('expression', var.get('expression'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_55_._set_name('anonymous')
    @Js
    def PyJs_anonymous_56_(operator, left, right, this, arguments, var=var):
        var = Scope({'operator':operator, 'this':this, 'right':right, 'arguments':arguments, 'left':left}, var)
        var.registers(['operator', 'right', 'left'])
        var.get("this").put('type', var.get('Syntax').get('AssignmentExpression'))
        var.get("this").put('operator', var.get('operator'))
        var.get("this").put('left', var.get('left'))
        var.get("this").put('right', var.get('right'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_56_._set_name('anonymous')
    @Js
    def PyJs_anonymous_57_(left, right, this, arguments, var=var):
        var = Scope({'this':this, 'right':right, 'arguments':arguments, 'left':left}, var)
        var.registers(['right', 'left'])
        var.get("this").put('type', var.get('Syntax').get('AssignmentPattern'))
        var.get("this").put('left', var.get('left'))
        var.get("this").put('right', var.get('right'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_57_._set_name('anonymous')
    @Js
    def PyJs_anonymous_58_(operator, left, right, this, arguments, var=var):
        var = Scope({'operator':operator, 'this':this, 'right':right, 'arguments':arguments, 'left':left}, var)
        var.registers(['operator', 'right', 'left'])
        var.get("this").put('type', (var.get('Syntax').get('LogicalExpression') if (PyJsStrictEq(var.get('operator'),Js('||')) or PyJsStrictEq(var.get('operator'),Js('&&'))) else var.get('Syntax').get('BinaryExpression')))
        var.get("this").put('operator', var.get('operator'))
        var.get("this").put('left', var.get('left'))
        var.get("this").put('right', var.get('right'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_58_._set_name('anonymous')
    @Js
    def PyJs_anonymous_59_(body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'arguments':arguments}, var)
        var.registers(['body'])
        var.get("this").put('type', var.get('Syntax').get('BlockStatement'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_59_._set_name('anonymous')
    @Js
    def PyJs_anonymous_60_(label, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'label':label}, var)
        var.registers(['label'])
        var.get("this").put('type', var.get('Syntax').get('BreakStatement'))
        var.get("this").put('label', var.get('label'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_60_._set_name('anonymous')
    @Js
    def PyJs_anonymous_61_(callee, args, this, arguments, var=var):
        var = Scope({'this':this, 'args':args, 'callee':callee, 'arguments':arguments}, var)
        var.registers(['args', 'callee'])
        var.get("this").put('type', var.get('Syntax').get('CallExpression'))
        var.get("this").put('callee', var.get('callee'))
        var.get("this").put('arguments', var.get('args'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_61_._set_name('anonymous')
    @Js
    def PyJs_anonymous_62_(param, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'arguments':arguments, 'param':param}, var)
        var.registers(['body', 'param'])
        var.get("this").put('type', var.get('Syntax').get('CatchClause'))
        var.get("this").put('param', var.get('param'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_62_._set_name('anonymous')
    @Js
    def PyJs_anonymous_63_(body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'arguments':arguments}, var)
        var.registers(['body'])
        var.get("this").put('type', var.get('Syntax').get('ClassBody'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_63_._set_name('anonymous')
    @Js
    def PyJs_anonymous_64_(id, superClass, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'id':id, 'arguments':arguments, 'superClass':superClass}, var)
        var.registers(['body', 'id', 'superClass'])
        var.get("this").put('type', var.get('Syntax').get('ClassDeclaration'))
        var.get("this").put('id', var.get('id'))
        var.get("this").put('superClass', var.get('superClass'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_64_._set_name('anonymous')
    @Js
    def PyJs_anonymous_65_(id, superClass, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'id':id, 'arguments':arguments, 'superClass':superClass}, var)
        var.registers(['body', 'id', 'superClass'])
        var.get("this").put('type', var.get('Syntax').get('ClassExpression'))
        var.get("this").put('id', var.get('id'))
        var.get("this").put('superClass', var.get('superClass'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_65_._set_name('anonymous')
    @Js
    def PyJs_anonymous_66_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({'test':test, 'this':this, 'alternate':alternate, 'arguments':arguments, 'consequent':consequent}, var)
        var.registers(['test', 'alternate', 'consequent'])
        var.get("this").put('type', var.get('Syntax').get('ConditionalExpression'))
        var.get("this").put('test', var.get('test'))
        var.get("this").put('consequent', var.get('consequent'))
        var.get("this").put('alternate', var.get('alternate'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_66_._set_name('anonymous')
    @Js
    def PyJs_anonymous_67_(label, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'label':label}, var)
        var.registers(['label'])
        var.get("this").put('type', var.get('Syntax').get('ContinueStatement'))
        var.get("this").put('label', var.get('label'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_67_._set_name('anonymous')
    @Js
    def PyJs_anonymous_68_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get("this").put('type', var.get('Syntax').get('DebuggerStatement'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_68_._set_name('anonymous')
    @Js
    def PyJs_anonymous_69_(body, test, this, arguments, var=var):
        var = Scope({'body':body, 'test':test, 'this':this, 'arguments':arguments}, var)
        var.registers(['body', 'test'])
        var.get("this").put('type', var.get('Syntax').get('DoWhileStatement'))
        var.get("this").put('body', var.get('body'))
        var.get("this").put('test', var.get('test'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_69_._set_name('anonymous')
    @Js
    def PyJs_anonymous_70_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get("this").put('type', var.get('Syntax').get('EmptyStatement'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_70_._set_name('anonymous')
    @Js
    def PyJs_anonymous_71_(expression, this, arguments, var=var):
        var = Scope({'this':this, 'expression':expression, 'arguments':arguments}, var)
        var.registers(['expression'])
        var.get("this").put('type', var.get('Syntax').get('ExpressionStatement'))
        var.get("this").put('expression', var.get('expression'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_71_._set_name('anonymous')
    @Js
    def PyJs_anonymous_72_(init, test, update, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'init':init, 'arguments':arguments, 'test':test, 'update':update}, var)
        var.registers(['test', 'body', 'init', 'update'])
        var.get("this").put('type', var.get('Syntax').get('ForStatement'))
        var.get("this").put('init', var.get('init'))
        var.get("this").put('test', var.get('test'))
        var.get("this").put('update', var.get('update'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_72_._set_name('anonymous')
    @Js
    def PyJs_anonymous_73_(left, right, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'right':right, 'arguments':arguments, 'left':left}, var)
        var.registers(['body', 'right', 'left'])
        var.get("this").put('type', var.get('Syntax').get('ForOfStatement'))
        var.get("this").put('left', var.get('left'))
        var.get("this").put('right', var.get('right'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_73_._set_name('anonymous')
    @Js
    def PyJs_anonymous_74_(left, right, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'right':right, 'arguments':arguments, 'left':left}, var)
        var.registers(['body', 'right', 'left'])
        var.get("this").put('type', var.get('Syntax').get('ForInStatement'))
        var.get("this").put('left', var.get('left'))
        var.get("this").put('right', var.get('right'))
        var.get("this").put('body', var.get('body'))
        var.get("this").put('each', Js(False))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_74_._set_name('anonymous')
    @Js
    def PyJs_anonymous_75_(id, params, defaults, body, generator, this, arguments, var=var):
        var = Scope({'body':body, 'params':params, 'defaults':defaults, 'generator':generator, 'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['body', 'generator', 'params', 'id', 'defaults'])
        var.get("this").put('type', var.get('Syntax').get('FunctionDeclaration'))
        var.get("this").put('id', var.get('id'))
        var.get("this").put('params', var.get('params'))
        var.get("this").put('defaults', var.get('defaults'))
        var.get("this").put('body', var.get('body'))
        var.get("this").put('generator', var.get('generator'))
        var.get("this").put('expression', Js(False))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_75_._set_name('anonymous')
    @Js
    def PyJs_anonymous_76_(id, params, defaults, body, generator, this, arguments, var=var):
        var = Scope({'body':body, 'params':params, 'defaults':defaults, 'generator':generator, 'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['body', 'generator', 'params', 'id', 'defaults'])
        var.get("this").put('type', var.get('Syntax').get('FunctionExpression'))
        var.get("this").put('id', var.get('id'))
        var.get("this").put('params', var.get('params'))
        var.get("this").put('defaults', var.get('defaults'))
        var.get("this").put('body', var.get('body'))
        var.get("this").put('generator', var.get('generator'))
        var.get("this").put('expression', Js(False))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_76_._set_name('anonymous')
    @Js
    def PyJs_anonymous_77_(name, this, arguments, var=var):
        var = Scope({'this':this, 'name':name, 'arguments':arguments}, var)
        var.registers(['name'])
        var.get("this").put('type', var.get('Syntax').get('Identifier'))
        var.get("this").put('name', var.get('name'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_77_._set_name('anonymous')
    @Js
    def PyJs_anonymous_78_(test, consequent, alternate, this, arguments, var=var):
        var = Scope({'test':test, 'this':this, 'alternate':alternate, 'arguments':arguments, 'consequent':consequent}, var)
        var.registers(['test', 'alternate', 'consequent'])
        var.get("this").put('type', var.get('Syntax').get('IfStatement'))
        var.get("this").put('test', var.get('test'))
        var.get("this").put('consequent', var.get('consequent'))
        var.get("this").put('alternate', var.get('alternate'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_78_._set_name('anonymous')
    @Js
    def PyJs_anonymous_79_(label, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'arguments':arguments, 'label':label}, var)
        var.registers(['body', 'label'])
        var.get("this").put('type', var.get('Syntax').get('LabeledStatement'))
        var.get("this").put('label', var.get('label'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_79_._set_name('anonymous')
    @Js
    def PyJs_anonymous_80_(token, this, arguments, var=var):
        var = Scope({'this':this, 'token':token, 'arguments':arguments}, var)
        var.registers(['token'])
        var.get("this").put('type', var.get('Syntax').get('Literal'))
        var.get("this").put('value', var.get('token').get('value'))
        var.get("this").put('raw', var.get('source').callprop('slice', var.get('token').get('start'), var.get('token').get('end')))
        if var.get('token').get('regex'):
            var.get("this").put('regex', var.get('token').get('regex'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_80_._set_name('anonymous')
    @Js
    def PyJs_anonymous_81_(accessor, object, property, this, arguments, var=var):
        var = Scope({'this':this, 'property':property, 'object':object, 'accessor':accessor, 'arguments':arguments}, var)
        var.registers(['property', 'object', 'accessor'])
        var.get("this").put('type', var.get('Syntax').get('MemberExpression'))
        var.get("this").put('computed', PyJsStrictEq(var.get('accessor'),Js('[')))
        var.get("this").put('object', var.get('object'))
        var.get("this").put('property', var.get('property'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_81_._set_name('anonymous')
    @Js
    def PyJs_anonymous_82_(meta, property, this, arguments, var=var):
        var = Scope({'this':this, 'property':property, 'meta':meta, 'arguments':arguments}, var)
        var.registers(['property', 'meta'])
        var.get("this").put('type', var.get('Syntax').get('MetaProperty'))
        var.get("this").put('meta', var.get('meta'))
        var.get("this").put('property', var.get('property'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_82_._set_name('anonymous')
    @Js
    def PyJs_anonymous_83_(callee, args, this, arguments, var=var):
        var = Scope({'this':this, 'args':args, 'callee':callee, 'arguments':arguments}, var)
        var.registers(['args', 'callee'])
        var.get("this").put('type', var.get('Syntax').get('NewExpression'))
        var.get("this").put('callee', var.get('callee'))
        var.get("this").put('arguments', var.get('args'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_83_._set_name('anonymous')
    @Js
    def PyJs_anonymous_84_(properties, this, arguments, var=var):
        var = Scope({'this':this, 'properties':properties, 'arguments':arguments}, var)
        var.registers(['properties'])
        var.get("this").put('type', var.get('Syntax').get('ObjectExpression'))
        var.get("this").put('properties', var.get('properties'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_84_._set_name('anonymous')
    @Js
    def PyJs_anonymous_85_(properties, this, arguments, var=var):
        var = Scope({'this':this, 'properties':properties, 'arguments':arguments}, var)
        var.registers(['properties'])
        var.get("this").put('type', var.get('Syntax').get('ObjectPattern'))
        var.get("this").put('properties', var.get('properties'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_85_._set_name('anonymous')
    @Js
    def PyJs_anonymous_86_(operator, argument, this, arguments, var=var):
        var = Scope({'operator':operator, 'this':this, 'argument':argument, 'arguments':arguments}, var)
        var.registers(['operator', 'argument'])
        var.get("this").put('type', var.get('Syntax').get('UpdateExpression'))
        var.get("this").put('operator', var.get('operator'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").put('prefix', Js(False))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_86_._set_name('anonymous')
    @Js
    def PyJs_anonymous_87_(body, sourceType, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'sourceType':sourceType, 'arguments':arguments}, var)
        var.registers(['body', 'sourceType'])
        var.get("this").put('type', var.get('Syntax').get('Program'))
        var.get("this").put('body', var.get('body'))
        var.get("this").put('sourceType', var.get('sourceType'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_87_._set_name('anonymous')
    @Js
    def PyJs_anonymous_88_(kind, key, computed, value, method, shorthand, this, arguments, var=var):
        var = Scope({'kind':kind, 'shorthand':shorthand, 'computed':computed, 'this':this, 'value':value, 'arguments':arguments, 'key':key, 'method':method}, var)
        var.registers(['kind', 'shorthand', 'computed', 'value', 'key', 'method'])
        var.get("this").put('type', var.get('Syntax').get('Property'))
        var.get("this").put('key', var.get('key'))
        var.get("this").put('computed', var.get('computed'))
        var.get("this").put('value', var.get('value'))
        var.get("this").put('kind', var.get('kind'))
        var.get("this").put('method', var.get('method'))
        var.get("this").put('shorthand', var.get('shorthand'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_88_._set_name('anonymous')
    @Js
    def PyJs_anonymous_89_(argument, this, arguments, var=var):
        var = Scope({'this':this, 'argument':argument, 'arguments':arguments}, var)
        var.registers(['argument'])
        var.get("this").put('type', var.get('Syntax').get('RestElement'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_89_._set_name('anonymous')
    @Js
    def PyJs_anonymous_90_(argument, this, arguments, var=var):
        var = Scope({'this':this, 'argument':argument, 'arguments':arguments}, var)
        var.registers(['argument'])
        var.get("this").put('type', var.get('Syntax').get('ReturnStatement'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_90_._set_name('anonymous')
    @Js
    def PyJs_anonymous_91_(expressions, this, arguments, var=var):
        var = Scope({'this':this, 'expressions':expressions, 'arguments':arguments}, var)
        var.registers(['expressions'])
        var.get("this").put('type', var.get('Syntax').get('SequenceExpression'))
        var.get("this").put('expressions', var.get('expressions'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_91_._set_name('anonymous')
    @Js
    def PyJs_anonymous_92_(argument, this, arguments, var=var):
        var = Scope({'this':this, 'argument':argument, 'arguments':arguments}, var)
        var.registers(['argument'])
        var.get("this").put('type', var.get('Syntax').get('SpreadElement'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_92_._set_name('anonymous')
    @Js
    def PyJs_anonymous_93_(test, consequent, this, arguments, var=var):
        var = Scope({'test':test, 'this':this, 'arguments':arguments, 'consequent':consequent}, var)
        var.registers(['test', 'consequent'])
        var.get("this").put('type', var.get('Syntax').get('SwitchCase'))
        var.get("this").put('test', var.get('test'))
        var.get("this").put('consequent', var.get('consequent'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_93_._set_name('anonymous')
    @Js
    def PyJs_anonymous_94_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get("this").put('type', var.get('Syntax').get('Super'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_94_._set_name('anonymous')
    @Js
    def PyJs_anonymous_95_(discriminant, cases, this, arguments, var=var):
        var = Scope({'this':this, 'cases':cases, 'arguments':arguments, 'discriminant':discriminant}, var)
        var.registers(['cases', 'discriminant'])
        var.get("this").put('type', var.get('Syntax').get('SwitchStatement'))
        var.get("this").put('discriminant', var.get('discriminant'))
        var.get("this").put('cases', var.get('cases'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_95_._set_name('anonymous')
    @Js
    def PyJs_anonymous_96_(tag, quasi, this, arguments, var=var):
        var = Scope({'this':this, 'quasi':quasi, 'tag':tag, 'arguments':arguments}, var)
        var.registers(['quasi', 'tag'])
        var.get("this").put('type', var.get('Syntax').get('TaggedTemplateExpression'))
        var.get("this").put('tag', var.get('tag'))
        var.get("this").put('quasi', var.get('quasi'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_96_._set_name('anonymous')
    @Js
    def PyJs_anonymous_97_(value, tail, this, arguments, var=var):
        var = Scope({'this':this, 'tail':tail, 'arguments':arguments, 'value':value}, var)
        var.registers(['tail', 'value'])
        var.get("this").put('type', var.get('Syntax').get('TemplateElement'))
        var.get("this").put('value', var.get('value'))
        var.get("this").put('tail', var.get('tail'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_97_._set_name('anonymous')
    @Js
    def PyJs_anonymous_98_(quasis, expressions, this, arguments, var=var):
        var = Scope({'quasis':quasis, 'this':this, 'expressions':expressions, 'arguments':arguments}, var)
        var.registers(['quasis', 'expressions'])
        var.get("this").put('type', var.get('Syntax').get('TemplateLiteral'))
        var.get("this").put('quasis', var.get('quasis'))
        var.get("this").put('expressions', var.get('expressions'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_98_._set_name('anonymous')
    @Js
    def PyJs_anonymous_99_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get("this").put('type', var.get('Syntax').get('ThisExpression'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_99_._set_name('anonymous')
    @Js
    def PyJs_anonymous_100_(argument, this, arguments, var=var):
        var = Scope({'this':this, 'argument':argument, 'arguments':arguments}, var)
        var.registers(['argument'])
        var.get("this").put('type', var.get('Syntax').get('ThrowStatement'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_100_._set_name('anonymous')
    @Js
    def PyJs_anonymous_101_(block, handler, finalizer, this, arguments, var=var):
        var = Scope({'this':this, 'finalizer':finalizer, 'handler':handler, 'arguments':arguments, 'block':block}, var)
        var.registers(['finalizer', 'handler', 'block'])
        var.get("this").put('type', var.get('Syntax').get('TryStatement'))
        var.get("this").put('block', var.get('block'))
        var.get("this").put('guardedHandlers', Js([]))
        var.get("this").put('handlers', (Js([var.get('handler')]) if var.get('handler') else Js([])))
        var.get("this").put('handler', var.get('handler'))
        var.get("this").put('finalizer', var.get('finalizer'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_101_._set_name('anonymous')
    @Js
    def PyJs_anonymous_102_(operator, argument, this, arguments, var=var):
        var = Scope({'operator':operator, 'this':this, 'argument':argument, 'arguments':arguments}, var)
        var.registers(['operator', 'argument'])
        var.get("this").put('type', (var.get('Syntax').get('UpdateExpression') if (PyJsStrictEq(var.get('operator'),Js('++')) or PyJsStrictEq(var.get('operator'),Js('--'))) else var.get('Syntax').get('UnaryExpression')))
        var.get("this").put('operator', var.get('operator'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").put('prefix', var.get('true'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_102_._set_name('anonymous')
    @Js
    def PyJs_anonymous_103_(declarations, this, arguments, var=var):
        var = Scope({'this':this, 'declarations':declarations, 'arguments':arguments}, var)
        var.registers(['declarations'])
        var.get("this").put('type', var.get('Syntax').get('VariableDeclaration'))
        var.get("this").put('declarations', var.get('declarations'))
        var.get("this").put('kind', Js('var'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_103_._set_name('anonymous')
    @Js
    def PyJs_anonymous_104_(declarations, kind, this, arguments, var=var):
        var = Scope({'this':this, 'kind':kind, 'declarations':declarations, 'arguments':arguments}, var)
        var.registers(['kind', 'declarations'])
        var.get("this").put('type', var.get('Syntax').get('VariableDeclaration'))
        var.get("this").put('declarations', var.get('declarations'))
        var.get("this").put('kind', var.get('kind'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_104_._set_name('anonymous')
    @Js
    def PyJs_anonymous_105_(id, init, this, arguments, var=var):
        var = Scope({'this':this, 'init':init, 'id':id, 'arguments':arguments}, var)
        var.registers(['init', 'id'])
        var.get("this").put('type', var.get('Syntax').get('VariableDeclarator'))
        var.get("this").put('id', var.get('id'))
        var.get("this").put('init', var.get('init'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_105_._set_name('anonymous')
    @Js
    def PyJs_anonymous_106_(test, body, this, arguments, var=var):
        var = Scope({'test':test, 'body':body, 'this':this, 'arguments':arguments}, var)
        var.registers(['test', 'body'])
        var.get("this").put('type', var.get('Syntax').get('WhileStatement'))
        var.get("this").put('test', var.get('test'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_106_._set_name('anonymous')
    @Js
    def PyJs_anonymous_107_(object, body, this, arguments, var=var):
        var = Scope({'body':body, 'this':this, 'object':object, 'arguments':arguments}, var)
        var.registers(['body', 'object'])
        var.get("this").put('type', var.get('Syntax').get('WithStatement'))
        var.get("this").put('object', var.get('object'))
        var.get("this").put('body', var.get('body'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_107_._set_name('anonymous')
    @Js
    def PyJs_anonymous_108_(local, exported, this, arguments, var=var):
        var = Scope({'this':this, 'local':local, 'exported':exported, 'arguments':arguments}, var)
        var.registers(['local', 'exported'])
        var.get("this").put('type', var.get('Syntax').get('ExportSpecifier'))
        var.get("this").put('exported', (var.get('exported') or var.get('local')))
        var.get("this").put('local', var.get('local'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_108_._set_name('anonymous')
    @Js
    def PyJs_anonymous_109_(local, this, arguments, var=var):
        var = Scope({'this':this, 'local':local, 'arguments':arguments}, var)
        var.registers(['local'])
        var.get("this").put('type', var.get('Syntax').get('ImportDefaultSpecifier'))
        var.get("this").put('local', var.get('local'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_109_._set_name('anonymous')
    @Js
    def PyJs_anonymous_110_(local, this, arguments, var=var):
        var = Scope({'this':this, 'local':local, 'arguments':arguments}, var)
        var.registers(['local'])
        var.get("this").put('type', var.get('Syntax').get('ImportNamespaceSpecifier'))
        var.get("this").put('local', var.get('local'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_110_._set_name('anonymous')
    @Js
    def PyJs_anonymous_111_(declaration, specifiers, src, this, arguments, var=var):
        var = Scope({'this':this, 'specifiers':specifiers, 'src':src, 'arguments':arguments, 'declaration':declaration}, var)
        var.registers(['specifiers', 'src', 'declaration'])
        var.get("this").put('type', var.get('Syntax').get('ExportNamedDeclaration'))
        var.get("this").put('declaration', var.get('declaration'))
        var.get("this").put('specifiers', var.get('specifiers'))
        var.get("this").put('source', var.get('src'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_111_._set_name('anonymous')
    @Js
    def PyJs_anonymous_112_(declaration, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'declaration':declaration}, var)
        var.registers(['declaration'])
        var.get("this").put('type', var.get('Syntax').get('ExportDefaultDeclaration'))
        var.get("this").put('declaration', var.get('declaration'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_112_._set_name('anonymous')
    @Js
    def PyJs_anonymous_113_(src, this, arguments, var=var):
        var = Scope({'this':this, 'src':src, 'arguments':arguments}, var)
        var.registers(['src'])
        var.get("this").put('type', var.get('Syntax').get('ExportAllDeclaration'))
        var.get("this").put('source', var.get('src'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_113_._set_name('anonymous')
    @Js
    def PyJs_anonymous_114_(local, imported, this, arguments, var=var):
        var = Scope({'this':this, 'imported':imported, 'local':local, 'arguments':arguments}, var)
        var.registers(['imported', 'local'])
        var.get("this").put('type', var.get('Syntax').get('ImportSpecifier'))
        var.get("this").put('local', (var.get('local') or var.get('imported')))
        var.get("this").put('imported', var.get('imported'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_114_._set_name('anonymous')
    @Js
    def PyJs_anonymous_115_(specifiers, src, this, arguments, var=var):
        var = Scope({'this':this, 'specifiers':specifiers, 'arguments':arguments, 'src':src}, var)
        var.registers(['specifiers', 'src'])
        var.get("this").put('type', var.get('Syntax').get('ImportDeclaration'))
        var.get("this").put('specifiers', var.get('specifiers'))
        var.get("this").put('source', var.get('src'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_115_._set_name('anonymous')
    @Js
    def PyJs_anonymous_116_(argument, delegate, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'argument':argument, 'delegate':delegate}, var)
        var.registers(['argument', 'delegate'])
        var.get("this").put('type', var.get('Syntax').get('YieldExpression'))
        var.get("this").put('argument', var.get('argument'))
        var.get("this").put('delegate', var.get('delegate'))
        var.get("this").callprop('finish')
        return var.get("this")
    PyJs_anonymous_116_._set_name('anonymous')
    PyJs_Object_49_ = Js({'processComment':PyJs_anonymous_50_,'finish':PyJs_anonymous_51_,'finishArrayExpression':PyJs_anonymous_53_,'finishArrayPattern':PyJs_anonymous_54_,'finishArrowFunctionExpression':PyJs_anonymous_55_,'finishAssignmentExpression':PyJs_anonymous_56_,'finishAssignmentPattern':PyJs_anonymous_57_,'finishBinaryExpression':PyJs_anonymous_58_,'finishBlockStatement':PyJs_anonymous_59_,'finishBreakStatement':PyJs_anonymous_60_,'finishCallExpression':PyJs_anonymous_61_,'finishCatchClause':PyJs_anonymous_62_,'finishClassBody':PyJs_anonymous_63_,'finishClassDeclaration':PyJs_anonymous_64_,'finishClassExpression':PyJs_anonymous_65_,'finishConditionalExpression':PyJs_anonymous_66_,'finishContinueStatement':PyJs_anonymous_67_,'finishDebuggerStatement':PyJs_anonymous_68_,'finishDoWhileStatement':PyJs_anonymous_69_,'finishEmptyStatement':PyJs_anonymous_70_,'finishExpressionStatement':PyJs_anonymous_71_,'finishForStatement':PyJs_anonymous_72_,'finishForOfStatement':PyJs_anonymous_73_,'finishForInStatement':PyJs_anonymous_74_,'finishFunctionDeclaration':PyJs_anonymous_75_,'finishFunctionExpression':PyJs_anonymous_76_,'finishIdentifier':PyJs_anonymous_77_,'finishIfStatement':PyJs_anonymous_78_,'finishLabeledStatement':PyJs_anonymous_79_,'finishLiteral':PyJs_anonymous_80_,'finishMemberExpression':PyJs_anonymous_81_,'finishMetaProperty':PyJs_anonymous_82_,'finishNewExpression':PyJs_anonymous_83_,'finishObjectExpression':PyJs_anonymous_84_,'finishObjectPattern':PyJs_anonymous_85_,'finishPostfixExpression':PyJs_anonymous_86_,'finishProgram':PyJs_anonymous_87_,'finishProperty':PyJs_anonymous_88_,'finishRestElement':PyJs_anonymous_89_,'finishReturnStatement':PyJs_anonymous_90_,'finishSequenceExpression':PyJs_anonymous_91_,'finishSpreadElement':PyJs_anonymous_92_,'finishSwitchCase':PyJs_anonymous_93_,'finishSuper':PyJs_anonymous_94_,'finishSwitchStatement':PyJs_anonymous_95_,'finishTaggedTemplateExpression':PyJs_anonymous_96_,'finishTemplateElement':PyJs_anonymous_97_,'finishTemplateLiteral':PyJs_anonymous_98_,'finishThisExpression':PyJs_anonymous_99_,'finishThrowStatement':PyJs_anonymous_100_,'finishTryStatement':PyJs_anonymous_101_,'finishUnaryExpression':PyJs_anonymous_102_,'finishVariableDeclaration':PyJs_anonymous_103_,'finishLexicalDeclaration':PyJs_anonymous_104_,'finishVariableDeclarator':PyJs_anonymous_105_,'finishWhileStatement':PyJs_anonymous_106_,'finishWithStatement':PyJs_anonymous_107_,'finishExportSpecifier':PyJs_anonymous_108_,'finishImportDefaultSpecifier':PyJs_anonymous_109_,'finishImportNamespaceSpecifier':PyJs_anonymous_110_,'finishExportNamedDeclaration':PyJs_anonymous_111_,'finishExportDefaultDeclaration':PyJs_anonymous_112_,'finishExportAllDeclaration':PyJs_anonymous_113_,'finishImportSpecifier':PyJs_anonymous_114_,'finishImportDeclaration':PyJs_anonymous_115_,'finishYieldExpression':PyJs_anonymous_116_})
    var.get('WrappingNode').put('prototype', var.get('Node').put('prototype', PyJs_Object_49_))
    var.get('exports').put('version', Js('2.6.0'))
    var.get('exports').put('tokenize', var.get('tokenize'))
    var.get('exports').put('parse', var.get('parse'))
    @Js
    def PyJs_anonymous_160_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['name', 'types'])
        PyJs_Object_161_ = Js({})
        var.put('types', PyJs_Object_161_)
        if PyJsStrictEq(var.get('Object').get('create').typeof(),Js('function')):
            var.put('types', var.get('Object').callprop('create', var.get("null")))
        for PyJsTemp in var.get('Syntax'):
            var.put('name', PyJsTemp)
            if var.get('Syntax').callprop('hasOwnProperty', var.get('name')):
                var.get('types').put(var.get('name'), var.get('Syntax').get(var.get('name')))
        if PyJsStrictEq(var.get('Object').get('freeze').typeof(),Js('function')):
            var.get('Object').callprop('freeze', var.get('types'))
        return var.get('types')
    PyJs_anonymous_160_._set_name('anonymous')
    var.get('exports').put('Syntax', PyJs_anonymous_160_())
PyJs_anonymous_0_._set_name('anonymous')
@Js
def PyJs_anonymous_162_(root, factory, this, arguments, var=var):
    var = Scope({'this':this, 'root':root, 'factory':factory, 'arguments':arguments}, var)
    var.registers(['root', 'factory'])
    Js('use strict')
    if (PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and var.get('define').get('amd')):
        var.get('define')(Js([Js('exports')]), var.get('factory'))
    else:
        if PyJsStrictNeq(var.get('exports',throw=False).typeof(),Js('undefined')):
            var.get('factory')(var.get('exports'))
        else:
            PyJs_Object_163_ = Js({})
            var.get('factory')(var.get('root').put('esprima', PyJs_Object_163_))
PyJs_anonymous_162_._set_name('anonymous')
PyJs_anonymous_162_(var.get("this"), PyJs_anonymous_0_)
pass


# Added manually
esprima = var.to_python().esprima # this will now behave exactly like JS esprima object

if __name__=='__main__':

    JSON = var.to_python().JSON
    print(('version', esprima.version))

    print('parsing var odds = evens.map(v => v + 1);')
    tree = esprima.parse('var odds = evens.map(v => v + 1);')
    py_tree = tree.to_dict()

    print((JSON.stringify(py_tree, None, 4)))

    another_tree = esprima.parse('export var answer = 42', {'sourceType': 'module' })
    print((JSON.stringify(another_tree, None, 4)))



