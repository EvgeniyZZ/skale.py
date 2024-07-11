from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes


class TokenManagerLinker(BaseContract):
    """Linker"""

    @transaction_method
    def connect_schain(self, schain_name) -> TxRes:
        return self.contract.functions.connectSchain(schain_name)

    @transaction_method
    def disconnect_schain(self, schain_name) -> TxRes:
        return self.contract.functions.disconnectSchain(schain_name)

    def has_schain(self, schian_name) -> bool:
        return self.contract.functions.hasSchain(schian_name).call()

    def registrar_role(self) -> bytes:
        return self.contract.functions.REGISTRAR_ROLE()

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)