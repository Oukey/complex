import unittest
import SimpleTree


class SimpleTreeTest(unittest.TestCase):
    '''
    0 --                 ch1
                       /    \
    1 --           ch2       ch3
    '''

    def test_norm(self):
        ch1 = SimpleTree.SimpleTreeNode(1, None)
        ch2 = SimpleTree.SimpleTreeNode(2, None)
        ch3 = SimpleTree.SimpleTreeNode(3, None)
        tree = SimpleTree.SimpleTree(None)
        self.assertIsNone(tree.Root)
        tree.AddChild(None, ch1)
        self.assertEqual(tree.Root, ch1)
        tree.AddChild(tree.Root, ch2)
        tree.AddChild(tree.Root, ch3)
        self.assertEqual(tree.Root.Children, [ch2, ch3])
        tree.DeleteNode(ch2)
        self.assertEqual(ch1.Children, [ch3])

        '''
        0 --                 rt(0)
                           /       \
        1 --           ch1          ch2
                      /   \       /    \
        2 --       ch3    ch4   ch5    ch6
        '''

    @staticmethod
    def creat_tree():
        rt = SimpleTree.SimpleTreeNode(0, None)
        ch1 = SimpleTree.SimpleTreeNode(1, None)
        ch2 = SimpleTree.SimpleTreeNode(2, None)
        ch3 = SimpleTree.SimpleTreeNode(1, None)
        ch4 = SimpleTree.SimpleTreeNode(2, None)
        ch5 = SimpleTree.SimpleTreeNode(1, None)
        ch6 = SimpleTree.SimpleTreeNode(4, None)
        tree = SimpleTree.SimpleTree(rt)
        tree.AddChild(tree.Root, ch1)
        tree.AddChild(tree.Root, ch2)
        tree.AddChild(ch1, ch3)
        tree.AddChild(ch1, ch4)
        tree.AddChild(ch2, ch5)
        tree.AddChild(ch2, ch6)
        return tree

    def test_Get_Find(self):
        tree = self.creat_tree()
        self.assertEqual(len(tree.GetAllNodes()), 7)
        self.assertEqual(list(node.NodeValue for node in tree.Root.Children), [1, 2])
        self.assertEqual(len(tree.FindNodesByValue(0)), 1)
        self.assertEqual(len(tree.FindNodesByValue(1)), 3)
        self.assertEqual(len(tree.FindNodesByValue(2)), 2)
        self.assertEqual(len(tree.FindNodesByValue(3)), 0)

    def test_count(self):
        tree = self.creat_tree()
        self.assertEqual(tree.Count(), 3)
        self.assertEqual(tree.LeafCount(), 4)
        ch7 = SimpleTree.SimpleTreeNode(7, None)
        ch8 = SimpleTree.SimpleTreeNode(8, None)
        ch6 = tree.Root.Children[1].Children[1]
        tree.AddChild(ch6, ch7)
        self.assertEqual(tree.Count(), 4)
        self.assertEqual(tree.LeafCount(), 4)
        tree.AddChild(tree.Root.Children[0], ch8)
        self.assertEqual(tree.Count(), 4)
        self.assertEqual(tree.LeafCount(), 5)

    def test_MoveNode(self):
        tree = self.creat_tree()
        self.assertEqual(len(tree.Root.Children), 2)
        self.assertEqual(len(tree.Root.Children[0].Children), 2)
        self.assertEqual(len(tree.Root.Children[1].Children), 2)
        ch1 = tree.Root.Children[0]
        ch2 = tree.Root.Children[1]
        tree.MoveNode(ch2, ch1)
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertEqual(len(tree.Root.Children[0].Children), 3)

    def test_get_level(self):
        tree = self.creat_tree()
        ch8 = SimpleTree.SimpleTreeNode(8, None)
        tree.AddChild(tree.Root.Children[0].Children[0], ch8)

        self.assertEqual(tree.Root.get_level(), 0)
        self.assertEqual(tree.Root.Children[0].get_level(), 1)
        self.assertEqual(tree.Root.Children[0].Children[0].get_level(), 2)
        self.assertEqual(ch8.get_level(), 3)


if __name__ == '__main__':
    unittest.main()
