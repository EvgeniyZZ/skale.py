from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak



class CommunityPool(BaseContract):  
    def check_user_balance(self, schain_name: bytes, receiver: int ) -> bool:
        keccak_hash = keccak.new(data=schain_name.encode("utf8"), digest_bits=256)
        schain_id = keccak_hash.digest()
        return self.contract.functions.checkUserBalance(schain_id,receiver).call()
    

    












