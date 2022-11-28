import angr
import claripy

userInputAddress = 0x100000
failureAddress = 0x10000
successAddress = 0x1000000

flagLength = 15

project = angr.project("binaryfile", main_opts={"base_addr": userInputAddress})
flagChars = [claripy.BVS(f"flagChars{index}", 8) for index in range(flagLength)]
flag = claripy.Concat(*flagChars + [claripy.BVV(b"\n")])

state = project.factory.full_init_state(
    args=["binaryfile"],
    add_options=angr.options.inicorn,
    stdin=flag
)

for index in flagChars:
    state.solver.add(index >= ord('!'))
    state.solver.add(index <= ord('-'))

simulationManager = project.factory.simulation_manager(state)
simulationManager.explore(find=successAddress, avoid=failureAddress)

if len(simulationManager.found) > 0:
    for found in simulationManager.found:
        print(found.posix.dumps(0))
