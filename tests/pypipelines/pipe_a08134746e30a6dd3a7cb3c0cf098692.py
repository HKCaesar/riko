# Pipe pipe_a08134746e30a6dd3a7cb3c0cf098692 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipestrconcat import pipe_strconcat
from pipe2py.modules.pipexpathfetchpage import pipe_xpathfetchpage
from pipe2py.modules.pipeloop import pipe_loop
from pipe2py.modules.piperename import pipe_rename
from pipe2py.modules.pipecreaterss import pipe_createrss
from pipe2py.modules.pipeoutput import pipe_output


def pipe_a08134746e30a6dd3a7cb3c0cf098692(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return [u'pipecreaterss', u'pipeloop', u'pipeoutput', u'piperename', u'pipestrconcat', u'pipexpathfetchpage']

    forever = pipe_forever()

    # We need to wrap submodules (used by loops) so we can pass the
    # input at runtime (as we can to subpipelines)
    def pipe_sw_515(context=None, item=None, conf=None, **kwargs):
        # todo: insert submodule description here
        return pipe_strconcat(
            context, forever, conf={'part': [{'type': 'text', 'value': '<img src="'}, {'type': 'text', 'subkey': 'img.src'}, {'type': 'text', 'value': '">'}]})

    sw_327 = pipe_xpathfetchpage(
        context, forever, conf={'URL': {'type': 'url', 'value': 'http://pinterest.com/popular/'}, 'xpath': {'type': 'text', 'value': "//a[@class='PinImage ImgLink']"}})

    sw_507 = pipe_loop(
        context, sw_327, embed=pipe_sw_515, conf={'assign_part': {'type': 'text', 'value': 'all'}, 'assign_to': {'type': 'text', 'value': 'description'}, 'emit_part': {'type': 'text', 'value': 'all'}, 'mode': {'type': 'text', 'value': 'assign'}, 'embed': {'type': 'module', 'value': {'type': 'strconcat', 'id': 'sw-515', 'conf': {'part': [{'type': 'text', 'value': '<img src="'}, {'type': 'text', 'subkey': 'img.src'}, {'type': 'text', 'value': '">'}]}}}, 'with': {'type': 'text', 'value': ''}})

    sw_303 = pipe_rename(
        context, sw_507, conf={'RULE': {'field': {'type': 'text', 'value': 'href'}, 'op': {'type': 'text', 'value': 'rename'}, 'newval': {'type': 'text', 'value': 'link'}}})

    sw_443 = pipe_createrss(
        context, sw_303, conf={'mediaContentHeight': {'type': 'text', 'value': ''}, 'mediaThumbURL': {'type': 'text', 'value': ''}, 'mediaContentType': {'type': 'text', 'value': ''}, 'description': {'type': 'text', 'value': ''}, 'pubdate': {'type': 'text', 'value': ''}, 'author': {'type': 'text', 'value': ''}, 'title': {'type': 'text', 'value': 'img.alt'}, 'mediaThumbHeight': {'type': 'text', 'value': ''}, 'link': {'type': 'text', 'value': ''}, 'mediaContentWidth': {'type': 'text', 'value': ''}, 'mediaContentURL': {'type': 'text', 'value': 'img.src'}, 'guid': {'type': 'text', 'value': ''}, 'mediaThumbWidth': {'type': 'text', 'value': ''}})

    sw_261 = pipe_output(
        context, sw_443, conf=None)

    return sw_261


if __name__ == "__main__":
    pipeline = pipe_a08134746e30a6dd3a7cb3c0cf098692(Context())

    for i in pipeline:
        print i
