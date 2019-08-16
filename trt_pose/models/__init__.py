from .resnet import *
from .densenet import *


MODELS = {
    'resnet18_baseline': resnet18_baseline,
    'resnet34_baseline': resnet34_baseline,
    'resnet50_baseline': resnet50_baseline,
    'resnet101_baseline': resnet101_baseline,
    'resnet152_baseline': resnet152_baseline,
    'resnet18_baseline_att': resnet18_baseline_att,
    'resnet34_baseline_att': resnet34_baseline_att,
    'resnet50_baseline_att': resnet50_baseline_att,
    'resnet101_baseline_att': resnet101_baseline_att,
    'resnet152_baseline_att': resnet152_baseline_att,
    'densenet121_baseline': densenet121_baseline,
    'densenet169_baseline': densenet169_baseline,
    'densenet201_baseline': densenet201_baseline,
    'densenet161_baseline': densenet161_baseline,
    'densenet121_baseline_att': densenet121_baseline_att,
    'densenet169_baseline_att': densenet169_baseline_att,
    'densenet201_baseline_att': densenet201_baseline_att,
    'densenet161_baseline_att': densenet161_baseline_att
}