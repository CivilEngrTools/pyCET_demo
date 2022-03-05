
class Calculation:
    def __init__(self):
        self.checks = []
        self.max_ratio_index = 0
        self.show_max_ratio_calc = False

    def add_item(self, location, name, check_item, check_force, unit):
        self.checks.append([location, name, check_item["result"], check_force,
                            check_item["equations"], check_item["reference"],
                            unit])

    def is_ok(self):
        ok = True
        for each in self.checks:
            design_value = each[2]
            check_value = each[3]
            if check_value / design_value > 1.0:
                ok = False
                break
        return ok

    def create_report_calc(self, loc, report):
        for each in self.checks:
            location = each[0]

            if location == loc:
                name = each[1]
                report += "#### " + name + "\n"
                equations = each[4]

                for item in equations:
                    if item["type"] == "equation":
                        report += item["content"]
                    elif item["type"] == "text":
                        report += item["content"] + "\n"
        return report

    def create_report_table_item(self, loc, report):
        for i in range(len(self.checks)):
            each = self.checks[i]
            location = each[0]

            if location == loc:
                name = each[1]
                reference = each[5]
                unit = each[6]
                design_value = str("%0.2f" % each[2]) + " " + unit
                check_value = str(each[3]) + " " + unit
                ratio_value = each[3] / each[2]
                ratio = str("%0.3f" % ratio_value)

                if self.show_max_ratio_calc and i == self.max_ratio_index:
                    ratio = "**" + ratio + "**"

                success = "o.k." if not ratio_value > 1.0 else "no good"

                report += "| " + name + " | " + design_value + " | " + check_value \
                          + " | " + ratio + " | " + success + " | " + reference + " |\n"
        return report

    def find_max_ratio_index(self):
        max_ratio = -1.0
        for i in range(len(self.checks)):
            design_value = self.checks[i][2]
            check_value = self.checks[i][3]
            ratio = check_value / design_value
            if ratio > max_ratio:
                max_ratio = ratio
                self.max_ratio_index = i
