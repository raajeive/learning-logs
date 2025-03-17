class ATM:

    def __init__(self):
        self.bankNotesDenominations = [500, 200, 100, 50,  20]
        self.bankNotesAmount = {20: 0, 50 : 0, 100 : 0, 200 : 0, 500 : 0}

    def deposit(self, banknotesCount):
        for value, count in zip([20, 50, 100, 200, 500], banknotesCount):
            self.bankNotesAmount[value] += count

    def withdraw(self, amount):
        res = []
        tempDict = {}
        for currency in self.bankNotesDenominations:
            temp = 0
            if amount >= currency and self.bankNotesAmount[currency]:
                temp = int(amount / currency)
                if temp < self.bankNotesAmount[currency]:
                    tempDict[currency] = temp
                    amount = amount % currency
                else:
                    temp = self.bankNotesAmount[currency]
                    tempDict[currency] = self.bankNotesAmount[currency]
                    amount = amount - (self.bankNotesAmount[currency] * currency)
            res.append(temp)

        if amount == 0:
            for key, value in tempDict.items():
                self.bankNotesAmount[key] -= value
            res.reverse()
            return res
        else:
            return [-1]

