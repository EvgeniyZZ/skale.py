from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak



class CommunityPool(BaseContract):
    @transaction_method
    def recharge_user_wallet(self, schain_name: str, address: int) -> TxRes:
        return self.contract.functions.rechargeUserWallet(schain_name, address)

    @transaction_method
    def withdraw_funds(self, schain_name: str, amount: int) -> TxRes:
        return self.contract.functions.withdrawFunds(schain_name, amount)

    @transaction_method
    def set_min_transaction_gas(self, min_gas_value: int) -> TxRes:
        return self.contract.functions.setMinTransactionGas(min_gas_value)

    @transaction_method
    def set_multiplier(self, new_multiplier_numertor: int, new_multiplier_divider: int) -> TxRes:
        return self.contract.functions.setMultiplier(new_multiplier_numertor, new_multiplier_divider)

    def get_balance(self, address: int, schain_name: str) -> int:
        return self.contract.functions.getBalance(address, schain_name).call()

    def check_user_balance(self, schain_name: bytes, receiver: int) -> bool:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.checkUserBalance(schain_id,receiver).call()

    def get_recomended_recharge_amount(self, schain_hash: bytes, receiver: int) -> int:
        keccak_hash = keccak.new(data=schain_hash.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.getRecommendedRechargeAmount(schain_id, receiver).call()

    def constant_setter_role(self) -> bool:
        return self.contract.functions.CONSTANT_SETTER_ROLE().call()

    def admin_role(self) -> bytes:
        return self.contract.functions.DEFAULT_ADMIN_ROLE().call()

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)

    def get_role_member(self, role: bytes, index: int) -> bytes:
        return self.contract.functions.getRoleMember(role, index).call()
