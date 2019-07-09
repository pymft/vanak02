class Tree:
    name = "derakht"
    is_something = True


    def get_height_of_tree(self):
        return self.height


tree_1 = Tree()
tree_1.height = 12

tree_2 = Tree()
tree_2.height = 10
tree_2.name = "not a derakht"

tree_3 = Tree()
tree_3.height = 100
tree_3.age = 50


res = Tree.get_height_of_tree(tree_1)


# print(Tree.__dict__)
# for tree in [tree_1, tree_2, tree_3]:
    # print(tree.__dict__)
    # print(tree.name, tree.is_something, tree.height)
