import os


class Node(object):

	def __init__(self, data):
		self.data = data
		self.siblings = []
		self.children = None


class Tree(object):

	def __init__(self, model_path):
		root, name = os.path.split(model_path)
		self.root = Node(name)
		self.model_path = model_path

	def find_sibling(self, data):
		"""return data node or None if not found"""
		for s in node.siblings:
			if s.data == data: return s
		return None

	def find_child(self, node, data):
		"""return data node or None if not found"""
		for c in node.children:
			if c.data == data: return c
		return None

	def add_sibling(self, node, data):
		if find_sibling(data) is None:
			node.siblings.append(Node(data))

	def add_child(self, parent, data):
		if find_child(node, data) is None:
			node.children.append(Node(data))

	def builder(self):
		for dirpath, dirnames, filenames in os.walk(self.model_path):
			print("dirpath:", dirpath)
			for d in dirnames:
				print("\tdir:", d)
			for f in filenames:
				print("\tfile:", f)

if __name__ == '__main__':
	MODELDIR = '/Users/rblack/_dev/math-magik-lpp/scad/math-magik-lpp'
	t = Tree(MODELDIR)
	t.builder()



