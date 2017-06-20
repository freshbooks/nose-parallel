import unittest
from noseparallel import ParallelPlugin


class PluginTest(unittest.TestCase):

    def test_want_file_should_accept_on_either_nodes_but_not_both(self):
        plugin = ParallelPlugin()
        plugin.salt = 'test'
        plugin.total_nodes = 2
        testFile = open("tests/plugin_test.py", "r")
        plugin.node_index = 0
        rv0 = plugin.wantFile(testFile)

        plugin.node_index = 1
        rv1 = plugin.wantFile(testFile)
        self.assertEqual({None, False}, {rv0, rv1})
