##
# Copyright (c) 2008-2010, 2014 MagicStack Inc.
# All rights reserved.
#
# See LICENSE for details.
##


from metamagic.utils import parsing, debug

from metamagic.caos.lang.caosql.errors import CaosQLQueryError
from metamagic.caos.lang.caosql.parser.errors import CaosQLSyntaxError

from .grammar import lexer


class CaosQLParserBase(parsing.Parser):
    def get_debug(self):
        return 'caos.lang.caosql.parser' in debug.channels

    def get_exception(self, native_err, context):
        return CaosQLQueryError(native_err.args[0], context=context)

    def get_lexer(self):
        return lexer.CaosQLLexer()


class CaosQLExpressionParser(CaosQLParserBase):
    def get_parser_spec_module(self):
        from .grammar import single
        return single


class CaosQLBlockParser(CaosQLParserBase):
    def get_parser_spec_module(self):
        from .grammar import block
        return block
