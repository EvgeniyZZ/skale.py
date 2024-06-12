from skale.contracts.base_contract import BaseContract, transaction_method
from skale.transactions.result import TxRes
from Crypto.Hash import keccak




class TokenManagerERC20(BaseContract):
    def automatic_deploy(self) -> bool:
        return self.contract.functions.automaticDeploy().call()

    @transaction_method
    def exit_to_main_erc20(self, token_address: int, amount: int) -> TxRes:
        return self.contract.functions.exitToMainERC20(token_address, amount)

    @transaction_method
    def transfer_to_schain_erc20(self, schain_name: str, token_address: int, amount: int) -> TxRes:
        return self.contract.functions.transferToSchainERC20(schain_name, token_address, amount)

    @transaction_method
    def add_erc20_token(self, schain_name: str, token_mn: int, token_sc: int) -> TxRes:
        return self.contract.functions.addERC20TokenByOwner(schain_name, token_mn, token_sc)

    @transaction_method
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

    def get_clones_erc20(self, schain_hash: bytes, address: str) -> int:
        '''schan_hash - origin chain, address - origin token address'''
        keccak_hash = keccak.new(data=schain_hash.encode("utf8"), digest_bits=256)
        hash = keccak_hash.digest()
        return self.contract.functions.clonesErc20(hash, address).call()
