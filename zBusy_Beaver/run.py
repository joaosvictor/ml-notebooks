# 6 possible states/
# 2 values
# 2 moves
# 6*2*2 = 24
# 24^10 possible for sigma(5, 2)

# See Tree Normal Form from Bra66

#t0 = "B1L A1L C1R B1R A1L D1R A1L E1R H1L C0R".split(" ")
t0 = "B1L C1R C1L B1L D1L E0R A1R D1R H1L A0R".split(" ")

def run(t0, ms=-1):
  t = [0]*30000
  pos = 15000
  s = "A"

  
  
  #O(log n)
  
  cnt = 0
  halt = True
  while 1:
    assert pos > 0
    assert pos < len(t)
    #if cnt%1000 == 0:
    #  print(cnt, s, pos)
    ns = ord(s) - ord("A")
    if t[pos] == 0:
      tt = t0[ns*2+0]
    elif t[pos] == 1:
      tt = t0[ns*2+1]
    s = tt[0]
    t[pos] = int(tt[1])
    if tt[2] == "L":
      pos -= 1
    else:
      pos += 1
    cnt += 1
    if s == "H":
      break
    if ms != -1 and cnt > ms:
      halt = False
      break
  return halt, cnt, sum(t)

def draw(t0):
  import matplotlib.pyplot as plt
  import networkx as nx
  G = nx.DiGraph()

  for i,x in enumerate(t0):
    ts = chr(ord("A") + i//2)
    ns = x[0]
    lbl = str(i%2)+x[1:]
    G.add_edge(ts, ns, label=lbl)

  pos = nx.spring_layout(G)
  nx.draw_networkx(G, pos)
  edge_labels = nx.get_edge_attributes(G, 'label')
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
  plt.show()


if __name__ == "__main__":
  print(run(t0))
  #draw(t0)
'''
# https://sci-hub.tw/10.1109/PGEC.1966.264572
# Hmm, the tree normal form description is kind of annoying, it's a graph, right?
# Oh, "Attacking the Busy Beaver 5" has a clearer description
# Does the first move need to print a one?

# A0 = B1L looks like the default start in "Attacking the Busy Beaver 5"
# E0 | E1 = H1L is the final one

# They even seem to be reasoning about the machines while they generate them
# This is a little annoying as the function can only be computed in order

# Hmm https://arxiv.org/pdf/1610.03184.pdf

from run import run

# 4*2*2 = 16
# 16^6 possible for sigma(3, 2)

def gen(x,b=3):
  e = (b+1)*2*2
  ret = []
  for i in range(b*2):
    t = x%e
    ss = "L" if t%2 else "R"
    t //= 2
    ss = ("0" if t%2 else "1") + ss
    t //= 2
    if t==b:
      ss = "H" + ss
    else:
      ss = chr(ord("A") + t) + ss
    ret.append(ss)
    x //= e
  return ret

if __name__ == "__main__":
  b = 3
  all_s = 0
  all_sigma = 0
  for m in range(((b+1)*2*2)**(b*2)):
    mm = gen(m, b)
    halt, s, sigma = run(mm, ms=100)
    print(mm, halt, s, sigma, all_s, all_sigma)
    if halt:
      all_s = max(s, all_s)
      all_sigma = max(sigma, all_sigma)
 graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)


class SQLAlchemy(object):
    class Engine(object):
        """Emulates SQLAlchemy look-a-like in our examples."""


def create_engine(db_uri: str):
    """Creates fake engine."""
    return SQLAlchemy.Engine()


@pytest.fixture(autouse=True)
def setup_doctest_context(doctest_namespace):
    """Here we register all classes that we use in our doctest examples."""
    doctest_namespace["SQLAlchemy"] = SQLAlchemy
    doctest_namespace["create_engine"] = 
    
    
    from typing import List

import pytest
from expects import be, be_a, equal, expect, have_len
from tempfile import NamedTemporaryFile
import os
from punq import (
    Container,
    Scope,
    InvalidRegistrationException,
    MissingDependencyException,
)
from tests.test_dependencies import (
    FancyDbMessageWriter,
    HelloWorldSpeaker,
    MessageSpeaker,
    MessageWriter,
    StdoutMessageWriter,
    TmpFileMessageWriter,
    WrappingMessageWriter,
)


def test_can_create_instance_with_no_dependencies():
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter)
    expect(container.resolve(MessageWriter)).to(be_a(StdoutMessageWriter))


def test_dependencies_are_injected():
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter)
    container.register(MessageSpeaker, HelloWorldSpeaker)

    speaker = container.resolve(MessageSpeaker)

    expect(speaker).to(be_a(HelloWorldSpeaker))
    expect(speaker.writer).to(be_a(StdoutMessageWriter))


def test_missing_dependencies_raise_exception():
    container = Container()
    container.register(MessageSpeaker, HelloWorldSpeaker)

    with pytest.raises(MissingDependencyException):
        container.resolve(MessageSpeaker)


def test_can_register_a_concrete_type():
    container = Container()
    container.register(StdoutMessageWriter)

    expect(container.resolve(StdoutMessageWriter)).to(be_a(StdoutMessageWriter))


def test_can_register_with_a_custom_factory():
    container = Container()
    container.register(MessageWriter, lambda: "win")
    container.register(MessageSpeaker, HelloWorldSpeaker)

    speaker = container.resolve(MessageSpeaker)

    expect(speaker).to(be_a(HelloWorldSpeaker))
    expect(speaker.writer).to(equal("win"))


def test_can_register_an_instance():
    container = Container()
    writer = TmpFileMessageWriter("my-file")
    container.register(MessageWriter, instance=writer)
    expect(container.resolve(MessageWriter)).to(equal(writer))


def test_resolves_instances():
    """
    No scope specified should work the way transient scope works
    """
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter)

    mw1 = container.resolve(MessageWriter)
    mw2 = container.resolve(MessageWriter)
    expect(mw1).not_to(equal(mw2))


def test_resolves_instances_with_singleton_scope():
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter, scope=Scope.singleton)

    mw1 = container.resolve(MessageWriter)
    mw2 = container.resolve(MessageWriter)
    expect(mw1).to(equal(mw2))


def test_resolves_instances_with_prototype_scope():
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter, scope=Scope.transient)

    mw1 = container.resolve(MessageWriter)
    mw2 = container.resolve(MessageWriter)
    expect(mw1).not_to(equal(mw2))


def test_registering_an_instance_as_concrete_is_exception():
    """
    Concrete registrations need to be a constructable type
    or there's no key we can use for resolution.
    """
    container = Container()
    writer = MessageWriter()

    with pytest.raises(InvalidRegistrationException):
        container.register(writer)


def test_registering_an_instance_as_factory_is_exception():
    """
    Concrete registrations need to be a constructable type
    or there's no key we can use for resolution.
    """
    container = Container()
    writer = MessageWriter()

    with pytest.raises(InvalidRegistrationException):
        container.register(MessageWriter, writer)


def test_registering_a_callable_as_concrete_is_exception():
    """
    Likewise, if we register an arbitrary callable, there's
    no key by which we can later resolve, so we reject the
    registration
    """

    container = Container()

    with pytest.raises(InvalidRegistrationException):
        container.register(lambda: "oops")


def test_can_provide_arguments_to_registrations():
    container = Container()
    container.register(MessageWriter, FancyDbMessageWriter, cstr=lambda: "Hello world")

    writer = container.resolve(MessageWriter)

    expect(writer).to(be_a(FancyDbMessageWriter))
    expect(writer.connection_string).to(equal("Hello world"))


def test_can_provide_arguments_to_resolve():
    container = Container()
    container.register(MessageWriter, TmpFileMessageWriter)

    instance = container.resolve(MessageWriter, path="foo")
    expect(instance.path).to(equal("foo"))


def test_can_provide_arguments_to_resolve_having_dependencies():
    container = Container()
    container.register(StdoutMessageWriter, StdoutMessageWriter)
    container.register(MessageWriter, WrappingMessageWriter)

    instance = container.resolve(MessageWriter, context="bar")
    expect(instance.context).to(equal("bar"))


def test_can_provide_typed_arguments_to_resolve():
    container = Container()
    container.register(MessageWriter, TmpFileMessageWriter)
    container.register(TmpFileMessageWriter)
    container.register(HelloWorldSpeaker)

    tmpfile = NamedTemporaryFile()

    writer = container.resolve(MessageWriter, path=tmpfile.name)
    speaker = container.resolve(HelloWorldSpeaker, writer=writer)

    speaker.speak()

    tmpfile.seek(0)
    expect(tmpfile.read().decode()).to(equal("Hello World"))


def test_resolve_returns_the_latest_registration_for_a_service():
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter)

    container.register(MessageWriter, TmpFileMessageWriter, path="my-file")

    expect(container.resolve(MessageWriter)).to(be_a(TmpFileMessageWriter))


def test_resolve_all_returns_all_registrations_in_order():
    container = Container()
    container.register(MessageWriter, StdoutMessageWriter)
    container.register(MessageWriter, TmpFileMessageWriter, path="my-file")

    [first, second] = container.resolve_all(MessageWriter)
    expect(first).to(be_a(StdoutMessageWriter))
    expect(second).to(be_a(TmpFileMessageWriter))


def test_can_use_a_string_key():
    container = Container()
    container.register("foo", instance=1)
    assert container.resolve("foo") == 1
    '''



