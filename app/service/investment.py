from datetime import datetime


def mark_fully_invested(obj, session):
    obj.fully_invested = True
    obj.close_date = datetime.now()


def investment_process(donation):
    найти проекты
    пока есть деньги в донате:
        берем неполный проект
        считаем недостающую сумму
        если недостающая сумма > доната:
            деньги с доната кладем в проект
            донат отмечаем fully_invested
            если сумма доната == нулю:
                отмечаем донат fully_invested
        иначе:
            сумму в донате уменьшаем на недостающую сумму
            отмечаем донат как fully_invested


def investment_process(project):
    найти донаты
    пока есть деньги для проекта:
        берем донат с деньгами
        считаем недостающую сумму
        если недостающая сумма > доната:
            деньги с доната кладем в проект
            донат отмечаем fully_invested
            если сумма доната == нулю:
                отмечаем донат fully_invested
        иначе:
            сумму в донате уменьшаем на недостающую сумму
            отмечаем донат как fully_invested
