# ruff: noqa: E402, F401
# ^ ignoring ruff errors for entire file (https://beta.ruff.rs/docs/rules/)

# imports, std lib
import sys

# local imports
if (toplevel:=r'C:\TestPrograms\applications.validation.circuit-margin.tpdev.aguila.meteorlake-tp\datacollection_python_rework') not in sys.path:
    sys.path.append(toplevel)
import generic_product.utilities.logger as logger
import generic_product.sv_ipc_wrapper as sv_ipc_wrapper

# imports, so that Aguila python has access to the scripts it needs
import mtl.cdie.frequency
import mtl.cdie.fuse_overrides
import mtl.cdie.temperature
import mtl.cdie.voltage
import mtl.cdie.recipe

import mtl.gcd.frequency
import mtl.gcd.fuse_overrides
import mtl.gcd.temperature
import mtl.gcd.voltage
import mtl.gcd.fuse_recipes.gcd_2023_09_20 as mtl_gcd_fuse_recipe

import mtl.soc.frequency
import mtl.soc.fuse_overrides
import mtl.soc.temperature
import mtl.soc.voltage

import mtl.bootstagetransitions
import mtl.targetpowercontrol as __targetpowercontrol # this should not be used within OTPL.

# create pythonsv / openipc wrapper object
# Instantiate PythonSV/OpenIPC wrapper singleton object
sv_ipc_wrapper_singleton = sv_ipc_wrapper.PySVOpenIPCWrapper(
    product = 'meteorlake',
    derivative = 'Auto',
    stepping = 'Auto',
    is_processor_on_fn = __targetpowercontrol.is_target_power_on,
    bootstagetransitions = mtl.bootstagetransitions
)
assert sv_ipc_wrapper_singleton._initialized