from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler):
        
        self.next=defaultdict(RouteTrieNode)
        self.handler=handler
        # Initialize the node with children as before, plus a handler

   # def insert(self, ...):
        # Insert the node as before
    
    
class RouteTrie:
    def __init__(self, roothandler=None):
        self.root=RouteTrieNode(roothandler)

        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, path,handler):
        pathparts=self.get_path_parts(path)
        node=self.root
        for part in path_parts:
            if part!='':
                node=node.next[part]
                
        node.handler=handler
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, path):
        part_paths=self.get_path_parts(path)
        node=self.root
        
        for part in path_parts:
            if part!='':
                node=node.next[part]
        return node.handler
    
    def get_path_parts(self,path):
        return path.split('/')
    
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class Router:
    def __init__(self, root_handler):  self.route_trie = RouteTrie(root_handler)

    def add_handler(self, path, handler): self.route_trie.insert(path, handler)

    def lookup(self, path): return self.route_trie.find(path)
if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home", "home handler")  # add a route
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home/about/me/edit", "edit handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'home handler'
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler'
    print(router.lookup("/home/about/me/edit"))  # should print 'edit handler'
