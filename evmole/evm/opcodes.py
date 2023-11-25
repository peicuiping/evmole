from enum import Enum


class Op(int, Enum):
    def __new__(cls, code, *args, **kwds):
        obj = int.__new__(cls, code)
        obj._value_ = code
        return obj

    def __init__(self, code, stack_in=0, stack_out=0, blen=1, gas=None) -> None:
        self.code = code
        self.stack_in = stack_in
        self.stack_out = stack_out
        self.blen = blen
        self.gas: int | None = gas

    STOP = (0x00, 0, 0, 1, 0)
    ADD = (0x01, 2, 1, 1, 3)
    MUL = (0x02, 2, 1, 1, 5)
    SUB = (0x03, 2, 1, 1, 3)
    DIV = (0x04, 2, 1, 1, 5)
    SDIV = (0x05, 2, 1, 1, 5)
    MOD = (0x06, 2, 1, 1, 5)
    SMOD = (0x07, 2, 1, 1, 5)
    ADDMOD = (0x08, 3, 1, 1, 8)
    MULMOD = (0x09, 3, 1, 1, 8)
    EXP = (0x0A, 2, 1, 1, None)
    SIGNEXTEND = (0x0B, 2, 1, 1, 5)

    LT = (0x10, 2, 1, 1, 3)
    GT = (0x11, 2, 1, 1, 3)
    SLT = (0x12, 2, 1, 1, 3)
    SGT = (0x13, 2, 1, 1, 3)
    EQ = (0x14, 2, 1, 1, 3)
    ISZERO = (0x15, 1, 1, 1, 3)
    AND = (0x16, 2, 1, 1, 3)
    OR = (0x17, 2, 1, 1, 3)
    XOR = (0x18, 2, 1, 1, 3)
    NOT = (0x19, 1, 1, 1, 3)
    BYTE = (0x1A, 2, 1, 1, 3)
    SHL = (0x1B, 2, 1, 1, 3)
    SHR = (0x1C, 2, 1, 1, 3)
    SAR = (0x1D, 2, 1, 1, 3)

    KECCAK256 = (0x20, 2, 1, 1, None)

    ADDRESS = (0x30, 0, 1, 1, 2)
    BALANCE = (0x31, 1, 1, 1, None)
    ORIGIN = (0x32, 0, 1, 1, 2)
    CALLER = (0x33, 0, 1, 1, 2)
    CALLVALUE = (0x34, 0, 1, 1, 2)
    CALLDATALOAD = (0x35, 1, 1, 1, 3)
    CALLDATASIZE = (0x36, 0, 1, 1, 2)
    CALLDATACOPY = (0x37, 3, 0, 1, None)
    CODESIZE = (0x38, 0, 1, 1, 2)
    CODECOPY = (0x39, 3, 0, 1, None)
    GASPRICE = (0x3A, 0, 1, 1, 2)
    EXTCODESIZE = (0x3B, 1, 1, 1, None)
    EXTCODECOPY = (0x3C, 4, 0, 1, None)
    RETURNDATASIZE = (0x3D, 0, 1, 1, None)
    RETURNDATACOPY = (0x3E, 3, 0, 1, None)
    EXTCODEHASH = (0x3F, 1, 1, 1, None)

    BLOCKHASH = (0x40, 1, 1, 1, 20)
    COINBASE = (0x41, 0, 1, 1, 2)
    TIMESTAMP = (0x42, 0, 1, 1, 2)
    NUMBER = (0x43, 0, 1, 1, 2)
    DIFFICULTY = (0x44, 0, 1, 1, 2)
    GASLIMIT = (0x45, 0, 1, 1, 2)
    CHAINID = (0x46, 0, 1, 1, 2)
    SELFBALANCE = (0x47, 0, 1, 1, 5)
    BASEFEE = (0x48, 0, 1, 1, 2)

    POP = (0x50, 1, 0, 1, 2)
    MLOAD = (0x51, 1, 1, 1, None)
    MSTORE = (0x52, 2, 0, 1, None)
    MSTORE8 = (0x53, 2, 0, 1, None)
    SLOAD = (0x54, 1, 1, 1, None)
    SSTORE = (0x55, 2, 0, 1, None)
    JUMP = (0x56, 1, 0, 1, 8)
    JUMPI = (0x57, 2, 0, 1, 10)
    PC = (0x58, 0, 1, 1, 2)
    MSIZE = (0x59, 0, 1, 1, 2)
    GAS = (0x5A, 0, 1, 1, 2)
    JUMPDEST = (0x5B, 0, 0, 1, 1)
    PUSH0 = (0x5F, 0, 1, 1, 2)

    PUSH1 = (0x60, 0, 1, 2, 3)
    PUSH2 = (0x61, 0, 1, 3, 3)
    PUSH3 = (0x62, 0, 1, 4, 3)
    PUSH4 = (0x63, 0, 1, 5, 3)
    PUSH5 = (0x64, 0, 1, 6, 3)
    PUSH6 = (0x65, 0, 1, 7, 3)
    PUSH7 = (0x66, 0, 1, 8, 3)
    PUSH8 = (0x67, 0, 1, 9, 3)
    PUSH9 = (0x68, 0, 1, 10, 3)
    PUSH10 = (0x69, 0, 1, 11, 3)
    PUSH11 = (0x6A, 0, 1, 12, 3)
    PUSH12 = (0x6B, 0, 1, 13, 3)
    PUSH13 = (0x6C, 0, 1, 14, 3)
    PUSH14 = (0x6D, 0, 1, 15, 3)
    PUSH15 = (0x6E, 0, 1, 16, 3)
    PUSH16 = (0x6F, 0, 1, 17, 3)

    PUSH17 = (0x70, 0, 1, 18, 3)
    PUSH18 = (0x71, 0, 1, 19, 3)
    PUSH19 = (0x72, 0, 1, 20, 3)
    PUSH20 = (0x73, 0, 1, 21, 3)
    PUSH21 = (0x74, 0, 1, 22, 3)
    PUSH22 = (0x75, 0, 1, 23, 3)
    PUSH23 = (0x76, 0, 1, 24, 3)
    PUSH24 = (0x77, 0, 1, 25, 3)
    PUSH25 = (0x78, 0, 1, 26, 3)
    PUSH26 = (0x79, 0, 1, 27, 3)
    PUSH27 = (0x7A, 0, 1, 28, 3)
    PUSH28 = (0x7B, 0, 1, 29, 3)
    PUSH29 = (0x7C, 0, 1, 30, 3)
    PUSH30 = (0x7D, 0, 1, 31, 3)
    PUSH31 = (0x7E, 0, 1, 32, 3)
    PUSH32 = (0x7F, 0, 1, 33, 3)

    DUP1 = (0x80, 1, 2, 1, 3)
    DUP2 = (0x81, 2, 3, 1, 3)
    DUP3 = (0x82, 3, 4, 1, 3)
    DUP4 = (0x83, 4, 5, 1, 3)
    DUP5 = (0x84, 5, 6, 1, 3)
    DUP6 = (0x85, 6, 7, 1, 3)
    DUP7 = (0x86, 7, 8, 1, 3)
    DUP8 = (0x87, 8, 9, 1, 3)
    DUP9 = (0x88, 9, 10, 1, 3)
    DUP10 = (0x89, 10, 11, 1, 3)
    DUP11 = (0x8A, 11, 12, 1, 3)
    DUP12 = (0x8B, 12, 13, 1, 3)
    DUP13 = (0x8C, 13, 14, 1, 3)
    DUP14 = (0x8D, 14, 15, 1, 3)
    DUP15 = (0x8E, 15, 16, 1, 3)
    DUP16 = (0x8F, 16, 17, 1, 3)

    SWAP1 = (0x90, 2, 2, 1, 3)
    SWAP2 = (0x91, 3, 3, 1, 3)
    SWAP3 = (0x92, 4, 4, 1, 3)
    SWAP4 = (0x93, 5, 5, 1, 3)
    SWAP5 = (0x94, 6, 6, 1, 3)
    SWAP6 = (0x95, 7, 7, 1, 3)
    SWAP7 = (0x96, 8, 8, 1, 3)
    SWAP8 = (0x97, 9, 9, 1, 3)
    SWAP9 = (0x98, 10, 10, 1, 3)
    SWAP10 = (0x99, 11, 11, 1, 3)
    SWAP11 = (0x9A, 12, 12, 1, 3)
    SWAP12 = (0x9B, 13, 13, 1, 3)
    SWAP13 = (0x9C, 14, 14, 1, 3)
    SWAP14 = (0x9D, 15, 15, 1, 3)
    SWAP15 = (0x9E, 16, 16, 1, 3)
    SWAP16 = (0x9F, 17, 17, 1, 3)

    LOG0 = (0xA0, 2, 0, 1, None)
    LOG1 = (0xA1, 3, 0, 1, None)
    LOG2 = (0xA2, 4, 0, 1, None)
    LOG3 = (0xA3, 5, 0, 1, None)
    LOG4 = (0xA4, 6, 0, 1, None)

    CREATE = (0xF0, 3, 1, 1, None)
    CALL = (0xF1, 7, 1, 1, None)
    CALLCODE = (0xF2, 7, 1, 1, None)
    RETURN = (0xF3, 2, 0, 1, None)
    DELEGATECALL = (0xF4, 6, 1, 1, None)
    CREATE2 = (0xF5, 4, 1, 1, None)

    STATICCALL = (0xFA, 6, 1, 1, None)
    REVERT = (0xFD, 2, 0, 1, None)
    INVALID = (0xFE, 0, 0, 1, None)
    SELFDESTRUCT = (0xFF, 1, 0, 1, None)
