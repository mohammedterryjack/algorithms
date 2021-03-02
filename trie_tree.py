from json import dumps

class TrieTree:
    def __init__(self) -> None:
        self.ROOT = {}

    def __repr__(self) -> str:
        return dumps(self.ROOT, indent=1)

    def insert_word(self, word:str) -> None:
        current_node = self.ROOT
        for child_node in word.lower():
            if child_node not in current_node: 
                current_node[child_node] = {}
            current_node = current_node.get(child_node)
        current_node[None] = {}

    def word_in_tree(self, word:str) -> bool:
        current_node = self.ROOT
        for child_node in word.lower():
            current_node = current_node.get(child_node)            
            if current_node is None: return False
        return self.is_end_of_a_word(current_node)

    @staticmethod
    def is_end_of_a_word(node:dict) -> bool:
        return None in node

#tree = TrieTree()
#for word in  ["the","they","there","thank"]:
#    print(word,tree.word_in_tree(word))
#    tree.insert_word(word)
#    print(word,tree.word_in_tree(word))
#    print()
#print(tree)
