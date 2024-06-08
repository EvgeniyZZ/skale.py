from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak



class CommunityLocker(BaseContract):
    @transaction_method
    def set_time_limit_per_message(self, schain_name: str, new_time_limit: int) -> TxRes:
        '''Set time limit'''
        return self.contract.functions.setTimeLimitPerMessage(schain_name, new_time_limit)

    def constant_setter_role(self) -> bytes:    
        return self.contract.functions.CONSTANT_SETTER_ROLE().call()

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)