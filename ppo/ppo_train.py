
from zeus.common.util.register import Registers

from ppo_ms import PPOMS
from ppo_mlp_ms import PpoMlpMS
from ppo_cnn_ms import PpoCnnMS

Registers.model(PPOMS)
Registers.model(PpoCnnMS)
Registers.model(PpoMlpMS)