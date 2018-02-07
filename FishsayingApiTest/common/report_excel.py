# -*- coding: utf-8 -*-
import time
from datetime import date, datetime

import os
import xlrd
import xlsxwriter

from common import Log


class Report:
    date = datetime.now()
    name = date.strftime("%Y-%m-%d %H-%M-%S") + 'report.xlsx'
    worksheet = ''
    worksheet2 = ''
    Fail = 0
    Pass = 0
    count_f = 0
    count_p = 0
    count_s = 0
    data = ''

    def __init__(self, path, data):
        self.data = data
        for info in data:
            if info.get("t_result") == "fail":
                self.count_f += 1
            elif info.get("t_result") == "pass":
                self.count_p += 1
            self.count_s += 1

        def get_format(wd, option={}):
            return wd.add_format(option)

        # 设置居中
        def get_format_center(wd, num=1):
            return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})

        def set_border_(wd, num=1):
            return wd.add_format({}).set_border(num)
        def set_coler_(wd, color):
            return wd.add_format({}).set_border_color(color)

        def _write_center(worksheet, cl, data, wd):
            return worksheet.write(cl, data, get_format_center(wd))

        workbook = xlsxwriter.Workbook(path + '\\' + 'report.xlsx')
        self.worksheet = workbook.add_worksheet("测试总况")
        self.worksheet.set_column("A:A", 17)
        self.worksheet.set_column("B:B", 20)
        self.worksheet.set_column("C:C", 20)
        self.worksheet.set_column("D:D", 20)
        self.worksheet.set_column("E:E", 20)
        self.worksheet.set_column("F:F", 18)
        self.worksheet.set_row(1, 30)
        self.worksheet.set_row(2, 30)
        self.worksheet.set_row(3, 30)
        self.worksheet.set_row(4, 30)
        self.worksheet.set_row(5, 30)
        define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)
        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("#737946")
        define_format_H2.set_color("#ffffff")
        self.worksheet.merge_range('A1:F1', '测试报告概况', define_format_H1)
        self.worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
        # worksheet.insert_image('A3:A6', 'testFile\\Logo.png', get_format_center(workbook))
        self.worksheet.insert_image('A3', 'testFile/Logo.png')

        _write_center(self.worksheet, "B3", '项目名称', workbook)
        _write_center(self.worksheet, "B4", '接口版本', workbook)
        _write_center(self.worksheet, "B5", '脚本语言', workbook)
        _write_center(self.worksheet, "B6", '测试网络', workbook)

        data1 = {"test_name": "FishSaying", "test_version": "v-", "test_pl": "python3.0", "test_net": "-"}
        _write_center(self.worksheet, "C3", data1['test_name'], workbook)
        _write_center(self.worksheet, "C4", data1['test_version'], workbook)
        _write_center(self.worksheet, "C5", data1['test_pl'], workbook)
        _write_center(self.worksheet, "C6", data1['test_net'], workbook)

        _write_center(self.worksheet, "D3", "接口总数", workbook)
        _write_center(self.worksheet, "D4", "通过总数", workbook)
        _write_center(self.worksheet, "D5", "失败总数", workbook)
        _write_center(self.worksheet, "D6", "测试日期", workbook)
        # data1 = {"test_sum": "-", "test_success": "-", "test_failed": "-",
        #         "test_date": self.date.strftime("%Y-%m-%d %H:%M")}
        _write_center(self.worksheet, "E3", self.count_s, workbook)
        _write_center(self.worksheet, "E4", self.count_p, workbook)
        _write_center(self.worksheet, "E5", self.count_f, workbook)
        _write_center(self.worksheet, "E6", self.date.strftime("%Y-%m-%d %H:%M"), workbook)
        _write_center(self.worksheet, "F3", "通过率", workbook)
        if self.count_s == 0:
            self.worksheet.merge_range('F4:F6', 0, get_format_center(workbook))
        else:
            passrate = self.count_p / self.count_s * 100
            self.worksheet.merge_range('F4:F6', str("%.2f" % passrate) + "%",
                                       get_format_center(workbook))
        self.worksheet2 = workbook.add_worksheet("测试详情")
        self.worksheet2.set_column("A:A", 10)
        self.worksheet2.set_column("B:B", 10)
        self.worksheet2.set_column("C:C", 10)
        self.worksheet2.set_column("D:D", 20)
        self.worksheet2.set_column("E:E", 20)
        self.worksheet2.set_column("F:F", 20)
        self.worksheet2.set_column("G:G", 20)
        self.worksheet2.set_column("H:H", 20)

        self.worksheet2.set_row(0, 30)

        self.worksheet2.merge_range('A1:H1', '测试详情',
                                    get_format(workbook, {'bold': True, 'font_size': 18, 'align': 'center',
                                                          'valign': 'vcenter', 'bg_color': '#737946',
                                                          'font_color': '#ffffff'}))
        _write_center(self.worksheet2, "A2", '用例ID', workbook)
        _write_center(self.worksheet2, "B2", '接口名称', workbook)
        _write_center(self.worksheet2, "C2", '请求方式', workbook)
        _write_center(self.worksheet2, "D2", 'URL', workbook)
        _write_center(self.worksheet2, "E2", '参数', workbook)
        _write_center(self.worksheet2, "F2", '预期值', workbook)
        _write_center(self.worksheet2, "G2", '实际值', workbook)
        _write_center(self.worksheet2, "H2", '测试结果', workbook)
        self.worksheet2.set_row(1, 20)
        temp = len(data) + 2
        for item in self.data:
            _write_center(self.worksheet2, "A" + str(temp), item["t_id"], workbook)
            _write_center(self.worksheet2, "B" + str(temp), item["t_name"], workbook)
            _write_center(self.worksheet2, "C" + str(temp), item["t_method"], workbook)
            _write_center(self.worksheet2, "D" + str(temp), item["t_url"], workbook)
            _write_center(self.worksheet2, "E" + str(temp), item["t_param"], workbook)
            _write_center(self.worksheet2, "F" + str(temp), item["t_hope"], workbook)
            # _write_center(self.worksheet2, "G" + str(temp), item["t_actual"], workbook)
            if len(str(item["t_actual"])) > 40:
                _write_center(self.worksheet2, "G" + str(temp), str(item["t_actual"])[:40] + "......", workbook)
            else:
                _write_center(self.worksheet2, "G" + str(temp), str(item["t_actual"]), workbook)
            _write_center(self.worksheet2, "H" + str(temp), item["t_result"], workbook)
            # if item["t_result"]=="fail":
            #     set_coler_("#FF4500")
            temp = temp - 1

        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name': '接口测试统计',
            'categories': '=测试总况!$D$4:$D$5',
            'values': '=测试总况!$E$4:$E$5',
        })
        chart1.set_title({'name': '接口测试统计'})
        chart1.set_style(10)
        self.worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})
        workbook.close()

