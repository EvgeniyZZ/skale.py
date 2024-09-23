from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes


class Paymaster(BaseContract):
    """Paymaster contract"""

    def get_reward_amount(self, validator_id: int) -> int:
        return self.contract.functions.getRewardAmount(validator_id).call()
