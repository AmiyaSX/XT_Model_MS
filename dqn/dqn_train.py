
from zeus.common.util.register import Registers

from dqn_cnn_ms import DqnCnnMS
from dqn_mlp_ms import DqnMlpMS
from dqn_cnn_pong_ms import DqnCnnPongMS
from model_ms import XTModel_MS

Registers.model(XTModel_MS)
Registers.model(DqnCnnMS)
Registers.model(DqnMlpMS)
Registers.model(DqnCnnPongMS)
