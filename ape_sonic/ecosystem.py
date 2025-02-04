from typing import ClassVar, cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (146, 146),
    "testnet": (57054, 57054),
}


class SonicConfig(BaseEthereumConfig):
    NETWORKS: ClassVar[dict[str, tuple[int, int]]] = NETWORKS
    opera: NetworkConfig = create_network_config(
        block_time=0, required_confirmations=0, is_mainnet=True
    )
    testnet: NetworkConfig = create_network_config(block_time=0, required_confirmations=0)


class Sonic(Ethereum):
    fee_token_symbol: str = "S"

    @property
    def config(self) -> SonicConfig:  # type: ignore[override]
        return cast(SonicConfig, self.config_manager.get_config("fantom"))
