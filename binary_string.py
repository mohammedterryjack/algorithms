from typing import Union

class BinaryString:
    def __init__(self, value:Union[str,int], length:int=10) -> None:
        if isinstance(value,str):
            self.initialise_binary_string(value)
        elif isinstance(value,int):
            self.initialise_integer_value(value,length)
        else:
            raise ValueError
    
    def initialise_binary_string(self,binary_string:str) -> None:
        self.integer_value = self.convert_binary_string_to_int(binary_string)
        self.binary_string = binary_string
        self.length = len(binary_string)

    def initialise_integer_value(self,integer_value:int,length:int) -> None:
        self.integer_value = integer_value
        self.binary_string = self.convert_integer_to_binary_string(integer_value,length)
        self.length = len(self.binary_string)

    def __str__(self) -> str:
        return self.binary_string
    
    def __int__(self) -> int:
        return self.integer_value
    
    def __iter__(self):
        return self

    def __next__(self) -> str:
        old_length = self.length
        self.initialise_integer_value(self.integer_value+1, self.length)
        if self.length > old_length:
            raise StopIteration
        return self 

    @staticmethod
    def convert_integer_to_binary_string(number:int,length:int=10) -> str:
        return format(number, f'#0{length+2}b')[2:]

    @staticmethod
    def convert_binary_string_to_int(binary_string:str) -> int:
        return int(binary_string,base=2)

# for permutation in BinaryString("000"):
#     chosen_indices = list(map(int,str(permutation)))
#     print(permutation, chosen_indices)
