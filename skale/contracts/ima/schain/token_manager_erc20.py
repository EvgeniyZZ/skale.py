from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes




class TokenManagerERC20(BaseContract):
    @transaction_method
    def exit_to_main_erc20(self, token_address: int, amount: int) -> TxRes:
        return self.contract.functions.exitToMainERC20(token_address, amount)

    @transaction_method
    def transfer_to_schain_erc20(self, schain_name: str, token_address: int, amount: int) -> TxRes:
        return self.contract.functions.transferToSchainERC20(schain_name, token_address, amount)

    @transaction_method
    def add_erc20_token(self, schain_name: str, token_mn: int, token_sc: int) -> TxRes:
        return self.contract.functions.addERC20TokenByOwner(schain_name, token_mn, token_sc)

    def automatic_deploy(self) -> bool:
        return self.contract.functions.automaticDeploy().call()

    @transaction_method
    def enable_automatic_deploy(self) -> TxRes:
        return self.contract.functions.enableAutomaticDeploy()

    @transaction_method
    def disableAutomaticDeploy(self) -> TxRes:
        return self.contract.functions.disableAutomaticDeploy()
