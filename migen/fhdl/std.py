from migen.fhdl.structure import *
from migen.fhdl.module import Module
from migen.fhdl.specials import TSTriple, Instance, Memory
from migen.fhdl.size import log2_int, bits_for, flen
from migen.fhdl.decorators import DecorateModule, InsertCE, InsertReset, RenameClockDomains
