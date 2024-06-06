from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes



class MessageProxyForSchain(BaseContract):
    @transaction_method
    def set_minimum_receiver_balance(self, amount: int) -> TxRes: 
        return self.contract.functions.setMinimumReceiverBalance(amount)

    def get_minimum_receiver_balance(self) - int:
        return self.contract.functions.minimumReceiverBalance().call()

    def constant_setter_role(self) -> bytes:
        return self.contract.functions.CONSTANT_SETTER_ROLE().call()

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)