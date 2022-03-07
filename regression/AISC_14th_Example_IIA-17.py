import copy
import sys
sys.path.append("..")

from src_pyc.member import Member
from src_pyc.connection import Connection
from src.civil_engr_tool import check_block_shear
from src.civil_engr_tool import check_bolt_shear
from src.civil_engr_tool import check_hole_bearing
from src.civil_engr_tool import check_shear_yield
from src.civil_engr_tool import check_shear_rupture
from src.civil_engr_tool import check_weld
from src.civil_engr_tool import init_tool
from src.report import Report

from src.calculation import Calculation

common_data = {
    "design method": "ASD",
    "code": "AISC 14th"
}

report = Report()
init_tool(common_data)

beam = Member()
beam.grade = "A992"
beam.type = "BEAM"
beam.rotation_x = 0.0
beam.section.set_size("W16X50")
beam.section_type = "H Shape"

beam.start.shear_force = 60

column = Member()
column.grade = "A992"
column.type = "COLUMN"
column.rotation_x = 0.0
column.section.set_size("W14X90")
column.section_type = "H Shape"

web_conn = Connection()
web_conn.set_default("web conn")
web_conn.grade = "A36"
web_conn.Fy = 36
web_conn.Fu = 58
web_conn.length = 11.5
web_conn.thickness = 0.25
web_conn.width = 4.5
web_conn.bolt.row = 4
web_conn.bolt.diameter = 0.75
web_conn.bolt.type = "A325N"
web_conn.bolt.hole_type = "Standard"
web_conn.bolt.row_spacing = 3
web_conn.bolt.edge_dist_along_force = 1.25
web_conn.bolt.edge_dist_prep_force = 1.5
web_conn.bolt.ecc_dist_along_force = 1.5
web_conn.weld.size = 0.1875
web_conn.weld.FEXX = 70.0
web_conn.weld.length = 11.5
# web_conn.weld.load_angle = 0.0
web_conn.weld.thinner_part_thickness = min(column.section.tf, web_conn.thickness)
web_conn.weld.base_plate_linear_rupture = 0.6 * column.section.tf * 65.0

beam.start.web.length = beam.section.d
beam.start.web.thickness = beam.section.tw
beam.start.web.bolt = copy.deepcopy(web_conn.bolt)
beam.start.web.bolt.edge_dist_along_force = 0.0
beam.start.web.check_force = beam.start.shear_force

loc_beam_web = "Beam Web"
loc_beam_web_conn = "Connection At Beam Web"

web_calc = Calculation()

beam.start.web.set_data(beam)
web_calc.add_item(loc_beam_web, "Shear Yielding", check_shear_yield(),
                  beam.start.shear_force, "Kips")
web_calc.add_item(loc_beam_web, "Hole Bearing", check_hole_bearing(),
                  beam.start.shear_force, "Kips")

web_conn.check_force = beam.start.shear_force
web_conn.set_data()
web_calc.add_item(loc_beam_web_conn, "Bolt Shear", check_bolt_shear(),
                  web_conn.check_force, "Kips")
web_calc.add_item(loc_beam_web_conn, "Shear Yielding", check_shear_yield(),
                  web_conn.check_force, "Kips")
web_calc.add_item(loc_beam_web_conn, "Shear Rupture", check_shear_rupture(),
                  web_conn.check_force, "Kips")
web_calc.add_item(loc_beam_web_conn, "Block Shear", check_block_shear(),
                  web_conn.check_force, "Kips")
web_calc.add_item(loc_beam_web_conn, "Hole Bearing", check_hole_bearing(),
                  web_conn.check_force, "Kips")
web_calc.add_item(loc_beam_web_conn, "Welds", check_weld(),
                  web_conn.check_force, "Kips")

# process report
web_calc.show_max_ratio_calc = True
web_calc.find_max_ratio_index()
report.content += "### 1 Summary\n"
report.content += """ 
To demonstrate the calcuations from AISC 14th Design Examples 
II.A-17, SINGLE-PLATE CONNECTION (CONVENTIONALBEAM-TO-COLUMN FLANGE). Origianl information\n
Given:\n
Design a single-plate connection between an ASTM A992 W1650 beam and an ASTM A992 W1490 column
flange to support the following beam end reactions:\n
RD = 8.0 kips \n
RL = 25 kips \n
Rn = 33 kips (ASD method) \n
Use 3/4-in.-diameter ASTM A325-N or F1852-N bolts in standard holes, 70-ksi electrode welds and an ASTM A36 plate \n
"""
report.content += "#### Capacity Table\n"

report.content += "Beam Web\n"
report.content += "| Limit State    | Design Value | Check value | Ratio | Check Result | Reference |\n"
report.content += "|----------------|-------|-------------|-------|-------|-------|\n"
report.content = web_calc.create_report_table_item(loc_beam_web,
                                                   report.content)

report.content += "\nBeam Web Connection\n"
report.content += "| Limit State    | Design Value | Check value | Ratio | Check Result | Reference |\n"
report.content += "|----------------|-------|-------------|-------|-------|-------|\n"
report.content = web_calc.create_report_table_item(loc_beam_web_conn,
                                                   report.content)

report.content += "### 2 Beam web check\n"
report.content = web_calc.create_report_calc(loc_beam_web, report.content)

report.content += "### 3 Beam web connection check\n"
report.content = web_calc.create_report_calc(loc_beam_web_conn, report.content)

report.write_file("./test/AISC_14th_Example_IIA-17.md")
