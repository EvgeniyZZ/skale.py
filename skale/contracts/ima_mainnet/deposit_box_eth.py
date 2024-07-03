from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak

class DepositBoxEth(BaseContract):
    @transaction_method
    def deposit(self, schain_name: str) -> TxRes:
        return self.contract.functions.deposit(schain_name)

    @transaction_method
    def deposit_direct(self, schain_name: str, receiver: int) -> TxRes: 
        return self.contract.functions.depositDirect(schain_name, receiver) 

    @transaction_method
    def get_my_eth(self) -> TxRes:
        return self.contract.functions.getMyEth()

    @transaction_method
    def enable_active_eth_transfers(self, schain_name: str) -> TxRes:
        return self.contract.functions.enableActiveEthTransfers(schain_name)

    def approve_transfers(self, address) -> int:
        return self.contract.functions.approveTransfers(address).call()

    def is_active_transfers(self, schain_name: str) -> bool:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        hash = keccak_hash.digest()
        return self.contract.functions.activeEthTransfers(hash).call()

    @transaction_method
    def disable_active_eth_transfers(self, schain_name: str) -> TxRes:
        return self.contract.functions.disableActiveEthTransfers(schain_name)

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)
