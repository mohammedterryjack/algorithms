from typing import Union

class BinaryString:
    def __init__(self, value:Union[str,int], length:int=10) -> None:
        if isinstance(value,str):
            self.binary_string = value
            self.length = len(value)
            self.integer_value = self.convert_binary_string_to_int(self.binary_string)
        elif isinstance(value,int):
            self.length = length
            self.integer_value = value
            self.binary_string = self.convert_integer_to_binary_string(self.integer_value,self.length)
        else:
            raise ValueError
    
    def __str__(self) -> str:
        return self.binary_string
    
    def __int__(self) -> int:
        return self.integer_value
    
    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.integer_value += 1
        self.binary_string = self.convert_integer_to_binary_string(self.integer_value,self.length)
        old_length = self.length
        self.length = len(self.binary_string)
        if self.length > old_length:
            raise StopIteration
        return self 

    @staticmethod
    def convert_integer_to_binary_string(number:int,length:int=10) -> str:
        return format(number, f'#0{length+2}b')[2:]

    @staticmethod
    def convert_binary_string_to_int(binary_string:str) -> int:
        return int(binary_string,base=2)


#efficiently explore combinations
#for permutation in BinaryString("00000"):
#    print(permutation)
