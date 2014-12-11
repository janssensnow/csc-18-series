from lettuce import *
from proxy import Proxy


@step(u'a proxy is started')
def a_proxy_is_started(step):
    proxy1 = Proxy()

@step(u'the proxy increments the count')
def the_proxy_increments_the_count(step):
    proxy1 = Proxy()
    assert_equal(proxy1.reference_count, 1)

#@step(u'the counted object is then sorted')
  #proxy1 = Proxy()

@step(u'Given I initialize proxy')
def given_i_initialize_proxy(step):
    assert False, 'This step must be implemented'
@step(u'And proxy is started')
def and_proxy_is_started(step):
    assert False, 'This step must be implemented'
@step(u'When the object is instantiated')
def when_the_object_is_instantiated(step):
    assert False, 'This step must be implemented'
@step(u'Then proxy counts then increments and sorts it')
def then_proxy_counts_then_increments_and_sorts_it(step):
    assert False, 'This step must be implemented'