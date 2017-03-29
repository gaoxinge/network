from twisted.web.client import Agent, readBody
from twisted.internet import reactor

def cbRequest(cb_response):
    global response
    response.append(cb_response.code)
    d = readBody(cb_response)
    d.addCallback(cbBody)
    return d

def cbBody(cb_body):
    global response
    print 'Response'
    response.append(cb_body)

def method_url(method, url):
    agent = Agent(reactor)
    d = agent.request(method, url)
    d.addCallbacks(cbRequest)
    d.addCallback(lambda ignored: reactor.stop())
    reactor.run()

def request(method, url):
    global response
    response = []
    method_url(method, url)
    return response
