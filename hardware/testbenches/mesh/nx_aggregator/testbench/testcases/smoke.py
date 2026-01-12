from cocotb.triggers import ClockCycles

from ..testbench import Testbench
from drivers.stream.common import StreamTransaction

@Testbench.testcase()
async def smoke(tb, log):
    await ClockCycles(tb.clk, 1000)

