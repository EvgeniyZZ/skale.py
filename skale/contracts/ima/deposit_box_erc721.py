from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak


class DepositBoxERC721(BaseContract):
    @transaction_method
    def deposit_erc721(self, schain_name: str, address: int, tokenID: int) -> TxRes: 
        return self.contract.functions.depositERC721(schain_name, address, tokenID)

    def 
    