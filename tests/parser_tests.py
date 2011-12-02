import unittest, os, datetime
import parser

class ParserTest(unittest.TestCase):
    def test_markdown_file_filter(self):
        prospects = [
            'file.txt',
            'file2.md',
            'file3.doc',
            'file4.markdown',
            '/dir1/file5.md',
            '/dir1/file6.txt'
        ]
        self.assertEqual(['file2.md', 'file4.markdown', '/dir1/file5.md'], 
                parser.filter_markdown_files(prospects))
    
    def test_yaml_splitter(self):
        post = open('tests/sample.md', 'r')
        expected_yaml = dict(
            title = 'Tracking changes to files',
            publish = True,            
            tags = ['python', 'forklift'],
            slug = '/tracking-changes-to-files',
            date = datetime.date(2011, 11, 27)
        )
        actual_yaml, post_content = parser.split_post(post)
        self.assertEqual(expected_yaml, actual_yaml)
        self.assertIn('#Tracking changes to files', post_content)
        self.assertIn('And Some other stuff', post_content)
        self.assertNotIn('~~~', post_content)
        
    
        