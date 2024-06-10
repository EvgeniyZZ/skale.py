from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak


class DepositBoxERC721(BaseContract):
    @transaction_method
    def deposit_erc721(self, schain_name: str, address: int, tokenID: int) -> TxRes: 
        return self.contract.functions.depositERC721(schain_name, address, tokenID)

    @transaction_method
    def add_erc721_token(self, schain_name: str, address: int) -> TxRes:
        return self.contract.functions.addERC721TokenByOwner(schain_name, address)

    def deposit_erc721_direct(self, schain_name: str, address: int, token_id: int, receiver: int) -> TxRes:
        return self.contract.functions.depositERC721Direct(schain_name, address, token_id, receiver)

    def get_schain_to_erc721(self, schain_name, token_address) -> int:
        return self.contract.functions.getSchainToERC721(schain_name, token_address)
