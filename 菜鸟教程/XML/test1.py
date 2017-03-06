from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print 'start_element: %s, attrs: %s' % (name, str(attrs))
        
    def end_element(self, name):
        print 'end_element: %s' % name
        
    def char_data(self, text):
        print 'char_data: %s' % text
        
if __name__ == '__main__':
    # parser
    parser = ParserCreate()
    parser.returns_unicode = True

    # handler
    handler = DefaultSaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data

    # parse
    with open('movies.xml', 'r') as f:
        xml = f.read()
    parser.Parse(xml)
