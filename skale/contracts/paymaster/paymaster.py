from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak


class Paymaster(BaseContract):
    """Paymaster contract"""

    @transaction_method
    def add_schain(self, schain_name: str) -> TxRes:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.addSchain(schain_id)
    
    @transaction_method
    def remove_schain(self, schain_name: str) -> TxRes:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.removeSchain(schain_id)
    
    @transaction_method
    def add_validator(self, validator_id: int, validator_address: int) -> TxRes:
        return self.contract.functions.addValidator(validator_id, validator_address)
    
    @transaction_method
    def remove_validator(self, validator_id: int) -> TxRes:
        return self.contract.functions.removeValidator(validator_id)
    
    @transaction_method
    def set_validator_address(self, validator_id: int, new_address: int) -> TxRes:
        return self.contract.functions.setValidatorAddress(validator_id, new_address)
    
    @transaction_method
    def set_active_nodes(self, validator_id: int, nodes_amount: int) -> TxRes:
        return self.contract.functions.setActiveNodes(validator_id, nodes_amount)

    @transaction_method
    def set_max_replenishment_period(self, month: int) -> TxRes:
        return self.contract.functions.setMaxReplenishmentPeriod(month)
    
    @transaction_method
    def set_schain_price(self, price: int) -> TxRes:
        return self.contract.functions.setSchainPrice(price)
    
    @transaction_method
    def set_skl_price(self, price: int) -> TxRes:
        return self.contract.functions.setSklPrice(price)
    
    @transaction_method
    def set_allowed_skl_price_lag(self, lag_seconds: int) -> TxRes:
        return self.contract.functions.setAllowedSklPriceLag(lag_seconds)
    
    @transaction_method
    def set_skale_token(self, token_address: int) -> TxRes:
        return self.contract.functions.setSkaleToken(token_address)
    
    @transaction_method
    def clear_history(self, timestamp_before: int) -> TxRes:
        return self.contract.functions.clearHistory(timestamp_before)
    
    @transaction_method
    def pay(self, schain_name: str, month: int) -> TxRes:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.pay(schain_id, month)

    @transaction_method
    def claim(self, to_address: int) -> TxRes:
        return self.contract.functions.claim(to_address)
    
    @transaction_method
    def set_version(self, new_version) -> TxRes:
        return self.contract.functions.setVersion(new_version)
    
    def get_schain_expiration_timestamp(self, schain_name: str) -> TxRes:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.getSchainExpirationTimestamp(schain_id).call()
    
    def get_reward_amount(self, validator_id: int) -> int:
        return self.contract.functions.getRewardAmount(validator_id).call()
    
    def get_nodes_number(self, validator_id: int) -> int:
        return self.contract.functions.getNodesNumber(validator_id).call()