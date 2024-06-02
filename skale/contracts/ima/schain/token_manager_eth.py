from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes


class TokenManagerETH(BaseContract):
    @transaction_method
    def exit_to_main(self, amount: int) -> TxRes:
        return self.contract.functions.exitToMain(amount)

    def get_erc20(self) -> int:
        return self.contract.functions.ethErc20().call()
