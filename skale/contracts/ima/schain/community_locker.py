from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak


class CommunityLocker(BaseContract):
    """ "Community locker"""

    @transaction_method
    def set_time_limit_per_message(
        self, schain_name: str, new_time_limit: int
    ) -> TxRes:
        """Set time limit"""
        return self.contract.functions.setTimeLimitPerMessage(
            schain_name, new_time_limit
        )

    def constant_setter_role(self) -> bytes:
        return self.contract.functions.CONSTANT_SETTER_ROLE().call()

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    @transaction_method
    def grant_role(self, role: bytes, address: int) -> TxRes:
        return self.contract.functions.grantRole(role, address)

    def check_allow_to_send_msg(self, schain_hash: bytes, address: int) -> int:
        keccak_hash = keccak.new(data=schain_hash.encode("utf8"), digest_bits=256)
        hash = keccak_hash.digest()
        return self.contract.functions.checkAllowedToSendMessage(hash, address).call()

    def schain_hash(self) -> bytes:
        return self.contract.functions.schainHash().call()

    def mainnet_hash(self) -> bytes:
        return self.contract.functions.MAINNET_HASH().call()

    def is_active_user(self, address) -> bool:
        return self.contract.functions.activeUsers(address).call()

    def last_message_timestamp(self, address) -> int:
        return self.contract.functions.lastMessageTimeStamp(address).call()

    def time_limit_per_msg(self, schain_hash: bytes) -> int:
        keccak_hash = keccak.new(data=schain_hash.encode("utf8"), digest_bits=256)
        hash = keccak_hash.digest()
        return self.contract.functions.timeLimitPerMessage(hash).call()
