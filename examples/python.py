from evmole import function_selectors

# output of `solc example.sol --bin-runtime --optimize`
code = '0x6080604052600436106025575f3560e01c8063b69ef8a8146029578063d0e30db014604d575b5f80fd5b3480156033575f80fd5b50603b5f5481565b60405190815260200160405180910390f35b60536055565b005b345f8082825460639190606a565b9091555050565b80820180821115608857634e487b7160e01b5f52601160045260245ffd5b9291505056fea2646970667358221220354240f63068d555e9b817619001b0dff6ea630d137edc1a640dae8e3ebb959864736f6c63430008170033'

r = function_selectors(code)
print('all signatures with default gas_limit', r)

r = function_selectors(code, gas_limit=100)
print('only 1 signature found with so low gas limit', r)

r = function_selectors(code, gas_limit=200)
print('200 gas is enough for all 2 signatures', r)
