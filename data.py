class ProfitData:
    def __init__(self):
        self.reset()

    def reset(self):
        self.total_profit = 0
        self.total_count = 0
        self.tp_profit = 0
        self.tp_count = 0

    def add_profit(self, amount, is_tp):
        self.total_profit += amount
        self.total_count += 1
        if is_tp:
            self.tp_profit += amount
            self.tp_count += 1

    def get_statistics(self):
        average_total_profit = self.total_profit / self.total_count if self.total_count else 0
        average_tp_profit = self.tp_profit / self.tp_count if self.tp_count else 0
        efficiency = self.tp_profit / self.total_profit if self.total_profit else 0

        stats = {
            "average_total_profit": average_total_profit,
            "average_tp_profit": average_tp_profit,
            "total_count": self.total_count,
            "tp_count": self.tp_count,
            "total_profit": self.total_profit,
            "tp_profit": self.tp_profit,
            "efficiency": efficiency
        }

        self.reset()

        return stats
