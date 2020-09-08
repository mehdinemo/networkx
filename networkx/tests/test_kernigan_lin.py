import pytest
from random import shuffle
import networkx as nx
from networkx.algorithms.community import kernighan_lin


class TestKerniganLin:
    def test_defined_partition_str_nodes(self):
        G = nx.Graph([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")])

        labels = list(G)
        shuffle(labels)

        with pytest.raises(KeyError):
            for i in range(1, len(labels)):
                k_partition = (set(labels[0:i]), set(labels[i:len(labels)]))
                partitions = kernighan_lin.kernighan_lin_bisection(G, partition=k_partition)

    def test_defined_partition_int_nodes(self):
        G = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 4)])

        labels = list(G)
        shuffle(labels)

        with pytest.raises(KeyError):
            for i in range(1, len(labels)):
                k_partition = (set(labels[0:i]), set(labels[i:len(labels)]))
                partitions = kernighan_lin.kernighan_lin_bisection(G, partition=k_partition)
