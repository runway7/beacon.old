import logging, re

def filter_markdown_files(prospects):
    predicate = lambda x: x.endswith('.md') or x.endswith('.markdown')
    return filter(predicate, prospects)
    
def split_post(post):
    import yaml
    raw_content = post.read()
    parse_exp = re.compile('\<!--\n?~~~(.*)~~~\n?-->(.*)', flags = re.MULTILINE + re.DOTALL)
    matches = re.match(parse_exp, raw_content)
    logging.info(matches.group(1))
    return yaml.load(matches.group(1)), matches.group(2)
    
    

    
        