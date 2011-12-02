import re, yaml, markdown2, functools

markdown = functools.partial(markdown2.markdown, extras = ['code-friendly', 'code-color'])

def filter_markdown_files(prospects):
    predicate = lambda x: x.endswith('.md') or x.endswith('.markdown')
    return filter(predicate, prospects)
    
def split_post(post):
    raw_content = post.read().strip()
    parse_expression = re.compile('\<!--\n?~~~(?P<metadata>.*)~~~\n?-->(?P<content>.*)', flags = re.MULTILINE + re.DOTALL)
    matches = re.match(parse_expression, raw_content)
    return yaml.load(matches.group('metadata')), matches.group('content').strip()

def parse(post):
    metadata, content = split_post(post)
    return metadata, markdown(content)