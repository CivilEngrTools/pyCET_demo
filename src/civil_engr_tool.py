import json
import sys

sys.path.append("")
import CET_MODULE


def init_tool(common_data):
    data = json.dumps(common_data, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)
    CET_MODULE.init(data)


def check_block_shear():
    result_obj = json.loads(CET_MODULE.check_block_shear())
    return result_obj


def check_block_shear_axial_load():
    result_obj = json.loads(CET_MODULE.check_block_shear_axial_load())
    return result_obj


def check_block_shear_interaction():
    result_obj = json.loads(CET_MODULE.check_block_shear_interaction())
    return result_obj


def check_bolt_shear():
    result_obj = json.loads(CET_MODULE.check_bolt_shear())
    return result_obj


def check_hole_bearing():
    result_obj = json.loads(CET_MODULE.check_hole_bearing())
    return result_obj


def check_flange_local_bending():
    result_obj = json.loads(CET_MODULE.check_flange_local_bending())
    return result_obj


def check_flexural_buckling():
    result_obj = json.loads(CET_MODULE.check_flexural_buckling())
    return result_obj


def check_flexural_interaction():
    result_obj = json.loads(CET_MODULE.check_flexural_interaction())
    return result_obj


def check_flexural_rupture():
    result_obj = json.loads(CET_MODULE.check_flexural_rupture())
    return result_obj


def check_shear_plate_max_thickness():
    result_obj = json.loads(CET_MODULE.check_shear_plate_max_thickness())
    return result_obj


def check_shear_yield():
    result = CET_MODULE.check_shear_yield()
    result_obj = json.loads(result)
    return result_obj


def check_shear_yield_interaction():
    result = CET_MODULE.check_shear_yield_interaction()
    result_obj = json.loads(result)
    return result_obj


def check_shear_rupture():
    result = CET_MODULE.check_shear_rupture()
    result_obj = json.loads(result)
    return result_obj


def check_shear_rupture_interaction():
    result = CET_MODULE.check_shear_rupture_interaction()
    result_obj = json.loads(result)
    return result_obj


def check_tensile_yield():
    result = CET_MODULE.check_tensile_yield()
    result_obj = json.loads(result)
    return result_obj


def check_tensile_yield_axial_load():
    result = CET_MODULE.check_tensile_yield_axial_load()
    result_obj = json.loads(result)
    return result_obj


def check_tensile_rupture():
    result = CET_MODULE.check_tensile_rupture()
    result_obj = json.loads(result)
    return result_obj


def check_tensile_rupture_axial_load():
    result = CET_MODULE.check_tensile_rupture_axial_load()
    result_obj = json.loads(result)
    return result_obj


def check_web_crippling():
    result = CET_MODULE.check_web_crippling()
    result_obj = json.loads(result)
    return result_obj


def check_web_local_yielding():
    result = CET_MODULE.check_web_local_yielding()
    result_obj = json.loads(result)
    return result_obj


def check_weld():
    result = CET_MODULE.check_weld()
    result_obj = json.loads(result)
    return result_obj
