# -*-coding:utf-8-*-
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """
    员工类
    """
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """获取薪水"""
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000.0


class Programer(Employee):

    def __init__(self, name, work_hours=0):
        super().__init__(name)
        self._work_hours = work_hours

    @property
    def work_hours(self):
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        self._work_hours = work_hours

    def get_salary(self):
        return 150.0 * self._work_hours


class Salesman(Employee):

    def __init__(self, name, sale_mount=0):
        super().__init__(name)
        self._sale_mount = sale_mount

    @property
    def sale_mount(self):
        return self._sale_mount

    @sale_mount.setter
    def sale_mount(self, sale_mount):
        self._sale_mount = sale_mount

    def get_salary(self):
        return 1200.0 + self._sale_mount * 0.05


def main():
    emps = [Manager('将'), Manager('帅'), Programer('炮'), Programer('相'), Programer('马'), Salesman('兵'), Salesman('卒')]
    for emp in emps:
        if isinstance(emp, Programer):
            emp.work_hours = int(input(f'请输入{emp.name}本月工时：'))
        elif isinstance(emp, Salesman):
            emp.sale_mount = int(input(f'请输入{emp.name}本月销售额：'))
        print(f'{emp.name}本月的工资：￥{emp.get_salary()}元')


if __name__ == '__main__':
    main()
