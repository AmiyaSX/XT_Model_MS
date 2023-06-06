
from zeus.common.util.register import Registers

from muzero_model_ms import MuzeroModelMS
from muzero_cnn_ms import MuzeroCnnMS
from muzero_mlp_ms import MuzeroMlpMS

Registers.model(MuzeroModelMS)
Registers.model(MuzeroCnnMS)
Registers.model(MuzeroMlpMS)