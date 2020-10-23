from Block import Block 

blockchain = []

genesis_block = Block("Chancellor on brink of second bailout for banks", ["Satoshi sent 1 BTC to Laurent", 
         "Maria sent 5 BTC to Jenny",
         "Satoshi sent 5 BTC to Hal Finney"])

second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz", "John sent 5 BTC to Jenny"])
third_block = Block(second_block.block_hash, ["Laurent sent 5 BTC to Stephan", "Stephan sent 2.5 BTC to Francis"])


print("Genesis block")
print(genesis_block.block_hash)
print("Second block")
print(second_block.block_hash)
print("Third block")
print(third_block.block_hash)
