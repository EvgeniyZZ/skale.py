from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak


class DepositBoxERC1155(BaseContract):
    """Class deposit"""
    @transaction_method
    def deposit_box_erc1155(self, schain_name: str, address: int, token_id: int, amount: int) -> TxRes:
        """Deposit ERC1155"""
        return self.contract.functions.depositERC1155(schain_name, address, token_id, amount)
    
    