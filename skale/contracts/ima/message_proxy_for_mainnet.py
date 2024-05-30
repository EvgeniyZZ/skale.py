from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak

#PAUSABLE_ROLE  EXTRA_CONTRACT_REGISTRAR_ROLE
class MessageProxyForMainnet(BaseContract): 
    @transaction_method
    def register_extra_contract(self, schain_name: str, contract_address: int) -> TxRes:
        return self.contract.functions.registerExtraContract(schain_name, contract_address)

    @transaction_method
    def remove_extra_contract(self, schain_name: str, contract_address: int) -> TxRes:
        return self.contract.functions.removeExtraContract(schain_name, contract_address)

    @transaction_method
    def add_reimbursed_contract(self, schain_name: str, contract_address: int) -> TxRes:
        return self.contract.functions.addReimbursedContract(schain_name, contract_address)

    @transaction_method
    def remove_reimbursed_contracts(self, schain_name: str, contract_address: int) -> TxRes:
        return self.contract.functions.removeReimbursedContract(schain_name, contract_address)

    @transaction_method
    def pause(self, schain_name: str) -> TxRes:
        return self.contract.functions.pause(schain_name)

    @transaction_method
    def resume(self, schain_name: str) -> TxRes:
        return self.contract.functions.resume(schain_name)

    def is_connected_chain(self, schain_name: str) -> bool:
        return self.contract.functions.isConnectedChain(schain_name)

    def is_reimbursed_contract(self, schain_name: str) -> bool:
        return self.contract.functions.isReimbursedContract(schain_name)

    def is_paused(self, schian_name: str) -> bool:
        return self.contract.functions.isPaused(schian_name)

    def extra_contract_register_role(self) -> bytes:
        return self.contract.functions.EXTRA_CONTRACT_REGISTRAR_ROLE().call()

    def pausable_role(self) -> bytes:
        return self.contract.functions.PAUSABLE_ROLE().call()

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    def get_role_member(self, role: bytes, index: int) -> bytes:
        return self.contract.functions.getRoleMember(role, index).call()
