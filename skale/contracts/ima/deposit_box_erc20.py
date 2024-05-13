from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak

class DepositBoxERC20(BaseContract):
    @transaction_method
    def add_erc20_token(self, schain_name: str, address: int) -> TxRes:
        return self.contract.functions.addERC20TokenByOwner(schain_name, address)
    

    @transaction_method
    def deposit_erc20(self,schain_name: str, address: int, amount: int) -> TxRes:
        return self.contract.functions.depositERC20(schain_name, address, amount)
    

    @transaction_method
    def deposit_erc20_direct(self, schain_name: str, address: int, amount: int, receiver: int) -> TxRes:
        return self.contract.functions.depositERC20Direct(schain_name, address, amount, receiver)
    
    
    @transaction_method
    def set_big_transfer_value(self, schain_name: str, token: int, value: int) -> TxRes:
        return self.contract.functions.setBigTransferValue(schain_name,token,value)
    
    
    @transaction_method
    def set_big_transfer_delay(self, schain_name: str, delay: int) -> TxRes:
        return self.contract.functions.setBigTransferDelay(schain_name, delay)
    
    
    @transaction_method
    def set_arbitrage_duration(self, schain_name: str, delay: int) -> TxRes:
        return self.contract.functions.setArbitrageDuration(schain_name, delay)
    
    
    @transaction_method
    def trust_receiver(self, schain_name: str, address: int) -> TxRes:
        return self.contract.functions.trustReceiver(schain_name, address)   


    def is_receiver_trusted(self, schain_hash: bytes, address: int) -> bool:
        keccak_hash = keccak.new(data=schain_hash.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.isReceiverTrusted(schain_id, address).call()
    

    def arbiter_role(self) -> bytes:
        return self.contract.functions.ARBITER_ROLE().call()
    
    
    def admin_role(self) -> bytes:
        return self.contract.functions.DEFAULT_ADMIN_ROLE().call()
    

    def has_arbiter_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role,address).call()
    
    
    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)
    

    def get_role_member(self, role: bytes, index: int) -> bytes:
        return self.contract.functions.getRoleMember(role, index).call()
