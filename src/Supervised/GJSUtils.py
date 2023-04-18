from torch.nn import functional as F
from torch.nn.modules.loss import _Loss
from torch import Tensor

def js_div(input, target, reduction = 'mean', log_target = False, pi = .5):
    m = pi * input + (1-pi) * target
    return pi * F.kl_div(input, m, reduction=reduction, log_target=log_target) + (1-pi) * F.kl_div(target, m, reduction=reduction, log_target=log_target)

class GJSDivLoss(_Loss):
    __constants__ = ['reduction'] # not sure what this does but the KLDivLoss has it
    def __init__(self, size_average=None, reduce=None, reduction: str = 'mean', log_target: bool = False, pi: int = .5) -> None:
        super(GJSDivLoss, self).__init__(size_average, reduce, reduction)
        self.log_target = log_target
        self.pi = pi
    def forward(self, p1: Tensor, p2: Tensor, y: Tensor):
        return js_div(input = (p1+p2) * .5, target = y, reduction = self.reduction, log_target = self.log_target, pi = self.pi) + (1-self.pi) * js_div(input = p1, target = p2, reduction = self.reduction, log_target = self.log_target, pi = .5)