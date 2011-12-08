import re, yaml, markdown2, functools

to_yaml = yaml.load
to_markdown = functools.partial(markdown2.markdown, extras = ['code-friendly', 'code-color'])
parse_expression = re.compile('\<!--\n?~~~(?P<metadata>.*)~~~\n?-->(?P<content>.*)', flags = re.MULTILINE + re.DOTALL)

def filter_markdown_files(prospects):
    predicate = lambda x: x.endswith('.md') or x.endswith('.markdown')
    return filter(predicate, prospects)
    
def split_post(post):
    raw_content = post.read().strip()    
    matches = re.match(parse_expression, raw_content)
    return matches.group('metadata').strip(), matches.group('content').strip()

def parse(post):
    metadata, content = split_post(post)
    return to_yaml(metadata), to_markdown(content)