from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes



class TokenManagerERC1155(BaseContract):
    @transaction_method
    def exit_to_main_erc1155(self, token_address: int, token_id: int, amount: int) -> TxRes:
        return self.contract.functions.exitToMainERC1155(token_address, token_id, amount)

    @transaction_method
    def exit_to_main_erc1155_batch(self, token_addres: int, token_ids: list, amount: list) -> TxRes:
        return self.contract.functions.exitToMainERC1155Batch(token_addres, token_ids, amount)

    @transaction_method
    def transfer_to_schain_erc1155(self, schain_name: str, token_address: int, token_id: int, amount: int) -> TxRes:
        """
        schain_name - destination chain
        token address - address on source chain
        """
        return self.contract.functions.transferToSchainERC1155(schain_name, token_address, token_id, amount)

    @transaction_method
    def transfer_to_schain_erc1155_batch(self, schain_name: str, token_address: int, token_ids: list, amount: list) -> TxRes:
        return self.contract.functions.transferToSchainERC1155Batch(schain_name, token_address, token_ids, amount)

    def enable_automatic_deploy(self) -> TxRes:
        return self.contract.functions.enableAutomaticDeploy()

    @transaction_method
    def disableAutomaticDeploy(self) -> TxRes:
        return self.contract.functions.disableAutomaticDeploy()

    def automatic_deploy_role(self) -> bytes:
        return self.contract.functions.AUTOMATIC_DEPLOY_ROLE().call()

    def token_registrar_role(self) -> bytes:
        return self.contract.functions.TOKEN_REGISTRAR_ROLE().call()

    def has_role(self, role: bytes, address: int) -> bool:
        return self.contract.functions.hasRole(role, address).call()

    @transaction_method
    def grant_role(self, role: bytes, address: str) -> TxRes:
        return self.contract.functions.grantRole(role, address)

    def get_role_member(self, role: bytes, index: int) -> bytes:
        return self.contract.functions.getRoleMember(role, index).call()