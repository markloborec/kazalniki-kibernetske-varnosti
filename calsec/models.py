import datetime
import statistics
from dataclasses import dataclass


@dataclass
class Incident:
    datum: datetime.date
    kategorija: str

    @staticmethod
    def groupByMonth(inc: list['Incident']):
        group = []
        for i in range(12):
            group.append([])
        for ele in inc:
            group[ele.datum.month-1].append(ele)
        return group

    @staticmethod
    def countByMonth(inc: list['Incident']):
        return [len(ele) for ele in Incident.groupByMonth(inc)]
    @staticmethod
    def averageByMonth(inc: list["Incident"]):
        return statistics.mean(Incident.countByMonth(inc))